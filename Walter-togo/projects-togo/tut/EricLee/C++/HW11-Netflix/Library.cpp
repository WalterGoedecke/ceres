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
			string id, ratings;
			getline(infile, id);
			if (id != "") {
				getline(infile, ratings);
				User newuser(id, ratings);
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
User Library::getCurrentUser(string currentUserFilename) {
  int sizeVec = userList.size(); 
  User selectUser;
  for(int i = 0; i < sizeVec; i++) {
    selectUser = userList.at(i);
    if (selectUser.getId() == currentUserFilename) {
      break;
    }
  }
  return selectUser;
}
User Library::getMostSimilarUser(User currentUser) {
  int userListSize = userList.size(), k; 
  double maxDotProduct = 0;
  User selectUser, mostSimilarUser;
  for(int i = 0; i < userListSize; i++) {
    selectUser = userList.at(i);
    if (currentUser.getId() == selectUser.getId()) { //Mark index of currentUser. 
      k = i;
    }
    //Compare user litterary tastes. 
    double dotProduct = 0;
    for (int j = 0; j < selectUser.getNumRatings(); j++) {
      dotProduct = dotProduct + currentUser.getRatingAt(j)*selectUser.getRatingAt(j);
    }
    if (maxDotProduct < dotProduct && k != i) {
      maxDotProduct = dotProduct;
      mostSimilarUser = selectUser;
    }
  }
  return mostSimilarUser;
}
void Library::printRecommendations(User mostSimilarUser, User currentUser) {
  //Compare user litterary tastes. 
  Book selectBook;
  cout << "\nWe recommend for you the following books:" << endl;
  for (int j = 0; j < currentUser.getNumRatings(); j++) {
    //If current user did not read the book. 
    if (currentUser.getRatingAt(j) == 0) {
      //If the most similar user rated the book higher than 4. 
      if (mostSimilarUser.getRatingAt(j) >= 4) {
        selectBook = bookList.at(j);
        cout << selectBook.toString() << endl;
      }
    }
  }
  cout << endl;
}


