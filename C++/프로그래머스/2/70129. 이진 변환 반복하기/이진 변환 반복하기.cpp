#include <string>
#include <vector>

using namespace std;

string to_bin(int n){
    string binary = "";
    // n이 0이 될 때까지 나누며 이진수로 변환
    while (n > 0) {
        binary = to_string(n % 2) + binary;  // 나머지를 앞쪽에 추가
        n /= 2;  // 2로 나눔
    }
    return binary;
}



vector<int> solution(string s) {
    vector<int> answer;
    
    int cnt_one = 0;
    int cnt_zero = 0;
    int trans = 0;
    
    while (s != "1"){
        cnt_one = 0;
        for (char ch : s){
            if (ch == '1') {
                cnt_one += 1;
            }
            else {
                cnt_zero += 1;
            }
        }
        s = to_bin(cnt_one);
        trans += 1;
    }
    
    answer.push_back(trans);
    answer.push_back(cnt_zero);
    return answer;
}