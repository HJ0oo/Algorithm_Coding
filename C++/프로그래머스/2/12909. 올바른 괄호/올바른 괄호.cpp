#include <string>
#include <iostream>
// #include <deque>
#include <stack>
/* 
// push() - 데이터를 스택에 추가
// top() - 스택의 가장 위에 있는 요소를 반환
// pop() - 스택의 가장 위에 있는 요소를 제거
    @@ 요소를 제거하지만, 제거된 요소를 반환하지 않습니다@@
    ==> top() 메서드로 값을 먼저 가져온 다음에 pop()을 호출해야.
// empty()
// size()
*/

using namespace std;

bool solution(string s)
{
    stack <char> my_stack;
    
    
    for (char ch : s){
        if (ch == ')'){
            if (my_stack.empty()) {
                return false;
            }
            char pop_ch = my_stack.top();
            my_stack.pop();
            if ( pop_ch == ')' || pop_ch == ch ){
                return false;
            }
        }
        else {
            my_stack.push(ch);
        }
    }
    
    if (my_stack.empty()) {
        return true;
    }
    else {
        return false;
    }
    
    
//         if (my_stack.empty()) {
//             my_stack.push(ch);
//         }
//         else {
//             char pop_ch = my_stack.top();
//             my_stack.pop();
//             if ( pop_ch == ')' || pop_ch == ch ){
//                 return false;
//             }
//         }
//     }
//     return true;
    
    
//     ///////////////////////////////////////
//     char pop_ch = my_stack.top();
//     my_stack.pop();
//     ///////////////////////////////////////
//     if ( pop_ch == '(' ) {
//         return false;
//     }
    
//     char temp;
//     for (int i = 1; i < my_stack.size(); i++){ // 하나 이미 뽑았음 i=1부터 시작
//         temp = my_stack.top();
//         my_stack.pop();
//         if (temp == pop_ch){
//             return false;
//         }
//         else {
//             pop_ch = temp;
//         }
        
//     }

//     return true;
}