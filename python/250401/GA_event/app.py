from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/item_info')
def item_info():
    user_select = int(request.args['item'])
    return render_template('item_info.html',
                           selected = user_select)

@app.route('/shop')
def shop():
    item_cnt = int(request.args['cnt'])
    item_price = int(request.args['price'])
    return render_template('shop.html',
                           price = item_cnt * item_price)

app.run(debug=True)