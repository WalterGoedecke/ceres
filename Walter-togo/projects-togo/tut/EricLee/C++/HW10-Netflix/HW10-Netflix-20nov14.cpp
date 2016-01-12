// This links reader ratings to books read. 
// Nov. 16, 2014.
  
// Input arguments are text files, e.g.: 
// books.txt & ratings.txt

#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <stdlib.h>     /* atoi */
#include <map>
#include <vector>

using namespace std;

//Book class.
class Book {
  //private:
    string author, title;

  public:
    // Overloaded constructor 
    Book ();
    Book (string, string);

    // Member Functions
    void set_author (string);
    void set_title (string);
    string get_author ();
    string get_title ();
    string toString() {
      string phrase = title + " by " + author;
      return phrase;
    }
};
// Constructor 
Book::Book () {
  author = "Unknown";
  title = "Unknown";
}
Book::Book (string a, string b) {
  author = a;
  title = b;
}
void Book::set_author (string str) {
  author = str;
}
void Book::set_title (string str) {
  title = str;
}
string Book::get_author () {
  return author;
}
string Book::get_title () {
  return title;
}

//User class.
//- id : string
//- ratings : vector<int>
//+ User( )
//+ User( string userid, string ratings )
//+ getId( ) : string
//+ getRatingAt( int index) : int
//+ addRating( int rating ) : void
//+ getNumRatings( ) : int
//+ toString( ) : String
//+ printRatings( ) : void
class User {
  //private:
    string id;
    vector<int> ratings;
  public:
    // Overloaded constructor 
    User () {
      id = "Default Constructor";
      //ratings = "User [user_id=Unknown]";
    }
    User (string a, vector<int> b) {
      id = a;
      ratings = b;
    }
    // Member Functions
    void set_id (string str) {
      id = str;
    }
    string get_id () {
      return id;
    }
    int getRatingAt( int index) {
      return ratings[index];
    }
    string toString() {
      string phrase = id;
      return phrase;
    }
};

class Library {
  private: 
    //vector<Book> bookList; 
    //vector<User> userList;
    //vector<string> bookList; 
    vector<string> authorList;
    vector<string> titleList;
    vector<string> idList;
    vector<string> ratingsList;

    vector<string> userList;

  public:
    //Constructor.
    Library() {
    }
    Library(string book_list_file, string user_list_file) {
      readInBookList(book_list_file);
      readUserFile(user_list_file);
    }
    //Member functions.
    void readInBookList(string filename) {
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
          //Book mybook(author, title);
          
          // TODO: add Book object to vector
          // Create a shel of books to get all the books
          //bookList.push_back(mybook);
          authorList.push_back(author);
          titleList.push_back(title);
          
          count++;
        }
        cout << count << " books read in. Closing book list file." << endl;
        infile.close();
      }
    }
    void readUserFile(string filename) {
      string line, word1, word2;
      
      ifstream infile;
      infile.open(filename.c_str());
      
      //getline(inputFile, line);
      //if (line != "") {
        //word1 = line;
      //}
      //getline(inputFile, line);
      //if (line != "") {
        //word2 = line;

        ////Add to vectors. 
        //vecRatingsName.push_back(word1);
        //vecRatingsNumbers.push_back(word2);
        //u1.set_id(word1);
        ////cout << vecRatingsName[indRatings] << ": " << endl << vecRatingsNumbers[indRatings] << endl;

        //indRatings++;
      //}

      if (infile.is_open()) {
        cout << "Reading in user list from file: " << filename << endl;
        int count = 0;

        getline(infile, line);
        if (line != "") {
          word1 = line;
        }
        getline(infile, line);
        if (line != "") {
          word2 = line;

          //Add to vectors. 
          idList.push_back(word1);
          ratingsList.push_back(word2);
          //u1.set_id(word1);

          count++;
          
          while (infile) {
            string id, ratings;
            getline(infile, line);
            
            if (line != "") {
              getline(infile, ratings);
              
              // TODO: Create new User object
              //User myuserlist(author, ratings);
              // TODO: Add new User object to vector
              //userList.push_back(myuserlist);

              idList.push_back(id);
              ratingsList.push_back(ratings);

              count++;
            }
          }
        }
        cout << count << " users read in. Closing user file." << endl;
        infile.close();
      }

      
    }
    void printUsers(); 
    void printAverageBookRatings() {

      //Create array to first hold the sums of ratings for each book, 
      // then calculate the average: avg = sum/divisor.
      int indBooks = authorList.size();
      int indRatings = ratingsList.size();
      double sum[indBooks], divisor[indBooks];  
      for (int i = 0; i < indBooks; i++) {
        sum[i] = 0.0;
        divisor[i] = 0.0;    
      }

      //Set average decimal precision. 
      cout << fixed << setprecision(2);
      cout << showpoint;

      //Loop thru the peoples' ratings, and accumulate score to 
      // sum[] array. 
      //string strWord;
      string strWord;
      float fltWord = 0;
      for (int i = 0; i < indRatings; i++) {
        //cout << vecRatingsName[i] << endl;
        //cout << vecRatingsNumbers[i] << endl;
        stringstream stream(ratingsList[i]);
        int indBook = 0;
        while (stream >> strWord) {
          if (indBook == indBooks) {
            break;
          }
          //Convert string to float. 
          fltWord = atof(strWord.c_str());
          //Accumulate ratings within sum array. 
          sum[indBook] = sum[indBook] + fltWord;
          if (fltWord != 0.0) {
            divisor[indBook]++; //Increment count of ratings if non-zero. 
          }
          //cout << avg << " " << b1.toString() << endl;
          //cout << avg << " " << self.toString() << endl;
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
        //cout << sum[i] << " " << titleList[i] << " by " << authorList[i] << endl;
        Book b1;
        b1.set_author(authorList[i]);
        b1.set_title(titleList[i]);
        cout << fixed;
        cout << setprecision(2);

        cout << avg << " " << b1.toString() << endl;
        //cout << b1.get_title() << " " << b1.get_author() << endl;
      }
      cout << endl;
      
    }
  };
      // TODO:
      //double count = 0;
      //double average = 0;
      //for (unsigned int i = 0; i < bookList.size(); i++) {
        //for(unsigned int  u = 0; u < userList.size(); u++) {
          //count += userList[u];
          //average = count / userList.size();
        //}
        //cout << average << " " << bookList[i].toString() << endl;
      //}
    //End Public.


