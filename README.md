# Average Things Tech

Simple tech. Real use. No drama.

Average Things Tech is a practical learning website for normal people exploring Linux, open-source tools, Neovim, home servers, backups, and useful computing systems.

This site is built with:

- Pelican
- Markdown
- Python virtual environment
- Git
- Future: GitHub Pages

## Current status

Version 0.1: Local Pelican site working.

## Local development

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Build the site:

```powershell
pelican content
```

Serve locally:

```powershell
python -m http.server --directory output 8000
```

Open in browser:

```text
http://localhost:8000
```

Stop the local server:

```text
Ctrl + C
```

## Project structure

```text
average-things-tech/
├── content/
│   ├── articles/
│   ├── pages/
│   └── images/
├── output/
├── pelicanconf.py
├── publishconf.py
├── requirements.txt
├── tasks.py
├── Makefile
├── README.md
├── .gitignore
└── .gitattributes
```

## Important Git rule

Do commit:

- Markdown content
- Pelican config files
- requirements.txt
- README.md
- .gitignore
- .gitattributes

Do not commit:

- .venv/
- output/
- __pycache__/

## Project rule

First make it work.  
Then make it automatic.  
Then make it beautiful.  
Then make it public.

Boring first. Fancy later. Drama never.
