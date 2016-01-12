/**
 * @author E.S.Boese
 * @version Fall 2014
 * Project #2
 */

#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include "User.h"
#include "Book.h"
#include "Library.h"
using namespace std;

Library::Library(string bookFilename, string userFilename) {
	readInBookList(bookFilename);
	readUserFile(userFilename);
}
void Library::readInBookList(string filename) {
	ifstream infile;
	infile.open(filename.c_str());
	string line;
	int count = 0;
	
	if (infile.is_open()) {
		cout << "Reading in book list from file: " << filename << endl;
		while ( getline (infile, line) ) {
			int comma_pos = line.find(",");
			string author = line.substr(0, comma_pos);
			string title = line.substr(comma_pos+1); 			
			Book book(author, title);
			bookList.push_back(book);
			count++;
		}
		cout << count << " books read in. Closing book list file." << endl;
		infile.close();
	}
}
void Library::readUserFile(string filename) {
	ifstream infile;
	infile.open(filename.c_str());
	
	if (infile.is_open()) {
		cout << "Reading in user list from file: " << filename << endl;
		int count = 0;
		while (infile) {
			string author, ratings;
			getline(infile, author);
			if (author != "") {
				getline(infile, ratings);
				User newuser(author, ratings);
				userList.push_back(newuser);
				count++;
			}
		}
		cout << count << " users read in. Closing user file." << endl;
		infile.close();
	}
}
void Library::printUsers() {
  //Avoid signed to unsigned int error. 
  int intUserListSize = userList.size();
	for (int i = 0; i < intUserListSize; i++) {
		cout << userList.at(i).toString() << endl;
	}
}
void Library::printBooks() {
  //Avoid signed to unsigned int error. 
  int intBookListSize = bookList.size();
	for (int i = 0; i < intBookListSize; i++) {
		Book book = bookList.at(i);
		cout << book.toString() << endl;
	}
}
void Library::printAverageBookRatings() {
  //Create array to first hold the sums of ratings for each book, 
  // then calculate the average: avg = sum/divisor.
  int indBooks = bookList.size();
  int indUsers = userList.size();  
  double sum[indBooks], divisor[indBooks];  
  for (int i = 0; i < indBooks; i++) {
    sum[i] = 0.0;
    divisor[i] = 0.0;    
  }

  //Set average decimal precision. 
  cout << fixed << setprecision(2);
  cout << showpoint;

  //Loop thru the peoples' ratings, and accumulate score to sum[] array. 
  for (int i = 0; i < indUsers; i++) {
    User userSelection = userList.at(i);

    int indBook = 0;
    while (indBook < indBooks) {
      float ratingSelection = userSelection.getRatingAt(indBook);      
      //Accumulate ratings within sum array. 
      sum[indBook] = sum[indBook] + ratingSelection;
      if (ratingSelection != 0.0) {
        divisor[indBook]++; //Increment count of ratings if non-zero. 
      }
      indBook++;
    }
  }

  //Loop thru the books for the ratings. 
  float avg; 
  for (int i = 0; i < indBooks; i++) {
    if (divisor[i] == 0) {
      avg = 0;
    }
    else {
      avg = sum[i]/divisor[i];
    }
    Book bookSelection = bookList.at(i);
    string titleSelection = bookSelection.getTitle();      
    string authorSelection = bookSelection.getAuthor();      

    cout << avg << " " << titleSelection << " by " << authorSelection << endl;
  }
  cout << endl;
  
}
