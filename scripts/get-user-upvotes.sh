#! /bin/bash

xmlstarlet sel -t -m "users/row" -v "@Id" -o ":" -v "@DisplayName" -o ":" -v "@Reputation" -o ":" -v "@UpVotes" -o ":" -v "@DownVotes" -n $1
#xmlstarlet sel -t -m "users/row" -v "@Id" -o "," -v "@DisplayName" -o "," -v "@Reputation" -o "," -v "@UpVotes" -o "," -v "@DownVotes" -n Users.xml
#xmlstarlet sel -t -m "users/row" -v "@Id" -o ":" -v "@UpVotes" -n Users.xml
