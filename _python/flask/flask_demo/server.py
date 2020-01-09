from flask import Flask, render_template

app = Flask(__name__)
print(__name__)

# get request
@app.route('/')
def index():
    return "Hello World"

# get request
@app.route('/cats')
def cats():
    return render_template('index.html')

#get request, with route parameter
@app.route('/dog/<number>')
def dogs(number):
    print(number)
    return render_template('dogs.html', amount = number)


if __name__ == '__main__':
    app.run(debug=True)