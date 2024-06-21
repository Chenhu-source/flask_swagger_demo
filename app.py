from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='API示例', description='一个简单的API')

ns = api.namespace('todos', description='TODO操作')

todos = {1: {'task': '构建一个API'}}

todo_model = api.model('Todo', {
    'task': fields.String(description='任务描述')
})

@ns.route('/<int:id>')
@ns.response(404, '任务未找到')
@ns.param('id', '任务标识符')
class TodoResource(Resource):
    @ns.doc('获取任务')
    @ns.marshal_with(todo_model)
    def get(self, id):
        if id not in todos:
            api.abort(404, f"任务 {id} 不存在")
        return todos[id]

@ns.route('/')
class TodoListResource(Resource):
    @ns.doc('列出任务')
    @ns.marshal_list_with(todo_model)
    def get(self):
        return todos

    @ns.doc('创建任务')
    @ns.expect(todo_model)
    def post(self):
        id = max(todos.keys()) + 1
        todos[id] = {'task': api.payload['task']}
        return todos[id], 201

api.add_namespace(ns)

if __name__ == '__main__':
    app.run(debug=True)

