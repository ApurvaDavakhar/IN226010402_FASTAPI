from fastapi import FastAPI

app = FastAPI()

products = [
    {"id":1,"name":"Pen Set","price":49,"category":"Stationery","in_stock":True},
    {"id":2,"name":"Notebook","price":120,"category":"Stationery","in_stock":True},
    {"id":3,"name":"Wireless Mouse","price":899,"category":"Electronics","in_stock":True},
    {"id":4,"name":"USB Cable","price":199,"category":"Electronics","in_stock":False}
]

@app.get("/")
def home():
    return {"message":"Store API Running"}
{
"id":5,
"name":"Laptop Stand",
"price":1299,
"category":"Electronics",
"in_stock":True
},
{
"id":6,
"name":"Mechanical Keyboard",
"price":2499,
"category":"Electronics",
"in_stock":True
},
{
"id":7,
"name":"Webcam",
"price":1899,
"category":"Electronics",
"in_stock":False
}
@app.get("/products")
def get_products():
    return {"products":products, "total":len(products)}
@app.get("/products/category/{category_name}")
def get_products_by_category(category_name: str):

    result = []

    for product in products:
        if product["category"].lower() == category_name.lower():
            result.append(product)

    return {
        "category": category_name,
        "products": result
    }
@app.get("/products/in-stock")
def get_in_stock_products():

    in_stock_products = []

    for product in products:
        if product["in_stock"] == True:
            in_stock_products.append(product)

    return {"in_stock_products": in_stock_products}