anagrams = {}
strs = ["eat","tea","tan","ate","nat","bat"]
for s in strs:
    if "".join(sorted(s)) in anagrams.keys():
        anagrams["".join(sorted(s))].append(s)
    else:
        anagrams["".join(sorted(s))] = [s]

print([anagram for anagram in anagrams.values()])