from flask import Flask
from views.views import admin_app
from models.data_base import DataBase
app=Flask(__name__)

db=DataBase()

app.register_blueprint(admin_app)

if __name__=='__main__':
    db.create_database()
    db.create_db_tables()
    app.run(debug=True)