#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int N;
vector<string> board;

// 주어진 행 뒤집기 조합(row_mask)에 대해 최소 T의 개수를 계산
int countTailsAfterRowFlips(int row_mask) {
    vector<vector<char>> new_board(N, vector<char>(N));
    
    // 행 뒤집기 적용
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (row_mask & (1 << i)) {  // i번째 행을 뒤집음
                new_board[i][j] = (board[i][j] == 'H') ? 'T' : 'H';
            } else {
                new_board[i][j] = board[i][j];
            }
        }
    }

    int total_tails = 0;
    // 열 단위로 처리
    for (int col = 0; col < N; ++col) {
        int tails = 0;
        for (int row = 0; row < N; ++row) {
            if (new_board[row][col] == 'T') tails++;
        }
        // T와 H 중 적은 쪽 선택
        total_tails += min(tails, N - tails);
    }

    return total_tails;
}

int main() {
    cin >> N;
    board.resize(N);
    for (int i = 0; i < N; ++i) {
        cin >> board[i];
    }

    int min_tails = N * N;  // 최대 가능한 T 개수

    // 모든 행 뒤집기 조합 탐색
    for (int row_mask = 0; row_mask < (1 << N); ++row_mask) {
        min_tails = min(min_tails, countTailsAfterRowFlips(row_mask));
    }

    cout << min_tails << endl;
    return 0;
}
