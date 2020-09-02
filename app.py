from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/projects', methods=['GET'])
def projects():
    # return 'Projects'
    return render_template('projects.html')

@app.route('/aclu', methods=['GET'])
def aclu():
    # return 'Projects'
    return render_template('aclu.html')

if __name__ == '__main__':
    app.run(debug=True)
