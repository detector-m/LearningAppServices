# *-* coding: utf-8 *-
# pylint: disable=unused-argument

from flask import Flask

from _response import response

def init_error(app: Flask):
    @app.errorhandler(400)
    def _error_400(e):
        return response(400)
    
    @app.errorhandler(404)
    def _error_404(e):
        return response(404)
    
    @app.errorhandler(405)
    def _error_405(e):
        return response(405)

    @app.errorhandler(500)
    def _error_500(e):
        return response(500)

# if __name__ == '__main__':
    # print(response.__name__)