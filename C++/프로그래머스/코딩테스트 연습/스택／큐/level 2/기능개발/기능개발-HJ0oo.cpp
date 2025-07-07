#include <string>
#include <vector>
#include <iostream>
#include <cmath> // ceil 함수 사용

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int temp = (100-progresses[0]+speeds[0]-1)/speeds[0];
    int descending = 0;
    for (int i=0; i<progresses.size(); i++){
        // cout << (100-progresses[i]+speeds[i]-1)/speeds[i] << " " << temp << endl;
        
        if (temp >= ((100-progresses[i]+speeds[i]-1)/speeds[i])){
            descending++;
        }
        else {
            answer.push_back(descending);
            descending = 1;
            temp = (100-progresses[i]+speeds[i]-1)/speeds[i];
        }
        
    }
    answer.push_back(descending);
    return answer;    
    
}