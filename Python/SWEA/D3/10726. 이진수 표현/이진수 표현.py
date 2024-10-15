#include <iostream>
#include <string>
#include <bitset>
using namespace std;
int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
		int N,M;
        cin >> N >> M;
        
        /*
        cpp에서는
        && : 논리AND
        &	: 비트AND
        
        파이썬에서는
        and : 논리AND
        &	: 비트AND
        */
        
        
        // # 시도 1 : 시간초과 -- (1 ≤ N ≤ 30 )인데 왜 시간초과가 뜨지
        string ans = "ON" ;
        for (int x = 0 ; x<N;x++){
        	// cout << (M & (1<<x)) ; // 오른쪽부터 x번째 비트 켜져있는지 판단
            if (!( M & (1<<x)) ){ //안켜져있으면
                ans = "OFF";
                break;
            }
        }

        
        
        /*
        // # 시도2 - 오류 : bitset<?> ?부분에는 상수가 들어가야함
        bitset<int(N)> binary(M);
        cout << to_string(binary) << endl;
        */
        
        
        
        /*
        // # 시도 3
        // 근데 마지막이 11111인지만 체크하면 되니까.
        int check_string = (1<<N) - 1 ; // N개의 1
        cout << to_string(M & check_string) << endl;
        
        */
        
		cout << "#" << test_case << " " << ans << endl;
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}