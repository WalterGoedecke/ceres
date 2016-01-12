/**  Test Part 1 of the project
 * @author E.S.Boese
 * @version Fall 2014
 */

#include <iostream>
#include "Book.h"
#include "User.h"
using namespace std;

int main()
{
	// test Book class
	Book b1("E.S.Boese", "Java Applets");
	cout << "Book 1: " << b1.toString() << endl;

	// test User class
	User u1("Miley", "1 0 -3 5 -5 1 2");
	cout << u1.toString() << endl;
	return 0;
}
