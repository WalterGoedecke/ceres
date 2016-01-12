#include <iostream>
#include <string>

using namespace std;

int main(int argc, char** argv)
{
    string arg_buffer = argv[1];
    //string arg_buffer = "name";
    cout << arg_buffer << std::endl;
    std::cout << "Hello New World!" << std::endl;
    return(0);
}

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
