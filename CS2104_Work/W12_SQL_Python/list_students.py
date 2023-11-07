import sqlite3
from os.path import exists
import sys

if len(sys.argv) != 2:
    print("Format: python list_students.py <requested_academic_year>")
    sys.exit(1)

try: 
    requested_academic_year = int(sys.argv[1])

    if exists('cs_course_scheduling.sqlite'):
        conn = sqlite3.connect('cs_course_scheduling.sqlite')
        cursor = conn.execute("SELECT first_name, last_name, academic_year FROM students WHERE academic_year = 4 ORDER BY last_name")
        
        html_code = "<!DOCTYPE html>\n<html>\n<style>\ntable, th, "
        html_code += "td {\nborder:1px solid black;\n}\n</style>\n<body>\n\n<h2>A basic HTML table</h2>\n\n"
        html_code += '<table style="width:100%">\n\t<tr>\n\t\t<th>Company</th>\n\t\t<th>Contact</th>\n\t\t<th>Country</th>\n\t</tr>'


        for row in cursor:
            html_code += "\n\t<tr>"
            for word in row:
                html_code += "\n\t\t<td>" + str(word) + "</td>"
            html_code += "\n\t</tr>"

        conn.close()
        #print("Database was accessed and closed")

        html_code += "</table>\n\n</body>\n</html>"
        print(html_code)

    else:
        print('Database file cs_course_scheduling.sqlite not found in current working directory.')
except ValueError:
    print(print("requested academic year must be an integer"))
