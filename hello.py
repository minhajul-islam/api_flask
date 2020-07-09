from flask import Flask,request, jsonify,  json
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config.from_pyfile('database.cfg')
app.config.from_pyfile('dbhost.cfg')

mysql.init_app(app)

@app.route('/course')
def getExperiences():
      connection = mysql.connect()
      cursor = connection.cursor()
      cursor.execute('''SELECT * FROM course''')
      result = cursor.fetchall()
      course = []
      for entry in result:
        record = {
                  'ID': entry[0],
                  'title': entry[1],
                  'details': entry[2],
                  'rating': entry[3],
                  'price': entry[4],
            }
        course.append(record)		

      return json.dumps(result)



@app.route('/courseDetails/<ID>')
def getCourseDetails(ID):

  connection = mysql.connect()
  cursor = connection.cursor()

  # cursor.execute('''SELECT * FROM course WHERE ID=entr ''')
  # resultForCourse = cursor.fetchall()

  sql = "SELECT * FROM course_section WHERE project_id = (%s)" % (ID)
  cursor.execute(sql)
  resultForSection = cursor.fetchall()

  cursor.execute('''SELECT * FROM content''')
  resultForContent = cursor.fetchall()
  
  # response = {}
  sections = []
  course_section = []
  for entry in resultForSection:
    contents = [];
    for entryContent in resultForContent:
      content = {
        'id':entryContent[0],
        'title':entryContent[1],
        'url': entryContent[2]
      }
      if entryContent[6] == entry[0]: 
        contents.append(content) 

    sections = {
      'ID': entry[0],
      'title': entry[1],
      'lecture': entry[2],
      'duration': entry[3],
      'project_id': entry[4],
      'contents': contents
    } 
    course_section.append(sections)

  



  response = {
    'status':100,
    'message':"successfull",
    'data':{
      'sections':course_section
      
    }
  }

  return json.dumps(response)


      
@app.route('/section')
def getSection():
      connection = mysql.connect()
      cursor = connection.cursor()
      cursor.execute('''SELECT * FROM course_section''')
      result = cursor.fetchall()
      course_section = []
      for entry in result:
        record = {
                  'ID': entry[0],
                  'title': entry[1],
                  'lecture': entry[2],
                  'duration': entry[3],
                  'project_id': entry[4],
            }
        course_section.append(record)		

      return json.dumps(result)




@app.route('/contentlist')
def getContent():
      connection = mysql.connect()
      cursor = connection.cursor()
      cursor.execute('''SELECT * FROM content''')
      result = cursor.fetchall()
      content = []
      for entry in result:
        record = {
                  'ID': entry[0],
                  'title': entry[1],
                  'duration': entry[2],
                  'url': entry[3],
                  'notes': entry[4],
                  'serial': entry[5],
                  'section_id': entry[6],
            }
        content.append(record)		

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
# /usr/local/mysql/bin/mysql -u root -p