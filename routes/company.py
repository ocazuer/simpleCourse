from models.company import Company
from routes import *

main = Blueprint('company', __name__)

Model = Company


@main.route('/')
def index():
    ms = Model.query.all()
    return render_template('company_index.html', companies=ms)


@main.route('/add', methods=['POST'])
def add_lesson():
    form = request.form
    m = Model(form)
    m.save()
    return redirect(url_for('.index'))