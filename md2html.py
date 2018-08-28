# Markdown to html converter

import markdown2 as md
import os
import sys


# User input
mdfile_path = sys.argv[1]
style = sys.argv[2]
html_name = sys.argv[3]

# Styles folder (css)
source_folder = os.getcwd()
css_folder = os.path.join(source_folder, 'css')

# Creating pre-html miscellaneous and adding style
pre_html = ''
pre_html += '<!DOCTYPE html>\n'
pre_html += '<html>\n'
pre_html += '<head>\n'
pre_html += '    <link rel="stylesheet" href="' + css_folder + '/' + style + \
            '.css">\n'
pre_html += '</head>\n'
pre_html += '<body>\n'

# Check validity of extension of markdown file
valid_extensions = ["md"]
filename = os.path.basename(mdfile_path)
extension = filename.split('.')[1]

if not extension in valid_extensions:
    raise RuntimeError("That file extension is not supported!")

# Reading markdown file and converting it
with open(mdfile_path, 'r') as mdfile:
    mdtext = mdfile.read()

main_html = md.markdown(mdtext)

# Creating post-html
post_html = ''
post_html += '</body>\n'
post_html += '</html>\n'

# Putting all the html text together
html = pre_html + main_html + post_html

# Getting path to where the md file is
mdfile_dir = os.path.dirname(os.path.abspath(mdfile_path))
html_path = os.path.join(mdfile_dir, html_name)
html_path += ".html"

# Write html to file
with open(html_path, 'w') as html_file:
    html_file.write(html)
