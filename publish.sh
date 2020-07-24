#!/bin/bash

mkdir -p out

git for-each-ref --format="%(refname:short)|%(taggerdate:short)|%(subject)" refs/tags > changelog.txt

python3 build.py

cp -r assets/* out/

git push

cp -r out/* ../ZeroNet/my_site/
