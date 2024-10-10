#include <string>
#include <vector>
#include <unordered_set>
using namespace std;

int solution(int N, int number) {
    if (N == number) return 1;  // 만약 N이 number와 같다면 N을 한 번만 사용해서 만들 수 있음
    
    vector<unordered_set<int>> DP(9); // DP[i]는 N을 i번 사용해서 만들 수 있는 모든 수의 집합

    // i번 사용해서 만들 수 있는 수들 초기화
    int NN = N;
    for (int i = 1; i < 9; i++) {
        DP[i].insert(NN);       // N, NN, NNN, NNNN 등을 넣음
        NN = NN * 10 + N;       // 5, 55, 555, 5555 등으로 변환
    }

    for (int i = 1; i < 9; i++) { // N을 1번부터 8번까지 사용해서 만들 수 있는 모든 경우
        for (int j = 1; j < i; j++) { // i = j + (i - j) 방식으로 모든 경우의 수 탐색
            for (int a : DP[j]) {
                for (int b : DP[i - j]) {
                    DP[i].insert(a + b); // 덧셈
                    DP[i].insert(a - b); // 뺄셈
                    DP[i].insert(a * b); // 곱셈
                    if (b != 0) DP[i].insert(a / b); // 나눗셈, 0으로 나누기 방지
                }
            }
        }
        // number가 DP[i]에 존재하면 i 반환
        if (DP[i].find(number) != DP[i].end()) {
            return i;
        }
    }
    
    return -1; // 8번 안에 못 찾으면 -1 반환
}
