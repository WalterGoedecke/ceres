// Userfile. 
#include <iostream>
//#include <string>
//#include <vector>
//#include <sstream>

//#include <stdlib.h>
//#include <stdio.h> /*stoi function*/

#include "User.h"

using namespace std;

//Overloaded constructor.
User::User() {
	id = "Unknown";
	//id = "User [user_id=Unknown]";
	//ratings = "unknown";
}
User::User(string userid, string userRatings) {
	id = userid;
	while(userRatings.find(" ") < userRatings.length())
	{
		int index = userRatings.find(" ");
		int x = stoi(userRatings.substr(0, index));
		ratings.push_back(x);
		userRatings = userRatings.substr(index+1);
	}
	if ( userRatings != "" ) {
    int userFinal = stoi(userRatings);
    ratings.push_back(userFinal);
  }
}
//Member functions.
void User::setId (string str) {
  id = str;
}
string User::getId() {
	return "User[user_id = " + id + "]";
}

int User::getRatingAt(int index)
{
	return ratings.at(index);
  //return vecRatings[index];
}

void User::addRating(int x) {
	ratings.push_back(x);
}
int User::getNumRatings() {
	return ratings.size();
}
string User::toString() {
	return "User [user_id=" + id + "]";
}
void User::printRatings() {
	for (unsigned int i = 0; i < ratings.size(); i++) {
		cout << ratings.at(i) << " " << endl;
	}
}


