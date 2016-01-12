//Hw6Problem3
// This program calculates the US population with an initial value 
// and periods (1/rate) of change. 

#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main()
{
    //Initial people.
    int intInitPop = 307357870;
    //Seconds.
    int intBirthPeriod = 7;
    int intDeathPeriod = 13; 
    int intImmigrantPeriod = 35;
    
    //Calculate number of seconds in year. 
    int intJulianSeconds = 365*86400;

    //Calculate number of periods in year. 
    // Since cast as integers, numbers will be rounded down. 
    int intNumBirthPeriods = intJulianSeconds/intBirthPeriod;
    int intNumDeathPeriods = intJulianSeconds/intDeathPeriod;
    int intNumImmigrantPeriods = intJulianSeconds/intImmigrantPeriod;

    //Calculate year's end total.
    int intTotal = intInitPop + intNumBirthPeriods - intNumDeathPeriods 
      + intNumImmigrantPeriods;

    //Output results.
    //The population will be 310338194 people
    cout << "The population will be " << intTotal << " people" << endl;

    return(0);
}

