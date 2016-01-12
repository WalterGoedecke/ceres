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

int main ()
{
	// -------------------------------------------------------------
	// 	Purpose: Create the library
	//			 read in books and users files 
	//			 & store data into lists
	// -------------------------------------------------------------
	string bookListFilename = "books.txt";
	string userRatingsFilename = "ratings.txt";
	Library library(bookListFilename, userRatingsFilename);

	//print out the users for the library
	// USE FOR DEBUGGING PURPOSES
	cout << "Library users: " << endl;
	library.printUsers();
		
		
	// -------------------------------------------------------------
	//		Purpose: Print book info
	// -------------------------------------------------------------
	cout << "\n\nBook list: " << endl;
	library.printBooks();
}
