from flask import Blueprint, render_template, request, flash

# Blueprint it means this file has lots of rules inside, lots of urls defined.
# 同时可以让 views seperate 到不同的 files
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():

    data = request.form
    print(data)
    # the text and user variable 能够被 login.html 访问到, see details in login.html
    return render_template("login.html", text="Testing", user="Tim", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')

        elif len(firstName) < 2:
            flash('Frist Name must be greater than 2 characters.', category='error')

        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')

        elif len(password1) < 7:
            flash('Password must be greater than 7 characters.', category='error')

        else:
            # add user to database
            flash('Account created!', category='success')

    return render_template("sign_up.html")


