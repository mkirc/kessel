import re
from configparser import ConfigParser

from kessel import Kessel
from kessel import Redirect
from kessel import setup_jinja2_environment

from kessel.logger import GunicornLogger, MockGunicornConfig

from kessel import current_app
from kessel import current_user
from kessel import current_request

from foo.fooController import foo_app

log = GunicornLogger(cfg=MockGunicornConfig())

app = Kessel(err_log=log)

app.add_recipe(foo_app)

render_template = setup_jinja2_environment()

config = ConfigParser()
config.read('project.cfg')

@app.route("/", methods=["GET"])
def home(request):

    request = current_request()
    log.info(f"{request.path}")
    return 'hello, world!'

# test precedence rules
@app.route("/retest/123")
def retest_static(req):
    return 'static'

@app.route(re.compile(r"/retest/(?P<re_id>\d+$)"))
def retest(request, re_id):
    return f"{re_id}"

@app.route(re.compile(r"/retest/\w+$"))
def retest(request):
    return "generic"

@app.route("/redirect", methods=["GET"])
def redirect(request):

    return Redirect(request, "/")

@app.secured
@app.route("/secure", methods=["GET"])
def secure(request):

    request = current_request()
    log.info(f"{request.path}")

    return render_template('home.html', user=current_user().uid)

@app.secured(roles=["admin"])
@app.route("/admin", methods=["GET"])
def admin(request):

    return render_template('home.html', user=current_user().uid)

