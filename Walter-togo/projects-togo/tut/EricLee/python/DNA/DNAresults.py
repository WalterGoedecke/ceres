#!/usr/bin/python3

import os
import sys
from collections import defaultdict

#Create file object, and write to club file form. 
#objFile = open(filePath, 'w')

def main(): 

  # -------------------------------
  # Variables & static class variables. 
  # - - - - - - - - - - - - - - - -
  # Create a static class of boolean Asian country flags, and initialize to True. 
  #  class ASflags(object):
  #    flgCN, flgKR, flgRU = (True,)*3
  # - - - - - - - - - - - - - - - -
  flgDiab = False
  tgDiab = '00'
  flgSkin = False
  tgSkin = '00'
  # - - - - - - - - - - - - - - - -
  # Create a static class of flags, and initialize to False.
  class Flags(object):
    flgDiab, flgSkin = (False,)*2
  # Create a static class of tags, and initialize to 'OO'.
  class Tags(object):
    tgDiab, tgSkin, tg4994, tg1042713, tg1801282, tg1042714, tg1799883 = ('OO',)*7
  # -------------------------------

  # -------------------------------
  # Classes. 
  # - - - - - - - - - - - - - - - -
  class data(object):
    #Diabetes test.
    @staticmethod
    def rs7754840(strLine):
      strPiece = strLine.split( )
      if strPiece[0] == "rs7754840":
        flag = True
        tag = strPiece[3]
      else:
        flag = False
        tag = "OO"
      return (tag, flag);      
    # - - - - - - - - - - - - - -
    #Skin test.
    @staticmethod
    def rs1426654(strLine):
      strPiece = strLine.split( )
      if strPiece[0] == "rs1426654":
        flag = True
        tag = strPiece[3]
      else:
        flag = False
        tag = "OO"
      return (tag, flag);      
  # -------------------------------
  
  # -------------------------------
  # Input command line arguments. 
  # - - - - - - - - - - - - - - - -
  total = len(sys.argv)
  cmdargs = str(sys.argv)
  #print ("The total numbers of args passed to the script: %d " % total)
  #print ("Args list: %s " % cmdargs)
  # -------------------------------

  # -------------------------------
  # Open file and read. 
  # - - - - - - - - - - - - - - - -
  try:
    objFile = open(sys.argv[1], 'r')
    inputfile = sys.argv[1]
  except IndexError: 
    objFile = open('dna1.txt', 'r')
    inputfile = 'dna1.txt'
  print ("\nParsing " + inputfile)
  # -------------------------------

  # -------------------------------
  # Create dictionary & read lines.
  # - - - - - - - - - - - - - - - -
  datadict = {}
  # - - - - - - - - - - - - - - - -
  # Skip over commented lines. 
  for strLine in objFile:
    strPiece = strLine.split( )
    if strPiece[0] != "#":
      break
  # Add first data line to dictionary.
  datadict[strPiece[0]] = strPiece[3]
  # - - - - - - - - - - - - - - - -
  # Read data lines. 
  for strLine in objFile:
    strPiece = strLine.split( )
    # - - - - - - - - - - - - - - - -
    # Add to dictionary.
    datadict[strPiece[0]] = strPiece[3]
    # - - - - - - - - - - - - - - - -
    # Type-2 diabetes test:
    (tag, flag) = data.rs7754840(strLine)
    if flag == True:
      flgDiab = True
      tgDiab = tag
    # - - - - - - - - - - - - - - - -
    # Skin type test:
    (tag, flag) = data.rs1426654(strLine)
    if flag == True:
      flgSkin = True
      tgSkin = tag
    # - - - - - - - - - - - - - - - -
  objFile.close 
  # -------------------------------

  # -------------------------------
  # Read dictionary. 
  # - - - - - - - - - - - - - - - -
  # RS4994 test:
  Tags.tg4994 = datadict.get("rs4994")
  # RS1042713 test:
  Tags.tg1042713 = datadict.get("rs1042713")
  # RS1801282 test:
  Tags.tg1801282 = datadict.get("rs1801282")
  # RS1042714 test:
  Tags.tg1042714 = datadict.get("rs1042714")
  # RS1799883 test:
  Tags.tg1799883 = datadict.get("rs1799883")
  # -------------------------------

  # -------------------------------
  # Output results. 
  # - - - - - - - - - - - - - - - -
  if flgDiab == True:
    if tgDiab == "CG" or tgDiab == "CC":
      print ("1.3x Increased risk for Type-2 Diabetes")
    elif tgDiab == "GG":
      print ("Normal risk for type-2 diabetes")
    else:
      print ("No DNA info on type-2 diabetes")
  elif flgDiab == False:
    print ("No info on type-2 diabetes")
  # - - - - - - - - - - - - - - - -
  #if Flags.flgSkin == True:
  if flgSkin == True:
    if tgSkin == "AA":
      print ("Probably light-skinned, European ancestry")
    elif tgSkin == "AG":
      print ("Probably mixed African/European ancestry")
    elif tgSkin == "GG":
      print ("Probably darker-skinned, Asian or African ancestry")
    else:
      print ("No DNA info on skin type")
  # - - - - - - - - - - - - - - - -
  if Tags.tg4994 == 'AA' or Tags.tg4994 == 'TT':
    if Tags.tg1042713 == 'AA' or Tags.tg1042713 == 'TT': #ADRB2.
      print ("[12%] Genetic Privilege: Any Exercise Works For You")
      PPARG(Tags)
    else:
      RedBox1(Tags)
  else:
    RedBox1(Tags)
  print ("\n")
# -------------------------------

# -------------------------------
# Definitions. 
# - - - - - - - - - - - - - - - -
# Decisions. 
def RedBox1(Tags):
  print ("[88%] Genetic Disprivilege: Only High Intensity Exercise Will Help You Lose Weight")
  if Tags.tg1799883 == 'GG': #FABP2
    PPARG(Tags)
  else:
    if Tags.tg1801282 == 'CC': #PPARG again?!
      RedBox3(Tags)
    else:
      print ("[45%] Genetic Disprivilege: You Will Lose 2.5x As Much Weight on a Low Carb Diet")
def PPARG(Tags):
  if Tags.tg1801282 == 'CC':
    if Tags.tg1042714 == 'AA': #ADRB2 also. 
      print ("[16%] Genetic Privilege: Any Exercise Works For You")
    else:
      RedBox3(Tags)
  else:
    RedBox3(Tags)
def RedBox3(Tags):
  print ("[39%] Genetic Disprivilege: You Will Lose 2.5x As Much Weight on a Low Fat Diet")
# - - - - - - - - - - - - - - - -
# Decisions. 
# Type-2 diabetes test:
def rs7754840(strLine, Tags, Flags):
  strPiece = strLine.split( )
  if strPiece[0] == "rs7754840":
    Flags.flgDiab = True
    Tags.tgDiab = strPiece[3]
  return (Tags, Flags);      
# - - - - - - - - - - - - - - - -
# Skin type test:
def rs1426654(strLine, Tags, Flags):
  strPiece = strLine.split( )
  if strPiece[0] == "rs1426654":
    Flags.flgSkin = True
    Tags.tgSkin = strPiece[3]
  return (Tags, Flags);      
# - - - - - - - - - - - - - - - -
# RS4994 test:
def rs4994(strLine):
  strPiece = strLine.split( )
  if strPiece[0] == "rs4994":
    flag = True
    tag = strPiece[3]
  else:
    flag = False
    tag = "OO"
  return (tag, flag);      
# -------------------------------

main() 
