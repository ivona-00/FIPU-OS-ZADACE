#!/bin/bash

rad_dir=$(pwd)
n=1
for datoteka in "$rad_dir"/screenshots/*; do
	mv "$datoteka" "$rad_dir/screenshots/screenshots_${n}_$(basename "$datoteka")"
	(( n++ ))
done

for datoteka in "$rad_dir"/screenshots; do
	echo "Novo ime datoteke je $(basename "$datoteka")"
done
