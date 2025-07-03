#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

int solution(string word) {
    int weights[5] = {781, 156, 31, 6, 1};
    unordered_map<char, int> charToIndex = {
        {'A', 0},
        {'E', 1},
        {'I', 2},
        {'O', 3},
        {'U', 4}
    };
    
    int answer = 0;
    for (int i = 0; i < word.size(); ++i) {
        int idx = charToIndex[word[i]];
        answer += idx * weights[i];
    }

    return answer + word.size();
}

/*
A
AA
AAA
AAAA    4
AAAAA   5
AAAAE   6
AAAAI   7
AAAAO   8
AAAAU   9
AAAE    10 = 
AAAI    16 = 
AAAO    22 = 
AAAU    28 = 
AAE     34
*/