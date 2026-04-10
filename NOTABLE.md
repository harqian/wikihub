# notable — blockers, questions, assumptions

updated as I work. check back here for status.

## in progress

- systematic component testing against dev server
- P0 beads issues (private band warning, per-wiki llms.txt, wikilink rewriting on rename)

## blockers

(none yet)

## assumptions made

- **html disabled in markdown-it**: set `html: false` to prevent XSS. this means `<!-- private -->` bands won't render as HTML comments in the output (they're stripped before rendering anyway), but it also means users can't embed raw HTML in their pages. the spec says the reader should support HTML — this is a security vs functionality tradeoff. currently favoring security.

- **no password for API accounts**: the spec says `POST /api/v1/accounts` creates an account with just a username. no password is set for API-only accounts, which means they can't log in via the web UI. this is intentional per the spec ("no CAPTCHA, no verification required") but means an agent-created account is API-only unless the user later sets a password via `PATCH /accounts/me`.

- **editor is textarea, not Milkdown**: the Milkdown WYSIWYG bundle exists in listhub but wasn't ported. the editor is a raw textarea with edit/preview toggle. Milkdown layering is deferred.

- **no real-time preview**: the Preview tab in the editor shows plaintext, not rendered markdown. would need either a client-side markdown renderer or an AJAX call to the server to render. deferred.

- **Railway volume for git repos**: persistent volume mounted at /data/repos. if Railway recycles the volume or loses it, all git repos are gone. DB has metadata but content is lost. need backup strategy before real users.

## questions for Harrison

1. **Google OAuth credentials** — do you have them ready? the flow is implemented but crashes without `GOOGLE_CLIENT_ID` / `GOOGLE_CLIENT_SECRET` env vars.

2. **Custom domain** — when to point wikihub.md at the Railway deployment? need to add the domain in Railway dashboard and set DNS.

3. **Milkdown priority** — is the textarea editor acceptable for launch, or do you want the WYSIWYG before any real users?

## fixed during testing

- frontmatter was rendering as visible text (stripped before markdown-it now)
- Google OAuth crashed with AttributeError when no creds configured (now graceful redirect)
- XSS via raw `<script>` tags in markdown (html disabled in markdown-it)
- landing page didn't show login state (now shows @username when logged in)
- signup redirected to landing instead of profile
- no action buttons on any page (added edit, star, fork, new page, new wiki)
- public mirror didn't respect frontmatter visibility (now checks both ACL and frontmatter)
- oversized uploads silently dropped files (now rejects with error message)
