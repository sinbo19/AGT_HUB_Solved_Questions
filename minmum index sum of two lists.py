lass Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {}

        for i in range(len(list1)):
            d[list1[i]] = i

        ans = []
        min_sum = float('inf')

        for j in range(len(list2)):
            if list2[j] in d:
                s = d[list2[j]] + j

                if s < min_sum:
                    min_sum = s
                    ans = [list2[j]]
                elif s == min_sum:
                    ans.append(list2[j])

        return ans
