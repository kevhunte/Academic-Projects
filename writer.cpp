#include <iostream>
 #include <fstream>
 //#include <stdlib>
using namespace std; 

int main() {  
  ofstream clientfile("current.dat", ios::out);  
  if (!clientfile) {  
    cerr<<"could not open file"<<endl;  
    exit(1); 
  }  
  cout<<"enter the voltage and resistance\n";  
  cout<<"enter the end-of-file to end input\n";  
  char volt[20];  
  char res[20];  
  while (cin>>volt>>res) {  
    clientfile<<volt<<' ' <<res <<' ' <<endl;  
    cout <<" ? "; 
  }  return 0;
 } // end of main
