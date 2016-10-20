from models.lesson import Lesson
from routes import *

Model = Lesson

main = Blueprint('lesson', __name__)


@main.route('/')
def index():
    ms = Model.query.all()
    return render_template('smg.html')


@main.route('/<int:id>')
def show(id):
    m = Model.query.get(id)
    return render_template('smg.html')