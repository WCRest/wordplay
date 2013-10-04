import json
import re
#import ID
#import pygn


def strToTimestamp(timeStr):
	minutes = float(timeStr[0:2])
	seconds = float(timeStr[3:])
	return 60.0 * minutes + seconds

#per-line outputs a tuple of (timestamp, lyric)
#####TODO: deal with every other line which is empty
def parseLine(line):
	time = re.findall('\[.+\]', line)[0][1:-1]
	time = strToTimestamp(time)
	#lyric = re.findall('\].+', line)[0][1:]
	lyricSet = re.findall('\].+', line)
	
	#deal with timestamps wthout lyrics
	if len(lyricSet) == 0:
		lyric = None
	else:
		lyric = lyricSet[0][1:]

	return [time, lyric]

def linesToArray(lines):
	parsedLines = []
	for i in range(4, len(lines)):
			line = parseLine(lines[i])
			if line[1] != None:
				parsedLines.append(line)
		#print i
	return parsedLines

"""
f = open('../lyrics/tiktok.lrc')
lines = f.readlines()
f.close()
pLines = parser.linesToArray(lines)
"""