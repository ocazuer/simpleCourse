from models.user import User
from routes import *
import hashlib
from models.user import hash_md5


Model = User

main = Blueprint('user', __name__)


def current_user():
    uid = session.get('user_id')
    if uid is not None:
        u = User.objects.get(id=uid)
        print('debug', u.id, u.username)
        return u
    return None

def sava_session(user_id):
    user_id = str(user_id)
    session['user_id'] = user_id


@main.route('/')
def index():
    ms = Model.objects
    return render_template('smg.html')


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    d = dict(
        username = form.get('username', ''),
        password = hash_md5(form.get('password', ''))
    )
    m = Model(**d)
    # m.save()
    if m.validate_register():
        m.save()
        sava_session(m.id)
        return redirect(url_for('index.index'))
    # else:
    #     return redirect(url_for('.signup'))


@main.route('/delete/<id>')
def delete(id):
    m = Model.objects(id=id)
    m.delete()
    return render_template('smg.html')


@main.route('/verification_login', methods=['POST'])
def verification_login():
    form = request.form
    u1 = Model(form)
    u2 = User.objects(username=u1.username).first()
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