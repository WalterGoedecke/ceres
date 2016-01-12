#include <iostream>
#include <string>
#include <sstream>

#include <stdlib.h>     /* atoi */

using namespace std;

class TimeCalc
{
   private:
    int hours, minutes;
 
   public:
 
      //Calculate days, if any:
      int calcDays(int daySeconds)
      {
        return daySeconds/86400;
      }
 
      //Calculate hours:
      int calcHours(int daySeconds)
      {
        return daySeconds/3600;
      }
 
      //Calculate minutes:
      int calcMinutes(int daySeconds)
      {
        return (daySeconds % 3600)/60;
      }
 
      //Calculate seconds:
      int calcSeconds(int daySeconds)
      {
        hours = TimeCalc::calcHours(daySeconds);
        minutes = TimeCalc::calcMinutes(daySeconds);
        return daySeconds - 3600*hours - 60*minutes;
      }
};
 
int main(int argc, char** argv)
{
    int intDaySeconds, intDays, intHours, intMinutes, intSeconds;

    string strDaySeconds = argv[1];

    TimeCalc obj;

    //String to integer:
    istringstream strStream(strDaySeconds);
    strStream >> intDaySeconds;

    //Calculate days, if any:
    //intDays = intDaySeconds/86400;
    intDays = obj.calcDays(intDaySeconds);
    if (intDays > 0)
    {
      intDaySeconds = (intDaySeconds % 86400);
    }

    //Calculate hours, minutes, & seconds:
    //intHours = intDaySeconds/3600;
    intHours = obj.calcHours(intDaySeconds);
    //intMinutes = (intDaySeconds % 3600)/60;
    intMinutes = obj.calcMinutes(intDaySeconds);
    //intSeconds = intDaySeconds - 3600*intHours - 60*intMinutes;
    intSeconds = obj.calcSeconds(intDaySeconds);

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
