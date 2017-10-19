from bottle import route,run, template

@route('/')
def hello():
    return "Hello World"

Stranger=input("Enter name of the user ")

@route('/hello')
def greet(name=Stranger):
    return template('Hello {{name}},How are you?',name=name)


run(host='localhost',port=8080,debug=True)