//Library::Library(string bookFilename, string userFilename)
//{
	//readInBookList(bookFilename);
	//readUserFile(userFilename);
//}
//void Library::printUsers()
//{
	//for (unsigned int i=0; i<userList.size(); i++)
	//{
		//cout << userList.at(i).toString() << endl;
	//}
//}
//void Library::readInBookList(string filename)
//{
	//ifstream infile;
	//infile.open(filename.c_str());
	//string line;
	//int count = 0;
	
	//if (infile.is_open())
	//{
		//cout << "Reading in book list from file: " << filename << endl;
		//while ( getline (infile, line) )
		//{
			//int comma_pos = line.find(",");
					
			//string author = line.substr(0, comma_pos);
			//string title = line.substr(comma_pos+1); 			

			//// TODO: create new Book object
			//Book mybook(author, title);
			
			//// TODO: add Book object to vector
			//// Create a shel of books to get all the books
			//bookList.push_back(mybook);
			
			//count++;
		//}
		//cout << count << " books read in. Closing book list file." << endl;
		//infile.close();
	//}
//}
//void Library::readUserFile(string filename)
//{
	//ifstream infile;
	//infile.open(filename.c_str());
	
	//if (infile.is_open())
	//{
		//cout << "Reading in user list from file: " << filename << endl;
		//int count = 0;
		//while (infile)
		//{
			//string author, ratings;
			//getline(infile, author);
			
			//if (author != "")
			//{
				//getline(infile, ratings);
				
				//// TODO: Create new User object
				//User myuserlist(author, ratings);
				//// TODO: Add new User object to vector
				//userList.push_back(myuserlist);
				//count++;
			//}
		//}
		//cout << count << " users read in. Closing user file." << endl;
		//infile.close();
	//}
//}
//void Library::printAverageBookRatings()
//{
	//cout << fixed << setprecision(2);
	//cout << showpoint;
	//// TODO:
	//double count = 0;
	//double average = 0;
	//for (unsigned int i = 0; i < bookList.size(); i++)
	//{
		//for(unsigned int  u = 0; u < userList.size(); u++)
		//{
		//count += userList[u];
		//average = count / userList.size();
		 
		//}
		//cout << average << " " << bookList[i].toString() << endl;
		
	//}  

