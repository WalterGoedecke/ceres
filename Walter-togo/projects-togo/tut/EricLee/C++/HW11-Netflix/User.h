#ifndef USER_H
#define USER_H

#include <vector>
 
class User {
	private: //cannot change in main
		std::string id;
		std::string ratings;
	public: //functions, can be changed
		//Overloaded constructor.
		User ();
		User (std::string id, std::string ratings);
    //User (string a, vector<int> b);
		//Member functions.
		void setId (std::string str);
		std::string getId();
		int getRatingAt(int index);
		void addRating (int rating);
		int getNumRatings();
		std::string toString();
		void printRatings();
};

#endif
