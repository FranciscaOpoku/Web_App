from flask import Flask, render_template, request, redirect
import os
app = Flask(__name__)
items=[]
@app.route('/')
def index():
    return render_template('form.html',items=items)
    
@app.route('/add_todo')
def add_todo():
    item=request.args.get('item')
    items.append(item)
   
    return redirect("/",code=302 )

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(debug=True, host='0.0.0.0',port=port)
