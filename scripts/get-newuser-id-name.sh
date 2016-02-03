#! /bin/bash

#xmlstarlet sel -t -m "users/row" -v "@Id" -o ":" -v "@DisplayName" -o ":" -v "@Reputation" -n Users.xml
xmlstarlet sel -t -m "users/row" -v "@Id" -o ":" -v "@DisplayName" -o ":" -v "@Reputation" -n newUsers.xml
#xmlstarlet sel -t -m "users/row" -v "@Id" -o ":" -v "@DisplayName" -o ":" -v "@Reputation" -n short-Users.xml
