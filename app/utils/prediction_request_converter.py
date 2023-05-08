class PredictionRequestConverter:

    def map_customer_data(self, data):
        mapping = {
            "customer_code": "ncodpers",
            "customer_gender": "sexo",
            "customer_age": "age",
            "customer_employee_index": "ind_empleado",
            "customer_country": "pais_residencia",
            "customer_join_date": "fecha_alta",
            "customer_is_new": "ind_nuevo",
            "customer_seniority": "antiguedad",
            "customer_primary": "indrel",
            "customer_last_date_primary": "ult_fec_cli_1t",
            "customer_type": "indrel_1mes",
            "customer_relation_type": "tiprel_1mes",
            "customer_residence_index": "indresi",
            "customer_foreign_index": "indext",
            "customer_spouse_index": "conyuemp",
            "customer_channel": "canal_entrada",
            "customer_decreased_index": "indfall",
            "customer_address_type": "tipodom",
            "customer_province_name": "nomprov",
            "customer_province_code": "cod_prov",
            "customer_activity_index": "ind_actividad_cliente",
            "customer_gross_income": "renta",
            "customer_segmentation": "segmento",
        }

        value_mapping = {
            "sexo": {
                "male": "H",
                "female": "V"
            },
            "ind_empleado": {
                "active": "A",
                "ex-employee": "B",
                "filial": "F",
                "not_employee": "N",
                "passive": "P"
            },
            "tiprel_1mes": {
                "active": "A",
                "inactive": "I",
                "former-customer": "P",
                "potential": "R"
            },
            "indrel_1mes": {
                "primary": "1",
                "co-owner": "2",
                "potential": "P",
                "former-primary": "3",
                "former-co-owner": "4"
            },
            "indrel": {
                "primary": "1",
                "none-primary": "0"
            },
            "tipodom": {
                "primary": "1",
                "none-primary": "1"
            },
            "segmento": {
                "vip": "01 - TOP",
                "individuals": "02 - Individuals",
                "college-graduate": "03 - college graduated"
            }
        }

        mapped_data = []
        for row in data:
            mapped_row = {}
            for key, value in row.items():
                if key in mapping:
                    mapped_key = mapping[key]
                    if isinstance(mapped_key, list):
                        for mk in mapped_key:
                            mapped_row[mk] = value_mapping.get(
                                mk, {}).get(value, value)
                    elif mapped_key.strip() in ["ind_nuevo"]:
                        mapped_row[mapped_key] = value and "1" or "0"
                    elif mapped_key in ["nomprov"]:
                        mapped_row[mapped_key] = '\"'+value+'\"'
                    elif mapped_key.strip() in ["indresi", "indext", "conyuemp", "indfall"]:
                        mapped_row[mapped_key] = value and "S" or "N"
                    else:
                        mapped_row[mapped_key] = value_mapping.get(
                            mapped_key, {}).get(value, value)
            # Adding prediction month (fecha_dato) ['2016-06-28'] to the data
            mapped_row['fecha_dato'] = '2016-06-28'
            mapped_data.append(mapped_row)
        return mapped_data

    def map_product_names(self, product_codes):
        product_map = {
            'ind_ahor_fin_ult1': 'saving_account',
            'ind_aval_fin_ult1': 'guarantees',
            'ind_cco_fin_ult1': 'current_accounts',
            'ind_cder_fin_ult1': 'derivada_account',
            'ind_cno_fin_ult1': 'payroll_account',
            'ind_ctju_fin_ult1': 'junior_account',
            'ind_ctma_fin_ult1': 'mas_particular_account',
            'ind_ctop_fin_ult1': 'particular_account',
            'ind_ctpp_fin_ult1': 'particular_plus_account',
            'ind_deco_fin_ult1': 'short_term_deposits',
            'ind_deme_fin_ult1': 'medium_term_deposits',
            'ind_dela_fin_ult1': 'long_term_deposits',
            'ind_ecue_fin_ult1': 'e_account',
            'ind_fond_fin_ult1': 'funds',
            'ind_hip_fin_ult1': 'mortgage',
            'ind_plan_fin_ult1': 'pensions',
            'ind_pres_fin_ult1': 'loans',
            'ind_reca_fin_ult1': 'taxes',
            'ind_tjcr_fin_ult1': 'credit_card',
            'ind_valo_fin_ult1': 'securities',
            'ind_viv_fin_ult1': 'home_account',
            'ind_nomina_ult1': 'payroll',
            'ind_nom_pens_ult1': 'pensions_2',
            'ind_recibo_ult1': 'direct_debit'
        }
        predictions = []
        for row in product_codes:
            products = []
            for code in row.split(' '):
                products.append(product_map.get(code, None))
                print(product_map.get(code))
            predictions.append(products)
        return predictions

    def prepare_prediction_save(self, prediction):
        preds = []
        for row in prediction:
            res = {}
            for item in row:
                res[item.lower().replace(' ', '_').replace('-', '_')] = True
            preds.append(res)
        return preds

    @staticmethod
    def convert_to_csv(data: dict) -> str:
        field_names = ['fecha_dato', 'ncodpers', 'ind_empleado', 'pais_residencia', 'sexo', 'age', 'fecha_alta',
                       'ind_nuevo', 'antiguedad', 'indrel', 'ult_fec_cli_1t', 'indrel_1mes', 'tiprel_1mes', 'indresi',
                       'indext', 'conyuemp', 'canal_entrada', 'indfall', 'tipodom', 'cod_prov', 'nomprov',
                       'ind_actividad_cliente', 'renta', 'segmento']
        data_list = []
        for field_name in field_names:
            if field_name in data:
                data_list.append(str(data[field_name]))
            else:
                data_list.append('')
        csv_string = ','.join(data_list) + '\n'
        return csv_string
