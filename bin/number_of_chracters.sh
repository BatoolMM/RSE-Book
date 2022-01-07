
#!bin/bash

for characters in $1
 do
	echo "Elinor mentioned $(grep -ic "Elinor" $1)"
	echo "Marianne mentioned $(grep -ic "Marianne" $1)"
 done
