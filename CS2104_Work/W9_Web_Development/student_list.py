"""
@date: 10/17/23
@author: Peter Murphy
@PID: pmurphy26
@assignment: W9 CW Reading data off html
"""

import re
# use regex to parse the html string and extract the target data

in_filename = 'student_list.html'
out_filename = 'student_list.txt'
# defines the name of the file that you're going to read and write into

content = open(in_filename,"r")
clear_output_file = open(out_filename,"w").close()
output = open(out_filename,"a")
# content and output are file stream object, you could use 'r'(read), 'w'(write) or 'a'(append)

str = content.read() 
# read() method will turn a file stream into a regular string

matches = re.findall('<td>(\w*)<\/td>\s*<td>(\w*)<\/td>\s*<td>(\d)', str)
for match in matches:
    data = match[0] + ", " + match[1] + "\t" + match[2]
    written_str = data.rjust(22)
    output.write(written_str)
    output.write("\n")
# use matches = re.findall(pattern,str), you need to figure out what pattern to use
# pattern = r'<td>(\w*)<\/td>\s*<td>(\w*)<\/td>\s*<td>(\d)'
# once you get a match, you access different components from the match object using indices.
# use output.write() to write content to the output file
# for output formatting, you can try rjust()

output.close()
content.close()
#close the stream