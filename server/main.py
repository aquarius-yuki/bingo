import module_path

from bottle import route, run

@route('/')
def version():
    version_info = {
        'server': '1.0.0'
    }
    return version_info

run(host='localhost', port=8080)