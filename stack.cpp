#include <bits/stdc++.h>
using namespace std;

int main(){
    stack<int> s;
    s.push(1);
    s.push(2);
    s.push(3);
    s.push(4);
    // s.pop();
    // s.pop();
    // s.pop();
    // s.pop();

    cout << " Top element is : " <<s.top() << endl;
    cout << " Empty or not : " <<s.empty() << endl;
    cout << " Size of stack :  " << s.size() << endl;

    cout << " Stack element " << endl;
    while(!s.empty()){
        cout << s.top() << " ";
        s.pop();
    }
}