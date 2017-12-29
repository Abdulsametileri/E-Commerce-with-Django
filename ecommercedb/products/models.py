from django.db import models
from ecommercedb.database_api import *

# Create your models here.


#facede

class Product(models.Model):

    def checkStock(id):
        CUR.callproc('ecommerce."checkStock"', [id])
        connection.commit()
        result = CUR.fetchone()
        return result[0]

    def getTopThreeRandomProduct():
        CUR.callproc('ecommerce."getTopThreeRandomProduct"',[])
        connection.commit()
        products = CUR.fetchall()
        return products

    def getRandomProducts(self):
        CUR.callproc('ecommerce."getRandomProducts"', [])
        connection.commit()
        product = CUR.fetchall()
        return product

    def getBySubCatId(id):
        CUR.callproc('ecommerce."getProductBySubcatId"', [id, ])
        connection.commit()
        product = CUR.fetchall()
        return product

    def getById(id):
        CUR.callproc('ecommerce."getProductByProductId"', [id, ])
        connection.commit()
        product = CUR.fetchone()
        return product

    def getAttrById(id):
        CUR.callproc('ecommerce."getProductAttrById"', [id, ])
        connection.commit()
        productAttr = CUR.fetchall()
        return productAttr

    def giveOrder(self,order_details):
        CUR.callproc('ecommerce."giveOrder"', [
            order_details['fname'],
            order_details['lname'],
            order_details['address'],
            order_details['phone'],
            order_details['card_name'],
            order_details['card_number'],
            order_details['card_cvc'],
            order_details['email'],
            order_details['piece'],
            order_details['carg_name'],
            order_details['given_date'],
            order_details['product_id'],
        ])
        connection.commit()
        op_result = CUR.fetchone()
        return op_result[0]


