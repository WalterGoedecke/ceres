// This program mimiks Eliza, the pre-artificial intelligence program long ago. 
// Oct. 28, 2014.
  
// Input argument is text file, e.g.: 
// responses.txt

#include <iostream>
#include <string>
#include <sstream>
#include <fstream>

#include <stdlib.h>     /* atoi */
#include <map>

using namespace std;

int main(int argc, char** argv)
{
  //Declarations.
  string strContent[100][2];

  //Get input arguments.
  char *filename = argv[1];
  
  //Open input file, e.g., responses.txt, and reads it.
  ifstream inputFile;

  if (filename != NULL)
  {
    inputFile.open(filename);
  }
  else
  {
    inputFile.open("responses.txt");
  }

  //Create map, similar to dictionary.
  map<string, string> dict;
      
  int index = 0;
  string line, word1, word2;
  while (!inputFile.eof())
  {
    //Fill string array. 
    getline(inputFile, line);
    stringstream stream(line);
    getline(stream, word1, '@');
    strContent[index][0] = word1;
    getline(stream, word2, '@');
    strContent[index][1] = word2;
    index++;
    //Fill dictionary.
    dict[word1] = word2;
  }
  inputFile.close();
  //printf("There were %d lines in the file.\n", i);

  //Output:
  string question, response; 
  bool flag;
  while (true)
  {
    flag = false;
    cout << "What question do you have about C++?" << endl; 
    cin >> question; 
    //Look in string array. 
    for (int i = 0;  i <= index; i++)
    {
      if (strContent[i][0] == question)
      {
        response = strContent[i][1];
        cout << response << endl;
        flag = true;
      }
    }
    //Look in dictionary. 
    map<string, string>::iterator it = dict.find(question);
    if(it != dict.end())
    {
      response = dict[question];
      cout << response << endl;
      flag = true;
    }
    //Exit strategy. 
    if (question == "quit" || question == "exit") 
    {
      cout << "Bye" << endl << endl;
      break;
    }
    if (!flag) 
    {
      cout << "Sorry, I don't know. What else can we talk about?" << endl;
    }
    cout << endl;
  } 
  
  return(0);
}



