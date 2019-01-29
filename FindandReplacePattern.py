# You have a list of words and a pattern, and you want to know which words in words matches the pattern.
#
# A word matches the pattern if there exists a permutation of letters p so that after replacing
# every letter x in the pattern with p(x), we get the desired word.
#
# (Recall that a permutation of letters is a bijection from letters to letters: every letter maps
# to another letter, and no two letters map to the same letter.)
#
# Return a list of the words in words that match the given pattern.
#
# You may return the answer in any order.

# def findAndReplacePattern(words, pattern):



words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern = "abb"
pattern = list(pattern)
res = []
for word in words:
    if len(set(word)) == len(set(pattern)):  # 排除一對多的情况

        flag = True
        mydict = {}

        for a, b in zip(word, pattern):
            if a not in mydict:
                mydict[a] = b
            else:
                if mydict[a] != b:  # 排除多對一的情况
                    flag = False
                    break

        if flag:
            res.append(word)

print(res)
# 了解字典 dictionary 和 zip 用法
# 用排除法的概念來實作