import logging
from marshmallow import ValidationError


logger = logging.getLogger(__name__)


def validate_schema(schema, data):
    try:
        result = schema.load(data)
        return result
    except ValidationError as err:
        error_messages = err.messages
        logger.error('Schema validation error: %s', error_messages)
        raise ValueError(error_messages)
