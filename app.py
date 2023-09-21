from flask import Flask, render_template

app = Flask(__name__)

# ...

@app.route('/')
def index():
    return render_template('index.html')

# Add a new route for Exercise 2
@app.route('/exercise2')
def exercise2():
    return render_template('index.html')  # Serve the same page as Exercise 1

if __name__ == '__main__':
    app.run(debug=True)
