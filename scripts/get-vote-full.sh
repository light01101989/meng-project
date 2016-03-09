#! /bin/bash

xmlstarlet sel -t -m "votes/row" -o "V" -v "@Id" -o ",P" -v "@PostId" -o "," -v "@VoteTypeId" -o "," -v "@CreationDate" -n Votes.xml
