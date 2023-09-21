from flask import Flask, render_template


import random

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# Added a new route for Exercise 2
@app.route('/exercise2')
def exercise2():
    return render_template('index.html')  # Served the same page as Exercise 1


# A list of random quotes
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


if __name__ == '__main__':
    app.run(debug=True)
