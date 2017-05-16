import re
import os
from time import *


def currenttime():
    """ return current time in string """
    tmp = "%02d" % (localtime(time())[1]) + "%02d" % (localtime(time())[2]) + '_' + "%02d" % (localtime(time())[3]) + "%02d" % (localtime(time())[4]) + "%02d" % (localtime(time())[5])
    return tmp


def getfilelist(folder, includesubfolder):
    if includesubfolder == 0:
        filelist = os.listdir(folder)
    else:
        filelist = []
        for path, subdirs, files in os.walk(folder):
            if path == folder:
                filelist.extend(files)
            else:
                subfolder = path.split(folder)[1]
                for filename in files:
                    f = os.path.join(subfolder, filename)
                    filelist.append(str(f))
    return filelist

def create_list(start, step, stop):
    list0 = []
    a = start
    if start < stop:
        while a <= stop:
            list0.append(a)
            a += step
    elif start == stop:
        list0.append(a)
    else:
        while a >= stop:
            list0.append(a)
            a += step
    return list0


def str2floatlist(sweep):
    list_a = re.split(',', sweep)
    list0 = []
    for item in list_a:
        list_b = re.split(':', item)
        if len(list_b) == 1:
            list0.append(float(item))
        elif len(list_b) == 2:
            if list_b[0]<=list_b[1]:
                list0 += create_list(float(list_b[0]), 1, float(list_b[1]))
            else:
                list0 += create_list(float(list_b[0]), -1, float(list_b[1]))
        elif len(list_b) == 3:
            list0 += create_list(float(list_b[0]), float(list_b[1]), float(list_b[2]))
    return list0


def str2intlist(sweep):
    list_a = re.split(',', sweep)
    list0 = []
    for item in list_a:
        list_b = re.split(':', item)
        if len(list_b) == 1:
            list0.append(int(item))
        elif len(list_b) == 2:
            if list_b[0]<=list_b[1]:
                list0 += create_list(int(list_b[0]), 1, int(list_b[1]))
            else:
                list0 += create_list(int(list_b[0]), -1, int(list_b[1]))
        elif len(list_b) == 3:
            list0 += create_list(int(list_b[0]), int(list_b[1]), int(list_b[2]))
    return list0


def str2strlist(sweep, separation):
    list0 = re.split(separation, sweep)
    for i in range(len(list0)):
        list0[i] = list0[i].strip()
    return list0


def getkey(filepath, keyname):
    fp = open(filepath, 'r')
    name = '[' + keyname + ']'
    found = 0
    for eachline in fp:
        if (name in eachline) and (eachline[0] == '['):
            found = 1
            break
    if found == 1:
        value = []
        value_tmp = fp.readline().strip()
        while value_tmp != '':
            value.append(value_tmp)
            value_tmp = fp.readline().strip()
    else:
        value = []
    fp.close()
    return value


def getvalue(filepath, keyname, valuename):
    fp = open(filepath, 'r')
    name = '[' + keyname + ']'
    keyfound = 0
    valuefound = 0
    for eachline in fp:
        if name in eachline:
            keyfound = 1
            break
    if keyfound == 1:
        for eachline in fp:
            if (eachline[0] != '#') and (valuename in eachline):
                valuefound = 1
                break
        if valuefound == 1:
            value = eachline.strip().split('=')[1].strip()
        else:
            value = ''
    else:
        value = ''
    fp.close()
    return value


def main():
    scale_start = 0.815
    scale_step = -0.05
    scale_stop = 0.815
    scale_sweep = str(scale_start) + ':' + str(scale_step) + ':' + str(scale_stop)
    scalelist = str2floatlist(scale_sweep)
    print(scalelist)


if __name__ == '__main__':
    main()



