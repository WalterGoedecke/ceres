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

int main (int argc, char* argv[])
{
	// -------------------------------------------------------------
	// 	Purpose: Create the library
	//	  read in books and users files 
	//		& store data into lists
	// -------------------------------------------------------------
	if (argc != 4)
	{
		cout << "Usage: " << argv[0] << " bookfilename ratingsfilename currentuserfilename" << endl;
		exit(1);
	}
	string bookListFilename(argv[1]);
	string userRatingsFilename(argv[2]);
	Library library(bookListFilename, userRatingsFilename);

	//print out the users for the library
	// USE FOR DEBUGGING PURPOSES
	//cout << "Library users: " << endl;
	//library.printUsers();
		
	// -------------------------------------------------------------
	//		Purpose: Print book info
	// -------------------------------------------------------------
	// USE FOR DEBUGGING PURPOSES
	//cout << "\nBook list: " << endl;
	//library.printBooks();

  // -------------------------------------------------------------
	// Part 3
  //      Purpose: Find the most similar user and print their recommendations
  // -------------------------------------------------------------
  //  Read in the "current user's" ratings from a file and
  //  find the user who is "most similar" to this current user
  //  and then list out the top 5 books liked by this similar user
  string currentUserFilename(argv[3]);
  //cout << "\nCurrent user: " << currentUserFilename << endl;
  User currentUser = library.getCurrentUser(currentUserFilename);
  cout << "Finding recommendations for user: " << currentUser.getId() << endl;

  User mostSimilarUser = library.getMostSimilarUser(currentUser);
  cout << "Most similar user: " << mostSimilarUser.getId() << endl;

  // -------------------------------------------------------------
	// Part 4
  // Now just print out books that the best matched user rated as 4 or higher, 
	//  that our current user hasn't read yet
  // -------------------------------------------------------------
  library.printRecommendations(mostSimilarUser, currentUser);
}
