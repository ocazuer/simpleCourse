from models.lesson import Lesson
from models.user import User
from routes import *

main = Blueprint('index', __name__)


@main.route('/')
def index():
    ms = Model.query.all()
    return render_template('user_index.html')
