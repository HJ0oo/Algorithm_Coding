#include <iostream>
#include <vector>
using namespace std;
#include <algorithm>


int solution(vector<int> A, vector<int> B)
{
    sort(A.begin(),A.end());
    sort(B.begin(),B.end(),greater<int>());
    int answer = 0;
    for (int i=0;i<A.size();i++){
        answer += A[i] * B[i];
    }

    return answer;
}