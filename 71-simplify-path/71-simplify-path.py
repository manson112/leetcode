class Solution:
    def simplifyPath(self, path: str) -> str:
        if path[-1] != "/":
            path = path + "/"
        result = ["/"]
        slash = [0]
        for i in range(1, len(path)):
            if path[i] == "/":
                print(result)
                print("i:", i)
                directory = path[slash[-1]+1:i]
                slash += [i]
                print(directory)
                if directory == "" or directory == ".":
                    continue
                if directory == "..":
                    print("result:", result)
                    if len(result) >= 2:
                        result = result[:-2]
                    print(result)
                    continue
                result += [directory] + ["/"]
        if len(result) != 1:
            result = result[:-1]
        print(result)
        return "".join(result)
                