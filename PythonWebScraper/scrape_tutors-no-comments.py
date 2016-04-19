#!/usr/python

import re
import urllib
import csv
index_url = "http://www.tutorfinder.com.au/tutor/"
source_code_object = urllib.urlopen(index_url)
source_code = source_code_object.read()
tutor_pattern = re.compile('href="([^"]*).*([0-9]{2}-[a-zA-Z]{3}-[0-9]{4}) ([0-9]{2}:[0-9]{2})')
tutor_urls = re.findall(tutor_pattern, source_code)
tutor_urls = [list(x) for x in tutor_urls]
for tutor in tutor_urls:
	tutor[0] = 'http://www.tutorfinder.com.au/tutor/' + tutor[0]
def find_details(tutor):
	tutor_url = tutor[0]
	try:
		tutor_page_code = urllib.urlopen(tutor_url).read()
	except:
		for i in range(0,3):
			tutor.append("ERROR with url")
		return
	not_operating = re.search('"message">', tutor_page_code)
	if not_operating:
		for i in range(0,3):
			tutor.append("Not Operating")
		return
	tutor_name = re.search('"float:left">([^<]*)', tutor_page_code)
	if tutor_name:
		tutor.append(tutor_name.groups()[0])
	if not tutor_name:
		tutor.append("NO NAME")
	tutor_phone = re.search("Phone:.*?'blue'>([^<]+)", tutor_page_code)
	if tutor_phone:
		tutor.append(tutor_phone.groups()[0])
	if not tutor_phone:
		tutor.append("NO PHONE")
	tutor_email = re.search("class='blue'><b>Email:.*?'blue'>([^<]+)", tutor_page_code)
	if tutor_email:
		tutor.append(tutor_email.groups()[0])
	if not tutor_email:
		tutor.append("NO EMAIL")
count = 1
number_of_tutors = len(tutor_urls)
for i in tutor_urls:
	print "Doing {:} of {:}".format(count,number_of_tutors)
	count +=1
	find_details(i)
with open('output.csv', 'w') as output:
	output_writer = csv.writer(output)
	tutor_urls[:0] = [['URL', 'Last Updated Date', 'Last Updated Time', 'Name', 'Phone', 'Email']]
	for i in tutor_urls:
		output_writer.writerows([i])
output.close()

