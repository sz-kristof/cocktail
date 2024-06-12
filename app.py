from flask import Flask, render_template, url_for

app = Flask(__name__)

# Sample product data
products = {
    'hot_or_not': {
        'name': 'Hot or Not?! - O.b.G. Edition',
        'description': 'This is a special one! Our podium cocktail at the Austrian Bartender Awards. Old brand. Old logo. Old bottle. The same popular taste and characteristics of: Vodka, Vermout and our Sangria-Blend with Cherry, Strawberry, Spices and much more... much more love! ...pssst, stock is selling out fast and will never be produced again in this form, so hurry and get yourself any of our Old but Gold cocktails.',
        'image': 'images/cocktail2.jpg'
    },
    'what_the_melon': {
        'name': 'What the Melon?! - O.b.G. Edition',
        'description': 'Old brand. Old logo. Old bottle. The same popular taste and characteristics of: Vodka, Watermelon, Lime, Mint.',
        'image': 'images/cocktail3.jpg'
    },
    'horny_bae': {
        'name': 'Horny Bae - O.b.G. Edition',
        'description': 'Old brand. Old logo. Old bottle. The same popular taste and characteristics of: White Rum, Cucumber, Pineapple, Almond, Melon.',
        'image': 'images/cocktail4.jpg'
    },
    'wet_ginger': {
        'name': 'Wet Ginger - O.b.G. Edition',
        'description': 'Old brand. Old logo. Old bottle. The same popular taste and characteristics of: Gin, Ginger, Lemon, Cucumber, Pink Pepper.',
        'image': 'images/cocktail5.jpg'
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

if __name__ == '__main__':
    app.run(debug=True)
