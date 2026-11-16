# Sapience Automata website

Static site (HTML + CSS, no build step) for GitHub Pages.

## Publish on GitHub Pages
1. Create a repo (e.g. `sapience-site`) and upload everything in this folder to the repo root.
2. Repo **Settings → Pages** → Source: *Deploy from a branch* → Branch: `main`, folder `/ (root)` → Save.
3. The site goes live at `https://<your-org>.github.io/<repo>/` in a minute or two.
4. Custom domain: add it under Settings → Pages, then point the domain's DNS to GitHub Pages.

## Edit
- Pages: `index.html`, `products.html`, `blinksmart.html`, `copilot-ai.html`, `bike-adas.html`, `solutions.html`, `public-transport.html`, `logistics.html`, `oem.html`, `defense.html`, `technology.html`, `about.html`, `research.html`, `news.html`, `careers.html`, `contact.html`
- Styles: `style.css` (brand blue is `--blue`)
- Images and video: `assets/`
- Contact form (Formspark): paste your form URL, e.g. `https://submit-form.com/YOUR_FORM_ID`, into `data-endpoint=""` on the form in `contact.html` (or in `build.py`). Until then the form asks visitors to email or call.
- `build.py` regenerates all pages if you prefer editing content in one place.
