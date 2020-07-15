import configparser

config = configparser.ConfigParser()

config.read("config.ini")

title = config.get("header","title")
subtitle = config.get("header","subtitle")

headerFile = open("partial/header.html","r")
outputFile = open("out/index.html", "w")

header = "".join(headerFile.readlines())

outputFile.write(header)

outputFile.write(f"<title>{title}</title>\n")
outputFile.write(f"<h1>{title}</h1>\n")
outputFile.write(f"<h3>{subtitle}</h3>\n")
outputFile.write(f"</head>\n")
