"""Peewee migrations -- 001_initial.py.

Some examples (model - class or model name)::

    > Model = migrator.orm['table_name']            # Return model in current state by name
    > Model = migrator.ModelClass                   # Return model in current state by name

    > migrator.sql(sql)                             # Run custom SQL
    > migrator.run(func, *args, **kwargs)           # Run python function with the given args
    > migrator.create_model(Model)                  # Create a model (could be used as decorator)
    > migrator.remove_model(model, cascade=True)    # Remove a model
    > migrator.add_fields(model, **fields)          # Add fields to a model
    > migrator.change_fields(model, **fields)       # Change fields
    > migrator.remove_fields(model, *field_names, cascade=True)
    > migrator.rename_field(model, old_field_name, new_field_name)
    > migrator.rename_table(model, new_table_name)
    > migrator.add_index(model, *col_names, unique=False)
    > migrator.add_not_null(model, *field_names)
    > migrator.add_default(model, field_name, default)
    > migrator.add_constraint(model, name, sql)
    > migrator.drop_index(model, *col_names)
    > migrator.drop_not_null(model, *field_names)
    > migrator.drop_constraints(model, *constraints)

"""

from contextlib import suppress

import peewee as pw
from peewee_migrate import Migrator
from decimal import *


with suppress(ImportError):
    import playhouse.postgres_ext as pw_pext


