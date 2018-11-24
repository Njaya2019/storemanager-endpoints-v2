from flask.views import MethodView
from flask import request, jsonify, abort
from models.sales import sales


class admin_sales(MethodView):
   
    s=sales(product_name=None,quantity=None)
    def get(self,saleId):
        if saleId:
            requested_sale=self.s.get_sale(saleId)
            if not isinstance(requested_sale,dict):
                return jsonify({'message':'The sale record wasn\'t found'}),404
            return jsonify({'Sale':requested_sale})
        else:
            sa_les=self.s.get_sales()
            return jsonify({'Sales':sa_les})
                                                  
                                                  
                                                  
                                                
                                    
            
   
    
