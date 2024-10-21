#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<vector<int>> solution(vector<vector<int>> arr1, vector<vector<int>> arr2) {
    vector<vector<int>> answer;
    int a = arr1.size();
    int b = arr1[0].size(); // arr2.size() 와 같음
    int c = arr2[0].size();
    
    
    for (int aa=0; aa<a; aa++){
        vector<int> temp;
        for (int cc=0; cc<c; cc++){
            int s = 0;
            for (int bb=0; bb<b; bb++){
                s += arr1[aa][bb] * arr2[bb][cc];                
            }
            temp.push_back(s);
        }
        answer.push_back(temp);
    }
    
    
    return answer;
}