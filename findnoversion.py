import os
i=0
for root, dirlist, filelist in os.walk("./"):
	toremove=[]

	for ss in ['.repo','out']:
		if ss in dirlist:
			toremove.append(ss)

	for ss in dirlist:
		gpath = os.path.join(root,ss,'.git')
		if os.path.isdir(gpath):
			toremove.append(ss)

	for ss in toremove:
		dirlist.remove(ss)

	if (len(dirlist)==0) and (len(toremove)==0):
		print i, root
		i=i+1
