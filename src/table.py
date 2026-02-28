ELLIPSIS = "…"
RIGHT = "right"
LEFT = "left"
COLUMN_SEPARATOR = " | "

class ANSI:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    FG_BLUE = "\033[34m"
    FG_CYAN = "\033[36m"
    FG_MAGENTA = "\033[35m"
    FG_YELLOW = "\033[33m"

_COLOR_ENABLED = True

def set_color_enabled(enabled: bool):
    global _COLOR_ENABLED
    _COLOR_ENABLED = enabled

def color_enabled():
    return _COLOR_ENABLED

class BorderStyle:
    def __init__(self, h="-", v="|", tl="+", tr="+", bl="+", br="+", jm="+"):
        self.h = h
        self.v = v
        self.tl = tl
        self.tr = tr
        self.bl = bl
        self.br = br
        self.jm = jm

ASCII_BORDER = BorderStyle("-", "|", "+", "+", "+", "+", "+")
UNICODE_BORDER = BorderStyle("─", "│", "┌", "┐", "└", "┘", "┬")
MARKDOWN_BORDER = BorderStyle(
    h="-",
    v="|",
    tl="",
    tr="",
    bl="",
    br="",
    jm="|"
)
NO_BORDER = None

BORDER_STYLES = {
    "ascii": ASCII_BORDER,
    "unicode": UNICODE_BORDER,
    "markdown": MARKDOWN_BORDER,
    "none": NO_BORDER,
}

class Cell:
    def __init__(self, value, width, align=LEFT, max_width=None, color=None):
        self.raw = "" if value is None else str(value)
        self.width = width
        self.align = align
        self.max_width = max_width or width
        self.color = color

    def _truncated(self, text):
        if len(text) <= self.max_width:
            return text
        if self.max_width <= 1:
            return ELLIPSIS
        return text[: self.max_width - 1] + ELLIPSIS

    def _apply_color(self, text):
        if self.color and color_enabled():
            return f"{self.color}{text}{ANSI.RESET}"
        return text

    def render(self):
        text = self._truncated(self.raw)
        aligned = text.rjust(self.width) if self.align == RIGHT else text.ljust(self.width)
        return self._apply_color(aligned)

class Column:
    def __init__(self, name, values, max_width=30):
        self.name = name
        self.max_width = max_width

        self.is_numeric = all(
            (v is None or isinstance(v, (int, float))) for v in values
        )

        raw_width = max(
            len(name),
            max(len(str(v)) for v in values if v is not None)
        )
        self.width = min(raw_width, max_width)

    @property
    def align(self):
        return RIGHT if self.is_numeric else LEFT

    def header_cell(self):
        color = ANSI.BOLD + ANSI.FG_BLUE
        return Cell(self.name, self.width, self.align, self.max_width, color=color)

    def make_cell(self, value):
        color = ANSI.FG_YELLOW if self.is_numeric else None
        return Cell(value, self.width, self.align, self.max_width, color=color)

class TableRenderer:
    def __init__(self, items, max_width=30, border=ASCII_BORDER):
        self.items = items
        self.max_width = max_width
        self.border = border
        self.columns = self._build_columns()

    def _build_columns(self):
        all_keys = sorted({key for item in self.items for key in item.keys()})
        return [
            Column(key, [item.get(key) for item in self.items], self.max_width)
            for key in all_keys
        ]

    def render_header(self):
        return " | ".join(col.header_cell().render() for col in self.columns)

    def render_rows(self):
        rows = []
        for item in self.items:
            row = " | ".join(
                col.make_cell(item.get(col.name)).render()
                for col in self.columns
            )
            rows.append(row)
        return rows

    def _border_line(self, top=False, bottom=False):
        if self.border is None:
            return ""

        parts = []
        for col in self.columns:
            parts.append(self.border.h * col.width)

        if top:
            return self.border.tl + self.border.jm.join(parts) + self.border.tr
        if bottom:
            return self.border.bl + self.border.jm.join(parts) + self.border.br

        return self.border.jm + self.border.jm.join(parts) + self.border.jm

    def _add_vertical_borders(self, line):
        parts = line.split(COLUMN_SEPARATOR)
        return f"{self.border.v} " + f" {self.border.v} ".join(parts) + f"{self.border.v}"

    def render(self):
        if not self.items:
            return ""

        if self.border is None:
            header = self.render_header()
            rows = self.render_rows()
            return "\n".join([header] + rows)

        top = self._border_line()
        header = self.render_header()
        mid = self._border_line()
        rows = self.render_rows()
        bottom = self._border_line()

        header = self._add_vertical_borders(header)
        rows = [self._add_vertical_borders(r) for r in rows]

        return "\n".join([top, header, mid] + rows + [bottom])

class Table:
    def __init__(self, items, max_width=30, border=ASCII_BORDER):
        self.renderer = TableRenderer(items, max_width, border)

    def render(self):
        return self.renderer.render()

def format_table(items, max_width=30, border="ascii"):
    style = BORDER_STYLES.get(border, ASCII_BORDER)
    return Table(items, max_width=max_width, border=style).render()