import sys, thread, Queue, re, urllib2, urlparse, time, csv

### Set the site you want to crawl & the patterns of the fields you want to extract ###

siteToCrawl = "http://www.tutorfinder.com.au/"
fields = {}
    
fields["Email"] = '([@])'
fields["Number"] = '([0-9]{10})|([0-9]{4}[\-\s\._][0-9]{3}[\-\s\._][0-9]{3})'
### USING REGULAR EXPRESSIONS
# [0-9]{10} means values 0-9, totalling 10 characters
# [0-9]{4} values 0-9, 4 total characters
# [\-\s\._] with a DASH, SPACE, DOT or UNDERSCORE

### Default Fields

'''
fields["TutorID"] = '<title>(.*?)</title>'
fields["Rating"] = 'title="(S+) out of 5 stars"'
fields["Price"] = 'data-price="(.*?)"'
fields["Image"] = 'src="(s.*?)"'
'''

########################################################################

dupcheck = set()
q = Queue.Queue(25)
q.put(siteToCrawl)
csvFile = open("output.csv", "w",0)
csvTitles = dict(fields)
csvTitles["Link"] = ""
writer = csv.DictWriter(csvFile, fieldnames=csvTitles)
writer.writeheader()
def queueURLs(html, origLink):
    for url in re.findall('''<a[^>]+href=["'](.[^"']+)["']''', html, re.I):
        try:
            if url.startswith("http") and urlparse.urlparse(url).netlock !=  urlparse.urlparse(siteToCrawl).netlock: # Make sure we keep crawling the same domain
                continue
        except Exception:
            continue
        link = url.split("#", 1)[0] if url.startswith("http") else '{uri.scheme}://{uri.netloc}'.format(uri=urlparse.urlparse(origLink)) + url.split("#", 1)[0]
        if link in dupcheck:
            continue
        dupcheck.add(link)
        if len(dupcheck) > 99999:
            dupcheck.clear()
        q.put(link)
def analyzePage(html,link):
    print "Analyzing %s" % link
    output = {}
    for key, value in fields.iteritems():
        m = re.search(fields[key],html, re.I | re.S)
        if m:
            output[key] = m.group(1)
    output["Link"] = link
    writer.writerow(output)
def getHTML(link):
    try:
        request = urllib2.Request(link)
        request.add_header('User-Agent', 'Structured Data Extractor')
        html = urllib2.build_opener().open(request).read()
        analyzePage(html,link)
        queueURLs(html, link)
    except (KeyboardInterrupt, SystemExit):
        raise
    except Exception, e:
        print e
while True:
    thread.start_new_thread( getHTML, (q.get(),))
    time.sleep(0.5)

### EXTRA NOTES



