from collections import Counter

def wordSubsets(words1, words2):
    need = Counter()

    for word in words2:
        cnt = Counter(word)
        for ch in cnt:
            need[ch] = max(need[ch], cnt[ch])

    ans = []

    for word in words1:
        cnt = Counter(word)

        ok = True
        for ch in need:
            if cnt[ch] < need[ch]:
                ok = False
                break

        if ok:
            ans.append(word)

    return ans

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]

print(wordSubsets(words1, words2))