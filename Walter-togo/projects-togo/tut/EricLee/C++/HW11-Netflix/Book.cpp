// Book class. 
// Keeps track of the books. 
#include <string>

#include "Book.h"

using namespace std;

//Overloaded constructor.
Book::Book() { 
	author = "unknown";
	title = "unknown";
}
Book::Book(string Writer, string Cover) {
	author = Writer;
	title = Cover;
}
//Member functions.
string Book::getAuthor() {
	return author;
}
string Book::getTitle() {
	return title;
}
void Book::setAuthor(string Writer) {
	author = Writer;
}
void Book::setTitle(string Cover) {
	title = Cover;
}
string Book::toString() {
	return title + " by " + author;
}
	
		
