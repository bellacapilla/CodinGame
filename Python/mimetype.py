import sys
import math

n = int(raw_input())  # Number of elements which make up the association table.
q = int(raw_input())  # Number Q of file names to be analyzed.

# Creates dictionary extention : mime identifier
exts_dic = {}
for i in xrange(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = raw_input().split()
    exts_dic[ext.lower()] = mt

# Creates list of valid extentions from each file name
ext_list = []
for i in xrange(q):
    fname = raw_input() 
    
    if len(fname) <= 258:
        verify = fname.rfind('.')
        
        if verify != -1 and 3 <= len(fname[verify+1:]) <= 10:
            ext_list.append(fname[verify+1:].lower())
        else:
            ext_list.append("UNKNOWN")
    else:
        ext_list.append("UNKNOWN")

# If extention from the list containing valid extentions exists in dictionary, the key is located and its value is retrieved, accordingly to the constraints.
for extention in ext_list:
    if extention in exts_dic and len(exts_dic[extention]) <= 50:
        print(exts_dic[extention])
    else:
        print("UNKNOWN")
