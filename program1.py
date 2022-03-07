from flask import Flask, jsonify, request

app= Flask(__name__)
tasks= [
    {
        "id":1,
        "title":U"Buy groceries",
        "description":"milk,cheese,carrots",
        'done': False
    }
]
@app.route("/addData", methods= ['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status':'error',
            'message': 'Please provide the data'
        },400)
    task={
            'id': tasks[-1]['id']+1,
            'title': request.json['title'],
            'description': request.json.get('description', ''),
            'done': False
    }
    tasks.append(task)
    return jsonify({
        'status': 'success',
        'message': 'Task added successfully'
    })
@app.route('/getData')
def getTask():
    return jsonify({
        'data': tasks
    })

if (__name__ == '__main__'):
    app.run(debug=True)