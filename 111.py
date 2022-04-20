import sys

def solution(s):
    answer = 1000
    #ans = []

    for num in range(1, len(s)//2 + 2):
        ans = '' #value값 넣어주기
        cnt = 1
        val = s[:num]
        for i in range(num, num + len(s), num):
            if val == s[i:i+num]:
                cnt += 1
            else:
                if cnt == 1:
                    ans += val
                    #print(ans)
                else:
                    ans += str(cnt) + val
                    # ans += val
                    #print(ans)
                val = s[i:i+num]
                cnt = 1
        answer = min(len(ans), answer)
    return answer

while(1):
    sentence = sys.stdin.readline().rstrip() #rstrip 개행문자
    if sentence == 'end':
        break
    print(solution(sentence))


