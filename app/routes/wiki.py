from app.routes import wiki_bp


@wiki_bp.route("/@<username>")
def user_profile(username):
    return f"@{username}"


@wiki_bp.route("/@<username>/<slug>")
def wiki_index(username, slug):
    return f"@{username}/{slug}"


@wiki_bp.route("/@<username>/<slug>/<path:page_path>")
def wiki_page(username, slug, page_path):
    return f"@{username}/{slug}/{page_path}"
