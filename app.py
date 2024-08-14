from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Necessary for flash messages

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'szerencsi.kristof@gmail.com'
app.config['MAIL_PASSWORD'] = 'jzbv wjdu mkfp icqw'

mail = Mail(app)

# Sample product data
products = {
    'hot_or_not': {
        'name': 'Hot or Not?!',
        'description': 'This is a special one! Our podium cocktail at the Austrian Bartender Awards. Old brand. Old logo. Old bottle. The same popular taste and characteristics of: Vodka, Vermout and our Sangria-Blend with Cherry, Strawberry, Spices and much more... much more love! ...pssst, stock is selling out fast and will never be produced again in this form, so hurry and get yourself any of our Old but Gold cocktails.',
        'image': 'images/cocktail2.jpg'
    },
    'what_the_melon': {
        'name': 'What the Melon?! ',
        'description': 'Old brand. Old logo. Old bottle. The same popular taste and characteristics of: Vodka, Watermelon, Lime, Mint.',
        'image': 'images/cocktail3.jpg'
    },
    'horny_bae': {
        'name': 'Horny Bae',
        'description': 'Old brand. Old logo. Old bottle. The same popular taste and characteristics of: White Rum, Cucumber, Pineapple, Almond, Melon.',
        'image': 'images/cocktail4.jpg'
    },
    'wet_ginger': {
        'name': 'Wet Ginger',
        'description': 'Old brand. Old logo. Old bottle. The same popular taste and characteristics of: Gin, Ginger, Lemon, Cucumber, Pink Pepper.',
        'image': 'images/cocktail5.jpg'
    },
    'hot_or_not_obg': {
        'name': 'Hot or Not?! O.b.g Edition',
        'description': 'This is a special one! Our podium cocktail at the Austrian Bartender Awards. Old brand. Old logo. Old bottle. The same popular taste and characteristics of: Vodka, Vermout and our Sangria-Blend with Cherry, Strawberry, Spices and much more... much more love! ...pssst, stock is selling out fast and will never be produced again in this form, so hurry and get yourself any of our Old but Gold cocktails.',
        'image': 'images/hotornotobg.jpg'
    },
    'what_the_melon_obg': {
        'name': 'What the Melon?! O.b.g Edition',
        'description': 'Old brand. Old logo. Old bottle. The same popular taste and characteristics of: Vodka, Watermelon, Lime, Mint.',
        'image': 'images/whatthemelonobg.jpg'
    },
    'horny_bae_obg': {
        'name': 'Horny Bae O.b.g Edition',
        'description': 'Old brand. Old logo. Old bottle. The same popular taste and characteristics of: White Rum, Cucumber, Pineapple, Almond, Melon.',
        'image': 'images/hornybaeobg.jpg'
    },
    'wet_ginger_obg': {
        'name': 'Wet Ginger O.b.g Edition',
        'description': 'Old brand. Old logo. Old bottle. The same popular taste and characteristics of: Gin, Ginger, Lemon, Cucumber, Pink Pepper.',
        'image': 'images/wetgingerobg.jpg'
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/references')
def references():
    return render_template('references.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/products')
def products_route():
    return render_template('products.html', products=products)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/product_detail/<product_id>')
def product_detail(product_id):
    product = products.get(product_id)
    if not product:
        return 'Product not found', 404
    return render_template('product_detail.html', product=product)

@app.route('/order', methods=['POST'])
def order():
    email = request.form['order-email']
    if email:
        msg = Message('Order Confirmation', recipients=[email])
        msg.body = 'Thank you for your order. We will process it shortly.'
        mail.send(msg)
        flash('Order email sent successfully!', 'success')
    else:
        flash('Failed to send email. Please try again.', 'danger')
    return redirect(url_for('contacts'))

if __name__ == '__main__':
    app.run(debug=True)
