def topKFrequent(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

    # freq = {}
    # ls = []
    # for num in nums:
    #     if num in freq:
    #         freq[num] += 1
    #     else:
    #         freq[num] = 1
    # for key in freq:
    #     ls.append((key, freq[key]))
    # ls.sort(reverse=True, key=lambda tup: tup[1])
    # most_freq = []
    # for i in range(k):
    #     most_freq.append(ls[i][0])
    # return most_freq
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(nums, k))
