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
        string ans;
        
        /*
        cpp에서는
        && : 논리AND
        &	: 비트AND
        
        파이썬에서는
        and : 논리AND
        &	: 비트AND
        */
        
		/*
        // # 시도 1
        string ans = "ON" ;
        for (int x = 0 ; x<N;x++){		  // 오른쪽부터 x번째 비트 켜져있는지 판단
            if (!( M & (1<<x)) ){			//안켜져있으면
                ans = "OFF";
                break;
            }
        }
		

        // # 시도2
        // 오류 : bitset<?> ?부분에는 상수가 들어가야함. N이 들어갈 수 없음.
        
        */
	
        
        
        // # 시도 3
        //맨 오른쪽 N개가 1이면 - (1<<N)-1 이용
        //M			   ????????11011
        //(1<<N)-1	000000011111
        //---------------------------------
        //				000000011011
        //				0이 하나라도 있으면 안됨
        //				000000011111 이어야함
             
        /* 
        // 오류 발생
        else if ( M & ( (1<<N) - 1 ) == (1<<N) - 1 ) 
        // 오류 이유
        == 연산자의 우선순위가 &보다 높기 때문에, (1<<N) - 1 == (1<<N) - 1 비교가 먼저 수행
        */
        if (  ( M & ((1<<N)-1) ) == (1<<N) - 1  ) {	// 이렇게 괄호 잘 묶기
            ans = "ON";
        }
        else {
            ans = "OFF";
        }

		cout << "#" << test_case << " " << ans << endl;
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}