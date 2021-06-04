import heapq
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        l=[(A[i],B[i]) for i in range(len(A))]
        l.sort()
        h=[]
        heapq.heapify(h)
        ans=0
        t=0
        for i in l:
            if i[0]>t:
                ans+=i[1]
                ans%=1000000007
                t+=1
                heapq.heappush(h,i[1])
            else:
                if h[0]<i[1]:
                    ans-=heapq.heappop(h)
                    ans+=i[1]
                    ans%=1000000007
                    heapq.heappush(h,i[1])
            # print(t,ans)
        return ans