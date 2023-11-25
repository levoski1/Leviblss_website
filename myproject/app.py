#!/usr/bin/python3

from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id' : 1,
    'tittle' : 'front-end developer',
    'location': 'Enugu',
    'salary' : '$200-000'
},

{
    'id' : 2,
    'tittle' : 'Back-end developer',
    'location': 'Anambra',
    'salary' : '$150-000'
},

{
    'id' : 3,
    'tittle' : 'Data Analysis developer',
    'location': 'Ebonyi',
    'salary' : '$90-000'
},

{
    'id' : 4,
    'tittle' : 'Cyber-Security developer',
    'location': 'Abia',
    
},
{
    'id' : 5,
    'tittle' : 'Software Engineer',
    'location' : 'Ikwo',
    'Salary' : '$30000',
}]


@app.route("/")
def hello_world():
    return render_template("home.html",jobs=JOBS,
                           __siteName__='LEVIBLISS')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090, debug=True)
 
