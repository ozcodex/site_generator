import os
import sys

def readFileContent(filename):
    f = open(filename,"r")
    content = "".join(f.readlines())
    return content

def writeHeader(f,name=None):
    global site
    header = readFileContent("partial/header.html")
    header = header.replace("{site}",site)
    f.write(header)
    if name:
        name = " - " + name.capitalize()

def buildPage(name,route,content=None):
    if not content:
        content = readFileContent(f"content/{route}{name}.html")
    if not os.path.isdir(f"out/{route}"):
        os.mkdir(f"out/{route}")
    outputFile = open(f"out/{route}{name}.html", "w")
    footer = readFileContent("partial/footer.html")
    writeHeader(outputFile,name)
    outputFile.write(content)
    outputFile.write(footer)

def generateChangelog():
    changelogFile = open("changelog.txt", "r")
    content = "<table>\n"
    content += "<thead>\n"
    content += "<tr>\n"
    content += "<th>Version</th>\n"
    content += "<th>Date</th>\n"
    content += "<th>Changes</th>\n"
    content += "</tr>\n"
    content += "</thead>\n"
    content += "<tbody>\n"
    for change in changelogFile.readlines():
        parts = change.split("|")
        vers = parts[0]
        date = parts[1]
        desc = parts[2]
        content += "<tr>\n"
        content += f"<td>{vers}</td>\n"
        content += f"<td>{date}</td>\n"
        content += f"<td>{desc}</td>\n"
        content += "</tr>\n"
    content += "</tbody>\n"
    content += "</table>\n"
    return content

def generateSiteMap():
    content = "<p>Estas son todas las paginas presentes en este sitio:</p>"
    content += "<ul>\n"
    for filename in os.listdir("content"):
        name, ext = os.path.splitext(filename)
        if ext == '.html':
            name = name.capitalize()
            content += f"<li><a href=\"{filename}\">{name}</a></li>\n"
    content += "<li><a href=\"changes.html\">Changelog</a></li>\n"
    content += "<li><a href=\"sitemap.html\">Sitemap</a></li>\n"
    content += "</ul>\n"
    return content

def buildPagesIn(folder,route):
    for filename in os.listdir(folder):
        name, ext = os.path.splitext(filename)
        path = os.path.join(folder, name)
        if os.path.isdir(path):
           buildPagesIn(path,route+name+"/")
        if ext == '.html':
            buildPage(name,route)


def main():
    global site
    if len(sys.argv) > 2:
        site = str(sys.argv[1])
    else:
        site = ""
    route = ""
    buildPage("changelog",route,generateChangelog())
    buildPage("sitemap",route,generateSiteMap())
    buildPagesIn("content",route) 

if __name__ == "__main__" :
    main()
