#! /bin/bash
 
NAME=$(./get-name.sh $1 | cut -d':' -f2)

echo "digraph G {"
for ANAME in $(./get-assoc-names.sh $1 | cut -d':' -f2)
do
    echo "   "${NAME}" -> "${ANAME}";"
done
echo "}"
