from flask import Flask, render_template, request
import mysql.connector as sql
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def home_page():
    return render_template('home.htm')

@app.route('/newemp/')
def new_emp():
    return render_template('emp.htm')

@app.route('/registration/', methods = ['POST', 'GET'])
def registration_page():
    msg = ''
    if request.method == 'POST':

        try:
            print("In try statement")
            empID = request.form['EmpID']
            empName = request.form['EmpName']
            empGender = request.form['EmpGender']
            empPhone = request.form['EmpPhone']
            empBdate = request.form['EmpBdate']
            print("")
            print("We created the variables")
            print(f"Received id: {empID}")
            print(f"Received name: {empName}")
            print(f"Received gender: {empGender}")
            print(f"Received phone: {empPhone}")
            print(f"Received bday: {empBdate}")

            with sql.connect(host = "localhost", user = "James", password = "bob14228", database = "new_employee") as con:
                print("")
                print("Connected to MySQL")
                cur = con.cursor()
                print("")
                print("TEST")
                cur.execute("INSERT INTO employee (EmpID, EmpName, EmpGender, EmpPhone, EmpBdate) VALUES('{0}', '{1}', '{2}', '{3}', '{4}');".format(empID, empName, empGender, empPhone, empBdate))

                print("SQL Statement has been executed")
                con.commit()
                print("Committed")
                msg = "Record successfully added"
                con.close()
                print("Connection closed")

        except:
            #print("In except statement")
            con.rollback()
            msg = "Error in insert operation"
            con.close()
        finally:
            #print("In finally statement")
            return render_template("registration.htm", msg = msg)


@app.route('/information/')
def information_page():
    con = sql.connect(host = "localhost", user = 'James', password = 'bob14228', database = "new_employee")

    cur = con.cursor()
    cur.execute("SELECT * FROM employee;")

    rows = cur.fetchall()
    print(rows)
    return render_template('information.htm', rows = rows)

if __name__ == "main":
    app.run(debug == True)
