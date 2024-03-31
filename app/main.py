from flask import Flask,redirect,url_for,request,render_template

app=Flask(__name__)
@app.route('/success/<name>')
def my_work(name):
    return 'successfully loged in {}'.format(name)

@app.route('/request', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        print("lll")
        return redirect(url_for('yes_request'))
        # return render_template('yes.html')
    return render_template('login.html')
@app.route('/yes_request')
def yes_request():
    return render_template('yes.html')
    # if request.method=='POST':
    #     user = request.form['nm']
    #     return redirect(url_for('my_work',name=user))
    # else:
    #     user = request.args.get('nm')
    #     return redirect(url_for('my_work',name=user))



if __name__=='__main__':
    app.run(debug=True)