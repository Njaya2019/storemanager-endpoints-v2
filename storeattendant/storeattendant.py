from flask.views import MethodView
from flask import request, jsonify, abort
from admin.admin import admin
from models.sales import sales
from Validators.validate_json import validate_json_numeric_value, validate_json_string_value



class storeattendant(MethodView):

    s=sales(product_name=None,quantity=None)

    def post(self):
        if not request.json:
            abort(400)
        pro_name=request.json['product_name']
        pro_qty=request.json['quantity']
        if not validate_json_numeric_value(pro_qty) or not validate_json_string_value(pro_name):
            return jsonify({'message':'Please provide valid strings or integers'})
        if not pro_name or not pro_qty:
            return jsonify({'message':'Please provide all values'})
        self.s=sales(pro_name,pro_qty)
        sale_made=self.s.make_sale()
        return jsonify({'message':sale_made})
            
        

    def get(self, saleId):
        if saleId:
            requested_sale=self.s.get_sale(saleId)
            if not isinstance(requested_sale, dict):
                return jsonify({'message':'The sale record wasn\'t found'}),404
            return jsonify({'Sale':requested_sale})
        else:
            sa_les=self.s.get_sales()
            return jsonify({'Sales':sa_les})
