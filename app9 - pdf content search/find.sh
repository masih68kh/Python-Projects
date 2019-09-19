#!/bin/bash
SAVEIFS=$IFS
IFS=$'\n'
# set me

for f in $(find "$1" -type f | grep ".pdf")
do
  echo $f
  echo "$(basename $f)"
  pdftotext -q "$f" ./txts/"$(basename $f)".txt || echo "Not a pdf file"
  echo '--'
done
# restore $IFS
