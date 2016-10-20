from models.lesson import Lesson
from models.user import User
from routes import *

main = Blueprint('index', __name__)

@main.route('/')
def index():
    lessons = Lesson.query.all()
    return render_template('index.html', lessons=lessons, user=current_user())
