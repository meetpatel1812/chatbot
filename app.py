import vanna as vn
from vanna.remote import VannaDefault
import pandas as pd
import pyodbc
import warnings
import platform
warnings.filterwarnings("ignore")
import sqlite3
from sqlalchemy import create_engine
import mysql.connector
from flask import Flask, jsonify, request

# Initialize Vanna
vn = VannaDefault(model='meet_model', api_key='d0cabdce2ea440b1a902ca99a2be8579')

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Meet@2001",
    database="testdb"
)

# Define the run_sql function
def run_sql(sql: str) -> pd.DataFrame:
    df = pd.read_sql_query(sql, conn)
    return df

# Assign the run_sql function to Vanna
vn.run_sql = run_sql
vn.run_sql_is_set = True

# Initialize the Flask app
app = Flask(__name__)

# Define the Vanna Flask App
from vanna.flask import VannaFlaskApp
VannaFlaskApp(
    vn,
    allow_llm_to_see_data=True,
    title='Welcome to AI powered CDW chatbot',
    subtitle='Here you can Ask any question related to data',
    function_generation=False,
    debug=False,
    chart=False,
    show_training_data=False,
    suggested_questions=False,
    sql=True,
    redraw_chart=False,
    ask_results_correct=False,
    logo='https://upload.wikimedia.org/wikipedia/commons/b/be/CDW_Logo.svg'
).run()

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
