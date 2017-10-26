from app import app, login_manager
from flask import render_template, flash, redirect, request, abort
from flask_login import login_required, current_user
from user import JwtUser
import logging


logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = getattr(logging, app.config.get('LOG_LEVEL').upper()), filename = app.config.get('LOG_PATH'))

@login_manager.request_loader
def get_user(req):
    logging.debug(req.environ)
    try:
        token = req.cookies[app.config.get('JWT_COOKIE_NAME')]
        logging.debug(token)
    except KeyError:
        logging.debug('KeyError exception, there is no jwt cookie')
        login_manager.login_message = 'User is not authenticated by HTTPD'
        return None
    user = JwtUser(token)
    return user

@login_manager.unauthorized_handler
def unauthorized():
    url = app.config.get('SSO_URL') + '?url=' + request.environ.get('HTTP_HOST') + app.config.get('REDIRECT_TO')
    return redirect(url)

@app.route('/', methods = ['GET'])
@login_required
def home():
    if current_user is not None:
        logging.debug('Login from user ' + current_user.get_id())
        return render_template('base.html')
    else:
        abort(403)
        
@app.route('/test')
def test():
    flash(request.environ)
    return render_template('base.html')
