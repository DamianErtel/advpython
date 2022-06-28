
html = '''
<h2>Execution environment</h2>
<p>
Python version: 3.8.5<br/>
Interpreter: CPython<br/>
Interpreter version: 3.8.5 (default, Jul 28 2020, 12:59:40) 
[GCC 9.3.0]<br/>
Operating system: Linux<br/>
Operating system version: 5.4.0-48-generic<br/>
Processor: PROCESOR_DO_PODSTAWIENIA<br/>
CPUs: LICZBA_CPU_DO_PODSTAWIENIA
</p>
'''

import os
liczba_cpu = os.cpu_count()

gotowy_html = (html
               .replace("LICZBA_CPU_DO_PODSTAWIENIA", str(liczba_cpu))
               .replace('PROCESOR_DO_PODSTAWIENIA', 'x86'))
