"""
 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter, 
    then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags
 4. convert 	`#` => `<h1>` and `</h1>` 
 		`##` => `<h2>` and `</h2>` 
 		`###` => `<h3>` and `</h3>`
 5. convert `>` => `<blockquote>` and on the next line with no `>` end it with `</blockquote>` 
"""

import fileinput
import re

indent = False

def convertStrong(line):
  line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
  line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
  return line

def convertEm(line):
  line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
  line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
  return line

def convertHeading(line):
  line = re.sub(r'###(.*)', r'<h3>\1</h3>', line)
  line = re.sub(r'##(.*)', r'<h2>\1</h2>', line)
  line = re.sub(r'#(.*)', r'<h1>\1</h1>', line)
  return line

def convertBlock(line):
  line = re.sub(r'>(.*)', r'\1', line)
  return line

def convertAll(line):
  line = line.rstrip() 
  line = convertStrong(line)
  line = convertEm(line)
  line = convertHeading(line)
  return line

for line in fileinput.input():

  if ('>' in line and indent == False):
    line = convertBlock(line)
    line = '<blockquote><p>' + convertAll(line) + '</p>'
    indent = True
  elif ('>' in line and indent == True):
    line = convertBlock(line)
    line = '<p>' + convertAll(line) + '</p>'
  elif (not '>' in line and indent == True):
    indent = False
    line = '</blockquote><p>' + convertAll(line) + '</p>'
  else: # skip blockquote add normal p tags for line 
    line = convertAll(line)
    line = '<p>' + line + '</p>'


  print line,
