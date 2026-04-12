def format_cell(text, width):
    text = str(text)
    if len(text) > width:
        text = text[:width - 3] + "..."
    return f"{text:<{width+3}}"

def format_row(items, width):
    row = ""

    for item in items:
        row += format_cell(item, width)
    
    return row
