import unittest, json, pytest
from application import app
from models.products import products
from models.users import users
from admin.admin import admin
import jwt
import datetime
class Test_admin:
    @pytest.fixture(scope='module')
    def cli_ent(self):
        client=app.test_client()
        return client

    @pytest.fixture(scope='module')
    def generate_token(self,cli_ent):
        #cli_ent.post('/api/v1/admin/signup', data=json.dumps(dict(full_name='Andrew Njaya',email='andrew@yahoo.com',role='Admin',password='1234',confirm_pwd='1234')), content_type="application/json")
        rv=cli_ent.post('/api/v1/admin/login', data=json.dumps(dict(user_email='njayaandrew@andela.com',user_password='1234')), content_type="application/json")
        data=json.loads(rv.data)
        token=data['token']
        return token


        


     
    def test_post(self,cli_ent,generate_token):
        headers = {'X-APP-SECRET':'{}'.format(generate_token)}
        response=cli_ent.post('/api/v1/admin/products',headers=headers,data=json.dumps(dict(product_name='Timberland shoes',
        price=40,quantity=10)), content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==200
        assert "The product has been added" in data["message"]

    def test_post_empty_string(self,cli_ent,generate_token):
        headers = {'X-APP-SECRET':'{}'.format(generate_token)}
        empty_response=cli_ent.post('/api/v1/admin/products',headers=headers,data=json.dumps(dict(product_name='',
        price=40,quantity=10)), content_type="application/json")
        empty_data=json.loads(empty_response.data)
        assert "Please provide all values" in empty_data["message"]
        

    def test_post_invalid_values(self,cli_ent,generate_token):
        headers = {'X-APP-SECRET':'{}'.format(generate_token)}
        invalid_response=cli_ent.post('/api/v1/admin/products',headers=headers,data=json.dumps(dict(product_name=123,
        price=40,quantity=10)), content_type="application/json")
        invalid_data=json.loads(invalid_response.data)
        assert "Please provide valid strings or integers" in invalid_data["message"]

    def test_get(self,cli_ent,generate_token):
        headers = {'X-APP-SECRET':'{}'.format(generate_token)}
        response=cli_ent.get('/api/v1/admin/products',headers=headers)
        data=json.loads(response.data)
        assert response.status_code==200
        assert data=={'Products':admin.p.get_products()}

    def test_get_one_product(self,cli_ent,generate_token):
        headers = {'X-APP-SECRET':'{}'.format(generate_token)}
        response=cli_ent.get('/api/v1/admin/products/'+str(1),headers=headers)
        data=json.loads(response.data)
        assert response.status_code==200
        assert data=={'Product':admin.p.get_a_product(product_id=1)}
    
    def test_put(self,cli_ent,generate_token):
        headers = {'X-APP-SECRET':'{}'.format(generate_token)}
        response=cli_ent.put('/api/v1/admin/products/'+str(1),headers=headers,data=json.dumps(dict(product_name='Iphone 8',price=900,quantity=20)), content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==200
        assert data=={'product_updated':[2,'Iphone 8',900]}
    
    
    def test_delete(self,cli_ent,generate_token):
        headers = {'X-APP-SECRET':'{}'.format(generate_token)}
        response=cli_ent.delete('/api/v1/admin/products/'+str(8),headers=headers)
        data=json.loads(response.data)
        assert response.status_code==200
        assert data['message']=='The product id doesn\'t exist'
