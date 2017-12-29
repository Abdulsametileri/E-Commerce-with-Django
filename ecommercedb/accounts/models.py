from django.db import models
from ecommercedb.database_api import *


class Accounts(models.Model):

    def register(params):
        CUR.callproc('ecommerce.register', [params['customer_email'], params['customer_password'],])
        connection.commit()
        return CUR.fetchone()[0]

    def authentication(email, password):
        CUR.callproc('ecommerce.login',[email, password,])
        connection.commit()
        user = CUR.fetchone()
        return user[0]  # array döndürdüğü için , ilk elemanı return et.
