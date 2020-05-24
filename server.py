from flask import Flask, render_template, redirect, request, url_for
from forms import RegistrationForm
from mailer import send_mail
from database import create_contact_table, update_contact_table, create_reg_table, update_reg_table
from database import create_mailing_table, update_mailing_table
from password import password_hash


app = Flask(__name__)

# Secret key for authentication
app.config['SECRET_KEY'] = 'd92316407ddd2e57079b9aa80cf7d334'
# Declares the database where the tables are to be created or data stored
db = 'contact'


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/mailing', methods=['GET', 'POST'])
def mailing():
    if request.method == 'POST':
        mailing_data = request.form.to_dict()
        table_name = 'mailing_list'

        create_mailing_table(db, table_name)
        update_mailing_table(db, table_name, mailing_data)

        return redirect('/home.html')

    else:
        return 'Something went wrong'


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    # validate the form successfully posts data from the user
    if request.method == 'POST' and form.validate_on_submit:
        reg_data = request.form.to_dict()
        table_name = 'register'

        # Password hashing received from the password call function
        reg_data['password'] = password_hash(reg_data['password'])

        # Database creation and storage of data
        create_reg_table(db, table_name)
        update_reg_table(db, table_name, reg_data)

        # Redirects on successful execution
        return redirect('/success.html')
    else:
        # Redirects on failed execution
        return render_template('register.html', form=form)


@app.route('/<string:html>')
def html_page(html):
    # Routes to the reqisite html template 'html' is the variable
    return render_template(html, title=html.rstrip('.html').upper())


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    # validate the form successfully posts data from the user
    if request.method == 'POST':
        contact_data = request.form.to_dict()
        table_name = 'query'

        # Database table creation and storage of data
        create_contact_table(db, table_name)

        # Query the checkbox name copy
        for response in request.form.getlist('copy'):
            if response == 'yes':
                contact_data['copy'] = 'yes'

                send_mail(contact_data['email'], contact_data['message'])
                update_contact_table(db, table_name, contact_data)

                return redirect('/success.html')

        # Updates database if copy is unchecked
        contact_data['copy'] = 'no'
        update_contact_table(db, table_name, contact_data)

        return redirect('/success.html')

    else:
        # Redirects on failed execution
        return "Something went wrong"


if __name__ == '__main__':
    app.run(debug=True)
