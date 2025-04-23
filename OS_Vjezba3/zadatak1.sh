#!/bin/bash

ap="$1"
dn="$2"
if [ $# -ne 2 ];then 
	echo "Potrebno je unijeti tocno 2 argumenta"
	exit 1
else	
	fajlovi=0
	
	for datoteka in "$ap"/*"$dn"; do	
			if [ -e "$datoteka" ]; then
				echo "$(basename "$datoteka")"
				(( fajlovi++ ))
			fi
	if [ "$fajlovi" -eq 0 ]; then
		echo "Nema fileova sa tim nastavkom"
	fi
		
	done
fi

