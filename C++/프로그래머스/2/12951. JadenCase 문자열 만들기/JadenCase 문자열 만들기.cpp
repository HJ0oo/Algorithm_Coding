#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    bool first = true;
    for (char ch : s){
        if (first == true){
            if ('a' <= ch && ch <= 'z') {
                // 대문자 아스키 코드 값이 더 작음
                // 소문자 > 대문자 변환 -
                ch = ch + 'A' - 'a';
                
            }
            first = false;
        }
        else{
            if ('A' <= ch && ch <= 'Z') {
                // 대문자 > 소문자 변환 +
                ch = ch + 'a' - 'A';
            }
            
        }
        
        if (ch == ' ') {
            first = true;
        }
        
        answer += ch;
    }
    return answer;
}