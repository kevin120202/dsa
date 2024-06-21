def groupAnagrams(strs):
    group_anag = {}
    for word in strs:
        count_pattern = [0] * 26
        for char in word:
            count_pattern[ord(char) - ord("a")] += 1
        key = tuple(count_pattern)
        print(key)
        if key in group_anag:
            group_anag[key].append(word)
        else:
            group_anag[key] = [word]

    return group_anag.values()


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
