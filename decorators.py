from functools import wraps
from flask import request, jsonify
from models.users import users
import jwt

def token_required(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        token=request.headers.get('X-APP-SECRET')
        if token is None:
            return jsonify({'message':'Token is missing'}),403
        try:
            data=jwt.decode(token, 'secret', algorithm='HS256')
            current_user_id=data['user_id']
        except:
            return jsonify({'message':'Token is invalid'})
        
        return f(current_user_id,*args,**kwargs)
    return decorated_function
