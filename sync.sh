#! /bin/sh

s3cmd -v -P -M sync --delete-removed files/ s3://static.ampify.it/