#include <string>
#include <vector>

using namespace std;

int solution(vector<int> citations) {
    // 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때,
    // 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.
    int arr[10001] = {} ;
    int n = citations.size() ;
    for (int i=0;i<n;i++){
        arr[citations[i]] += 1;
    }
    
    int sum = 0;
    for (int i=10000;i>=0;i--){
        sum += arr[i];
        if (sum>=i){
            return i;
        }
    }
    return -99999999;

}