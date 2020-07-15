import configparser

config = configparser.ConfigParser()

config.read("config.ini")

title = config.get("header","title")
subtitle = config.get("header","subtitle")

outputFile = open("out/index.html", "w")

headerFile = open("partial/header.html","r")
header = "".join(headerFile.readlines())

footerFile = open("partial/footer.html","r")
footer = "".join(footerFile.readlines())

outputFile.write(header)

outputFile.write(f"<title>{title}</title>\n")
outputFile.write(f"<h1>{title}</h1>\n")
outputFile.write(f"<h3>{subtitle}</h3>\n")
outputFile.write(f"</head>\n")

contentFile = open("content/index.html","r")
content = "".join(contentFile.readlines())

outputFile.write(f"<body>\n")
outputFile.write(content)

outputFile.write(footer)
