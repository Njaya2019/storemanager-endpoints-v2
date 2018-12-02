
[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/Njaya2019/storemanager-endpoints/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/test_coverage)](https://codeclimate.com/github/Njaya2019/storemanager-endpoints/test_coverage)
# Andrew's store endpoints
- These are endpoints that implement the store's general operations,making sure that it runs smoothly and meet any budget or sales goal and ensuring high level of customers satisfaction through excellent service. 
- The store **owner** can add products, view all products in the inventory, view sales made by all store attendants, request to view a specific product alongside it's details and inquire a specific sale record.
- A **store attendant** can make a sale, view all sales he/she made and request a sale record with it's details.

## Tasks List
  - [x] GET /products
  - [x] GET /products/productId
  - [x] GET /sales
  - [x] GET /sales/saleId
  - [x] POST /products
  - [x] POST /sales
  - [ ] POST /auth/signup
  - [ ] POST /auth/login
  - [ ] PUT /products/productId
  - [ ] DELETE /products/productId

## Build status
[![Build Status](https://travis-ci.org/Njaya2019/storemanager-endpoints-v2.svg?branch=ft-endpoint-add-user)](https://travis-ci.org/Njaya2019/storemanager-endpoints-v2)


## Test coverage status
[![Coverage Status](https://coveralls.io/repos/github/Njaya2019/storemanager-endpoints/badge.png?branch=ft-endpoint-add-user)](https://coveralls.io/github/Njaya2019/storemanager-endpoints?branch=ft-endpoint-add-user)


## Build with
### Flask Web framework 
This framework was used because it provides simplicity and flexibility control. it lets you decide how you want to implement things

## Version
Version 1

## Installation
Clone this repository
```
- git clone https://github.com/Njaya2019/storemanager-endpoints/tree/developer
```
Go into the repository
```
- cd developer
```

Install project dependencies
```
- pip install flask
- pip install pytest
```

Start the app
```
- python application.py
```
### URL requests
Use postman to test all these endpoints

| url                       | http method   | function         |
| ------------------------  | ------------- | ---------------- |
| api/v1/admin/products     | POST          | Store a product  |
| api/v1/admin/products     | GET           | View all products|
| api/v1/attendant/sales    | POST          | Make a sale      |
| api/v1/admin/sales/saleid | GET           | View a sale      |
| api/v1/admin/sales        | GET           | View all sales   |


 
## Tests
These tests `test` all endpoints.They test a response code and the data being sent along. The tests used pytest framework because it is easy to write small tests yet scales to support complex functional testing for applications,gives detail infomation on failing assert statements auto discovery of test modules and functions.

The `example` below tests an endpoint that returns a status code 404 and message the server could not find what was requested.

```python

def test_get_sale_no_record(cli_ent):
    response=cli_ent.get('/api/v1/admin/sales/'+str(2))
    data=json.loads(response.data)
    assert response.status_code==404
    assert 'The sale record wasn\'t found' in data["message"]

```

How to run the tests.
```
- Run the tests
  - py.test -vv

```
## Authors

[Andrew Njaya](https://github.com/Njaya2019)

