/*
제일 마지막에 들어간 것과 지금 들여보낼 것을 비교 = LIFO 스택 사용
*/
#include <vector>
#include <iostream>
#include <stack>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;
    stack <int> my_stack;
    for (auto thing : arr) {
        if ((my_stack.size()!=0) && (my_stack.top()==thing)){
            my_stack.pop();
        }
        my_stack.push(thing);    
    }   
    
    // stack을 pop하면서 vector에 담기 (top → bottom 순서)
    while (!my_stack.empty()) {
        answer.push_back(my_stack.top());
        my_stack.pop();
    }

    // bottom → top 순서로 바꾸기
    reverse(answer.begin(), answer.end());
    
    return answer;
}