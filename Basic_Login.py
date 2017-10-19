from bottle import get, post, request, run,template

@get('/')
def login():
      return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
           <br/>
            <input value="Login" type="submit" />
        </form>
    '''
@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p> "+username+" your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

def check_login(username, password):
    if((username=='chai') and (password=='1234')):
        return True
    
run(host='localhost', port=8080, debug=True)
