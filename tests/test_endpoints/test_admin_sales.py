import pytest, json
from application import app
from admin.admin_sales import admin_sales

 
@pytest.fixture(scope="module")
def cli_ent():
    client=app.test_client()
    return client

def test_get_sales(cli_ent):
    response=cli_ent.get('/api/v1/admin/sales')
    data=json.loads(response.data)
    assert response.status_code==200
    assert data== {"Sales":admin_sales.s.get_sales()}

def test_get_sale_no_record(cli_ent):
    response=cli_ent.get('/api/v1/admin/sales/'+str(2))
    data=json.loads(response.data)
    assert response.status_code==404
    assert 'The sale record wasn\'t found' in data["message"]
