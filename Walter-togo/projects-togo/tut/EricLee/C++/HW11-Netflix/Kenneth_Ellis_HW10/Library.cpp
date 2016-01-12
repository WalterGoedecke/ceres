/*
 * Kenny Ellis
 * 11/17/14
 * HW 10
 */

#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <cmath>

#include "Book.cpp"	 // This is NOT how it should be done but for now we will do it this way
#include "User.cpp"	 // This is NOT how it should be done but for now we will do it this way


using namespace std;

class Library 
{
  public:
	Library(string book_list_file, string user_list_file); 
	void readInBookList(string filename);  
	void readUserFile(string filename); 
	void printUsers(); 
	void printAverageBookRatings(); 
	
  private: 
	vector<Book> bookList; 
	vector<User> userList;
};


Library::Library(string bookFilename, string userFilename)
{
	readInBookList(bookFilename);
	readUserFile(userFilename);
}

void Library::printUsers()
{
	for (unsigned int i=0; i<userList.size(); i++)
	{
		cout << userList.at(i).toString() << endl;
	}
}


void Library::readInBookList(string filename)
{
	ifstream infile;
	infile.open(filename.c_str());
	string line;
	int count = 0;
	
	if (infile.is_open())
	{
		cout << "Reading in book list from file: " << filename << endl;
		while ( getline (infile, line) )
		{
			int comma_pos = line.find(",");
					
			string author = line.substr(0, comma_pos);
			string title = line.substr(comma_pos+1); 			

			// TODO: create new Book object
				Book mybook= Book(author, title);
			// TODO: add Book object to vector
				bookList.push_back(mybook);
			count++;
		}
		cout << count << " books read in. Closing book list file." << endl;
		infile.close();
	}
}

void Library::readUserFile(string filename)
{
	ifstream infile;
	infile.open(filename.c_str());
	
	if (infile.is_open())
	{
		cout << "Reading in user list from file: " << filename << endl;
		int count = 0;
		while (infile)
		{
			string author, ratings;
			getline(infile, author);
			
			if (author != "")
			{
				getline(infile, ratings);
				
				// TODO: Create new User object
				cout << "creating user" << endl;
					User myuserlist= User(author, ratings);
				// TODO: Add new User object to vector
				cout << "adding to vector " << endl;
					userList.push_back(myuserlist);
				count++;
			}
		}
		cout << count << " users read in. Closing user file." << endl;
		infile.close();
	}
}

void Library::printAverageBookRatings()
{
	cout << fixed << setprecision(2);
	cout << showpoint;
	// TODO:
	
	
	for ( unsigned int i = 0; i < bookList.size(); i++)
	{
		double count = 0;
		double average = 0;
		double sum = 0;
		
		for( unsigned int u = 0; u < userList.size(); u++)
		{
			int sumofrating = userList.at(u).getRatingAt(i);
			
			if (sumofrating != 0)
			{
				sum += sumofrating;
				count ++;
				
			}
			
		}
			if ( count != 0)
			{
					average  = sum / count;
			}
			cout << average << " " << bookList[i].toString() << endl;
	}
	// Loop through the book list vector
	//	 Loop through user list
	//		get the rating from each user for this book
	//		if the rating isn't zero, add it to the sum and increment a count of ratings
	//	 Print the average for this book




}
