from models.lesson import Lesson
from models.point import Point
from routes import *

Model = Lesson

main = Blueprint('lesson', __name__)


@main.route('/')
def index():
    ms = Model.query.all()
    return render_template('lesson_index.html')


@main.route('/<int:id>')
def show(id):
    m = Model.query.get(id)
    return render_template('lesson.html')


@main.route('/new')
def write_lesson():
    return render_template('lesson_add_step1.html')


@main.route('/add', methods=['POST'])
def add_lesson():
    form = request.form
    lesson = Lesson(form)
    lesson.save()
    return redirect(url_for('.write_point', lesson_id=lesson.id))


@main.route('/point/new/<int:lesson_id>')
def write_point(lesson_id):
    return render_template('lesson_add_step2.html', lesson_id=lesson_id)


@main.route('/point/add/<int:lesson_id>', methods=['POST'])
# @main.route('/point/add', methods=['POST'])
def add_point(lesson_id):
    form = request.form
    point = Point(form)
    point.save()
    return redirect(url_for('.write_point', lesson_id=point.lesson_id))