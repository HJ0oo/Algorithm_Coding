#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

bool solution(vector<string> phone_book) {
    // phone_book 예시: ["119", "97674223", "1195524421"]
    
    bool answer = true;  // 최종적으로 반환할 값. 기본값은 true (접두사 관계가 없다고 가정)
    
    unordered_map<string, int> hash_map;  // 전화번호들을 저장할 해시맵 생성
    
    // 모든 전화번호를 해시맵에 저장
    for(int i = 0; i < phone_book.size(); i++) {
        hash_map[phone_book[i]] = 1;  // 전화번호를 키로 하여 해시맵에 삽입, 값은 1로 설정
    }
    // hash_map 내용 예시: {"119": 1, "97674223": 1, "1195524421": 1}
    
    // 각 전화번호를 하나씩 검사
    for(int i = 0; i < phone_book.size(); i++) {
        string phone_number = "";  // 현재 번호의 접두사를 저장할 임시 변수

        // phone_book[i]에서 문자 하나씩 붙여가며 접두사 생성
        for(int j = 0; j < phone_book[i].size(); j++) {
            phone_number += phone_book[i][j];  // phone_number에 현재 문자를 추가하여 접두사 생성
            // 예: "119"의 경우, j=0 -> "1", j=1 -> "11", j=2 -> "119"
            
            // 해시맵에 접두사가 존재하고, 전체 번호와 다를 경우 접두사 관계가 성립
            if(hash_map[phone_number] && phone_number != phone_book[i]) {
                // 조건1: hash_map에 phone_number가 키로 존재하는지 확인 (접두사인지 확인)
                // 조건2: phone_number != phone_book[i] ("자기 자신과 비교하지 않도록" 설정)
                
                answer = false;  // 접두사 관계가 있음을 확인했으므로 false로 설정
                return answer;   // 즉시 반환하여 함수 종료
            }
        }
    }
    
    return answer;  // 모든 경우를 확인했을 때 접두사 관계가 없다면 true 반환
}
