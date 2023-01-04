from app import db_api as db
from datetime import datetime
from app.utils import totaluptimeformat
from flask import (
    Blueprint, render_template, request
)

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    uptime = db.get_uptime()
    d = datetime.strptime(uptime['last_update'], '%Y-%m-%d %H:%M:%S.%f+00')
    total_uptime_string = totaluptimeformat(uptime['total_uptime'])
    return render_template('index.html', total_uptime=total_uptime_string, d=d)


@bp.route('/update', methods=['POST'])
def update():
    uptime = request.form['uptime']
    db.update_total_uptime(uptime)
    return 'Data updated'