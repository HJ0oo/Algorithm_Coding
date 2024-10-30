#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;
// 다시 체크해야함
int main() {
	int n, s; // n: 카의 개수, s: 사물 인터넷에 처음 연결할 카의 번호
	cin >> n >> s;

	// 위치와 연료량을 저장할 벡터
	vector<long long> position(n); // 위치
	vector<long long> fuel(n);      // 연료량
	vector<bool> visited(n, false); // 방문 여부를 체크할 벡터

	// 위치 입력
	for (int i = 0; i < n; i++) {
		cin >> position[i];
	}

	// 연료량 입력
	for (int i = 0; i < n; i++) {
		cin >> fuel[i];
	}

	// S번 카를 0 기반으로 조정 (입력은 1 기반)
	s--;

	// BFS 탐색을 위한 큐 초기화
	queue<int> q;
	q.push(s);              // 처음 연결할 카를 큐에 추가
	visited[s] = true;     // 해당 카를 방문한 것으로 표시

	// BFS 탐색 시작
	while (!q.empty()) {
		int current = q.front(); // 큐에서 현재 카를 꺼냄
		q.pop();

		// 현재 카의 이동 가능한 범위를 계산
		long long left_bound = position[current] - fuel[current]; // 왼쪽 경계
		long long right_bound = position[current] + fuel[current]; // 오른쪽 경계

		// 왼쪽 카들 탐색
		for (int i = current - 1; i >= 0; i--) {
			if (position[i] < left_bound) break; // 범위를 벗어나면 탐색 중단
			if (!visited[i] && position[i] <= right_bound) { // 연결 가능할 경우
				visited[i] = true; // 방문 표시
				q.push(i); // 큐에 추가
			}
		}

		// 오른쪽 카들 탐색
		for (int i = current + 1; i < n; i++) {
			if (position[i] > right_bound) break; // 범위를 벗어나면 탐색 중단
			if (!visited[i] && position[i] >= left_bound) { // 연결 가능할 경우
				visited[i] = true; // 방문 표시
				q.push(i); // 큐에 추가
			}
		}
	}

	// 결과를 저장할 벡터
	vector<int> result;
	for (int i = 0; i < n; i++) {
		if (visited[i]) {
			result.push_back(i + 1); // 1-based 인덱스으로 변환하여 추가
		}
	}

	// 정렬 및 출력
	sort(result.begin(), result.end()); // 결과 정렬
	for (int idx : result) {
		cout << idx << " "; // 각 카의 번호 출력
	}
	cout << endl; // 줄 바꿈

	return 0;
}
