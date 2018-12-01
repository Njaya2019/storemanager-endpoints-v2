import unittest, json, pytest
from application import app
from models.products import products
from models.users import users
import jwt
import datetime
class Test_add_user:
    @pytest.fixture(scope='module')
    def cli(self):
        cli=app.test_client()
        return cli
    
    @pytest.fixture(scope='module')
    def generate_token(self,cli):
        rv=cli.post('/api/v1/admin/login', data=json.dumps(dict(user_email='njayaandrew@andela.com',user_password='1234')), content_type="application/json")
        data=json.loads(rv.data)
        token=data['token']
        return token


    def test_post_user(self,cli,generate_token):
        headers = {'X-APP-SECRET':'{}'.format(generate_token)}
        response=cli.post('/api/v1/admin/signup',headers=headers,data=json.dumps(dict(user_fullname='Darius ndubi',
        user_email='njayaandrew@andela.com',user_role='attendant',user_password='1234',user_confirm_pwd='1234')), content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==200
        assert "Email already exists" in data["message"]

    
    def test_post_confirm_password(self,cli,generate_token):
        headers = {'X-APP-SECRET':'{}'.format(generate_token)}
        response=cli.post('/api/v1/admin/signup',headers=headers,data=json.dumps(dict(user_fullname='Darius ndubi',
        user_email='njayaandrew@companyname.com',user_role='attendant',user_password='secret12',user_confirm_pwd='secret')), content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==200
        assert "Passwords do not match" in data["message"]


    def test_post_empty_values(self,cli,generate_token):
        headers = {'X-APP-SECRET':'{}'.format(generate_token)}
        response=cli.post('/api/v1/admin/signup',headers=headers,data=json.dumps(dict(user_fullname='',
        user_email='',user_role='attendant',user_password='secret',user_confirm_pwd='secret')), content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==200
        assert "Please provide all values" in data["message"]

 
