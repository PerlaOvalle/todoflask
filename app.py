from flask import Flask, json
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'todo'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()

cursor = conn.cursor()






@app.route('/')
def main():
    return 'Bienvenido a la api todo 0.0.1'


@app.route('/todo')
def select_todos():
    query = cursor.execute('SELECT * FROM todo')
    data = cursor.fetchall()
    return json.dumps({'data': data, 'status': 200})

@app.route('/todo/<int:id>')
def select_todo(id):
    query = cursor.execute('SELECT * FROM todo WHERE id=' + str(id))
    response = cursor.fetchall()
    return json.dumps({'status': 200, 'todo': response})

if __name__ == "__main__":
    app.run()