from models.lesson import Lesson
from models.company import Company
from models.user import User
from routes import *

main = Blueprint('index', __name__)

@main.route('/')
def index():
    lessons = Lesson.objects
    return render_template('index.html', lessons=lessons, Company=Company, user=current_user())
