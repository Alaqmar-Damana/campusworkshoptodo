"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaa43qk728r8861kev0-a.oregon-postgres.render.com",
        database="todoapp_hkae",
        user="todoapp_hkae_user",
        password="yuDd1pQ7Ith9wSL5KGmFiKCzXdn9JN1V")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
