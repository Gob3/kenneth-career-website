from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "Sekondi, Takoradi",
        "salary": "55,000ghc"
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "location": "Apremdo, Takoradi",
        "salary": "70,000ghc"
    },
    {
        "id": 3,
        "title": "Frontend Engineer",
        "location": "New Takoradi, Takoradi",
        #"salary": "50,000ghc"
    },
    {
        "id": 4,
        "title": "Backend Engineer",
        "location": "New Takoradi, Takoradi",
        "salary": "80,000ghc"
    }
]


@app.route('/')
def hello_world():
    return render_template("home.html", jobs=JOBS, company_name="Gob3")


@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
