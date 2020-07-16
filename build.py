from configparser import ConfigParser

config = ConfigParser()

def readFileContent(filename):
    f = open(filename,"r")
    content = "".join(f.readlines())
    return content

def writeHeader(f,name=None):
    title = config['header']['title']
    subtitle = config['header']['subtitle']
    header = readFileContent("partial/header.html")
    f.write(header)
    if name:
        name = " - " + name.capitalize()
    f.write(f"<title>{title}{name}</title>\n")
    f.write(f"</head>\n")
    f.write(f"<body>\n")
    f.write(f"<h1>{title}</h1>\n")
    f.write(f"<h3>{subtitle}</h3>\n")

def buildPage(name,content=None):
    if not content:
        content = readFileContent(f"content/{name}.html")
    outputFile = open(f"out/{name}.html", "w")
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
    content = "<ul>"
    content += "<li><a href=\"index.html\">Index</a></li>"
    content += "<li><a href=\"changes.html\">Changelog</a></li>"
    content += "<li><a href=\"sitemap.html\">Sitemap</a></li>"
    return content

def main():
    config.read("config.ini")
    content = readFileContent("content/index.html")
    buildPage("index")
    buildPage("changes",generateChangelog())
    buildPage("sitemap",generateSiteMap())

if __name__ == "__main__" :
    main()
