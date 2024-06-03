def word_break(s: str, wordDict: list[str]) -> bool:
    word_set = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True  # La stringa vuota è segmentabile
    
    for i in range(1, len(s) + 1):
        for j in range(i):
            print(s[j:i], dp[j])
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break  # Se troviamo una segmentazione valida, possiamo uscire dal ciclo
        
    return dp[len(s)]

# Esempio di test
#s1 = "leetcode"
#wordDict1 = ["leet", "code"]
#print(word_break(s1, wordDict1))  # Output: True

#s2 = "applepenapple"
#wordDict2 = ["apple", "pen"]
#print(word_break(s2, wordDict2))  # Output: True

s3 = "catsandog"
wordDict3 = ["cats", "dog", "sand", "and", "cat"]
print(word_break(s3, wordDict3))  # Output: False
