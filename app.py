from flask import Flask, render_template, request, session, url_for
from api import fetch_offers, format_offer
import secrets

app = Flask(__name__)
# Generate a secret key for session management
app.secret_key = secrets.token_hex(16)

@app.route('/')
def index():
    shopping_list = session.get('shopping_list', [])
    return render_template('index.html', shopping_list=shopping_list)

@app.route('/search')
def search():
    query = request.args.get('q', '')
    if not query:
        return ""

    raw_offers = fetch_offers(query=query)
    offers = [format_offer(o) for o in raw_offers]
    return render_template('results.html', offers=offers)

@app.route('/add_to_list', methods=['POST'])
def add_to_list():
    item = {
        'id': request.form.get('id'),
        'heading': request.form.get('heading'),
        'price': request.form.get('price'),
        'currency': request.form.get('currency'),
        'store_name': request.form.get('store_name'),
        'image': request.form.get('image')
    }

    shopping_list = session.get('shopping_list', [])

    # Avoid duplicates based on ID
    if not any(i['id'] == item['id'] for i in shopping_list):
        shopping_list.append(item)
        session['shopping_list'] = shopping_list
        session.modified = True

    return render_template('shopping_list.html', items=shopping_list)

@app.route('/remove_from_list', methods=['POST'])
def remove_from_list():
    item_id = request.form.get('id')
    shopping_list = session.get('shopping_list', [])

    shopping_list = [i for i in shopping_list if i['id'] != item_id]
    session['shopping_list'] = shopping_list
    session.modified = True

    return render_template('shopping_list.html', items=shopping_list)

@app.route('/list')
def get_list():
    shopping_list = session.get('shopping_list', [])
    return render_template('shopping_list.html', items=shopping_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
