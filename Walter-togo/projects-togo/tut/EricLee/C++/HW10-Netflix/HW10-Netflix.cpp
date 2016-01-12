// This links reader ratings to books read. 
// Nov. 16, 2014.
  
// Input arguments are text files, e.g.: 
// books.txt & ratings.txt

#include <iostream>
//#include <string>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <stdlib.h>     /* atoi */
//#include <map>
#include <vector>

//#include "Book.cpp"	 // This is NOT how it should be done but for now we will do it this way
#include "Book.h"
#include "User.h"

using namespace std;

/* * * * * * * * * * * * */
class Library {
  private: 
    vector<Book> bookList; 
    vector<User> userList;

    vector<string> authorList;
    vector<string> titleList;
    vector<string> idList;
    vector<string> ratingsList;

  public:
    //Constructor.
    Library() {}
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
          Book book(author, title);
          
          // TODO: add Book object to vector
          bookList.push_back(book);
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
          User u1;
          u1.setId(word1);

          count++;
          
          while (infile) {
            string id, ratings;
            getline(infile, line);
            
            if (line != "") {
              getline(infile, ratings);
              
              // TODO: Create new User object
              //User newuser(author, ratings);
              User newuser(id, ratings);
              // TODO: Add new User object to vector
              userList.push_back(newuser);

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
        b1.setAuthor(authorList[i]);
        b1.setTitle(titleList[i]);
        cout << fixed;
        cout << setprecision(2);

        cout << avg << " " << b1.toString() << endl;
        //cout << b1.getTitle() << " " << b1.getAuthor() << endl;
      }
      cout << endl;
      
    }
    void printBooks();
  };
void Library::printUsers() {
	for (int i = 0; i < userList.size(); i++) {
		cout << userList.at(i).toString() << endl;
	}
}
void Library::printBooks() {
	for (int i = 0; i < bookList.size(); i++) {
		Book book = bookList.at(i);
		cout << book.toString() << endl;
	}
}  

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
  cout << b1.getTitle() << " " << b1.getAuthor() << endl;
  User u1; 
  
  //-----------------------
  // Open book file and reads it, e.g., book.txt. 
  //-----------------------
  ifstream inputFile;
  if (bookfile != NULL) {
    inputFile.open(bookfile);
  }
  else {
    inputFile.open("books.txt");
  }

  //cout << endl << "Reading in book list from file: " << bookfile << endl;
  //Create a book index. 
  int indBooks = 0;

  string line, strAuthor, strTitle, word1, word2;
  while (!inputFile.eof()) {
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
  if (ratingfile != NULL) {
    inputFile.open(ratingfile);
  }
  else {
    inputFile.open("ratings.txt");
  }

  //Read lines from ratings book file. 
  //cout << "Reading in user list from file: " << ratingfile << endl;
  //Create a ratings index. 
  int indRatings = 0;
  while (!inputFile.eof()) {
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
      //u1.setId(word1);
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

  //This prints out the results. 
  lib1.printAverageBookRatings();

  return(0);
}



