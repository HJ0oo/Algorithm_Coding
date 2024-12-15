#include <cstdio>
#include <string>

int m;
int S = 0;

int main() {
    char cmd[10];
    int x;

    scanf("%d", &m); // 명령의 수 입력
    while (m--) {
        scanf("%s", cmd); // 명령 입력
        if (cmd[0] == 'a' && cmd[1] == 'd') { // "add"
            scanf("%d", &x);
            S |= (1 << (x - 1)); // x번째 비트를 1로 설정
        } else if (cmd[0] == 'r') { // "remove"
            scanf("%d", &x);
            S &= ~(1 << (x - 1)); // x번째 비트를 0으로 설정
        } else if (cmd[0] == 'c') { // "check"
            scanf("%d", &x);
            printf("%d\n", (S & (1 << (x - 1))) ? 1 : 0); // x번째 비트 확인
        } else if (cmd[0] == 't') { // "toggle"
            scanf("%d", &x);
            S ^= (1 << (x - 1)); // x번째 비트를 반전
        } else if (cmd[0] == 'a' && cmd[1] == 'l') { // "all"
            S = (1 << 20) - 1; // 모든 비트를 1로 설정
        } else if (cmd[0] == 'e') { // "empty"
            S = 0; // 공집합으로 초기화
        }
    }

    return 0;
}
