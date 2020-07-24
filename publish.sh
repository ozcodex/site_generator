#!/bin/bash

mkdir -p out

git for-each-ref --format="%(refname:short)|%(subject)" refs/tags > changelog.txt

python3 build.py

cp -r assets/* out/

git push

git push --tags

cp -r out/* ../ZeroNet/my_site/
