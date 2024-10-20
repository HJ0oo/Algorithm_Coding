#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int ans = 0;
    for (int k = 1; k * (k + 1) / 2 <= n; ++k) {
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