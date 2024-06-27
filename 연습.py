from itertools import permutations

baby_lang = ["aya", "ye", "woo", "ma"]
baby_lang_comb = list(permutations(baby_lang, 2))

words = []
for line in baby_lang_comb:
    a = line[0] + line[1]
    words.append(a)

words = words + baby_lang

def solution(babbling):

    if len(babbling) < 1 or len(babbling) > 100:
        return "babbling을 제대로 입력해주세요"
    
    answer = 0
    
    for word in babbling:
        if 1 <= len(word) <=15:
            pass
        else:
            return "babbling을 제대로 입력해주세요"
        
        if word in words:
            answer += 1

    return answer
b = ['aya']
a = solution(b)
print(a)