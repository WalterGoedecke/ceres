#ifndef BOOK_H
#define BOOK_H
 
class Book {
	private:
		std::string author;
		std::string title;
	public:
		//Overloaded constructor.
    Book();
		Book(std::string Writer, std::string Cover);
		//Member functions.
		std::string getAuthor();
		std::string getTitle();
		void setAuthor(std::string Writer);
		void setTitle(std::string Cover);
		std::string toString();
};

#endif
