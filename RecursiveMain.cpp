//foo

#include <iostream>
#include <string>
using namespace std;

int power(int val, int times ){

    if(times < 1){
        return 1;
    }
    else{
        return val * power(val, times - 1);
    }
 }


int main(){
  static int count = 1;
  count++;
  cout<<count<<"\n";
  if(count < 4){
    main();
  }
  //cout<<"Hello World\n"<<endl;
  //cout<<power(3,4)<<"\n";
  return 0;
}
