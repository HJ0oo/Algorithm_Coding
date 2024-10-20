#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int ans = 0;
    /*
    a + a+1 + a+2 + ... + a+(k-1) : k개의 연속된 숫자의 합
    = k * a + (0+1+2+ ... +(k-1))
    = k * a + (k * (k - 1)) / 2
    
    n = k * a + (k * (k - 1)) / 2
    k * a = n - (k * (k - 1)) / 2
    n - (k * (k - 1)) / 2가 k로 나누어떨어진다면 연속된 k개의 자연수로 n을 표현할 수 있음.
    */
    for (int k = 1; k * (k + 1) / 2 <= n; ++k) { // k개의 연속된 자연수의 합은 최소 k * (k + 1) / 2가 되므로, 이 값이 n을 초과하지 않는 한 반복을 계속함.
        if ((n - k * (k + 1) / 2) % k == 0) {
            ans++;
        }
    }
    return ans;
}


/*
int solution(int n) {
    int ans = 0;
    for (int start_n = n; start_n > 0 ; start_n--) {
        int temp = start_n * (start_n + 1) / 2; // start_n부터 1까지 더한 값
        if (temp == n) ans++;
    }
    return ans;
}
*/


/*
int solution(int n) {
    int ans = 0;
    for (int start_n = n; start_n > 0 ; start_n--) {
        int temp = 0;
        for (int i=start_n; i>0; i--){
            temp += i;
            if (temp >= n) {
                if (temp == n) {
                    ans += 1;
                }
                break;
            }

        }
    }
    
    return ans;
}
*/