from flask import Flask,redirect,url_for,request,render_template

app=Flask(__name__)
@app.route('/success/<name>')
def my_work(name):
    return 'successfully loged in {}'.format(name)

@app.route('/login/<user>')
def login(user):
    return render_template('login.html',name=user)
    # if request.method=='POST':
    #     user = request.form['nm']
    #     return redirect(url_for('my_work',name=user))
    # else:
    #     user = request.args.get('nm')
    #     return redirect(url_for('my_work',name=user))


    
# @app.route('/hello/<name>')
# def hello_world(name):
#     if name=='admin':
#         return redirect(url_for('my_work'))
#     else:
#         return 'hello world {}'.format(name)

if __name__=='__main__':
    app.run(debug=True)