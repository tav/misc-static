#! /bin/sh

python2.5 `which s3cmd` -v -P -M sync --delete-removed files/ s3://static.ampify.it/