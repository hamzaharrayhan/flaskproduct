from app.model.product import Product

def formatData(datas):
    array = []
    for i in datas:
        array.append(objectParser(i))
    
    return array

def objectParser(data):
    data = {
        'id': data.id,
        'name': data.name,
        'price': data.price,
        'description': data.description,
        'quantity': data.quantity,
        'created_at': data.created_at,
        'updated_at': data.updated_at
    }
    
    return data

def jsonParser(data):
    product = Product(name=data['name'], price=data['price'], description=data['description'], quantity=data['quantity'])
    return product