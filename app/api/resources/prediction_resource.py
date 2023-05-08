import json
from flask import request
from flask_restx import Resource, Namespace, fields, abort
from flask_jwt_extended import jwt_required


from app.models import MLModel, preprocess_data
from app.utils import PredictionRequestConverter
from app.api.models import PredictionRequest, Prediction
from app.extensions import mongo
from app.api.validators import PredictionRequestSchema, PredictionSchema


pred_ns = Namespace(
    'prediction', description='Prediction request operations')


prediction_request = pred_ns.model('PredictionRequest', {
    'customer_code': fields.String(required=True, unique=True, description='The customer code'),
    'customer_name': fields.String(description='The customer name'),
    'customer_age': fields.Integer(description='The customer age'),
    'customer_employee_index': fields.String(description='The customer employee index'),
    'customer_gender': fields.String(description='The customer gender'),
    'customer_country': fields.String(description='The customer country'),
    'customer_join_date': fields.DateTime(description='The customer join date'),
    'customer_is_new': fields.Boolean(description='Is the customer new'),
    'customer_seniority': fields.Integer(description='The customer seniority'),
    'customer_primary': fields.String(description='The customer primary'),
    'customer_last_date_primary': fields.DateTime(description='The customer last date primary'),
    'customer_type': fields.String(description='The customer type'),
    'customer_relation_type': fields.String(description='The customer relation type'),
    'customer_residence_index': fields.Boolean(description='The customer residence index'),
    'customer_foreign_index': fields.Boolean(description='The customer foreign index'),
    'customer_spouse_index': fields.Boolean(description='The customer spouse index'),
    'customer_channel': fields.String(description='The customer channel'),
    'customer_decreased_index': fields.String(description='The customer decreased index'),
    'customer_address_type': fields.String(description='The customer address type'),
    'customer_province_code': fields.String(description='The customer province code'),
    'customer_province_name': fields.String(description='The customer province name'),
    'customer_activity_index': fields.Integer(description='The customer activity index'),
    'customer_gross_income': fields.Float(description='The customer gross income'),
    'customer_segmentation': fields.String(description='The customer segmentation')
})

prediction_request_list = pred_ns.model('PredictionRequestList', {
    'prediction_requests': fields.List(fields.Nested(prediction_request))
})

pred_converter = PredictionRequestConverter()


@pred_ns.route('/')
class PredictionResource(Resource):

    @pred_ns.expect(prediction_request_list)
    # @jwt_required
    def post(self):
        # Parse request data
        data = request.get_json().get('prediction_requests', [])
        pred_ns.logger.info('Incoming request')
        # pred_ns.logger.info(f'rquest data: {data}')

        # Initialize schema
        prediction_request_schema = PredictionRequestSchema(many=True)

        # Validate request data using schema
        pred_ns.logger.info('Validating Data')
        errors = prediction_request_schema.validate(data)

        if errors:
            # Return a 400 Bad Request response with the validation errors
            pred_ns.logger.error(
                f'Prediction failed: Validation errors {errors}')
            abort(400, message='Validation errors', errors=errors)

        try:
            # Try to retrive predition from database
            pred_ns.logger.info('Try to retrive predition from database')
            pred = Prediction.objects(
                customer_code=data[0]['customer_code']).first()
            if pred:
                pred_ns.logger.info('prediction retrived from database')
                pred_ns.logger.info(f"Response: {pred.to_json()}" )
                return pred.to_json(), 200

            # Convert validated request data to CSV format
            pred_ns.logger.info('Map field names to the ML model field names')
            mapped_data = pred_converter.map_customer_data(data)
            pred_ns.logger.info(f'ML mapped data: {mapped_data}')

            # Convert the request data to the format expected by the machine learning model
            pred_ns.logger.info('preproccessing data')
            processed_data = preprocess_data(mapped_data)
            pred_ns.logger.info(f'Proccesed Data: {processed_data}')

            # Load the machine learning model
            ml_model = MLModel()
            ml_model.load()
            pred_ns.logger.info('ML model loaded')

            # Make prediction using the machine learning model
            pred_ns.logger.info('Prdicting...')
            prediction = ml_model.predict(processed_data)

            # Map product names to readable names
            pred_ns.logger.info(f'Map product names to readable names')
            prediction_readable = pred_converter.map_product_names(
                prediction)
            pred_ns.logger.info(f'Product readable: {prediction_readable}')

            # Save prediction request to database
            pred_ns.logger.info(f'Save prediction requests to database')
            prediction_requests = [PredictionRequest(
                **pred_req) for pred_req in data]
            PredictionRequest.objects.insert(prediction_requests)

            # Save prediction to database
            pred_ns.logger.info(f'Save prediction to database')
            preds_save = pred_converter.prepare_prediction_save(
                prediction_readable)
            preds = [Prediction(customer_code=data[i]['customer_code'],
                                **preds_save[i]) for i in range(len(preds_save))]
            Prediction.objects.insert(preds)

            # Return prediction result
            preds = {k:v for k, v in zip(prediction_readable[0], [True] * (len(prediction_readable[0])-1))}
            res = {'customer_code': data[0]['customer_code'], **preds}
            pred_ns.logger.info(f"Response: {res}" )
            return {'customer_code': data[0]['customer_code'], **preds}, 200

        except Exception as e:
            # Log the error
            pred_ns.logger.exception('Prediction failed')
            # Return a 500 Internal Server Error response with the error message
            abort(500, message='Prediction failed: {}'.format(str(e)))
