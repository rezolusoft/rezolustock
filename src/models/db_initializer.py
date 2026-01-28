from pathlib import Path
import logging
from peewee import SqliteDatabase
from peewee_migrate import Router

# Ton fichier SQLite
db_path = Path(__file__).parent.parent.joinpath("db/rstock.db")
db = SqliteDatabase(db_path)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def db_initializer():
    logging.info("##### DB MIGRATIONS START #####")
    router = Router(db, migrate_dir="src/models/migrations")
    router.run() 
    logging.info("##### DB MIGRATIONS DONE #####")
