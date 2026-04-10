from app.routes import main_bp


@main_bp.route("/")
def index():
    return "wikihub"


@main_bp.route("/explore")
def explore():
    return "explore"
