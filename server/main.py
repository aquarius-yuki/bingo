import module_path
import endpoint_main
import endpoint_error
from bottle import route, run

@route('/')
def version():
    version_info = {
        'server': '1.0.0'
    }
    return version_info

run(host='localhost', port=8080)