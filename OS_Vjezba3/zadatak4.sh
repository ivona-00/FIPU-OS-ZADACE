#!/bin/bash

naziv_dir="$1"
radni_dir="$(pwd)"
zip_dat="svi_zapisi.zip"
kon_dir="$radni_dir/$naziv_dir"
if [ $# -ne 1 ];then
	echo "Moras unijeti tocno 1 argument"
	exit 1
else
	if [ -d "$kon_dir" ]; then
		echo "Taj direktorij postoji u istome direktoriju kao i skripta"
		(
		cd  "$kon_dir"
			zip -r "$zip_dat" . > /dev/null
		echo "Datoteke su kompresirane u $zip_dat"	
		)
	else 
		echo "Taj direktorij ne postoji"
		exit 1
	fi
fi

