from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')

def index():
	return render_template('index.html')

@app.route('/blog')
def blog() :
    return render_template('blog.html')

@app.route('/test/<username>')
def test(username) :
    print(username)
    return render_template('test_result.html', name = username)

@app.route('/method', methods = ['GET', 'POST'])
def method() :
    if request.method == 'POST' :
        print('Post')
    else :
        print('Get')
    return request.method
if __name__ == '__main__' :
    app.run(debug = True, port = 80)


