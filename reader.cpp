#include <iostream>
 #include <fstream> 
#include <iomanip> 
//#include <stdlib>
using namespace std;
 //void output( char*, int); 
void output(string, string);

int main() {  
  ifstream inClientfile("current.dat", ios::in);  
  if (!inClientfile ) {  
    cerr<<"couldnot open file\n";  
    exit(1);
 } 
  char volts[20];  
  char ress[20];  
  //cout<<"Voltage "<<"Resistance \n"; 
  cout<<"Current \n"; 
  while (inClientfile >>volts>>ress)  
  output(volts, ress);  
  return 0; 
} // end of main  
void output(string volts, string res) {
  string voltVal = volts.substr(0, volts.find("V")); // parse vals
  string resVal = res.substr(0, res.find("ohm"));
  int current = (stoi(voltVal)/ stoi(resVal));
    //cout <<resVal<<" "<<voltVal<<endl; 
    cout <<setprecision(2)<<current<<" A"<<endl; 
}
