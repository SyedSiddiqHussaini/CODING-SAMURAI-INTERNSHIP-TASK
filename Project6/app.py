import os
from flask import Flask, render_template, redirect, url_for, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ssh-blogs-personal-project-2026'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ssh_blog.db'

db = SQLAlchemy(app)

# --- MODELS ---
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()

# --- ROUTES ---

@app.route('/')
@app.route('/home')
def home():
    all_posts = Post.query.all()
    all_feedback = Feedback.query.all()
    return render_template('home.html', posts=all_posts, feedbacks=all_feedback)

@app.route('/post/<int:post_id>')
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('view_post.html', post=post)

@app.route('/contact')
def contact():
    return render_template('contact.html')

# NEW: Route to download your Resume
@app.route('/download_resume')
def download_resume():
    # Place your resume file (e.g., resume.pdf) inside a folder named 'static'
    return send_from_directory(directory='static', path='resume.pdf')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    name = request.form.get('name')
    message = request.form.get('message')
    if name and message:
        new_feedback = Feedback(name=name, message=message)
        db.session.add(new_feedback)
        db.session.commit()
    return redirect(url_for('home'))

@app.route('/my_account')
@login_required
def my_account():
    user_posts = Post.query.filter_by(user_id=current_user.id).all()
    return render_template('my_account.html', posts=user_posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('my_account'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        hashed_pw = generate_password_hash(request.form['password'])
        new_user = User(username=request.form['username'], password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

# CRUD Operations (Create, Edit, Delete)
@app.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        new_post = Post(title=request.form['title'], content=request.form['content'], user_id=current_user.id)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('my_account'))
    return render_template('create_post.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_post(id):
    post = Post.query.get_or_404(id)
    if post.user_id != current_user.id:
        return redirect(url_for('my_account'))
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        db.session.commit()
        return redirect(url_for('my_account'))
    return render_template('edit_post.html', post=post)

@app.route('/delete/<int:id>')
@login_required
def delete_post(id):
    post = Post.query.get_or_404(id)
    if post.user_id == current_user.id:
        db.session.delete(post)
        db.session.commit()
    return redirect(url_for('my_account'))

if __name__ == '__main__':
    # This allows the platform to choose the port
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
