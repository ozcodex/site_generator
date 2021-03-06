#!/bin/bash

git commit -am "Update Content"

git push

git push --tags

mkdir -p out

FORMAT="%(refname:short)|%(*creatordate:short)|%(subject)"

git for-each-ref --sort=-refname --format="$FORMAT" refs/tags > changelog.txt

python3 build.py

cp -r assets/* out/
cp -r out/* ../ozcodex.github.io/
rm -r out/*

cd ../ozcodex.github.io/
git add .
git commit -am "Update Content"
git push
cd -

echo "Done!"
