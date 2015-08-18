import os
import sys
import xml.dom.minidom

# STEP 1 : get all project path in manifest.xml
xmlroot = xml.dom.minidom.parse('./.repo/manifest.xml')
manifestprojlist=[]
for node in xmlroot.childNodes[0].childNodes:
	if node.nodeName == 'project':
		manifestprojlist.append(os.path.join('./',node.getAttribute('path')))

for manpname in manifestprojlist:
	print manpname

print "---------------------------------------------------------------------"

# STEP 2 : search all the source tree to get the .git project list
emptylist = []
gitlist = []
for root, dirlist, filelist in os.walk('./'):
	for ingpath in ['.repo','out']:
		if ingpath in dirlist:
			dirlist.remove(ingpath)
	
	if len(dirlist) == 0:
		emptylist.append(root)
	else:
		foundpath=[]
		for dirname in dirlist:
			if os.path.isdir(os.path.join(root,dirname,'.git')):
				foundpath.append(dirname)
				gitlist.append(os.path.join(root,dirname))
print "---------------------------------------------------------------------"

# STEP 3 : compare and print result
for projname in gitlist:
	if projname not in manifestprojlist:
		print projname


