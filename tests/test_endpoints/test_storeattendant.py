import pytest, json
from application import app
from storeattendant.storeattendant import storeattendant
from models.sales import sales
from models.products import products


sa=storeattendant()
@pytest.fixture(scope="module")
def cli_ent():
    client=app.test_client()
    return client

def test_post(cli_ent):
    response=cli_ent.post('/api/v1/attendant/sales', data=json.dumps(dict(
    product_name='Iphone 6 plus',quantity=1
    )), content_type="application/json")
    data=json.loads(response.data)
    assert data=={'message':'The product is not in the inventory'}

def get_sale_record(cli_ent):
    response=cli_ent.get('/api/v1/attendant/sales/'+str(1))
    data=json.loads(response.data)
    assert response.status_code==200
    assert data=={'Sale':storeattendant.s.get_sale(1)}
def get_sales_records(cli_ent):
    response=cli_ent.get('/api/v1/attendant/sales/')
    data=json.loads(response.data)
    assert response.status_code==200
    assert data=={'Sales':storeattendant.s.get_sales()}
    


def test_get__empty_sale_record(cli_ent):
    response=cli_ent.get('/api/v1/attendant/sales/'+str(2))
    data=json.loads(response.data)
    assert response.status_code==404
    assert 'The sale record wasn\'t found' in data["message"]
def test_post_empty_values(cli_ent):
    empty_values=cli_ent.post('/api/v1/attendant/sales', data=json.dumps(dict(
    product_name='',quantity=1
    )), content_type="application/json")
    empty_data=json.loads(empty_values.data)
    assert empty_data=={'message':'Please provide all values'}

def test_post_invalid_values(cli_ent):
    invalid_values=cli_ent.post('/api/v1/attendant/sales', data=json.dumps(dict(
    product_name=123,quantity=1
    )), content_type="application/json")
    invalid_data=json.loads(invalid_values.data)
    assert invalid_data=={'message':'Please provide valid strings or integers'}





