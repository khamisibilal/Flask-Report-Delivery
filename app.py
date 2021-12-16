from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/report')
def report():
    username = request.args.get('username')


    if (any(x.isupper() for x in username) and any(x.islower() for x in username)
            and any(x.isdigit() for x in username) and len(username) >= 7):

        username = request.args.get('username')
    else:

        errors =[]
        if not any(x.isupper() for x in username):
            errors.append('Your password needs at least 1 capital.')
        if not any(x.islower() for x in username):
            errors.append('Your password needs at least 1 small letter.')
        if not any(x.isdigit() for x in username):
            errors.append('Your password needs at least 1 digit.')
        if not any(x.len() for x in username):
            errors.append('Your password should be at least 7 letters.')

        return render_template('report.html', username=username,errors=errors)


if __name__ == '__main__':
    app.run(debug=True)
