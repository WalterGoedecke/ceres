//Hw9crypto
// This program encrypts and decrypts messages. 

#include <iostream>
#include <string>
#include <sstream>
#include <fstream>

#include <stdlib.h>     /* atoi */
#include <algorithm>    // std::for_each

using namespace std;
//using namespace system;

/*---------Functions---------*/
/*- - - - - - - - - - - - - -*/
//Open & read input file.
string readFile (char* filename)
{
  string strLine;
  ifstream inFile;
  inFile.open(filename);
  getline(inFile, strLine);
  return strLine;
}
/*- - - - - - - - - - - - - -*/
//Open & write to output file.
void writeToFile (char *filename, const char *type, string output)
{
  string strFilename, newfilename;
  // Convert input file name character array to string. 
  stringstream ss;
  ss << filename;
  ss >> strFilename;
  cout << filename << " " << strFilename;
  //Create output file name. 
  if (type[1] == 'e')
  {
    newfilename = strFilename + ".enc";
  }
  else //if (type[1] == 'd')
  {
    newfilename = strFilename + ".dec";
  }

  cout << newfilename << endl;

  //Convert string back to character array. 
  const char *cOutFile = newfilename.c_str();
  //Open and write to file. 
  ofstream outFile;
  outFile.open(cOutFile);
  outFile << output;
  return;
}
/*- - - - - - - - - - - - - -*/
//Encrypt character. 
char encryptChar (char crypt, int intNum)
//crypt is the character, intNum is the integer offset. 
{
  int intPiece = (int)crypt;
  int intNewPiece;
  char cNewPiece;

  //If puncutuation or space character, leave. 
  if (intPiece >= 32 and intPiece <= 47)
  {
    intNewPiece = intPiece;
  }
  else 
  {
    int intNumber = intPiece + intNum - 97;
    intNewPiece = (intNumber % 26) + 97;
  }
  cNewPiece = (char)intNewPiece;
  return cNewPiece;
}
/*- - - - - - - - - - - - - -*/
//Decrypt character. 
char decryptChar (char crypt, int intNum)
//crypt is the character, intNum is the integer offset. 
{
  int intPiece = (int)crypt;
  int intNewPiece;
  char cNewPiece;

  //If puncutuation or space character, leave. 
  if (intPiece >= 32 and intPiece <= 47)
  {
    intNewPiece = intPiece;
  }
  else 
  {
    intPiece = (int)crypt;
    //If lower case letter. 
    if (intPiece >= 97)
    {
      int intNumber = intPiece - intNum - 97;
      intNewPiece = (intNumber % 26);
      if (intNewPiece < 0)
      {
        intNewPiece = intNewPiece + 26;
      }
      intNewPiece = intNewPiece + 97;
    }
    else //If uppercase. 
    {
      int intNumber = intPiece - intNum - 65;
      intNewPiece = (intNumber % 26);
      if (intNewPiece < 0)
      {
        intNewPiece = intNewPiece + 26;
      }
      intNewPiece = intNewPiece + 65;
    }
  }
  cNewPiece = (char)intNewPiece;
  return cNewPiece;
}
/*- - - - - - - - - - - - - -*/
//Encrypt string. 
string encryptMessage (string strCrypto, int intNum)
{
  int len = strCrypto.length();
  char cNewPiece;
  string strOutput;

  for (int i = 0; i < len; i++)
  {
    cNewPiece = encryptChar(strCrypto[i], intNum);
    strOutput = strOutput + cNewPiece;
  }
  return strOutput;
}
/*- - - - - - - - - - - - - -*/
//Decrypt string. 
string decryptMessage (string strCrypto, int intNum)
{
  int len = strCrypto.length();
  char cNewPiece;
  string strOutput;

  for (int i = 0; i < len; i++)
  {
    cNewPiece = decryptChar(strCrypto[i], intNum);
    strOutput = strOutput + cNewPiece;
  }
  return strOutput;
}
/*---------End Functions---------*/

int main(int argc, char** argv)
{
  int intNum;
  string strCrypto, strInputFile, strOutFile;

  //string strType = argv[1];
  char *cType = argv[1];
  //string strNum = argv[2];
  char *cNum = argv[2];
  //string strInputFile = argv[3];
  char *cInputFile = argv[3];

  //Convert character to integer. This is the offset value.
  istringstream strStream(cNum);
  strStream >> intNum;

  //Encrypting sequence.
  if (cType[1] == 'e')
  {
    cout << endl << "Encrypting file: " << cInputFile << endl;	

    //Open and read input file.
    strCrypto = readFile(cInputFile);
    
    //Display to screen.
    cout << strCrypto << endl;;

    //Modify string. 
    string strOutput = encryptMessage(strCrypto, intNum);

    //Display to screen.
    cout << strOutput << endl << endl;

    //Open & write to output file.
    writeToFile(cInputFile, cType, strOutput);
  }
  else //Decrypting sequence.
  {
    cout << endl << "Decrypting file: " << cInputFile << endl;	

    //Open and read input file.
    strCrypto = readFile(cInputFile);

    //Display to screen.
    cout << strCrypto << endl;

    //Modify string. 
    string strOutput = decryptMessage(strCrypto, intNum);

    //Display to screen.
    cout << strOutput << endl << endl;

    //Open & write to output file.
    writeToFile(cInputFile, cType, strOutput);
  }  
  //Close input and output files. 
  //inFile.close();
  //outFile.close();
  return(0);
}

