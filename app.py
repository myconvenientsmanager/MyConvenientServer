from flask import Flask, redirect, request

app = Flask(__name__)

@app.before_request
def enforce_ssl():
    if not request.is_secure:
        # Thực hiện redirect đến URL mới với giao thức HTTPS
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)

@app.route('/')
def home():
    return 'Đây là trang chủ nhé Triple D!'

if __name__ == '__main__':
    app.run()
