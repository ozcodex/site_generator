# Site Generator

The idea behind this proyect is generate the html for a 90's styled website that i'm creating in Zeronet, you can see it here:

http://127.0.0.1:43110/19NW5k68A3qRsomy42hLBZFsHbQ6kFg2yN/index.html

You need to have [Zeronet](https://github.com/HelloZeroNet/ZeroNet) on you machine to be able to visit that site.

A mirror to the site was published in this repository at: [ozcodex.github.io](https://ozcodex.github.io/)

I want to do it in the lowest level possible, using only the language tools, without external libraries.

Initially i will use python to make the things a bit simpler.

The idea is to have partial content of the site (like header, footer, menu, each page content) maybe a site structure in a text file.

### The changelog

If im able to i will try to use semantic versioning with git tags and use that to generate the changelog

the instruction used to generate the changelog can be seen on the publish.sh script

To add a new version I use:

``` git tag -a v1.0 -m "Description" ```