int main(int argc, char** argv) {
  //-----------------------
  // Input arguments and create vectors.
  //-----------------------
  //Get input arguments.
  char *bookfile = argv[1];
  char *ratingfile = argv[2];
  //- - - - - - - - - - - -
  //Initialize vectors.
  vector<string> vecBooksAuthor;
  vector<string> vecBooksTitle;
  vector<string> vecRatingsName;
  vector<string> vecRatingsNumbers;
      
  //-----------------------
  // Instantiate obects with classes.
  //-----------------------
  Book b1;
  //Book b1("yes", "no");
  cout << b1.get_title() << " " << b1.get_author() << endl;
  User u1; 
  
  //-----------------------
  // Open book file and reads it, e.g., book.txt. 
  //-----------------------
  ifstream inputFile;
  if (bookfile != NULL)
  {
    inputFile.open(bookfile);
  }
  else
  {
    inputFile.open("books.txt");
  }

  //cout << endl << "Reading in book list from file: " << bookfile << endl;
  //Create a book index. 
  int indBooks = 0;

  string line, strAuthor, strTitle, word1, word2;
  while (!inputFile.eof())
  {
    //Fill string array. 
    getline(inputFile, line);
    if (line != "") {
      stringstream stream(line);
      getline(stream, strAuthor, ',');
      getline(stream, strTitle, ',');

      //Add to vectors. 
      vecBooksAuthor.push_back(strAuthor);
      vecBooksTitle.push_back(strTitle);
      //cout << vecBooksTitle[indBooks] << " by " << vecBooksAuthor[indBooks] << endl;

      indBooks++;
    }
  }
  inputFile.close();
  //printf("There were %d lines in the file.\n", i);
  //cout << indBooks << " books read in. Closing book list file." << endl;
  
  //cout << "Mark 1" << endl;
  Library lib1; 
  lib1.readInBookList(bookfile);
  
  //-----------------------

  //-----------------------
  // Open ratings list and read it, e.g., ratings.txt.
  //-----------------------
  if (ratingfile != NULL)
  {
    inputFile.open(ratingfile);
  }
  else
  {
    inputFile.open("ratings.txt");
  }

  //Read lines from ratings book file. 
  //cout << "Reading in user list from file: " << ratingfile << endl;
  //Create a ratings index. 
  int indRatings = 0;
  while (!inputFile.eof())
  {
    getline(inputFile, line);
    if (line != "") {
      word1 = line;
    }
    getline(inputFile, line);
    if (line != "") {
      word2 = line;

      //Add to vectors. 
      vecRatingsName.push_back(word1);
      vecRatingsNumbers.push_back(word2);
      u1.set_id(word1);
      //cout << vecRatingsName[indRatings] << ": " << endl << vecRatingsNumbers[indRatings] << endl;

      indRatings++;
    }
  }
  inputFile.close();
  //cout << indRatings << " users read in. Closing user file." << endl;

  lib1.readUserFile(ratingfile);
  cout << endl;
  
  //-----------------------

  //-----------------------
  // Manupulate data stored in vectors.
  //-----------------------

  ////Create array to first hold the sums of ratings for each book, 
  //// then calculate the average: avg = sum/divisor.
  //double sum[indBooks], divisor[indBooks];  
  //for (int i = 0; i < indBooks; i++) {
    //sum[i] = 0.0;
    //divisor[i] = 0.0;    
  //}
    
  ////Loop thru the peoples' ratings, and accumulate score to 
  //// sum[] array. 
  ////string strWord;
  //string strWord;
  //float fltWord = 0;
  //for (int i = 0; i < indRatings; i++) {
    ////cout << vecRatingsName[i] << endl;
    ////cout << vecRatingsNumbers[i] << endl;
    //stringstream stream(vecRatingsNumbers[i]);
    //int indBook = 0;
    //while (stream >> strWord) {
      //if (indBook == indBooks) {
        //break;
      //}
      ////Convert string to float. 
      //fltWord = atof(strWord.c_str());
      ////Accumulate ratings within sum array. 
      //sum[indBook] = sum[indBook] + fltWord;
      //if (fltWord != 0.0) {
        //divisor[indBook]++; //Increment count of ratings if non-zero. 
      //}
      //indBook++;
    //}
  //}
  //cout << endl;

  ////Loop thru the books for the ratings. 
  //float avg; 
  //for (int i = 0; i < indBooks; i++) {
    //if (divisor[i] == 0) {
      //avg = 0;
    //}
    //else {
      //avg = sum[i]/divisor[i];
    //}
    ////cout << sum[i] << " " << vecBooksTitle[i] << " by " << vecBooksAuthor[i] << endl;
    //b1.set_author(vecBooksAuthor[i]);
    //b1.set_title(vecBooksTitle[i]);
    //cout << fixed;
    //cout << setprecision(2);
    ////cout << avg << " " << b1.toString() << endl;
    ////cout << b1.get_title() << " " << b1.get_author() << endl;
  //}
  //cout << endl;

  //This prints out the results. 
  lib1.printAverageBookRatings();

  return(0);
}



