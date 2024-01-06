def permute(N, M):
    nums = list(range(1, N+1))
    result = []

    def dfs(nums, output=[]):
        if len(output) == M:
            result.append(output[:])
            return

        for num in nums:
            output.append(num)
            next_nums = nums[:]
            next_nums.remove(num)
            dfs(next_nums, output)
            output.pop()
        
    dfs(nums)
    return result

if __name__ == "__main__":
    print(permute(4, 2))

