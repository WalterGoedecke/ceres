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

//Constructors. 
Library::Library() {}
Library::Library(string bookFilename, string userFilename) {
	readInBookList(bookFilename);
	readUserFile(userFilename);
}
//Member functions.
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

			// TODO: create new Book object
			Book book(author, title);
			
			// TODO: add Book object to vector
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
				
				// TODO: Create new User object
				User newuser(author, ratings);
				
				// TODO: Add new User object to vector
				userList.push_back(newuser);
				
				count++;
			}
		}
		cout << count << " users read in. Closing user file." << endl;
		infile.close();
	}
}
void Library::printUsers() {
	for (int i=0; i<userList.size(); i++) {
		cout << userList.at(i).toString() << endl;
	}
}
void Library::printBooks() {
	for (int i=0; i<bookList.size(); i++) {
		Book book = bookList.at(i);
		cout << book.toString() << endl;
	}
}
