#include <iostream>
#include <string>
#include <sstream>

#include <stdlib.h>     /* atoi */

using namespace std;

int main(int argc, char** argv)
{
    int intDaySeconds, intDays, intHours, intMinutes, intSeconds;

    string strDaySeconds = argv[1];

    //String to integer:
    istringstream strStream(strDaySeconds);
    strStream >> intDaySeconds;

    //Calculate days, if any:
    intDays = intDaySeconds/86400;
    if (intDays > 0)
    {
      intDaySeconds = (intDaySeconds % 86400);
    }

    //Calculate hours, minutes, & seconds:
    intHours = intDaySeconds/3600;
    intMinutes = (intDaySeconds % 3600)/60;
    intSeconds = intDaySeconds - 3600*intHours - 60*intMinutes;

    //Integer to string:
    if (intDays > 0)
    {
      cout << "The time is " << intDays << " days, " << intHours << " hours, " 
      << intMinutes << " minutes, and " << intSeconds << " seconds" << endl;
    }
    else
    {
      cout << "The time is " << intHours << " hours, " << intMinutes << 
      " minutes, and " << intSeconds << " seconds" << endl;
    }

    return(0);
}

//The time is 19 hours, 26 minutes, and 40 seconds
/*
//Integer to string:
string command ;
int value ;
cin >> command >> value;

string s = "20";
std::int a = to_string(s);

int main()
{
    int i(42);
    std::ostringstream oss;
    oss << i;
    std::string s(oss.str());
    std::cout << s << '\n'; // prints 42
    return 0;
}

//String to integer:
string test="AAA 123 SSSSS 3.141592654";
istringstream totalSString( test );
string string1, string2;
int integer1;
double PI;
totalSString >> string1 >> integer1 >> string2 >> PI;
 
td::string s = std::to_string(42);
*/
/*
int main(int argc, char** argv)
{
  string arg_buffer;
  if(argc==1)
  {
    cout << "No arguments given!";
  }
  else
  {
    for(int i=1; i<argc; ++i)
    {
      arg_buffer = argv[i];
      cout << arg_buffer << endl;
    }
  }
}
*/
