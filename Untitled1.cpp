#include <iostream>
#include <vector>
using namespace std;
void show_vector( vector<int>&a)
{
    for (vector<int>::iterator it = a.begin() ; it!=a.end() ; ++it)
        cout<<*it;
}
int main()
{
    int x;
    vector<int>a;
    while (cin>>x)
        a.push_back(x);
    show_vector(a);
    return 0;
}