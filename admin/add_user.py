from flask.views import MethodView
from flask import request, jsonify, abort
from models.users import users
import jwt
import datetime
from Validators.validate_json import validate_json_numeric_value,validate_json_string_value

class user_s(MethodView):
    u=users(full_name=None,email=None,role=None,password=None,confirm_pwd=None)
    def post(self):
        user_name=request.json['user_fullname']
        user_email=request.json['user_email']
        user_role=request.json['user_role']
        user_pwd=request.json['user_password']
        user_confirm_pwd=request.json['user_confirm_pwd']
        if not validate_json_string_value(user_name) or not validate_json_string_value(user_email):
                return jsonify({'message':'Please provide valid strings or integers'})
        if not user_name or not user_email or not user_role or not user_pwd or not user_confirm_pwd:
            return jsonify({'message':'Please provide all values'})
        self.u=users(user_name,user_email,user_role,user_pwd,user_confirm_pwd)
        added_user=self.u.add_user()
        return jsonify({'message':added_user})
    
class AccessAPI(MethodView):
    u=users(full_name=None,email=None,role=None,password=None,confirm_pwd=None)
    def post(self):
        user_email=request.json['user_email']
        user_pwd=request.json['user_password']
        u_r=self.u.login_user(user_email,user_pwd)
        if type(u_r) != dict:
            return jsonify({'message':u_r})
        else:
            token=jwt.encode({'user_id':u_r['user_id'], 'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=30)},'secret',algorithm='HS256')
            return jsonify({'token':token.decode('UTF-8')})

        
    


