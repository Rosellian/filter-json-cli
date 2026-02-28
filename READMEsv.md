# JSON Filter CLI
Ett snabbt, modulärt och testdrivet CLI‑verktyg för att filtrera, transformera och presentera JSON‑data i tabellform. 
Verktyget är byggt för att vara enkelt att använda, lätt att utöka och robust nog för professionella arbetsflöden inom
backend, DevOps och dataanalys.
---

## Funktioner
- Flexibla filter - stöd för `--key=value`, regex, jämförelser och `--not` för inverterade filter.
- Tabellrendering - kolumn auto-shrink, vänster- högerjustering, ANSI-färger, 
border styles(ASCII, Unicode, Markdown, none).
- Färgteman - växla mellan färgprofiler eller stäng av färg helt med --no-color.
- Modulär arkitektur - separata klasser för celler, kolumner, tabeller och renderers.
- Installerbar CLI - installeras via pip install tack vare pyproject.toml.
- TDD-driven kodbas - hög testtäckning och tydlig separation av ansvar.
---

## Installation
```bash
git clone https://github.com/Rosellian/filter_json-cli.git

cd filter-json-cli
```
```bash
pip install .
```
Eller för utveckling:
```bash
pip install -e .
```

## Användning

---
### Filtrera JSON
```bash
cat data.json | filterjson --key age
```
### Invertera filter
```bash
cat data.json | filterjson --not "city=London"
```
### Välj border style
```bash
cat data.json | filterjson --border unicode
```
### Stäng av färger
```bash
cat data.json | filterjson --no-color
```

## Exempelutdata
| name  |  age | city      |
|:------|-----:|:----------|
| Alice |   25 | New York  |
| Bob   |   30 | London    |

---
## Projektstruktur
```
filter-json-cli/
├── src
│   ├── __init__.py
│   ├── argparse_ext.py
│   ├── cli.py
│   ├── core.py
│   ├── filterjson.egg-info
│   │   ├── PKG-INFO
│   │   ├── SOURCES.txt
│   │   ├── dependency_links.txt
│   │   ├── entry_points.txt
│   │   └── top_level.txt
│   ├── filters.py
│   ├── helptext.py
│   └── table.py
├── tests
│   ├── __init__.py
│   ├── test_cli.py
│   ├── test_core.py
│   └── test_table.py
├── Makefile
├── README.md
├── READMEsv.md
├── data.json
├── pyproject.toml
```
---

## Utveckling
### Köra tester
```bash
pytest -q
```
### Linting
```bash
ruff check .
```
### Format
```bash
ruff format .
```