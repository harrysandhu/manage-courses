#!/usr/bin/env python3
"""
    Generates homework from markdown notes.
"""
import os
import sys
import fnmatch
from dateutil.parser import parse 
from datetime import datetime
from dateutil.parser._parser import ParserError
import markdown2

def isDir(d):
    return (fnmatch.fnmatch(d, '*.*') == False)

def read_file(filename):
    try:
        f = open(filename, "r")
        return f.readlines()
    except IOError:
        print("File Input Error")
        sys.exit()


def main():
    drs = []
    for d in os.listdir("."):
        if isDir(d):
            drs.append(d)


    currentWeek = sys.argv[1]
    currentDate = parse(datetime.now().date().strftime('%Y-%b-%d')).date()
    todos = {}
    """
        go to lecture/ and lab/ and current week, 
        get all the TODOS in a list with key of the course
        output a txt file.
    """
    for d in drs:
        for f in ['lecture', 'lab']:
            weekDir = os.path.join(d, f, "week-"+str(currentWeek))
            for l in os.listdir(weekDir):
                if fnmatch.fnmatch(l, "*.md"):
                    content = read_file(os.path.join(weekDir, l))
                    if len(content) >= 2:
                        dstr = content[1][2:]
                        try:
                            dstr = parse(dstr).date()
                            if dstr == currentDate:
                                for i in range(len(content)):
                                    for line in content[i].split():
                                        if 'TODO:' in line:
                                            if d in todos:
                                                todos[d] = todos[d] + ['#### ',f,'\n'] + content[i+1:]
                                            else:
                                                todos[d] = content[i:i+1] + ['#### ', f,'\n'] + content[i+1:]
                        except ParserError:
                            continue

    htmlstr = ""                      
    f = open("./hw.main/"+str(currentDate)+".md", 'w')
    htmlstr += markdown2.markdown("# "+ str(currentDate) + "\n")
    f.write("# "+ str(currentDate) + "\n")                        
    for c in todos:
        htmlstr += markdown2.markdown("## "+ c+ ":\n")
        f.write("## "+ c+ ":\n")
        for i in todos[c]:
            htmlstr += markdown2.markdown(i)
            f.write(i)
        htmlstr += markdown2.markdown("---------------------------")
        f.write("---------------------------")    
    f.close()

    html5Base = """<!DOCTYPE html>
        <html>
        <head><title>%s</title></head>
        <body>
        %s
        </body>
        </html>
     """
    
    htmldoc = html5Base % (str(currentDate), htmlstr)
    f = open("./hw.main/"+str(currentDate)+".html", 'w')
    f.write(htmldoc)
    f.close()

if __name__=="__main__":
    main()