import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

class MergeKth:
  def __init__(self, A, K):
    self.A = A
    self.K = K
    self.tmp = [0] * len(A)
    self.cnt = 0
    self.kth = -1

  # merge(A[p..q], A[q+1..r]) → A[p..r]
  # 리턴값 없음 (정렬/카운트만 수행)
  def merge(self, p, q, r):
    A, tmp = self.A, self.tmp
    i, j, t = p, q + 1, p
    while i <= q and j <= r:
      if A[i] <= A[j]:
        tmp[t] = A[i]; i += 1
      else:
        tmp[t] = A[j]; j += 1
      t += 1
    while i <= q:
      tmp[t] = A[i]; i += 1; t += 1
    while j <= r:
      tmp[t] = A[j]; j += 1; t += 1

    # 결과를 A[p..r]에 저장하면서만 카운트
    i, t = p, p
    while i <= r:
      A[i] = tmp[t]
      self.cnt += 1
      if self.cnt == self.K and self.kth == -1:
        self.kth = A[i]
      i += 1; t += 1

  # merge_sort(A[p..r]) — 리턴값 없음
  def merge_sort(self, p, r):
    if p >= r:
      return
    q = (p + r) // 2
    self.merge_sort(p, q)
    self.merge_sort(q + 1, r)
    self.merge(p, q, r)

N, K = map(int, input().split())
Ai = list(map(int, input().split()))

mergeKth = MergeKth(Ai, K)

mergeKth.merge_sort(0, N - 1)
print(mergeKth.kth)
