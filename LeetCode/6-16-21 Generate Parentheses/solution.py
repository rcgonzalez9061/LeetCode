class Solution:
    '''
    >>> Solution().generateParenthesis(1)
    ["()"]
    >>> Solution().generateParenthesis(3)
    ["((()))","(()())","(())()","()(())","()()()"]
    '''
    def generateParenthesis(self, n: int):
        return self.recurse_gen_paren('(', 1, 0, n)

    @staticmethod
    def recurse_gen_paren(parentheses, num_opened, num_closed, n):
        if num_closed == n:
            return [parentheses]

        if num_opened == num_closed:
            return Solution.recurse_gen_paren(parentheses + '(', num_opened+1, num_closed, n)
        if num_opened == n:
            return Solution.recurse_gen_paren(parentheses + ')', num_opened, num_closed+1, n)
        else:
            return (
            Solution.recurse_gen_paren(parentheses + ')', num_opened, num_closed+1, n)
            + Solution.recurse_gen_paren(parentheses + '(', num_opened+1, num_closed, n)
            )
