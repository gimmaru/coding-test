def combine(N, M):
    assert N >= M >= 0, "check, N >= M >= 0"
    assert N != 0, "check N != 0"
    
    nums = list(range(1, N+1))
    result = []

    def dfs(nums, output=[]):
        if len(output) == M:
            result.append(output[:])
            return
        
        for idx, num in enumerate(nums, 1):
            output.append(num)
            dfs(nums[idx:], output)
            output.pop()
    
    dfs(nums)
    return result


if __name__ == "__main__":
    N, M = 4, 2
    print(combine(N, M))