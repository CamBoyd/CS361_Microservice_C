# Configuration
from flask import *
import os
import flask_mysqldb

app = Flask(__name__)

# Continue with database initialization using secret username / password.
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'CarbonCrash'
app.config['MYSQL_DB'] = 'invoicetracking'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"
app.config['SECRET_KEY'] = 'secret!'
mysql = flask_mysqldb.MySQL(app)

# Routes 

@app.route('/', methods=["POST"])
def home():
    data = request.json
    user = data.get("username")
    validation_type = data.get("validation_type")

    if validation_type == "Admin":
        return admin_access_validation(user)
    if validation_type == "AR":
        return ar_access_validation(user)
    if validation_type == "AP":
        return ap_access_validation(user)

    return "Microservice C"

def admin_access_validation(user):
    query = """
        SELECT
            1
        FROM Users
        WHERE
            Username = %s AND
            AdminAccess = 1
    """
    cursor = mysql.connection.cursor()
    cursor.execute(query, (user,))
    results = cursor.fetchall()
    if len(results) > 0:
        return Response(status=200)

def ar_access_validation(user):
    query = """
        SELECT
            1
        FROM Users
        WHERE
            Username = %s AND
            ARAccess = 1
    """
    cursor = mysql.connection.cursor()
    cursor.execute(query, (user,))
    results = cursor.fetchall()
    if len(results) > 0:
        return Response(status=200)

def ap_access_validation(user):
    query = """
        SELECT
            1
        FROM Users
        WHERE
            Username = %s AND
            APAccess = 1
    """
    cursor = mysql.connection.cursor()
    cursor.execute(query, (user,))
    results = cursor.fetchall()
    if len(results) > 0:
        return Response(status=200)

# Listener

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 50002)) 
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(port=port)