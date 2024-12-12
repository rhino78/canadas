from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'yes'

account_sid = ''
auth_token = ''
twilio_number = ''
# client = Client(account_sid, auth_token)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/patient')
def patient():
    return render_template('patient.html')


@app.route('/ma')
def medicalassistant():
    return render_template('medicalassistant.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    # retrieve form data
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if not name or not email or not message:
        flash('All fields required', 'error')
        return redirect(url_for('contact'))

    flash('Your message has been sent successfully', 'success')
    return redirect(url_for('contact'))


@app.route('/confirmation')
def confirmation():
    slot = request.args.get('slot')
    return render_template('confirmation.html', slot=slot)


def send_sms(phone, slot):
    print('phone: {0} slot:{1}'.format(phone, slot))


if __name__ == '__main__':
    app.run(debug=True)
