#include <string>
#include <vector>

using namespace std;
/*
dp사용
*/
long long solution(int n) {
    long long dp[20001] = {0};
    dp[1] = 1;
    dp[2] = 2;
    for (int i=3;i<=n;i++){
        dp[i] = dp[i-1] + dp[i-2];
        dp[i] %= 1234567;
    }
    return dp[n];
}