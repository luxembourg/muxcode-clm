INPUT="muxcode.raw"
OUTPUT="muxcode.plist"
KEYWORDS="keywords.txt"
FUNCTIONS="functions.txt"

keywords = open(KEYWORDS, "rU").readlines()
functions = open(FUNCTIONS, "rU").readlines()

input = open(INPUT, "rU").read()
output = open(OUTPUT, "w")

input = input.replace("@KEYWORDS@", "\n".join("<string>%s</string>" % k.strip() for k in keywords if k))
input = input.replace("@FUNCTIONS@", "\n".join("<string>%s</string>" % k.strip() for k in functions if k))

output.write(input)
output.close()
print "Compiled to", OUTPUT