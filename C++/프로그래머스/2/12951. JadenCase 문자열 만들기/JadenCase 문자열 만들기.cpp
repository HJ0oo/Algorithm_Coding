/*
isupper, islower, toupper, tolower 등의 함수는 C 표준 라이브러리의 <ctype.h>에 정의되며, C++에서는 <cctype>로 제공됩니다. 이 함수들은 문자를 대문자나 소문자로 변환하거나, 문자가 대문자인지 소문자인지 확인하는 데 사용됩니다
다만, <string>만 포함해도 작동하는 이유는 일부 컴파일러가 자동으로 <cctype> 또는 <ctype.h>를 포함하거나 간접적인 의존성을 가질 수 있기 때문입니다. 하지만 표준적으로는 <cctype>를 명시적으로 포함하는 것이 권장됩니다
*/
#include <string>
#include <vector>
// #include <cctype>

using namespace std;

string solution(string s) {
    string answer = "";
    answer += toupper(s[0]);
    for (int i = 1; i < s.size(); i++)
        if (s[i - 1] == ' '){
            answer += toupper(s[i]);
        }
        else {
            answer += tolower(s[i]);
        }

    return answer;
}


/////////////////////////////
/*

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
*/