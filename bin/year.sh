!#bin/bash

for filename in $1 
	do
	  cut -d, -f 2 $1 | sort -n | uniq
	done
