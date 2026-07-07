# Average Things Tech

Simple tech. Real use. No drama.

Average Things Tech is a beginner-friendly static site for Linux, open-source tools, Neovim, practical computing, and respectful technology advocacy.

## Live site

The site is live at:

    https://tddc.github.io/average-things-tech/

## Repository

Source code and content are hosted on GitHub:

    https://github.com/TDDC/average-things-tech

## This site is built with

- Pelican
- Markdown
- Python virtual environment
- Git
- GitHub Actions
- GitHub Pages

## Current status

Version 1.1 public beta:

- Local Pelican development works
- GitHub repository is active
- GitHub Pages deployment is working
- Site is live on the GitHub Pages URL
- Guides, Articles, Open Letters, and White Papers sections have been added

## Local development

Activate the virtual environment:

    .\.venv\Scripts\Activate.ps1

Build the site locally:

    pelican content

Serve locally:

    python -m http.server --directory output 8000

Open locally:

    http://localhost:8000

Stop the local server:

    Ctrl + C

## Publishing workflow

Every push to the `main` branch triggers GitHub Actions.

GitHub Actions builds the Pelican site and publishes the generated output to GitHub Pages.

Normal workflow:

    pelican content
    git status
    git add .
    git commit -m "Your commit message"
    git push

Then GitHub Actions deploys the site automatically.

## Project structure

    average-things-tech/
    ├── .github/
    │   └── workflows/
    ├── content/
    │   ├── articles/
    │   ├── episodes/
    │   ├── guides/
    │   ├── images/
    │   ├── notes/
    │   ├── open-letters/
    │   ├── pages/
    │   └── white-papers/
    ├── pelicanconf.py
    ├── publishconf.py
    ├── requirements.txt
    ├── tasks.py
    ├── Makefile
    ├── README.md
    ├── .gitignore
    └── .gitattributes

## Important Git rule

Do commit:

- Markdown content
- Pelican config files
- GitHub Actions workflow files
- requirements.txt
- README.md
- .gitignore
- .gitattributes

Do not commit:

- .venv/
- output/
- __pycache__/

## Content sections

The site currently includes:

- Guides
- Articles
- Open Letters
- White Papers
- Notes
- Episode companion pages

## Project rule

First make it work.  
Then make it automatic.  
Then make it beautiful.  
Then make it public.

Boring first. Fancy later. Drama never.
