#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

long long minTimeToHome(long long X, long long Y, long long W, long long S) {
    // Case 1: 가로나 세로로만 이동하는 경우
    long long case1 = (X + Y) * W;

    // Case 2: 대각선으로 최대한 이동하고 나머지는 가로나 세로로 이동하는 경우
    long long case2 = min(X, Y) * S + abs(X - Y) * W;

    // Case 3: 대각선으로만 이동하는 경우
    long long case3;
    if ((X + Y) % 2 == 0) {
        // X와 Y의 합이 짝수인 경우 대각선으로 정확히 도달 가능
        case3 = max(X, Y) * S;
    } else {
        // X와 Y의 합이 홀수인 경우 대각선 이동 후 가로나 세로 이동 한 번 필요
        case3 = (max(X, Y) - 1) * S + W;
    }

    // 세 가지 경우 중 최소값을 반환
    return min({case1, case2, case3});
}

int main() {
    long long X, Y, W, S;
    cin >> X >> Y >> W >> S;
    cout << minTimeToHome(X, Y, W, S) << endl;
    return 0;
}
