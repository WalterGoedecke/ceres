//Hw6Problem1
// Footbal passer rating program.

#include <iostream>
#include <string>
#include <sstream>

using namespace std;
//using std::setprecision;

int main()
{
    double intPassAttempts, intPassCompletions, intPassYards, intTouchdowns, intInterceptions;
    double C, Y, T, I; 
    double completionRatio, yardsRatio, touchdownRatio, interceptionRatio;
    double PasserRating;
      
    //User input.
    cout << "Enter # of pass attempts" << endl;
    cin >> intPassAttempts; 
    cout << "Enter # of pass attempts" << endl;
    cin >> intPassCompletions; 
    cout << "Enter # of pass attempts" << endl;
    cin >> intPassYards; 
    cout << "Enter46 # of pass attempts" << endl;
    cin >> intTouchdowns;
    cout << "Enter # of pass attempts" << endl;
    cin >> intInterceptions;
    
    //Ratio calculations:
    completionRatio = 1.0*intPassCompletions/intPassAttempts;
    yardsRatio = 1.0*intPassYards/intPassAttempts;
    touchdownRatio = 1.0*intTouchdowns/intPassAttempts;
    interceptionRatio = 1.0*intInterceptions/intPassAttempts;
    
    //Calculations:
    /*
    C = (completions per attempt – 0.30)*5;
    Y = (yards per attempt – 3)*0.25	
    T = touchdowns per attempt * 20	
    I = 2.375 – (Intercepts per attempt * 25)	
    PasserRating = (C+Y+T+I)/6*100 */
    C = (completionRatio - 0.30)*5;
    Y = (yardsRatio - 3)*0.25;
    T = touchdownRatio*20;
    I = 2.375 - interceptionRatio*25;
    PasserRating = (C + Y + T + I)/6*100;
    /*
    cout << "Pass attempts: " << intPassAttempts << endl;
    cout << "Pass completions: " << intPassCompletions << endl;
    cout << "Passing yards: " << intPassYards << endl;
    cout << "Touchdowns: " << intTouchdowns << endl;
    cout << "Interceptions: " << intInterceptions << endl;
    */ 

    // set to 1 or 3 digits after the decimal
    cout.precision(3);
    cout << showpoint;

    cout << "The passer rating is " << PasserRating << endl;
  
    return(0);
}
