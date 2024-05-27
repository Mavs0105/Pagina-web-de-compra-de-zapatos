from flask import Flask, render_template
from flask_bootstrap import Bootstrap
shoes = [
    {
        'name': 'Nike Air Max 👟',
        'description': 'Zapatillas Nike air Max poco usadas y en perfecto estado',
        'price': '544.990'
    },
    {
        'name': 'Adidas Superstar 👞',
        'description': 'Zapatillas adidas superstar sin usar',
        'price': '350.000'
    },
    {
        'name': 'Vans Old Skool 🥾',
        'description': 'Zapatillas vans old skool ligeramente usadas, perfectas para uso casual',
        'price': '209.990'
    }
]

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html', shoes = shoes)

if __name__ == '__main__':
    app.run(debug=True)
