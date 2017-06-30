#!/usr/bin/env bash
# GET VARIABLES
filePath=$1
s3Path=$2
# GZIP FILE AND CREATE NEW FILEPATH NAME

gzip $filePath

uploadFile=$filePath".gz"
# UPLOAD FILE TO S3
aws s3 cp $uploadFile "s3://"$s3Path
# IF UPLOAD IS SUCCESSFULL REMOVE FILE
if [ "$?" == 0 ]; then
 rm $uploadFile
else
 echo "UPLOAD NOT SUCCESSFULL"
fi 
