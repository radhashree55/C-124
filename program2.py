from flask import Flask, jsonify, request

app= Flask(__name__)
@app.route('/helloworld')
def HelloWorld():
    return "Hello, world"

if (__name__ == '__main__'):
    app.run(debug=True)