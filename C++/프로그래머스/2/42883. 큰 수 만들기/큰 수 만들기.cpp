#include <string>
#include <vector>
#include <algorithm>
#include <deque>

using namespace std;

string solution(string number, int k) {
    vector<char> stack;  // 가장 큰 숫자를 저장할 스택
    int to_remove = k;   // 제거할 숫자의 개수
    
    // 각 자리의 숫자를 순차적으로 확인
    for (int i = 0; i < number.size(); i++) {
        // 스택이 비어 있지 않고, 제거할 수가 남아 있고,
        // 스택의 마지막 숫자보다 현재 숫자가 크다면 스택의 숫자를 제거
        while (!stack.empty() && to_remove > 0 && stack.back() < number[i]) {
            stack.pop_back();
            to_remove--;
        }
        // 스택에 현재 숫자를 추가
        stack.push_back(number[i]);
    }
    
    // 아직 제거해야 할 숫자가 남아 있다면 뒤에서부터 제거
    while (to_remove > 0) {
        stack.pop_back();
        to_remove--;
    }
    
    // 스택에 있는 숫자들을 문자열로 변환
    string answer(stack.begin(), stack.end());
    return answer;
}