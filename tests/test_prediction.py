import json


def test_post_with_valid_data(client):
    mock_request_data = {'prediction_requests': [
        {
            "customer_code": '19424',
            "customer_age": '56',
            "customer_employee_index": 'filial',
            "customer_gender": 'female',
            "customer_country": 'ES',
            "customer_join_date": "1995-01-16",
            "customer_is_new": "0",
            "customer_seniority": '256',
            "customer_primary": 'primary',
            "customer_type": 'primary',
            "customer_relation_type": 'active',
            "customer_residence_index": "1",
            "customer_foreign_index": "0",
            "customer_spouse_index": "0",
            "customer_channel": 'KAT',
            "customer_decreased_index": 'N',
            "customer_address_type": 'primary',
            "customer_province_code": '28',
            "customer_province_name": 'MADRID',
            "customer_activity_index": '1',
            "customer_gross_income": 326124.9,
            "customer_segmentation": 'vip'
        }
    ]}
  
    response = client.post(
        '/api/v1/prediction/', data=json.dumps(mock_request_data), content_type='application/json')
    data = json.loads(response.data)

    if isinstance(data, str):
        data = json.loads(data)
    
    assert response.status_code == 200
    assert data['customer_code'] == '19424'
    assert data['direct_debit'] == True
    assert data['credit_card'] == True
    assert data['long_term_deposits'] == True
    assert data['pensions_2'] == True
    assert data['payroll'] == True
