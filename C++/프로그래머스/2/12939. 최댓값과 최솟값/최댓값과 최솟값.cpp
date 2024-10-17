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

/*
// 시도 1
string solution(string s) {
    stringstream string_into_stream(s);
    vector<int> numbers;
    
    int number;
    while (string_into_stream >> number){
        numbers.push_back(number);
    }
    
    sort(numbers.begin(),numbers.end());
    
    string answer = to_string(*numbers.begin()) + " " + to_string(*(numbers.end()-1));
                                                                // numbers.back();
    
    return answer;
}
*/


// 시도 2
string solution(string s) {
    string sTemp = "";
    vector<int> my_vec;

    for (int i = 0; i < s.size(); i++)
    {
        if (s[i] == ' ')
        {
            my_vec.push_back(stoi(sTemp)); // 음수인 경우에도 -까지 담은 그 string을 int로 바꿔줄거니까.
            sTemp = ""; // 초기화 잊지 않기
            continue;
        }

        sTemp += s[i];
    }

    my_vec.push_back(stoi(sTemp));

    sort(my_vec.begin(), my_vec.end());

    string answer = to_string(*my_vec.begin()) + " " + to_string(*(my_vec.end()-1));

    return answer;
}