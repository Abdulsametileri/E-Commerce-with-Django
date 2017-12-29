from django.db import models
from ecommercedb.database_api import *




class Admin(models.Model):

    def insertProduct(pname, pdescr, purl,
            pprice, pstock, psubcatid):
        CUR.callproc('ecommerce."insertProduct"',
                     [pname,
                      pdescr,
                      purl,
                      pprice,
                      pstock,
                      psubcatid])
        connection.commit()




