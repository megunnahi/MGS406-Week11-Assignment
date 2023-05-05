from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

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

            with sqlite3.connect('/home/jbai/week12/MGS406-Week11-Assignment/flask_project/employee.db') as con:
                print("")
                print("Connected")
                cur = con.cursor()
                print("")
                print("TEST")
                cur.execute("INSERT INTO information (EmpID, EmpName, EmpGender, EmpPhone, EmpBdate) VALUES('{0}', '{1}', '{2}', '{3}', '{4}');".format(empID, empName, empGender, empPhone, empBdate))

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
    con = sqlite3.connect('/home/jbai/week12/MGS406-Week11-Assignment/flask_project/employee.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM information;")

    rows = cur.fetchall()
    return render_template('information.htm', rows = rows)

if __name__ == "main":
    app.run(debug == True)
