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
  },
  {
    'id':4,
    'title':'Data Analyst',
    'Experiance':'1 Year',
    'location': 'WFH'
  }
  
]

SERVICES=[
  {
    'id':1,
    'title':'Web Development',
  },
  {
    'id':2,
    'title':'APP Development',
  },
  {
    'id':3,
    'title':'Digital Marketing',
  },
  {
    'id':4,
    'title':'Market Research',
  },
  {
    'id':5,
    'title':'Data Analytics',
  },
  {
    'id':6,
    'title':'Business Analytics',
  }
]
@app.route('/')
def hello_world():
  return render_template('home.html',
                        jobs=JOBS,services=SERVICES)

@app.route('/api/jobs')
def list_jobs():
  return render_template('jobpage.html')


@app.route('/services')
def list_services():
  return jsonify(SERVICES)

@app.route('/services/web')
def list_web():
  return render_template('web_development.html')

@app.route('/services/app')
def list_app():
  return render_template('App_development.html')

@app.route('/services/digital')
def list_digital():
  return render_template('digital_marketing.html')

@app.route('/services/research')
def list_research():
  return render_template('market_research.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)