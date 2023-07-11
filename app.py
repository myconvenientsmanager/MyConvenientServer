from flask import Flask, redirect, request, render_template

app = Flask(__name__, static_folder='templates/static')

@app.before_request
def enforce_ssl():
    if not request.is_secure:
        # Thực hiện redirect đến URL mới với giao thức HTTPS
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
