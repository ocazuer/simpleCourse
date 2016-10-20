from models.user import User
from routes import *

Model = User

main = Blueprint('user', __name__)


def current_user():
    uid = session.get('user_id')
    if uid is not None:
        u = User.query.get(uid)
        return u
    return None

def sava_session(user_id):
    session['user_id'] = user_id


@main.route('/')
def index():
    ms = Model.query.all()
    return render_template('smg.html')


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    m = Model(form)
    if m.validate_register():
        m.save()
        sava_session(m.id)
        return redirect(url_for('index.index'))
    else:
        return redirect(url_for('.signup'))


@main.route('/delete/<id>')
def delete(id):
    m = Model.query.filter_by(id=id).first()
    m.delete()
    return render_template('smg.html')


@main.route('/verification_login', methods=['POST'])
def verification_login():
    form = request.form
    u1 = Model(form)
    u2 = User.query.filter_by(username=u1.username).first()
    if u2 is not None and u2.validate_login(u1):
        sava_session(u2.id)
        return redirect(url_for('index.index'))
    else:
        print('登录失败')
        return redirect(url_for('.login'))


@main.route('/login')
def login():
    return render_template('user_login.html', user=current_user())


@main.route('/signup')
def signup():
    return render_template('user_signup.html', user=current_user())


@main.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('index.index'))