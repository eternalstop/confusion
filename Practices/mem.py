# coding=utf-8
from __future__ import division
total_mem = 0
free_mem = 0
with open('M:\Python Pro\Practices\meminfo.txt') as memfd:
    for mem_lines in memfd:
        if mem_lines.startswith('MemTotal'):
            global total_mem
            total_mem = mem_lines.split()[1]
            continue
        if mem_lines.startswith('MemFree'):
            global free_mem
            free_mem = mem_lines.split()[1]
            break
print ("Following are information of System Memry \n")
print ("TotalMem" + "=" "%.2f Mb \n" % (int(total_mem)/1024.0), "FreeMem" + "=" "%.2f Mb" % (int(free_mem)/1024.0))
print ("UsePer" + "=" "%.2f" % ((1-int(free_mem)/int(total_mem))*100) + "%" + "\n")
