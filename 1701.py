class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        visited = [False for _ in range(len(students))]
        i = 0
        j = 0
        count = len(students)
        while count != 0:
            if not visited[i] and students[i] == sandwiches[j]:
                j += 1
                visited[i] = True
                count = len(students)
            else:
                count -= 1
            i = (i + 1) % len(students)

        
        return len(sandwiches) - j
