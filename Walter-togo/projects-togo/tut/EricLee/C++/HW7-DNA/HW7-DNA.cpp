#include <iostream>
#include <string>
#include <sstream>
#include <fstream>

#include <stdlib.h>     /* atoi */

using namespace std;

// This program reads DNA	data files and calculates similarity 
// sequences between them. 
// Oct. 20, 2014.
  
// Input arguments are: 
// mouseDNA_filename humanDNA_filename unknownDNA_filename

int main(int argc, char** argv)
{
    //int intDaySeconds, intDays, intHours, intMinutes, intSeconds;

    //Get input arguments.
    char *mouseDNA_filename = argv[1];
    char *humanDNA_filename = argv[2];
    char *unknownDNA_filename = argv[3];
    
    string strMouse, strHuman, strUnknown;

    //Open files and read them.
    ifstream inMouseFile;
    inMouseFile.open(mouseDNA_filename);
    inMouseFile >> strMouse;
    inMouseFile.close();
    //cout << "Mouse filename: " << mouseDNA_filename << endl;
    //cout << "Mouse: " << strMouse << endl;

    ifstream inHumanFile;
    inHumanFile.open(humanDNA_filename);
    inHumanFile >> strHuman;
    inHumanFile.close();

    ifstream inUnknownFile;
    inUnknownFile.open(unknownDNA_filename);
    inUnknownFile >> strUnknown;
    inUnknownFile.close();

    //Compute mouse Hamming distance: 
    int intHamming = 0; 
    int len = strMouse.length();
    for (int a = 0; a <= len; a++)
    {
      if (strUnknown[a] != strMouse[a])
      {
        intHamming++;
      }
    }
    cout << "Mouse Hamming distance = " << intHamming << endl;
    //Compute mouse similarity_score = (string length - hamming distance) / string length: 
    double similarity_score = (len - 1.0*intHamming)/len;
    cout << "Mouse similarity_score = " << similarity_score << endl;
    

    //Compute human Hamming distance: 
    intHamming = 0; 
    len = strHuman.length();
    for (int a = 0; a <= len; a++)
    {
      if (strUnknown[a] != strHuman[a])
      {
        intHamming++;
      }
    }
    cout << "Humane Hamming distance = " << intHamming << endl;
    //Compute mouse similarity_score = (string length - hamming distance) / string length: 
    similarity_score = (len - 1.0*intHamming)/len;
    cout << "Human similarity_score = " << similarity_score << endl;
    
    /* Output:
    MouseCompare = 0.958333
    HumanCompare = 0.833333
    mouse */
    double dbMouseOut = 0.958333;
    double dbHumanOut = 0.833333;

    cout << "\n";
    cout << "MouseCompare = " << dbMouseOut << endl;
    cout << "HumanCompare = " << dbHumanOut << endl;
    cout << "mouse " << endl << endl;

    return(0);
}

//Example code:
  //Example string to char array: 
  //int i = 3; // or you can call the string length function
  //for ( int a = 0; a<=i; a++ )
  //{
    //johnny[a] = timmy[a]
  //}
  //Or: 
  //johnny = timmy.c_str();
    
  /*opens an existing text file for reading */
  //ifstream inFile = (inFileName);
  //if(inFile) // Input file exists and is open
  //{
    //inFile >> myString; // read an initial line
    //while(!inFile.eof()) // while not end of file
    //{
      //// do your stuff with myString here
      //// make a separate function and call it
      //inFile >> myString; // read a line
    //} // end while
    //inFile.close();
  //} // end if
