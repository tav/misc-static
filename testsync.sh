#! /bin/sh

s3cmd -v -P -M sync --dry-run --delete-removed files/ s3://static.ampify.it/