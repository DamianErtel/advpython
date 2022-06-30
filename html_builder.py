import platform
import sys
import os

html_boilerplate_top = '<!DOCTYPE html><html lang="pl"><head><meta charset="UTF-8"><title>DAMIAN ERTEL ADV. PYTHON PROJECT</title><link rel="stylesheet" href="style.css"></head>'
html_boilerplate_middle = '<body>'
html_boilerplate_bottom = '</body></html>'

python_v = platform.python_version()
python_interpreter_name = platform.python_implementation()
python_interpreter = sys.version
system_type = platform.system()
system_v = platform.release()
processor_type = platform.processor()
processor_count = os.cpu_count()

sys_info_base = '''
<h2>Execution environment</h2>
<p>
Python version: python_v<br/>
Interpreter: python_interpreter_name<br/>
Interprete versionr: python_interpreter<br/>
Operating system: system_type<br/>
Operating system version: system_v<br/>
Processor: processor_type<br/>
CPUs: processor_count
</p>
'''

sys_info_complete = (sys_info_base
                     .replace("python_v", str(python_v))
                     .replace("python_interpreter_name", str(python_interpreter_name))
                     .replace("python_interpreter", str(python_interpreter))
                     .replace("system_type", str(system_type))
                     .replace("system_v", str(system_v))
                     .replace("processor_type", str(processor_type))
                     .replace("processor_count", str(processor_count))
                     )

project_header = '<h1>Multithreading/Multiprocessing benchmark results</h1>'
execution = '<div><h2>Execution:</h2><span><div>1</div><div>2</div><div>3</div><div>4</div><div>5</div></span></div>'
execution_median = '<div><h2>Execution:</h2><span>Median:</span></div>'
top_heading = '<div><h1>Test results</h1><p>The following table shows detailed test results:</p></div>'
bottom_heading = '<div><h1>Summary</h1><p>The following table shows the median of all results:</p></div>'
author = '<span>App author: Damian Ertel</span>'

def createColumn(results, tag):
    table_data = ""
    for i in results[tag]:
        table_data += i

    return table_data


def create_headers(column_name):
    table_header = "<h2>" + column_name + "</h2>"
    return table_header


def build_html(results, median_list, nameplate_list):
    # mp = results["MP"]
    # mpm = results["MPM"]
    # mt = results["MT"]
    # st = results["ST"]

    headers = "<div>"
    cols = "<section>"
    cols += execution
    for i in results:
        header = "<h2>" + i + "</h2>"
        row = "<span class=" + i + ">"
        span = map(lambda x: "<div>" + str(x) + "</div>", results[i])
        results[i] = list(span)
        headers += create_headers(i)
        column = createColumn(results, i)
        row += column
        row += "</span>"
        col = "<div>" + header + row + "</div>"
        cols += col
        # print("COLUMN", row)

    cols += "</section>"
    headers += "</div>"
    # print(headers)

    median_section = '<section class="median">' + execution_median
    median_span = list(map(lambda x, name: '<div><h2>' + name + '</h2><span class="result">' + str(x) + '</span></div>', median_list, nameplate_list))
    for i in median_span:
        median_section += i

    median_section += '</section>'

    ready_html = html_boilerplate_top + html_boilerplate_middle + project_header + sys_info_complete + top_heading + cols + bottom_heading + median_section + author + html_boilerplate_bottom

    f = open("./results/myfile.html", "w")
    f.write(ready_html)
