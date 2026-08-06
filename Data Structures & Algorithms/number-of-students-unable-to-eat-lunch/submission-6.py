class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        N = len(students)
        q = deque(students)

        res = N

        for sandwich in sandwiches:
            cnt = 0
            
            while cnt < len(q) and q[0] != sandwich:
                q.append(q.popleft())
                cnt += 1
            
            if q[0] == sandwich:
                print(q, sandwich)
                q.popleft()
                res -= 1
            else:
                return res
        
        return res