def migrate(migrator: Migrator, database: pw.Database, *, fake=False):
    """Write your migrations here."""
    
    @migrator.create_model
    class RstockObject(pw.Model):
        id = pw.AutoField()
        created_at = pw.DateTimeField()
        updated_at = pw.DateTimeField(null=True)
        deleted = pw.BooleanField(default=False)

        class Meta:
            table_name = "rstockobject"

    @migrator.create_model
    class Category(pw.Model):
        id = pw.AutoField()
        created_at = pw.DateTimeField()
        updated_at = pw.DateTimeField(null=True)
        deleted = pw.BooleanField(default=False)
        code = pw.CharField(max_length=255, unique=True)
        name = pw.CharField(max_length=150)
        description = pw.TextField(null=True)
        parent = pw.ForeignKeyField(column_name='parent_id', field='id', model='self', null=True)

        class Meta:
            table_name = "category"

    @migrator.create_model
    class Customer(pw.Model):
        id = pw.AutoField()
        created_at = pw.DateTimeField()
        updated_at = pw.DateTimeField(null=True)
        deleted = pw.BooleanField(default=False)
        first_name = pw.CharField(max_length=50)
        last_name = pw.CharField(max_length=50)
        company_name = pw.CharField(max_length=100, null=True)
        email = pw.CharField(max_length=50, null=True)
        phone = pw.CharField(max_length=20)
        ifu = pw.CharField(max_length=50, null=True)

        class Meta:
            table_name = "customer"

    @migrator.create_model
    class User(pw.Model):
        id = pw.AutoField()
        created_at = pw.DateTimeField()
        updated_at = pw.DateTimeField(null=True)
        deleted = pw.BooleanField(default=False)
        first_name = pw.CharField(max_length=50)
        last_name = pw.CharField(max_length=50)
        email = pw.CharField(max_length=50, null=True)
        phone = pw.CharField(max_length=50)
        password = pw.CharField(max_length=500)
        account_type = pw.CharField(default='seller', max_length=10)
        last_seen = pw.DateTimeField(null=True)

        class Meta:
            table_name = "user"

    @migrator.create_model
    class Sale(pw.Model):
        id = pw.AutoField()
        created_at = pw.DateTimeField()
        updated_at = pw.DateTimeField(null=True)
        deleted = pw.BooleanField(default=False)
        amount = pw.DecimalField(auto_round=False, decimal_places=2, max_digits=10, rounding=ROUND_HALF_EVEN)
        sale_id = pw.UUIDField()
        code = pw.CharField(max_length=255)
        seller = pw.ForeignKeyField(column_name='seller_id', field='id', model=migrator.orm['user'])

        class Meta:
            table_name = "sale"

    @migrator.create_model
    class Invoice(pw.Model):
        id = pw.AutoField()
        created_at = pw.DateTimeField()
        updated_at = pw.DateTimeField(null=True)
        deleted = pw.BooleanField(default=False)
        code = pw.CharField(max_length=255)
        sale = pw.ForeignKeyField(column_name='sale_id', field='id', model=migrator.orm['sale'])
        customer = pw.ForeignKeyField(column_name='customer_id', field='id', model=migrator.orm['customer'])
        comment = pw.TextField(null=True)

        class Meta:
            table_name = "invoice"

    @migrator.create_model
    class Product(pw.Model):
        id = pw.AutoField()
        created_at = pw.DateTimeField()
        updated_at = pw.DateTimeField(null=True)
        deleted = pw.BooleanField(default=False)
        name = pw.CharField(max_length=150)
        description = pw.TextField(null=True)
        category = pw.ForeignKeyField(column_name='category_id', field='id', model=migrator.orm['category'])
        code = pw.CharField(max_length=255, unique=True)
        image = pw.CharField(max_length=500, null=True)
        price = pw.DecimalField(auto_round=False, decimal_places=2, max_digits=10, null=True, rounding=ROUND_HALF_EVEN)
        cost = pw.DecimalField(auto_round=False, decimal_places=2, max_digits=10, rounding=ROUND_HALF_EVEN)

        class Meta:
            table_name = "product"

    @migrator.create_model
    class SaleItem(pw.Model):
        id = pw.AutoField()
        created_at = pw.DateTimeField()
        updated_at = pw.DateTimeField(null=True)
        deleted = pw.BooleanField(default=False)
        sale = pw.ForeignKeyField(column_name='sale_id', field='id', model=migrator.orm['sale'])
        product = pw.ForeignKeyField(column_name='product_id', field='id', model=migrator.orm['product'])
        quantity = pw.IntegerField(default=1)
        price = pw.DecimalField(auto_round=False, decimal_places=2, max_digits=10, rounding=ROUND_HALF_EVEN)
        comment = pw.TextField(null=True)

        class Meta:
            table_name = "saleitem"

    @migrator.create_model
    class Shop(pw.Model):
        id = pw.AutoField()
        created_at = pw.DateTimeField()
        updated_at = pw.DateTimeField(null=True)
        deleted = pw.BooleanField(default=False)
        name = pw.CharField(max_length=50)
        logo = pw.CharField(max_length=500, null=True)
        email = pw.CharField(max_length=50)
        phone = pw.CharField(max_length=20)
        adress = pw.CharField(max_length=150, null=True)
        balance = pw.DecimalField(auto_round=False, decimal_places=2, default=Decimal('0'), max_digits=10, rounding=ROUND_HALF_EVEN)
        ifu = pw.CharField(max_length=100, null=True)
        rccm = pw.CharField(max_length=100, null=True)
        manager = pw.CharField(max_length=150)

        class Meta:
            table_name = "shop"

    @migrator.create_model
    class Transaction(pw.Model):
        id = pw.AutoField()
        created_at = pw.DateTimeField()
        updated_at = pw.DateTimeField(null=True)
        deleted = pw.BooleanField(default=False)
        title = pw.CharField(max_length=255)
        transaction_id = pw.UUIDField()
        amount = pw.DecimalField(auto_round=False, decimal_places=2, max_digits=10, rounding=ROUND_HALF_EVEN)
        type = pw.CharField(max_length=255)
        description = pw.TextField(null=True)
        issuer = pw.ForeignKeyField(column_name='issuer_id', field='id', model=migrator.orm['user'])

        class Meta:
            table_name = "transaction"


def rollback(migrator: Migrator, database: pw.Database, *, fake=False):
    """Write your rollback migrations here."""
    
    migrator.remove_model('user')

    migrator.remove_model('transaction')

    migrator.remove_model('shop')

    migrator.remove_model('saleitem')

    migrator.remove_model('sale')

    migrator.remove_model('product')

    migrator.remove_model('invoice')

    migrator.remove_model('customer')

    migrator.remove_model('category')

    migrator.remove_model('rstockobject')
