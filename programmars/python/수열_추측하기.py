import sys

sys.stdin = open("input.txt", "r")

class Solution:
    def check_prev_value(self, n):
        return True if self.factorials[n] != 1 else False
            
    def get_factorial(self, n, comsum=1):
        if n <= 1:
            return int(comsum)
        return self.get_factorial(n - 1, comsum * n)

    def calculate_comb(self, n, r):
        if not self.check_prev_value(n):
            self.factorials[n] = self.get_factorial(n)
        
        if not self.check_prev_value(r):
            self.factorials[r] = self.get_factorial(r)

        if not self.check_prev_value(n-r):
            self.factorials[n-r] = self.get_factorial(n-r)
        
        return int( self.factorials[n] / (self.factorials[r] * self.factorials[n-r]) )
        
    def get_coef(self, N):
        return [self.calculate_comb(N-1, r) for r in range(N)]
    
    def predict(self, N, F):
        self.factorials = [1] * N
        self.bin_coef = self.get_coef(N)
        self.checklist = [0] * (N+1) # 같은 깊이에서 합이 반복되지 않도록 방지
        result = [0] * N

        def dfs(L=0, sum=0):
            if L > N or sum > F:
                return
            
            if L == N and sum == F:
                print(result)
                sys.exit(0)
                
            for num in range(1, N+1):
                if not self.checklist[num]:
                    self.checklist[num] = 1
                    result[L] = num
                    coef = self.bin_coef[L]
                    dfs(L + 1, sum + (num * coef))
                    self.checklist[num] = 0
        dfs()            

if __name__ == "__main__":
    N, F = map(int, input().split())
    solution = Solution()
    solution.predict(N, F)

# 답지 풀이
def DFS(L, sum):
    if L==n and sum==f:
        for x in p:
            print(x, end=' ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                p[L]=i
                DFS(L+1, sum+(p[L] * b[L]))
                ch[i]=0

if __name__=="__main__":  
    n, f=map(int, input().split())
    p=[0] * n #순열 만들기
    b=[1] * n #이항 계수
    ch=[0]*(n+1) #체크 리스트
    for i in range(1,n):
        b[i]=b[i-1]*(n-i)//i
    DFS(0,0)
