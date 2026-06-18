class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = {}

        for path in paths:
            parts = path.split()
            directory = parts[0]

            for file in parts[1:]:
                name, content = file.split("(")
                content = content[:-1]  # remove ')'

                full_path = directory + "/" + name

                if content not in d:
                    d[content] = []

                d[content].append(full_path)

        ans = []

        for files in d.values():
            if len(files) > 1:
                ans.append(files)

        return ans
