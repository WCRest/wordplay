import pystache
from pystache import Renderer



def getAttr(ind):
	return 'class="step" data-x="' + str(ind * 500) + '" data-y="0"'

def getDiv(line, ind):
	content = "<div " + getAttr(ind) + " >"
	content += line + "</div>\n"
	return content

def createContent(lines):
	content = ""
	for i in range(0,len(lines)):
		content+= getDiv(lines[i][1], i)
	return content

def writeTo(linesArray, fName):
	fTemp1 = open("temp1._html").read()
	fTemp2 = open("temp2._html").read()
	handle = open(fName, "w")
	cont = createContent(linesArray)
	handle.write(fTemp1 + cont + fTemp2)
	handle.close()


##>>> cont = content.createContent(pLines)