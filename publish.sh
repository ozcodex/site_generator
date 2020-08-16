#!/bin/bash

git commit -am "Update Content"

git push

git push --tags

mkdir -p out

FORMAT="%(refname:short)|%(*creatordate:short)|%(subject)"

git for-each-ref --sort=-refname --format="$FORMAT" refs/tags > changelog.txt

python3 build.py "/19NW5k68A3qRsomy42hLBZFsHbQ6kFg2yN"

cp -r assets/* out/
cp -r out/* ../ZeroNet/my_site/
rm -r out/*

python3 build.py

cp -r assets/* out/
cp -r out/* ../ozcodex.github.io/
rm -r out/*
git --git-dir=../ozcodex.github.io/.git push

echo "Done!"
