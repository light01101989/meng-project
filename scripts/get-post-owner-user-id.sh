#! /bin/bash

#xmlstarlet sel -t -m "posts/row" -o "P" -v "@Id" -o ":" -v "@PostTypeId" -o ":" -v "@OwnerUserId" -o ":P" -v "@ParentId" -o ":" -v "@Score" -n short-Posts.xml
#xmlstarlet sel -t -m "posts/row" -o "P" -v "@Id" -o ":" -v "@PostTypeId" -o ":" -v "@OwnerUserId" -o ":P" -v "@ParentId" -o ":" -v "@Score" -o ":" -v "@AcceptedAnswerId" -n short-Posts.xml
xmlstarlet sel -t -m "posts/row" -o "P" -v "@Id" -o ":" -v "@PostTypeId" -o ":" -v "@OwnerUserId" -o ":P" -v "@ParentId" -o ":" -v "@Score" -o ":" -v "@AcceptedAnswerId" -n Posts.xml
#xmlstarlet sel -t -m "posts/row" -o "P" -v "@Id" -o ":" -v "@PostTypeId" -o ":" -v "@OwnerUserId" -n Posts.xml
