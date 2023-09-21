from flask import Flask, render_template, redirect, url_for, request

import random

import json

DATA_FILE = 'form_submissions.json'

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# Added a new route for Exercise 2
@app.route('/exercise2')
def exercise2():
    return render_template('index.html')  # Served the same page as Exercise 1


# A list of random quotes by Steve Jobs.
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Innovation distinguishes between a leader and a follower. - Steve Jobs",
    "Stay hungry, stay foolish. - Steve Jobs",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "Design is not just what it looks like and feels like. Design is how it works. - Steve Jobs"
]

# Created a route for Exercise 3
@app.route('/exercise3')
def exercise3():
    # Generated a random quote
    random_quote = random.choice(quotes)
    return render_template('exercise3.html', quote=random_quote)



@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Got form data from the request
        name = request.form.get('name')
        email = request.form.get('email')

        # Created a dictionary with the form data
        submission = {'name': name, 'email': email}

        # Stored the form submission in the JSON file
        submissions = []
        try:
            with open(DATA_FILE, 'r') as file:
                submissions = json.load(file)
        except FileNotFoundError:
            pass  

        submissions.append(submission)

        with open(DATA_FILE, 'w') as file:
            json.dump(submissions, file, indent=4)


    return render_template('form.html')


@app.route('/submissions')
def submissions():
    try:
        with open(DATA_FILE, 'r') as file:
            submissions = json.load(file)

        return render_template('submissions.html', submissions=submissions)
    except FileNotFoundError:
        return "No submissions yet."



if __name__ == '__main__':
    app.run(debug=True)
