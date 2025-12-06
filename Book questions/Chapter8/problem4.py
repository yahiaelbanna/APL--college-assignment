from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello, Advanced Python!"

if __name__ == '__main__':
    app.run(debug=True)