from app import db
from app.model.product import Product
from app import response
from app.helper import formatter

def getAllProduct(filterBy,order):
    try:
        if order == 'asc':
            if filterBy == 'time':
                product = Product.query.order_by(Product.created_at)
            if filterBy == 'price':
                product = Product.query.order_by(Product.price)
            if filterBy == 'name':
                product = Product.query.order_by(Product.name)
        elif order == 'desc':
            if filterBy == 'time':
                product = Product.query.order_by(Product.created_at.desc())
            if filterBy == 'price':
                product = Product.query.order_by(Product.price.desc())
            if filterBy == 'name':
                product = Product.query.order_by(Product.name.desc())
        else:
            product = Product.query.all()
        data = formatter.formatData(product)
        return response.success(data,'success')
    except Exception as e:
        print(e)

def createProduct(request):
    try:
        data = formatter.jsonParser(request.get_json())
        db.session.add(data)
        db.session.commit()
        data = formatter.objectParser(data)
        return response.success(data,"success")
    except Exception as e:
        print(e)