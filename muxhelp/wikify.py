import os
from xml.sax.saxutils import escape

PATH = "../../muxcode-clm.wiki"
INPUT = "help.txt"

help_file = open(INPUT, "rU")

last_page = ""
current_page = ""
current_sequence = 0

current_file = None

for line in help_file:
    line = line.strip()
    
    if line.startswith("&"):
        symbol = line[2:].lower()
        if symbol.endswith("()"):
            symbol = symbol[:-2]

        if symbol[-1].isdigit():
            sequence = symbol[-1]
            symbol = symbol[:-1]
        else:
            sequence = 0
                    
        if last_page != symbol:
            last_page = current_page
            current_file = open(os.path.join(PATH, symbol + ".md"), "w")
            current_page = symbol
    else:
        if line.startswith("Related Topics:"):
            links = []
            for item in line[15:].split(","):
                if item.endswith("."):
                    item = item[:-1]
                if item.endswith("()"):
                    item = item[:-2]

                links.append("[[%s]]" % (item.strip(),))
            line = "Related Topics: " + ", ".join(links)

        current_file.write(escape(line))
        current_file.write("\n")

