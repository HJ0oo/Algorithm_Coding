#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int by_sum = brown + yellow;
    for (int i = by_sum-1; i>=3; i--){
        if (by_sum % i == 0){
            if (yellow % (i-2) == 0){
                answer.push_back(i);
                answer.push_back(by_sum/i);
                return answer;
            }
        }
    }
    
   
    return answer;
}