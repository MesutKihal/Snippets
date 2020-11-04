import csv

html_str = ''

html_str += '<html>\n'
html_str += '\t<ul>\n'

with open('csv_business.csv' , 'r') as csv_file:
	csv_read = csv.DictReader(csv_file)
	for line in csv_read:
		html_str += f'\t\t<li><b style="font-size:22px;font-family:rod">Series reference:</b> {line["Series reference"]} <b style="font-size:22px;font-family:rod">Period:</b> {line["Period"]} <b style="font-size:22px;font-family:rod">Description:</b> {line["Description"]}</li>\n'

html_str += '\t</ul>\n'
html_str += '</html>'

with open('csv_html_page.html', 'w') as html_file:
	html_file.write(html_str)
