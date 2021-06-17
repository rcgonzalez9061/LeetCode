'''
Ruben Gonzalez
6/15/2021
LeetCode: Matchsticks to Square
https://leetcode.com/problems/matchsticks-to-square
'''
class Solution:
    '''Solution for class for LeetCode'''
    def __init__(self):
        self.cache = None
        self.matchsticks = None
        self.cutoff = None

    def makesquare(self, matchsticks) -> bool:
        '''
        Returns whether matchsticks can be partitioned into 4 equal length
        groups.
        '''
        self.matchsticks = sorted(matchsticks)
        self.cutoff = sum(matchsticks) / 4
        self.cache = {}
        return sum(matchsticks) % 4 == 0 and self.rec_makesquare(0,0,0,0, len(matchsticks)-1)

    def rec_makesquare(self, s_1, s_2, s_3, s_4, idx):
        '''
        Recursive makesquare function.
        '''
        def recurse_helper(s_1, s_2, s_3, s_4, idx):
            '''
            Helper function that takes sides and the index.
            Makes for cleaner but will double the callstack.
            '''
            # sort sides, tuple-ize, and hash to check if previously computed
            sorted_sides = tuple(sorted((s_1,s_2,s_3,s_4)))
            args_hash = hash((sorted_sides, self.matchsticks[idx]))
            if args_hash in self.cache:
                return self.cache[args_hash] # check

            self.cache[args_hash] = self.rec_makesquare(s_1, s_2, s_3, s_4, idx)
            return self.cache[args_hash]

        # if all matchsticks used, check solution
        if idx==-1:
            return s_1==s_2==s_3

        match = self.matchsticks[idx] # size of next match
        idx -= 1 # decrement idx

        # check all possible groups
        if s_1+match <= self.cutoff: # prune impossible combinations w/ cutoff
            if recurse_helper(s_1+match, s_2, s_3, s_4, idx):
                return True
        if s_2+match <= self.cutoff:
            if recurse_helper(s_1, s_2+match, s_3, s_4, idx):
                return True
        if s_3+match <= self.cutoff:
            if recurse_helper(s_1, s_2, s_3+match, s_4, idx):
                return True
        if s_4+match <= self.cutoff:
            return recurse_helper(s_1, s_2, s_3, s_4+match, idx)
