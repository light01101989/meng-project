#! /bin/bash
 
xmlstarlet sel -T -t -m "/Identity/associatedNames/name" -v "normName"  -o ":\"" -v "rawName/suba" -o " " -v "rawName/subb" -o "\"" -n $1 | grep 'lccn' | tr -d ' '
