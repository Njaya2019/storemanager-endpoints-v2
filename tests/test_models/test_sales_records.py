from models.sales import sales
from models.products import products
import pytest
pro=products(p_name=None,price=None,quantity=None)
pro.products_list=None
s_a_l=sales(product_name=None,quantity=None)
s_a_l.sales_list=None

def test_no_produc_ts():
    products.products_list=None
    sal_e=s_a_l.make_sale()
    assert sal_e=='There are no products yet'

def test_no_product_s():
    sa_l_e=s_a_l.get_sales()
    assert sa_l_e=='There are no sales records yet'

def test_no_pr_oduct_s():
    sa_l_e=s_a_l.get_sale(1)
    assert sa_l_e=='There are no sales records yet'