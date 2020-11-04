import csv
import re
#Read data from a csv file
with open('re_examples.csv', 'r') as csv_file:
	csv_data = csv.reader(csv_file)
	names = ''
	phone_numbers = ''
	emails = ''
	#Store data in a string 
	for data in csv_data:
		names += data[0]
		phone_numbers += data[1]
		emails += data[2]+'\n'


#Patterns
name_pattern = re.compile(r'[A-Z]{1}[a-z]*\s{1}[A-Z]{1}[a-z]*')
phone_pattern = re.compile(r'[0-9]{3}(-|.)[5]{3}(-|.)[0-9]{4}')
email_pattern = re.compile(r'[A-Za-z0-9+_.-]+@[A-Za-z0-9-]+\.[a-z]+')
#Matched names, phone number, and emails
name_matches = name_pattern.finditer(names)
phone_matches = phone_pattern.finditer(phone_numbers)
email_matches = email_pattern.finditer(emails)

#Print matches
for name in name_matches:
	print(name)