#!/bin/bash

git commit -am "Update Content"

mkdir -p out

FORMAT="%(refname:short)|%(*creatordate:short)|%(subject)"

git for-each-ref --sort=-refname --format="$FORMAT" refs/tags > changelog.txt

python3 build.py

cp -r assets/* out/

git push

git push --tags

cp -r out/* ../ZeroNet/my_site/

echo "Done!"
