#!/bin/bash

git commit -am "Update Content"

mkdir -p out

FORMAT="%(refname:short)|%(*creatordate:short)|%(subject)"

git for-each-ref --sort=-refname --format="$FORMAT" refs/tags > changelog.txt

python3 build.py

cp -r assets/* out/
cp -r out/* ../ZeroNet/my_site/

cp -r out/* 19NW5k68A3qRsomy42hLBZFsHbQ6kFg2yN/

git commit -am "Update site mirror"

git push

git push --tags

echo "Done!"
