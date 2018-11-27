from flask import Blueprint

from admin.add_user import user_s, AccessAPI

login_app=Blueprint("login_app", __name__)

signup_view=user_s.as_view('signup_api')
login_app.add_url_rule('/api/v1/admin/signup',view_func=signup_view, methods=['POST'])

login_view=AccessAPI.as_view('login_api')
login_app.add_url_rule('/api/v1/admin/login',view_func=login_view, methods=['POST'])