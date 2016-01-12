#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstdlib>
#include <sstream>
#include <string>
#include <vector>

using namespace std;
struct book
{
	string numWord;
	int numCount;
};

bool CommonWords(string tempWord)
{
	bool found = false;
	string txtArray[50]= {"the", "you", "one", "be", "do", "all", "to", "at", "would", "of", 
	"this", "there", "and", "but", "their", "a", "his", "what", "in", "by", "so", "that", 
	"from", "up", "have", "they", "out", "i", "we", "if", "it", "say", "about", "for", "her", 
	"who", "not", "she", "get", "on", "or", "which", "with", "an", "go", "he", "will", "me", "as", 
	"my"};
	
	for(int i=0; i<50; i++)
	{
		if(tempWord == txtArray[i])
		{
			found = true;
			break;
		}
		
	}
	
	return found;
}

/*book *DoubleArray(book array[], int size)
{
	cout << 2*size << endl;
	
	book *Array2 = new book [2*size];
	for (int i=0; i<size; i++)
	{
		Array2[i] = array[i];
		Array2[i+size] = array[i];//*2;
	}
	delete[] array;
	return Array2;

}*/

void mostFrequent(book Array[], int length)
{
	for(int i=0; i < length; i++)
	{
		for(int k=0; k <i; k++)
		{
			if(Array[k].numCount <= Array[k+1].numCount)
			{
				int counts = Array[k].numCount;
				string myArray = Array[k].numWord;
				Array[k].numCount = Array[k+1].numCount;
				Array[k].numWord = Array[k+1].numWord;
				Array[k+1].numCount = counts;
				Array[k+1].numWord = myArray;
			}
		}
	}
}


int main(int argc, char*argv[])
{
	string word;
	ifstream infile;
	infile.open(argv[1]);
	int n = atoi(argv[2]);
	book *Array = new book[100] ;
	int length = 0;
	int currentArraySize = 100;
	int doublecount = 0;
	int totalcount =0;
	//int count = 0;
	//int num = 0;
	//book DoublingArray[];
	
	while(infile >> word)
	{
		//totalcount++;
		bool CommonWord = CommonWords(word);
		book currentWord;
		currentWord.numWord = word;
		currentWord.numCount = 0;
		bool matched = false;
		if(length == currentArraySize)
		{
			//cout << "commonWord" << endl;
			//book *Array= DoubleArray(Array, currentArraySize);
			//doubling array
			//cout << currentArraySize*2<< endl;
			//cout << doublecount<<endl;
	
			book *Array2 = new book [2*currentArraySize];
			for (int i=0; i<currentArraySize; i++)
			{
				//totalcount++;
				Array2[i] = Array[i];
				//Array2[i+size] = array[i];//*2;
			}
			delete[] Array;
			Array = Array2;
			currentArraySize = 2*currentArraySize;
			doublecount++;
	
			//return Array2;
		}
		if(!CommonWord)
		{
			totalcount++;
			for (int i=0; i<length; i++)
			{

				if(Array[i].numWord == currentWord.numWord)//if it is in array
				{
					matched = true;
					Array[i].numCount++;
					
					break;
					
				}
			}
			if (matched == false) //if its not in array
			{
				
					Array[length] = currentWord;
					Array[length].numCount++;
					length++;
					
					//cout << "commonWord" << endl;
			}
		
		}
		
		}
	
	mostFrequent(Array, length);
	for(int i=0; i< n; i++)
	{
	cout<<Array[i].numCount<<" – "<<Array[i].numWord<<endl;	
	}
		
	cout<<"#"<<endl;
	cout<<"Array doubled: "<<doublecount<<endl;
	cout<<"#"<<endl;
	cout<<"Unique non-common words: "<<length<<endl;
	cout<<"#"<<endl;
	cout <<"Total non-common words: "<< totalcount<<endl;
}


/*if(tempWord.length() <1)
		{
			found = true;
		}
*/

