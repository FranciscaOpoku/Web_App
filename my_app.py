from flask import Flask, render_template, request, redirect
 
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
    app.run(debug=True, host='0.0.0.0')
