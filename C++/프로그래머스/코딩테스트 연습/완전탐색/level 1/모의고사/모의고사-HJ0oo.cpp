#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> answers) {
    int student1[5] = {1, 2, 3, 4, 5}; // 5
    int student2[8] = {2, 1, 2, 3, 2, 4, 2, 5}; // 8
    int student3[10] = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}; // 10
    vector<pair<int,int>> result = {
        {1,0},
        {2,0},
        {3,0},
    };
    for (int i=0; i<answers.size(); i++){
        if(answers[i] == student1[i%5]){result[0].second++;}
        if(answers[i] == student2[i%8]){result[1].second++;}
        if(answers[i] == student3[i%10]){result[2].second++;}
    }
    
    int max_value = max({result[0].second,result[1].second,result[2].second});
    
    vector<int> answer;
    for (int i = 0; i<result.size();i++){
        if ( max_value == result[i].second) {
        answer.push_back(result[i].first);
        }
    }
    return answer;
}