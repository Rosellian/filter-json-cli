HELP_TEXT_SV = """
filterjson — Filter, sök och transformera JSON-data direkt i terminalen.

ANVÄNDNING:
  filterjson --file PATH [FILTERS...] [SORTERING...] [OUTPUT...] [TABELL...]

OBLIGATORISKA FLAGGOR:
  --file PATH
      JSON-fil att läsa in. Filen måste innehålla en lista av objekt.

FILTERFLAGGOR (kan kombineras fritt och upprepas):
  --key NAME
      Sätter aktivt fält för efterföljande filter. Kan anges flera gånger.

  --equals VALUE
      Matchar poster där fältet är exakt lika med VALUE.

  --not-equals VALUE
      Matchar poster där fältet INTE är lika med VALUE.

  --contains TEXT
      Matchar poster där fältet innehåller TEXT (case-insensitive).

  --not-contains TEXT
      Matchar poster där fältet INTE innehåller TEXT.

  --regex PATTERN
      Matchar poster där fältet matchar regex PATTERN (case-insensitive).

  --not-regex PATTERN
      Matchar poster där fältet INTE matchar regex PATTERN.

  --min NUMBER
      Matchar poster där fältet är >= NUMBER.

  --max NUMBER
      Matchar poster där fältet är <= NUMBER.

  --invert
      Inverterar hela resultatet efter alla filter har körts.

SORTERING:
  --sort FIELD
      Sorterar resultatet på FIELD.

  --desc
      Sorterar i fallande ordning.

OUTPUTFORMAT:
  --json
      Skriver ut resultatet som rå JSON.

  --no-color
      Inaktiverar ANSI-färger.

TABELLFORMAT:
  --border STYLE
      ascii | unicode | markdown | none

  --max-width N
      Maxbredd per kolumn innan text trunkeras.

EXEMPEL:
  filterjson --file data.json --key name --contains anna
"""

HELP_TEXT_EN = """
filterjson — Filter, search and transform JSON data directly in the terminal.

USAGE:
  filterjson --file PATH [FILTERS...] [SORT...] [OUTPUT...] [TABLE...]

REQUIRED FLAGS:
  --file PATH
      JSON file to load. Must contain a list of objects.

FILTER FLAGS (can be combined and repeated):
  --key NAME
      Sets the active field for subsequent filters.

  --equals VALUE
      Matches items where the field equals VALUE.

  --not-equals VALUE
      Matches items where the field does NOT equal VALUE.

  --contains TEXT
      Matches items where the field contains TEXT (case-insensitive).

  --not-contains TEXT
      Matches items where the field does NOT contain TEXT.

  --regex PATTERN
      Matches items where the field matches regex PATTERN.

  --not-regex PATTERN
      Matches items where the field does NOT match regex PATTERN.

  --min NUMBER
      Matches items where the field is >= NUMBER.

  --max NUMBER
      Matches items where the field is <= NUMBER.

  --invert
      Inverts the entire result after filtering.

SORTING:
  --sort FIELD
      Sorts the result by FIELD.

  --desc
      Sorts in descending order.

OUTPUT FORMAT:
  --json
      Outputs raw JSON instead of a table.

  --no-color
      Disables ANSI colors.

TABLE FORMAT:
  --border STYLE
      ascii | unicode | markdown | none

  --max-width N
      Maximum column width before truncation.

EXAMPLES:
  filterjson --file data.json --key name --contains anna
"""

HELP_TEXTS = {
    "sv": HELP_TEXT_SV,
    "en": HELP_TEXT_EN,
}