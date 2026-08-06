class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        N = len(students)

        res = N
        for sandwich in sandwiches:
            cnt = 0
            while cnt < N and sandwich != q[0]:
                cur = q.popleft()
                q.append(cur)
                cnt += 1
            
            if sandwich == q[0]:
                res -= 1
                q.popleft()
            else:
                break
        return res
