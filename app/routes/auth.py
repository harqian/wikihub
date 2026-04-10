from app.routes import auth_bp


@auth_bp.route("/login")
def login():
    return "login"


@auth_bp.route("/signup")
def signup():
    return "signup"
