"""Peewee migrations -- 002_update_sho_user.py.

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


with suppress(ImportError):
    import playhouse.postgres_ext as pw_pext


def migrate(migrator: Migrator, database: pw.Database, *, fake=False):
    """Write your migrations here."""
    
    migrator.change_fields('user', email=pw.CharField(max_length=100, unique=True))

    migrator.add_not_null('user', 'email')

    migrator.add_index('user', 'phone', unique=True)

    migrator.change_fields('shop', email=pw.CharField(max_length=100, unique=True))

    migrator.add_index('shop', 'phone', unique=True)


def rollback(migrator: Migrator, database: pw.Database, *, fake=False):
    """Write your rollback migrations here."""
    
    migrator.change_fields('shop', email=pw.CharField(max_length=50))

    migrator.drop_index('shop', 'phone')

    migrator.drop_index('shop', 'email')

    migrator.change_fields('user', email=pw.CharField(max_length=50, null=True))

    migrator.drop_not_null('user', 'email')

    migrator.drop_index('user', 'phone')

    migrator.drop_index('user', 'email')
