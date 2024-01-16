import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(database="munster-stats",
                        host="localhost",
                        user="stephen",
                        port="5432")
cursor = conn.cursor()