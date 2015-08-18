import os
import xml.dom.minidom

emptyproject = []
gitproject = []

def recursive_list( pathname ):
	global emptyproject
	global gitproject
	dirs = os.listdir( pathname )
	if '.git' in dirs:
		gitproject.append(pathname)
		return
	if not dirs:
		emptyproject.append(pathname)
		return
	for item in dirs:
		itempath = os.path.join(pathname,item)
		if os.path.isdir(itempath):
			recursive_list( itempath )

for ii in os.listdir("."):
	if ii not in ['out','.repo']:
		iipath = os.path.join(".",ii)
		if os.path.isdir(iipath):
			recursive_list( iipath )

xmlroot = xml.dom.minidom.parse('./.repo/manifest.xml')
manifestproj = []
for node in xmlroot.childNodes[0].childNodes:
	if node.nodeName == 'project':
		manifestproj.append(os.path.join('./',node.getAttribute('path')))


print "----------------------------------"
print "Find not git(ize) folder:"
for ii in emptyproject:
	print ii
print "-----------------------------------"
print "Find project not in manifest:"
for ii in gitproject:
	if ii not in manifestproj:
		print ii
print "-----------------------------------"
print "Find manifest project not exist:"
for ii in manifestproj:
	if ii not in gitproject:
		print ii
print ""


