#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> cal;
    for (int i=0;i<progresses.size();i++){
        cal.push_back((((100-progresses[i])%speeds[i])==0)? (100-progresses[i])/speeds[i] : ((100-progresses[i])/speeds[i])+1);
    }
    // return cal;
    
    vector<int> answer;
    int temp  = cal[0];
    int cnt = 0;
    for (int th : cal) {
        if (temp >= th) {
            cnt++;
        }
        else {
            temp = th;
            answer.push_back(cnt);
            cnt = 1;
        }
    }
    answer.push_back(cnt);
    return answer;
}