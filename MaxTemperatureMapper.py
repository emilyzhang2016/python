
#!/usr/bin/env python
#coding=utf-8

import re
import sys 

for line in sys.stdin:
	val = line.strip()
	(year, temperature, quality) =(val[15:19] ,val[87:92] ,val[92:93])
	if( temperature != "+9999" and re.match("[01459]" , quality)):
		print("%s\t%s" %(year, temperature)
