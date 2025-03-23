from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/home.html')
def home1():
    return render_template('home.html')
# Route for about page
@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/portfolio.html')
def portfolio():
    return render_template('portfolio.html')

@app.route('/services.html')
def services():
    return render_template('services.html')

# Route for contact page
@app.route('/contact.html')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)