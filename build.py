import configparser

config = configparser.ConfigParser()

config.read("config.ini")

title = config.get("header","title")
subtitle = config.get("header","subtitle")

headerFile = open("partial/header.html","r")
header = "".join(headerFile.readlines())

footerFile = open("partial/footer.html","r")
footer = "".join(footerFile.readlines())

contentFile = open("content/index.html","r")
content = "".join(contentFile.readlines())

#start of index page

outputFile = open("out/index.html", "w")

outputFile.write(header)

outputFile.write(f"<title>{title}</title>\n")
outputFile.write(f"</head>\n")
outputFile.write(f"<body>\n")

outputFile.write(f"<h1>{title}</h1>\n")
outputFile.write(f"<h3>{subtitle}</h3>\n")

outputFile.write(content)

outputFile.write(footer)

#end of index page

#start of changelog

outputFile = open("out/changes.html", "w")

outputFile.write(header)

outputFile.write(f"<title>{title} - Changelog</title>\n")
outputFile.write(f"</head>\n")
outputFile.write(f"<body>\n")

outputFile.write(f"<h1>{title}</h1>\n")
outputFile.write(f"<h3>{subtitle}</h3>\n")

outputFile.write("<table>\n")
outputFile.write("<tr>\n")
outputFile.write("<th>Version<th>\n")
outputFile.write("<th>Date<th>\n")
outputFile.write("<th>Changes<th>\n")
outputFile.write("</tr>\n")


#start of dinamicly generate table

changelogFile = open("changelog.txt", "r")

for change in changelogFile.readlines():
    parts = change.split("|")
    vers = parts[0]
    date = parts[1]
    desc = parts[2]
    
    outputFile.write("<tr>\n")
    outputFile.write(f"<td>{vers}</td>\n")
    outputFile.write(f"<td>{date}</td>\n")
    outputFile.write(f"<td>{desc}</td>\n")
    outputFile.write("</tr>\n")

#end of dinamic table
outputFile.write(f"</table>\n")

outputFile.write(footer)

#end of changelog
