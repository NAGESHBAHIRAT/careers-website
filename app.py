from flask import Flask, render_template, jsonify
app=Flask(__name__)
JOBS=[
  {
    'id':1,
    'title':'Business Development Execative',
    'Experiance':'1 Year',
    'location': 'WFH'
  },
  {
    'id':2,
    'title':'Python Developer',
    'Experiance':'2 Year',
    'location': 'WFH'
  },
  {
    'id':3,
    'title':'Android Developer',
    'Experiance':'2 Year',
    'location': 'WFH'
  }
  
]
@app.route('/')
def hello_world():
  return render_template('home.html',
                        jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)
  
if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)