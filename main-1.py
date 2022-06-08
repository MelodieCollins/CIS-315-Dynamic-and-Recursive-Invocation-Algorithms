import sys

from collections import defaultdict
def split(string):
    # store result
    store = defaultdict(str)
    
    # memoization
    def memoization(s):
        # check if the string is already computed
        if store[s] != "":
            return store[s]

        if len(s) == 0:
            return ""

        ans = []
        # check if string forms word present in dictionary
        for word in dictionary:
            
            n = len(word)
            if s[:n] == word:
                
                # substring can be split from the string
                if len(s)-n <= 0:
                    ans.append(word)

                else:
                    # call for the remaining word
                    res = memoization(s[n:])
                    for ch in res:
                        ans.append(word+" "+ch)

        # store result
        store[s] = ans
        return ans

    return memoization(string)


dictionary = []

f = open("diction10k.txt","r")
for word in f:
    dictionary.extend(word.split())
f.close()

i = 0
file = sys.stdin

for line in file.readlines():

    # skip first line
    if i == 0:
        i+=1
        continue

    string = line

    ans = split(string.strip())

    print(f"phrase {i}")
    print(string)
    print("memoized attempt:")

    if len(ans) == 0:
        print("NO, cannot be split\n")
    else:
        print("YES, can be split")
        print(ans[0], "\n")

    i += 1