from flask import Flask,request, jsonify,  json
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config.from_pyfile('database.cfg')
app.config.from_pyfile('dbhost.cfg')

mysql.init_app(app)

@app.route('/experiences')
def getExperiences():
      connection = mysql.connect()
      cursor = connection.cursor()
      cursor.execute('''SELECT * FROM Persons''')
      result = cursor.fetchall()
      persons = []
      for entry in result:
        record = {
                  'id': entry[0],
                  'name': entry[1],
            }
        persons.append(record)		

      return json.dumps(result)


@app.route('/projects',methods=['GET'])
def getProjects():
    return 'projects'

@app.route('/blogs',methods=['GET'])
def getBlogs():
    return jsonify({
    "massage":"Succecfull",    
    "satus":100,    
    "blogs": [
    {
      "url": "https://blog.usejournal.com/create-a-google-assistant-action-and-win-a-google-t-shirt-and-cloud-credits-4a8d86d76eae",
      "title": "Win a Google Assistant Tshirt and $200 in Google Cloud Credits",
      "description": "Do you want to win $200 and Google Assistant Tshirt by creating a Google Assistant Action in less then 30 min?"
    },
    {
      "url": "https://medium.com/@saadpasta/why-react-is-the-best-5a97563f423e",
      "title": "Why REACT is The Best?",
      "description": "React is a JavaScript library for building User Interface. It is maintained by Facebook and a community of individual developers and companies."
    }
  ]
})

# . venv/bin/activate
# export FLASK_APP=hello.py
# flask run