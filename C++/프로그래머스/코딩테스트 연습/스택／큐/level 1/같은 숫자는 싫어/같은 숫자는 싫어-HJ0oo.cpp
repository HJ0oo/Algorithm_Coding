/*
방법 1. 제일 마지막에 들어간 것과 지금 들여보낼 것을 비교 = LIFO 스택 사용
방법 2. unique 함수 사용 - 두 줄의 코드로 짧게 끝낼 수 있음

    unique 함수는 연속된 중복 요소만 제거하는 알고리즘입니다.
    즉, 동일한 값이 인접해 있어야 중복 제거가 가능합니다.
    
    unique는 중복되지 않은 값들을 벡터의 앞부분으로 이동시키고,
    그 뒤의 값들은 그대로 남아 있게 됩니다.
    
    반환값은 중복 제거된 요소의 '새로운 끝(iterator)'입니다.
    따라서 그 이후의 값들을 벡터에서 삭제하려면 erase를 함께 사용해야 합니다.
    
    (정렬되지 않은 상태에서 unique를 쓰면 연속된 중복만 제거되므로,
    완전한 중복 제거를 원한다면 먼저 정렬이 필요합니다.)
    
    // 중복 제거 및 불필요한 요소 삭제
    arr.erase(unique(arr.begin(), arr.end()), arr.end());
    vector<int> answer = arr;
    
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


    