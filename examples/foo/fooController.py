from kessel.recipe import Recipe


foo_app = Recipe("/foo")

@foo_app.secured
@foo_app.route("")
@foo_app.route("/")
def foo_home(request):
    return 'foo!'


@foo_app.secured
@foo_app.route("/bar")
def foo_bar(request):
    return 'bar!'

