#!/bin/bash

dir_name=$1
mkdir "$dir_name"
arc_name=$2

shift
shift

arr=("$@")

for var in ${arr[*]}
do
	find ~ -depth -name "*.$var" -print0 | while IFS= read -r -d '' path
	do
		base=$(basename --suffix=".$var"  "$path")
		new_path="$dir_name"/"$base.$var"
		echo "$new_path"
		counter=0
		while [ -f "$new_path" ]
		do
	    	counter=$(($counter+1))
	    	new_path="$dir_name"/"$base($counter).$var"
		done
		cp "$path" "$new_path"
	done
done

tar -cf $arc_name.tar $dir_name

echo 'done'