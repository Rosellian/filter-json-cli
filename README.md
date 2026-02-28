# filterjson  
A fast, modular, test‑driven CLI tool for filtering, searching, and transforming JSON data directly in the terminal.

`filterjson` is designed for developers, DevOps engineers, data analysts, and anyone who works with structured JSON data.  
It provides a powerful query language, expressive filters, flexible table rendering, and a clean, extensible architecture.

---

## ✨ Features

### 🔍 Powerful Filtering
- `--key` to select the active field  
- `--equals`, `--contains`, `--regex`  
- Negative filters: `--not-equals`, `--not-contains`, `--not-regex`  
- Numeric filters: `--min`, `--max`  
- `--invert` to invert the entire result set  

### 📊 Beautiful Table Output
- Auto‑detected numeric alignment  
- Automatic truncation with ellipsis  
- ANSI color support (headers, numeric columns)  
- `--no-color` for script‑friendly output  
- Multiple border styles: `ascii`, `unicode`, `markdown`, `none`  
- Configurable column width via `--max-width`

### 🔧 Sorting & Output Options
- `--sort` and `--desc`  
- `--json` for raw JSON output  
- `--select` (future extension)  
- `--align` per column (future extension)

### 🌍 Multi‑language Help
- `--lang sv` (Swedish)  
- `--lang en` (English)

### 🧪 Fully Test‑Driven
The entire tool is built using TDD with:
- unit tests for filters  
- integration tests for CLI behavior  
- snapshot‑ready table rendering  

---

## 🚀 Installation

Install in development mode:

```bash
pip install -e .
```
## Examples
### Usage
Basic usage:
```bash
filterjson --file data.json [filters...] [options...]
```
Example json:
```json
[
  {"name": "Anna", "age": 30, "city": "Halmstad"},
  {"name": "Bob", "age": 8, "city": "Göteborg"},
  {"name": "Carl", "age": 40, "city": "Stockholm"}
]
```
### Example commands
**Basic filtering**

Filter items where the `name` field contains “anna” (case‑insensitive):
```bash
filterjson --file data.json --key name --contains anna
```
Filter items where `age` is greater than or equal to 30:
```bash
filterjson --file data.json --key age --min 30
```
Filter items where `city` matches a regex:
```bash
filterjson --file data.json --key city --regex "göte"
```
**Negative filters**

Show all items where `name` does not contain “anna”:
```bash
filterjson --file data.json --key name --not-contains anna
```
Show all items where `age` is not equal to 30:
```bash
filterjson --file data.json --key age --not-equals 30
```
Show all items where `city` does not match a regex:
```bash
filterjson --file data.json --key city --not-regex "holm$"
```
**Combining filters**

Filter by name AND age:
```bash
filterjson --file data.json \
  --key name --contains anna \
  --key age --min 30
```
Filter by multiple fields with mixed positive/negative filters:
```bash
filterjson --file data.json \
  --key name --not-contains anna \
  --key city --regex "göte"
```
**Inverting the entire result**

Show everything that does not match the filter:
```bash
filterjson --file data.json --key age --min 30 --invert
```
**Select fields**

Select `name` and `age` fields only:
```bash
filterjson --file data.json --select name,age
```
Combine with filter and sorting:
```bash
filterjson --file data.json \
  --key age --min 20 \
  --select name,city \
  --sort name
```
**Sorting**

Sort by age:
```bash
filterjson --file data.json --sort age
```
Sort descending:
```bash
filterjson --file data.json --sort age --desc
```
Sort after filtering:
```bash
filterjson --file data.json \
  --key name --contains anna \
  --sort age --desc
```
**JSON output**

Return raw JSON instead of a table:
```bash
filterjson --file data.json --json
```
**Table formatting**

Use Unicode borders:
```bash
filterjson --file data.json --border unicode
```
Use Markdown table format:
```bash
filterjson --file data.json --border markdown
```
Disable borders entirely:
```bash
filterjson --file data.json --border none
```
Disable ANSI colors:
```bash
filterjson --file data.json --no-color
```
Limit column width:
```bash
filterjson --file data.json --max-width 20
```
Combine formatting options:
```bash
filterjson --file data.json \
  --border unicode \
  --max-width 25 \
  --no-color
```
**Multi-language help**

Swedish help:
```bash
filterjson --lang sv --help
```
English help:
```bash
filterjson --lang en --help
```
---

## 🧱 Architecture Overview
The project is built around clean, modular components:
### Filtering Engine
- Pure functions
- Composable
- Easy to test
### Table Rendering Engine
- Cell — alignment, truncation, color
- Column — width calculation, numeric detection
- TableRenderer — borders, layout, rendering
- Table — simple wrapper
### CLI Layer
- Argument parsing
- Language selection
- Output formatting
- Error handling
Everything is designed for extensibility and clarity.

## 🧪 Running Tests
```bash
pytest -q
```