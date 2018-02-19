from pdb import set_trace


class AllParanthesis:
    def solution_recur(self, n):
        """
        A recursive solution
        :type n: int
        :rtype: List[str]
        """
    
        def paranthesize(string, left, right, N, combinations):
            if left == N and right == N:
                combinations.append(string)
            else:
                if left < N:
                    paranthesize(string+"(", left+1, right, N, combinations)
                if right < left:
                    paranthesize(
                        string + ")", left, right + 1, N, combinations)
            return combinations
        
        return paranthesize(string="", left=0, right=0, N=n, combinations=[])


    def solution_dprog(self, n):
        """
        My dynamic programing solution
        :type n: int
        :rtype: List[str]
        """

        combinations = [[] for _ in xrange(n + 1)]
        combinations[0] = [""]
        combinations[1] = ["()"]

        if n == 0:
            return combinations[n]
        for i in xrange(1, n + 1):
            for string in combinations[i - 1]:
                for idx, s in enumerate(string):
                    new = string[:idx] + "()" + string[idx:]
                    if not new in combinations[i]:
                        combinations[i].append(new)

        return combinations[n]


if __name__ == "__main__":
    all_paranthesis = AllParanthesis()
    sol = all_paranthesis.solution_recur(3)
    print sol
