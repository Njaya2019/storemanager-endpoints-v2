from models.sales import sales
from models.products import products
import pytest
import time

p=products('Iphone 7',800,40)
p.add_product()
s=sales('Iphone 7', 2)
sa=sales('Iphone 8', 2)
sp=sales('Iphone 7', 41)
def test_init():
    assert s.sale_id==1
    assert s.quantity==2
    assert s.product_name=='Iphone 7'
    assert s.date_sale_made==time.strftime("%b %d, %Y %H:%M %p")
def test_make_sale():
    sale=s.make_sale()
    assert sale=={'sale_id':1,'attendant_id':1, 'product_id':1, 'quantity':2, 'date':s.date_sale_made,'transanction_cost':1600} 

def test_gate_sales():
    sales_records=s.get_sales()
    assert sales_records==[{'Product name':'Iphone 7','Date sold':s.date_sale_made, 'Total cost':1600, 'Quantity bought':2,'Sale id':1}]

def test_sale_product_exist():
    pro_not_found=sa.make_sale()
    assert pro_not_found=='The product is not in the inventory'

def test_sale_produc_stock():
    qty_exceeds=sp.make_sale()
    assert qty_exceeds=='Quantity to be bought exceeds amount in invetory'

def test_products_inventory():
    sl=sales('subwoofer',2)
    no_products=sl.make_sale()
    assert no_products=='The product is not in the inventory'

def test_pro_not_inventory():
    s=sales('Iphone 7', 38)
    s.make_sale()
    s_l=sales('Iphone 7', 2)
    s_a=s_l.make_sale()
    assert s_a=='The product is out of stock'

def test_sale_record_exist():
    se=s.get_sale(8)
    assert se=='The sale record wasn\'t found'
    







    
    

    