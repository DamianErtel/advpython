html_boilerplate_top = '<!DOCTYPE html><html lang="pl"><head><meta charset="UTF-8"><title>DAMIAN ERTEL ADV. PYTHON PROJECT</title><link rel="stylesheet" href="style.css"></head>'
html_boilerplate_middle = '<body><section>'
html_boilerplate_bottom = '</section></body></html>'
#


def createColumn(results, tag):
    table_data = ""
    for i in results[tag]:
        table_data += i

    return table_data

def create_headers(column_name):
    table_header = "<h2>" + column_name + "</h2>"
    return table_header

def build_html(results):
    # mp = results["MP"]
    # mpm = results["MPM"]
    # mt = results["MT"]
    # st = results["ST"]

    headers = "<div>"
    cols = ""

    for i in results:
        header = "<h2>" + i + "</h2>"
        row = "<div className=" + i + ">"
        span = map(lambda x: "<div>" + str(x) + "</div>", results[i])
        results[i] = list(span)
        headers += create_headers(i)
        column = createColumn(results, i)
        row += column
        row += "</div>"
        col = "<div>" + header + row + "</div>"
        cols += col
        # print("COLUMN", row)

    headers += "</div>"
    # print(headers)
    ready_html = html_boilerplate_top + html_boilerplate_middle + cols + html_boilerplate_bottom

    f = open("./results/myfile.html", "w")
    f.write(ready_html)
