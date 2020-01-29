#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Finder
{
public:
  Finder(int n)
  {
    this->size = n;
  };
  void loadVector()
  {
    srand(time(0));
    for(int i = 0; i < size; i++)
    {
      this->Vals.push_back((rand() % 81) + 10); // 10 to 90 inclusive
    }
  };
  void printVals()
  {
    cout<<"vector values: ";
    for(int i: Vals)
    {
      cout<<i<<" ";
    }
    cout<<endl;
  };
  void findUniqueVals()
  {
    cout<<"Unique Values: ";
    vector<int> dist; // holds unique values
    for(int i: Vals){
      if(searchForVal(dist,i) == 0) // can't find it
      {
        dist.push_back(i);
        cout<<i<<" ";
      }
    }
    cout<<endl;

  };
private:
  vector<int> Vals;
  int size;
  int searchForVal(vector<int> arr, int val)
  {
    for(int n: arr)
    {
      if(val == n)
      {
        return 1;
      }
    }

    return 0;
  };
};

int main()
{
  //load with random vals. print vals find unique vals, and print those
  Finder finder(20);
  finder.loadVector();
  finder.printVals();
  cout<<endl;
  finder.findUniqueVals();

  return 0;
}
