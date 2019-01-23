from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#Mysql Conexion
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)

# configuraciones
#Como ira protegida nuestra sesion
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', contacts=data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur= mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)', (fullname, phone, email))
        mysql.connection.commit()

        flash('Contacto agregado satisfactoriamente')

        return redirect(url_for('index'))

#@app.route('/edit/<id>', methods=['POST'])
#def get_contact(id):
 #   if request.method == 'POST':
  #      cur = mysql.connection.cursor()
   #     cur.execute('SELECT * FROM contacts WHERE id = %s', (id))
    #    data = cur.fetchall()
     #   print(data)
      #  return render_template(url_for('edit_contact.html', contact = data[0]))

#@app.route('/update/<id>', methods=['POST'])
#def update_contact(id):
 #   if request.method == 'POST':
  #      fullname = request.form['fullname']
   #     phone = request.form['phone']
    #    email = request.form['email']
     #   cur = mysql.connection.cursor()
      #  cur.execute("""
       #     UPDATE contacts
        #    SET fullname = %s,
         #       phone = %s,
          #      email = %s
           # WHERE id = %s
        #""", (fullname, phone, email, id))
       # flash('Contacto actualizado')
    #    mysql.connection.commit()
  #      return redirect(url_for('index'))

@app.route('/delete_contact/<string:id>')
def deleteContact(id):
    cur= mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id= {0}'.format(id))
    mysql.connection.commit()
    flash('Contacto eliminado con exito')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)