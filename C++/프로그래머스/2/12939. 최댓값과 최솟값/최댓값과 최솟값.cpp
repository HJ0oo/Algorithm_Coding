#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>

/*
문자열에서 숫자로 변환:
    std::stoi, std::stod, std::stof, std::stol, std::stoll
숫자에서 문자열로 변환:
    std::to_string
이 함수들은 모두 <string> 헤더에 포함
*/
using namespace std;

string solution(string s) {
    stringstream string_into_stream(s);
    vector<int> numbers;
    
    int number;
    while (string_into_stream >> number){
        numbers.push_back(number);
    }
    
    sort(numbers.begin(),numbers.end());
    
    string answer = to_string(*numbers.begin()) + " " + to_string(*(numbers.end()-1));
    // answer += numbers.back();
    
    return answer;
}