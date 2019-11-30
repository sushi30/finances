from app.main.views import main


@main.app_errorhandler(403)
def forbidden(_):
    return "Forbidden", 403


@main.app_errorhandler(404)
def page_not_found(_):
    return "Not Found", 404


@main.app_errorhandler(500)
def internal_server_error(_):
    return "Server Error", 500
