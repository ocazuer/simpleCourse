from models.company import Company
from routes import *

main = Blueprint('company', __name__)

Model = Company


@main.route('/')
def index():
    ms = Model.objects
    return render_template('company_index.html', companies=ms, user=current_user())


@main.route('/add', methods=['POST'])
def add_lesson():
    form = request.form
    m = Model(logo_path=form['logo_path'], name=form['name'])
    m.save()
    print("Company's id", m.id)
    return redirect(url_for('.index'))