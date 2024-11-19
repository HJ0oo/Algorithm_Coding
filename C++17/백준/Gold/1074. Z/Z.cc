#include <iostream>
using namespace std;


int N,R,C;

int cal(int n, int r, int c){
    if (n == 0) {
        return 0;
    }
    // (1 << n) = 2^n
    int temp = (1<<(n-1)); // 2^(n-1)
    if ((r<temp) && (c<temp)){ // 2사분면
        return cal(n-1, r, c);
    }
    else if ((r<temp) && (temp<=c)){ // 1사분면
        return (1 << (2*n-2)) + cal(n-1, r, c-temp); // 2^(2n-2) - 1 + cal(n-1, r, c);
    }
    else if ((temp<=r) && (c<temp)){ // 3사분면
        return (1 << (2*n-2))*2 + cal(n-1, r-temp, c); // 2^(2n-2) * 2 - 1 + cal(n-1, r, c);
    }
    else if ((temp<=r) && (temp<=c)){ // 4사분면
        return (1 << (2*n-2))*3 + cal(n-1, r-temp, c-temp); // 2^(2n-2) * 3 - 1 + cal(n-1, r, c);
    }
    return 0;
}

int main()
{
    cin >> N >> R >> C;
    cout << cal(N,R,C) << endl;
    return 0;
}