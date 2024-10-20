#include <string>
#include <vector>

using namespace std;


string to_bin_1(int num) {
    string binaryString = "";
    for (int i = num; i > 0; i = i / 2) {
        binaryString.push_back((i % 2) + '0');
    }
    return binaryString;
}

string to_bin_2(int num) {
    string s = "";
    // 숫자가 0이 될 때까지 나누면서 이진수로 변환
    for (int i = num; i > 0; i = i / 2) {
        s = to_string(i % 2) + s;  // 앞쪽에 추가
    }
    return s;
}


string to_bin_3(int n){
    string binary = "";
    while (n > 0) { // n이 0이 될 때까지 나누며 이진수로 변환
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
        s = to_bin_1(cnt_one);
        trans += 1;
    }

    
    answer.push_back(trans);
    answer.push_back(cnt_zero);
    return answer;
}