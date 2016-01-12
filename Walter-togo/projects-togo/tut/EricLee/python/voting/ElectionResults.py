#!/usr/bin/python3

import os
import sys

#Create file object, and write to club file form. 
#objFile = open(filePath, 'w')

# -------------------------------
# Command line arguments. 
total = len(sys.argv)
cmdargs = str(sys.argv)
#print ("The total numbers of args passed to the script: %d " % total)
#print ("Args list: %s " % cmdargs)

# - - - - - - - - - - - - - - - -
# Open file and read. 
try:
  objFile = open(sys.argv[1], 'r')
except IndexError: 
  objFile = open('Voting-data1.txt', 'r')
  
strContents = objFile.readlines() 
objFile.close 
# - - - - - - - - - - - - - - - -
# Assign lists for names and for vote sub-totals. 
lstNames = []
lstVotes = []
# - - - - - - - - - - - - - - - -
# Print header. 
print "\n"
print "Candidates     Votes    Percent"
print "==========     =====    ======="
# - - - - - - - - - - - - - - - -
# Process lines. 
for line in strContents:
  #Strip out white spaces.
  line = line.strip() 
  #Split the text
  words = line.split()
  #Form full name from 1st & 2nd words.
  name = words[0] + " " + words[1]
  lstNames.append(name)
  # - - - - - - - - - - - - - - - -
  #Add election results from 4 regions.
  count1 = int(words[2])
  count2 = int(words[3])
  count3 = int(words[4])
  count4 = int(words[5])
  sum = count1 + count2 + count3 + count4
  lstVotes.append(str(sum))
# - - - - - - - - - - - - - - - -
# Calculate grand total. 
Sum = 0
for sum in lstVotes:
  Sum = Sum + int(sum)
# - - - - - - - - - - - - - - - -
# Print line information. 
size = len(lstNames)
for i in range(size):
  strVote = str(int(lstVotes[i])*100/Sum) + " %"
  print "{} {} {}".format(lstNames[i].ljust(11), lstVotes[i].rjust(8), strVote.rjust(10))

# - - - - - - - - - - - - - - - -
# Print final analysis. 
maxVotes = max(lstVotes)
maxIndex = lstVotes.index(maxVotes)

winner = lstNames[maxIndex]
winner = winner.strip()
votes = lstVotes[maxIndex]

# - - - - - - - - - - - - - - - -
# Print final analysis. 
print "\nThe winner is {} with {} votes!\n".format(winner, votes)
print "Total votes polled: {}\n".format(Sum)

# -------------------------------
# Extras
# - - - - - - - - - - - - - - - -
#print 'We are the {} who say "{}!"'.format('knights', 'Ni')

#from array import *
#a=array('i',[1,2,3,4,5])
#for i in a:
#  print(i)

# split the text
#words = strContents.split()
# for each word in the line:
#for word in words:
  # prints each word on a line
  #print(word)
  
#lines = [line.strip() for line in open('filename')]
