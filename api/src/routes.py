from api.src import controllers


def setup_routes(app):
    app.register_blueprint(controllers.bp, url_prefix="/channels")

    @app.errorhandler(404)
    def not_found(error):
        return "not found", 404

    return
