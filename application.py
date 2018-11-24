from flask import Flask
from views.views import admin_app, attendant_app, admin_sales_app
from admin.view_add_user import login_app
app=Flask(__name__)



app.register_blueprint(admin_app)
app.register_blueprint(attendant_app)
app.register_blueprint(admin_sales_app)
app.register_blueprint(login_app)

if __name__=='__main__':
    app.run(debug=True)