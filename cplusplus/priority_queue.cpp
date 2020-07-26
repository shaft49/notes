/*
How to use priority queue for custom data type, here I am using pair<int, string>, But it can be any class, structure whatever you want.
[Note]that the Compare parameter is defined such that it returns true if its first argument comes before its second argument in a weak ordering.
But because the priority queue outputs largest elements first, the elements that "come before" are actually output last.
That is, the front of the queue contains the "last" element according to the weak ordering imposed by Compare.
*/
#include<iostream>
#include<queue>
using namespace std;
int main() {
    using ptype = pair<int, string>;
    auto Compare = [](ptype a, ptype b) {
        if(a.first == b.first) return a.second < b.second;
        return a.first > b.first;
    };
    priority_queue<ptype, vector<ptype>, decltype(Compare)>PQ(Compare);
    PQ.push({1, "hello"});
    PQ.push({1, "there"});
    PQ.push({9, "zzzz"});
    PQ.push({9, "aaaa"});
    while (!PQ.empty()){
        ptype cur = PQ.top(); PQ.pop();
        cout << cur.first << " " << cur.second << endl;
        /*
            Output order is
            1 there
            1 hello
            9 zzzz
            9 aaaa
            To understand, please reade the note written above.
        */
    }

    return 0;
}