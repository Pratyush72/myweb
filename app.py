from flask import Flask, render_template, request, redirect, url_for, session, flash,jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message 
from const import Connect, createTable, connectToDatabase
from models import User
import razorpay
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Email configuration
# app.config['MAIL_SERVER'] = 'smtp.your-email-provider.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'pratyush2chaubey@gmail.com'
# app.config['MAIL_PASSWORD'] = 'infr eubk pnwl aucq'
# mail = Mail(app)

# Create tables if they don't exist
createTable()

Session = connectToDatabase()
db_session = Session()

@app.route('/')
def index():
    username = session.get('username')
    return render_template('index.html', username=username)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:
            username = request.form['username']
            email = request.form['email']
            password = generate_password_hash(request.form['password'], method='pbkdf2:sha256')
            new_user = User(username=username, email=email, password=password)
            
            # Check if email already exists
            existing_user = db_session.query(User).filter_by(email=email).first()
            if existing_user:
                flash('Email already registered.', 'danger')
                return render_template('signup.html')
            
            db_session.add(new_user)
            db_session.commit()
            flash('Account created successfully!', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db_session.rollback()
            flash(f'Error: {str(e)}', 'danger')
            return render_template('signup.html')
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            email = request.form['email']
            password = request.form['password']
            user = db_session.query(User).filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                session['username'] = user.username
                return redirect(url_for('index'))
            flash('Invalid email or password', 'danger')
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        try:
            email = request.form['email']
            user = db_session.query(User).filter_by(email=email).first()
            if user:
                new_password = generate_password_hash(request.form['new_password'], method='pbkdf2:sha256')
                user.password = new_password
                db_session.commit()
                flash('Password updated successfully!', 'success')
                return redirect(url_for('login'))
            flash('Email not found', 'danger')
        except Exception as e:
            db_session.rollback()
            flash(f'Error: {str(e)}', 'danger')
    return render_template('reset_password.html')


@app.route('/home')
def home():
    return redirect(url_for('index'))


@app.route('/portfolio', methods=['GET', 'POST'])
def portfolio():
    return render_template('portfolio.html')

@app.route('/free' , methods =['GET', 'POST'])
def free():
    
    return render_template('free.html')



# razorpay_client = razorpay.Client(auth=("rzp_test_tV8hhS0olbbfGd", "bLZMe2pOY0hqOysqLAZriZoX"))


@app.route('/paidproject', methods=['GET'])
def paidproject():
    return render_template('p-project.html')




import logging
from flask_mail import Mail, Message

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'pratyush2chaubey@gmail.com'
app.config['MAIL_PASSWORD'] = 'infr eubk pnwl aucq'
app.config['MAIL_DEFAULT_SENDER'] = 'pratyush2chaubey@gmail.com'

mail = Mail(app)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            message = request.form['message']

            # Send email
            msg = Message('New Contact Form Submission',
                          sender='pratyush2chaubey@gmail.com',
                          recipients=['pratyush2chaubey@gmail.com'])
            msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            mail.send(msg)

            flash('Message sent successfully!', 'success')
            return render_template('portfolio.html')
        except Exception as e:
            logging.error('Error sending email', exc_info=True)
            flash(f'An error occurred: {str(e)}', 'danger')

    return render_template('base.html')

# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
#     if request.method == 'POST':
#         try:
#             name = request.form['name']
#             email = request.form['email']
#             message = request.form['message']

#             # Social Media Links with Logos in a Row (HTML format)
#             social_media_links = """
#             <p>Social Media Links:</p>
#             <p>
#                 <a href="https://github.com/Pratyush72" target="_blank" title="GitHub" style="display: inline-block; margin-right: 10px;">
#                     <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub" style="width:24px;height:24px;"> 
#                 </a>
#                 <a href="https://www.linkedin.com/in/pratyush-chaubey-8ab289188" target="_blank" title="LinkedIn" style="display: inline-block; margin-right: 10px;">
#                     <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" style="width:24px;height:24px;"> 
#                 </a>
#                 <a href="https://codepen.io/@Pratyush-Chaubey" target="_blank" title="CodePen" style="display: inline-block; margin-right: 10px;">
#                     <img src="https://blog.codepen.io/wp-content/uploads/2012/06/Button-White-Large.png" alt="CodePen" style="width:24px;height:24px;"> 
#                 </a>
#                 <a href="https://youtube.com/@softwareengineer72" target="_blank" title="YouTube" style="display: inline-block; margin-right: 10px;">
#                     <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/YouTube_icon_%282013-2017%29.png/1024px-YouTube_icon_%282013-2017%29.png" alt="YouTube" style="width:24px;height:24px;"> 
#                 </a>
#                 <a href="https://www.instagram.com/pratyush_72" target="_blank" title="Instagram" style="display: inline-block; margin-right: 10px;">
#                     <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram" style="width:24px;height:24px;"> 
#                 </a>
#             </p>
#             """

#             # Send email
#             msg = Message('New Contact Form Submission',
#                           sender='pratyush2chaubey@gmail.com',
#                           recipients=['pratyush2chaubey@gmail.com'])
#             msg.html = f"""
#             <p>Name: {name}</p>
#             <p>Email: {email}</p>
#             <p>Message:</p>
#             <p>{message}</p>
#             <br>
#             {social_media_links}
#             """
#             mail.send(msg)

#             flash('Message sent successfully!', 'success')
#             return render_template('portfolio.html')
#         except Exception as e:
#             logging.error('Error sending email', exc_info=True)
#             flash(f'An error occurred: {str(e)}', 'danger')

#     return render_template('base.html')





if __name__ == '__main__':
    app.run(debug=True)
