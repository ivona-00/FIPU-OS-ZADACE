#!/bin/bash

broj=$1

if [ $# -ne 1 ]; then
	echo "Moras unijeti samo 1 argument"
	exit 1
else 
	if [[ $broj -lt 1 || $broj -gt 10 ]]; then
		echo "Moras unijeti broj od 1 do 10"
		exit 1
	else
		trenutni_broj=1
		touch brojevi.txt
		while [ $trenutni_broj -lt "$broj" ]; do
			echo "$trenutni_broj">>brojevi.txt
			((trenutni_broj++))
		done
	fi
fi
