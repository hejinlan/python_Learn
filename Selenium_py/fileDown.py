import os,urllib.request,re
os.chdir(r'd:')
url = 
data = urllib.request.urlopen(url).read()
with open(filename, 'wb') as f:
f.write(data)
