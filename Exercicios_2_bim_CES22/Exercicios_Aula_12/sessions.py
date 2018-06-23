from flask import Flask, session, render_template, request, redirect, g, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('home'))
    return '''
	
   <form id="login" action="" method="post">
    Usuario :  <input type="text" id="username" name="username">
    Senha : <input type="password" id="password" name="password">
    <input type="submit" id="submit" text="Login">
</form>
	
   '''

@app.route('/home')
def home():
    if 'username' in session:
      username = session['username']
      return 'Bem-vindo ' + username + '<br>' + \
         "<b><a href = '/sair'>clique aqui para sair</a></b>"


@app.route('/sair')
def sair():
    session.pop('user', None)
    return 'Saiu!'

if __name__ == '__main__':
    app.run(debug=True)

