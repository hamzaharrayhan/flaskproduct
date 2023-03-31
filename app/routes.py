from app import app, cache
from app.controller import productController
from flask import request

@app.route('/products',methods=['GET'])
@cache.cached(timeout=50, query_string=True)
def products():
    args = request.args
    filterBy = args.get('filterBy')
    order = args.get('order')
    return productController.getAllProduct(filterBy,order)
    
@app.route('/add-product',methods=['POST'])
def addProduct():
    return productController.createProduct(request)