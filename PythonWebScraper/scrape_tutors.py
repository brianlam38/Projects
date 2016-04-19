#!/usr/python

#import some packages. Google to find out more about them.
import re
import urllib
import csv

#I like to put the url into a variable to save typing out again if I need it. 
index_url = "http://www.tutorfinder.com.au/tutor/"

#This is a request object. From this you can grab source code, headers, other useful things. We will just use the source code.
source_code_object = urllib.urlopen(index_url)
source_code = source_code_object.read()

#The pattern that matches the url and (for funsies) the last update date and time. Putting into a variable to save space writing later.
tutor_pattern = re.compile('href="([^"]*).*([0-9]{2}-[a-zA-Z]{3}-[0-9]{4}) ([0-9]{2}:[0-9]{2})')

#Note how I use findall. I could have fed in each line of the variable source_code and looked at that. But findall just finds them all into a list for me :)
tutor_urls = re.findall(tutor_pattern, source_code)

#turn a list of tuples into list of list for ease of manipulations and index access
tutor_urls = [list(x) for x in tutor_urls]

#add on the rest of the url to the first part
for tutor in tutor_urls:
	tutor[0] = 'http://www.tutorfinder.com.au/tutor/' + tutor[0]
#Function to now go to each of the tutor urls and pull the details

def find_details(tutor):
	tutor_url = tutor[0]
#putting in an exception-grabber so that if the url fails, it doesn't mess up the whole program
	try:
		tutor_page_code = urllib.urlopen(tutor_url).read()
	except:
		for i in range(0,3):
			tutor.append("ERROR with url")
		return
#Some tutors are not operating and show the same message
	not_operating = re.search('"message">', tutor_page_code)
	if not_operating:
		for i in range(0,3):
			tutor.append("Not Operating")
		return
#regex to find name, phone and email and append to the tutor details list element
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
#There are 3000+ of these, so good to know where we are up to when running it.
for i in tutor_urls:
	print "Doing {:} of {:}".format(count,number_of_tutors)
	count +=1
	find_details(i)

#output to a csv file
with open('output.csv', 'w') as output:
	output_writer = csv.writer(output)
#add some headers would make it look nicer
	tutor_urls[:0] = [['URL', 'Last Updated Date', 'Last Updated Time', 'Name', 'Phone', 'Email']]
	for i in tutor_urls:
		output_writer.writerows([i])
output.close()

