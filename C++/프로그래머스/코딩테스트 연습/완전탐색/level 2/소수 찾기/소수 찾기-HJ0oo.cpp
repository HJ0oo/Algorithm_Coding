#include <string>
#include <vector>
#include <iostream>
#include <string>
#include <set>

using namespace std;
bool used[10] = {false,};
set <int> total_set;

bool is_prime(unsigned int a) {
    // cout << a << " 프라임" << endl;
    
    if (a == 1) { return false; }
    for (int i=a-1; i>=2; i--){
        if (a % i == 0) {
            return false;
        }
    }
    return true;
}

void permu(int now, string numbers, string k){
    // cout << "*" << k << endl;
    if ((k != "") && (stoi(k)!=0) ) {
        total_set.insert(stoi(k));
    }
    if (now == numbers.size()) { return; }
    
    //순서바뀌는거
    for (int i=0; i<numbers.size(); i++){
        if (used[i] == false) {
            used[i] = true;
            permu(now+1,numbers,k+numbers[i]); // i+1 아니고 now+1임
            used[i] = false;
        }
    }
    
}

int solution(string numbers) {
    int answer = 0;
    permu(0,numbers,"");

    for (int a : total_set) {
        // cout << "#" << a << endl;
       if (is_prime(a)) {
           answer++;
       } 
    }    

    return answer;
}