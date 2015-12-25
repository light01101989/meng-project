#! /bin/bash
 
xmlstarlet sel -T -t -v "/Identity/pnkey" -o ":\"" -v "/Identity/nameInfo[@type='personal']/rawName/suba" -o "\"" -n $1 | tr -d ' '
