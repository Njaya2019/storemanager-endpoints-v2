from flask.views import MethodView
from flask import request, jsonify, abort
from models.products import products
from models.users import users
from Validators.validate_json import validate_json_numeric_value,validate_json_string_value

from decorators import token_required

class admin(MethodView):
    decorators=[token_required]
    p=products(p_name=None, price=None,quantity=None)

    def get(self, current_user_id, product_id):
        if not product_id:
            available_products=self.p.get_products()
            return jsonify({'Products':available_products}), 200
        if product_id:
            requested_product=self.p.get_a_product(product_id)
            return jsonify({'Product':requested_product}), 200
    
    def post(self,current_user_id):
        #u=users(full_name=None,email=None,role=None,password=None,confirm_pwd=None)
        for u_s in users.users_list:
            if u_s['user_id']==current_user_id:
                if u_s['user_role']!='Admin':
                    return jsonify({'message':'User is not authorized'}), 403
        if not request.json:
            abort(400)
        pro_name=request.json['product_name']
        pro_price=request.json['price']
        pro_qty=request.json['quantity']
        if not validate_json_numeric_value(pro_price) or not validate_json_string_value(pro_name) or not validate_json_numeric_value(pro_qty):
            return jsonify({'message':'Please provide valid strings or integers'})
        if not pro_name or not pro_price or not pro_qty:
            return jsonify({'message':'Please provide all values'})
        self.p=products(pro_name,pro_price, pro_qty)
        msg=self.p.add_product()
        return jsonify({'message':msg}), 200
    def put(self, current_user_id, product_id):
        for p in products.products_list:
            if p['product_id']==product_id:
                p['product_name']=request.json['product_name']
                p['price']=request.json['price']
                p['quantity']=request.json['quantity']
                return jsonify({'Product Updated':p}),200
    def delete(self,current_user_id, product_id):
        del products.products_list[product_id-1]
        return jsonify({'message':'The product was deleted'}), 204



