from flask import Blueprint, render_template, request, flash, Flask
import psycopg2
views = Blueprint('views', __name__)

# Routes main url to homepage
@views.route('/')
def start():
    return render_template("home.html")

# Routes to page showing all companies in database
@views.route('/companies', methods=['GET', 'POST'])
def companies():
    
    # Makes connection to database
    conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="yy!K3m1q8H0F")

    # Gets data from request form website
    data = request.form
    name = request.form.get('name')

    
    cur = conn.cursor()

    # Runs query on database
    if name:
        select_Query = f"select * from companies where (naam) ILIKE '%{name}%' OR (plaats) ILIKE '%{name}%' OR (type) ILIKE '%{name}%'"
    else:
        select_Query = "select * from companies"
    cur.execute(select_Query)
    companies = cur.fetchall()
    print(companies)
    cur.close()
    conn.close()

    return render_template("companies.html", companies = companies)

# Routes to page showing all materials in database
@views.route('/materials', methods=['GET','POST'])
def materials():

    # Connects to database
    conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="yy!K3m1q8H0F")

    # Gets data from request form website
    data = request.form
    name = request.form.get('name')

    
    # Runs query on database
    cur = conn.cursor()
    if name:
        select_Query = f"select * from materials where (naam) ILIKE '{name}'"
    else:
        select_Query = "select * from materials"
    cur.execute(select_Query)
    materials = cur.fetchall()
    print(materials)
    cur.close()
    conn.close()
    return render_template("materials.html", materials = materials)

# Routes to page showing all studies/casestudies in database
@views.route('/studies', methods=['GET'])
def studies():
    return render_template("studies.html")

# Routes to page showing login page
@views.route('/login', methods=['GET'])
def login():
    return render_template("login.html")