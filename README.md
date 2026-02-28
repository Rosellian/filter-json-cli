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

## Examples

### Basic filtering
Filter items where the `name` field contains “anna” (case‑insensitive):

```bash
filterjson --file data.json --key name --contains anna