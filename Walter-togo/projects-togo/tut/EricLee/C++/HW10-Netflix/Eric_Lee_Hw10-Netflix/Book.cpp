//Eric Lee
// Worked with Kenny 
// book class
// keeps track of the books
#include <iostream>
#include <string>

using namespace std;

class Book
{
	private:
		string author;
		string title;
	public:
		Book();
		Book(string Writer, string Cover);
		string getAuthor();
		string getTitle();
		void setAuthor(string Writer);
		void setTitle(string Cover);
		string toString();
} ;
//function prototypes

Book::Book() // constructor takes book as a 
{
	author = "unknown";
	title = "unknown";
}


Book::Book(string Writer, string Cover)
{
	author = Writer;
	title = Cover;
}

string Book::getAuthor()
{
	return author;
}

string Book::getTitle()
{
	return title;
}


void Book::setAuthor(string Writer)
{
	author = Writer;
}
void Book::setTitle(string Cover)
{
	title = Cover;
}

string Book::toString()
{
	return title + " by " + author;
}
	
		
