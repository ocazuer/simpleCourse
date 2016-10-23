from models.lesson import Lesson
from models.company import Company
from models.point import Point
from models.user import User
from routes import *

from flask_weasyprint import HTML, render_pdf

from models import timestamp

Model = Lesson

main = Blueprint('lesson', __name__)


@main.route('/')
def index():
    ms = Model.objects
    return render_template('lesson_index.html', user=current_user())


@main.route('/<id>')
def show(id):

    lesson = Lesson.objects.get(id=id)
    points = lesson.get_points_by_updated_time()
    company = Company.objects.get(lessons__in=[lesson])
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
    cs = Company.objects()
    return render_template('lesson_add_step1.html', companies=cs, user=current_user())


@main.route('/add', methods=['POST'])
def add_lesson():
    form = request.form
    lesson = Lesson(name=form['name'])
    lesson.save()
    company = Company.objects(id=form['company_id']).first()
    company.insert_lesson(lesson)
    company.save()
    return redirect(url_for('.write_point', lesson_id=lesson.id))


@main.route('/point/new/<lesson_id>')
def write_point(lesson_id):
    return render_template('lesson_add_step2.html', lesson_id=lesson_id, user=current_user())


@main.route('/point/add/<lesson_id>', methods=['POST'])
def add_point(lesson_id):
    form = request.form
    d = dict(
        name=form.get('name', ''),
        target = form.get('target', ''),
        content = form.get('content', ''),
        created_time = timestamp(),
        updated_time = timestamp(),
    )
    point = Point(**d)
    point.save()
    lesson = Lesson.objects.get(id=lesson_id)
    print('debug', lesson.id)

    lesson.insert_point(point)

    # return redirect(url_for('.write_point', lesson_id=point.lesson_id))
    return redirect(url_for('.write_point', lesson_id=lesson_id))
