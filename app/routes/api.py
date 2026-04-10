from app.routes import api_bp


@api_bp.route("/accounts", methods=["POST"])
def create_account():
    return {"error": "not_implemented"}, 501


@api_bp.route("/accounts/me", methods=["PATCH"])
def update_account():
    return {"error": "not_implemented"}, 501
