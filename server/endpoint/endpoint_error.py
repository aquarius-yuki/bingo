from bottle import error

@error(404)
def error404(error):
    return "Nothing here sorry {error}".format(error=error)