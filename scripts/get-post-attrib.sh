#! /bin/bash

xmlstarlet sel -t -m "posts/row" -o "P" -v "@Id" -o "," -v "@PostTypeId" -o "," -v "@OwnerUserId" -o ",P" -v "@ParentId" -o "," -v "@Score" -o "," -v "@AcceptedAnswerId"  -o "," -v "@CreationDate" -o ",C" -v "@AnswerCount" -n $1
