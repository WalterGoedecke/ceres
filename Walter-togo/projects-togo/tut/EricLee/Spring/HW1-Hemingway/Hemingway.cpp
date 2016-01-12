// This program reads a text file and counts the number of 
//  words in it. 
// Jan. 28, 2015.
  
// Input argument is text file, e.g.: 
// responses.txt

#include <iostream>
#include <string>
#include <sstream>
#include <fstream>

#include <stdlib.h>     /* atoi */
#include <map>

#include <algorithm>
#include <cstdio>

using namespace std;


//Compare two strings while ignoring case. 
bool compareString(const string& a, const string& b) {
    // If a and b are not string of same length. 
    if(a.length() != b.length()) {
        return false; 
    }
    //for loop (i to a.length() ) {
    for (uint i = 0; i < a.length(); i++ ) {
        if( std::toupper(a[i]) != std::toupper(b[i]) ) {
            return false; 
        }
    }
    return true;
}

int main(int argc, char** argv) {
    //Declarations.
    //string strContent[100][2];

    //Get input arguments.
    char *filename = argv[1];

    //Open input files: the list of words and their rank, and the text file to read. 
    ifstream inputList, inputFile;
    inputList.open("rank_word.txt");
    if (filename != NULL) {
        inputFile.open(filename);
    }
    else {
        inputFile.open("responses.txt");
    }

    //Create map, similar to dictionary, to hold the list of words and their rank.
    map<int, string> dict;

    int numLines = 0, intKey;
    string line, strKey, strValue; //, strContent[100][2];
    while (!inputList.eof()) {
        //Fill string array. 
        getline(inputList, line);
        stringstream stream(line);
        //Split string at space.
        getline(stream, strKey, ' ');
        //Convert string key to integer. 
        stringstream(strKey) >> intKey;
        //strContent[numLines][0] = word1;
        getline(stream, strValue, ' ');
        //strContent[numLines][1] = word2;
        numLines++;
        //Fill dictionary.
        dict[intKey] = strValue;
    }
    inputList.close();
    //printf("There were %d lines in the list.\n", --numLines);

    //Create two arrays, one to hold the new found word, and the other to 
    // hold the number of times the word is found. 
    int arraysize = 100; 
    //string strContent[arraysize];
    //int intContent[arraysize];
    string* strContent = new string[arraysize];
    int* intContent = new int[arraysize];

    for (int i = 0; i < arraysize; i++) {
        intContent[i] = 0;
    }
    // Set index of number of new found words. 
    int newWords = 0;

    int numWords = 0, numMatch = 0;
    string word;
    while (inputFile >> word) {
        //cout << word << endl; 
        numWords++;
        //cout << word << ": " << endl; 
        // Count number of words not in common rank/words list. 
        bool flgWord = false;
        for ( int i = 1; i < numLines; i++ ) {
            //cout << dict[i] << ", "; 
            if(compareString(word, dict[i])) { // strings match
                numMatch++;
                flgWord = true;
            }
        }
        if (flgWord == false) {
            //Check to see if listed already in array. 
            bool flgWordInList = false;
            for ( int i = 1; i < newWords; i++ ) {
                if(compareString(word, strContent[i])) { // strings match
                    intContent[i]++; //Increment word count. 
                    flgWordInList = true;
                }
            }
            if (flgWordInList == false) {
                newWords++;
                // If the number of new words is greater than the array size, 
                // double the array size. 
                if (newWords >= arraysize) {
                    int newsize = 2*arraysize; 
                    //int* newArr = new int[new_size];
                    string* strArr = new string[newsize];
                    int* intArr = new int[newsize];
                    //std::copy(oldArr, oldArr + std::min(old_size, new_size), newArr);
                    std::copy(strContent, strContent + std::min(arraysize, newsize), strArr);
                    std::copy(intContent, intContent + std::min(arraysize, newsize), intArr);
                    //delete[] oldArr;
                    delete[] strContent;
                    delete[] intContent;
                    //oldArr = newArr;
                    strContent = strArr;
                    intContent = intArr;
                    arraysize = newsize; 
                }
                strContent[newWords] = word;
                intContent[newWords]++;
            }
        }
        //cout << endl; 
    }
    inputFile.close();

    for ( int i = 1; i < newWords; i++ ) {
        cout <<  strContent[i] << ": "<< intContent[i] << endl;
    }

    printf("There were %d words in the file.\n", numWords);
    printf("There were %d matches in the file.\n", numMatch);
    int numSpecialWords = numWords - numMatch;
    printf("There were %d special words in the file.\n", numSpecialWords);
    printf("There were %d new words in the file.\n", newWords);
    printf("The new array size is %d.\n", arraysize);

  //Output:
  //string question, response; 
  //bool flag;
  //while (true) {
    //flag = false;
    //cout << "What question do you have about C++?" << endl; 
    //cin >> question; 
    ////Look in string array. 
    //for (int i = 0;  i <= index; i++) {
      //if (strContent[i][0] == question) {
        //response = strContent[i][1];
        //cout << response << endl;
        //flag = true;
      //}
    //}

    //Look in dictionary. 
    //map<string, string>::iterator it = dict.find(question);
    //if(it != dict.end()) {
      //response = dict[question];
      //cout << response << endl;
      //flag = true;
    //}
    
    //Exit strategy. 
    //if (question == "quit" || question == "exit") {
      //cout << "Bye" << endl << endl;
      //break;
    //}
    //if (!flag) {
      //cout << "Sorry, I don't know. What else can we talk about?" << endl;
    //}
    //cout << endl;
  //} 
  
    return(0);
}



