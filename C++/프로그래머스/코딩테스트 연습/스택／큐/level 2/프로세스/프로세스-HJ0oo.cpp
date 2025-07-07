#include <iostream>
#include <vector>
#include <queue>

using namespace std;
// cout << 'A' - 0 ; // 65
// cout << char(0 + 'A'); // A
int solution(vector<int> priorities, int location) {
    queue<pair<int, int>> processQueue;
    for (int i = 0; i < priorities.size(); ++i) {
        processQueue.push({priorities[i], i});
    }

    int order = 0;
    while (!processQueue.empty()) {
        int currentPriority = processQueue.front().first;
        int currentIndex = processQueue.front().second;
        processQueue.pop();

        bool hasHigher = false;
        queue<pair<int, int>> tempQueue = processQueue;
        while (!tempQueue.empty()) {
            if (tempQueue.front().first > currentPriority) {
                hasHigher = true;
                break;
            }
            tempQueue.pop();
        }

        if (hasHigher) {
            processQueue.push({currentPriority, currentIndex});
        } else {
            order++;
            if (currentIndex == location) {
                return order;
            }
        }
    }

    return -1; // Should not be reached
}
