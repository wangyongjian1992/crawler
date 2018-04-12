import urllib2
import re

req = urllib2.Request('http://www.budejie.com/text/2')
req.add_header('User-Agent','Mozilla/5.0 (X11;Ubuntu;Linux x86_64;rv:31.0) Gecko/20100101 Firefox/31.0')
req.add_header('Referer','http://www.budejie.com/text/1')
resp = urllib2.urlopen(req)


html = resp.read().decode('utf-8')


pattern = re.compile(r'<div class="j-r-list-c-desc">\s+(.*)\s+</div>')
subpattern = re.compile(r'<.*?>')
result = re.findall(pattern,html)
print '--------------before process:'
print result[0]
print '--------------after process:'

process_result = []
for passage in result:
    process_result.append(re.sub(subpattern,'',passage))

for p_passage in process_result:
    print '================' * 5
    print p_passage

