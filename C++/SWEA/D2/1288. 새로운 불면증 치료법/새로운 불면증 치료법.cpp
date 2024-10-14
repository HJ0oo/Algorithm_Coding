#include <iostream>
#include <string> // 문자열 숫자 변환
#include <unordered_set>
using namespace std;

int main() {
	int T;
	cin >> T;

	for (int tc = 1; tc <= T; tc++) {
		int N;
		cin >> N;

		unordered_set<char> num_set{ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };
		int cnt = 1;

		while (!num_set.empty()) {
			int multi_num = cnt * N;
			string multi_str = to_string(multi_num);

			for (char c : multi_str) {
				num_set.erase(c);
			}

			cnt++;
		}

		cout << "#" << tc << " " << N * (cnt - 1) << endl;
	}

	return 0;
}
