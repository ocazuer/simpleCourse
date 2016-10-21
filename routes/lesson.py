from models.lesson import Lesson
from models.company import Company
from models.point import Point
from models.user import User
from routes import *

from flask_weasyprint import HTML, render_pdf

Model = Lesson

main = Blueprint('lesson', __name__)


@main.route('/')
def index():
    ms = Model.query.all()
    return render_template('lesson_index.html', user=current_user())


@main.route('/<int:id>')
def show(id):
    lesson = Lesson.query.get(id)
    points = lesson.get_points_by_updated_time()
    company = Company.query.get(lesson.company_id)
    user = current_user()
    return render_template('lesson.html', lesson=lesson, points=points, company=company, user=user)

@main.route('/pdfprinter')
def pdfprinter():

    ar = request.args
    id = ar['id']

    # filename = 'test' + str(id) + '.pdf'
    # url = 'http://www.ocazuer.com/lesson/8'
    # HTML(url).write_pdf('static/pdf/{}'.format(filename))
    # return redirect(url_for('.show', id=id))

    # Make a PDF from another view
    return render_pdf(url_for('.show', id=id))

@main.route('/new')
def write_lesson():
    cs = Company.query.all()
    return render_template('lesson_add_step1.html', companies=cs, user=current_user())


@main.route('/add', methods=['POST'])
def add_lesson():
    form = request.form
    lesson = Lesson(form)
    lesson.save()
    return redirect(url_for('.write_point', lesson_id=lesson.id))


@main.route('/point/new/<int:lesson_id>')
def write_point(lesson_id):
    return render_template('lesson_add_step2.html', lesson_id=lesson_id, user=current_user())


@main.route('/point/add/<int:lesson_id>', methods=['POST'])
# @main.route('/point/add', methods=['POST'])
def add_point(lesson_id):
    form = request.form
    point = Point(form)
    point.save()
    return redirect(url_for('.write_point', lesson_id=point.lesson_id))