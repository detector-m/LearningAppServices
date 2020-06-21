# *-* coding: utf-8 *-

from flask import Flask
# from flask_cors import CORS

from config import Config

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    import error
    error.init_error(app)

    import log
    log.init_log(app)

    import routes
    routes.init_routes(app)

    if app.config['ENV'] == 'development':
        print(app.url_map)

    return app

# app = create_app()

def main():
    app = create_app()
    
    # @app.route('/')
    # def index():
    #     return 'hello'

    app.run()

if __name__ == '__main__':
    main()