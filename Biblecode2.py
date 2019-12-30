#!/usr/bin/python
import sys
import time
import os
print ("{:>55}".format("Where Word"))
print ("{:>60}".format("barradarcy@hotmail.com"))
print ' '
print ' '
text = raw_input('What is the name of the text file to read,\n if this has .txt at the end please type this too: '); #what file should be used as input.
print ' '
print ' '
blah = "~ ~ r e a d i n g t e x t . . . . \n"
for l in blah:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.2)
print (' ')
print (' ')
f = open(text, 'r') #open text for reading.
string = (f.read()) #read it.
charless=''.join(e for e in string if e.isalpha()).lower() #remove spaces, numbers, puct, also make it lowcase.
r = input("How many letters do you want to jump; ") #input number of jumps.
x = raw_input ('What are you looking for; ') #search term.
p = charless [::r] #extract every rth letter from charless text.
poss = p.rfind(x)
print p #print the string of r chars.
if x in p:
  print ' '
  print "Jump is:", #the ' , ' after this print means that the next print will be on the same line.
  print r
  print "Text is:"+text
  print "Term is:"+x
  print ' '
  print "{match}" #if x term is in pstring.
  print "Fist letter possition is the",
  print poss,
  print "th letter of every",
  print r,
  print "th letter"
  chose=raw_input ('Do you want to restart:y/n: ')
if x not in p:
  print ' '
  print "Jump is:",
  print r
  print "Text is:"+text
  print "Term is:"+x
  print ' ' 
  print "{no match}" #if x term is not in pstring.
  chose=raw_input ('Do you want to restart:y/n: ')
if chose == 'y':
 print ' '
 print("<RESTARTING>")
 print ' '
 os.system('cls') #clear screen, only works in windows.
 os.execl(sys.executable, sys.executable, *sys.argv)
if chose == 'n':
 print 'END'
 quit()
