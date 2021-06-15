class Solution:
    def __init__(self):
        self.cache = set()

    def makesquare(self, matchsticks) -> bool:
        self.matchsticks = sorted(matchsticks)
        self.cutoff = sum(matchsticks) / 4
        self.cache = {}
        return sum(matchsticks) % 4 == 0 and self.rec_makesquare(0,0,0,0, len(matchsticks)-1)

    def rec_makesquare(self, s1, s2, s3, s4, idx):
        def recurse_helper(s1, s2, s3, s4, idx):
            '''
            Helper function that takes sides and the index.
            Makes for cleaner but will double the callstack.
            '''
            # sort sides, tuple-ize, and hash to check if previously computed
            sorted_sides = tuple(sorted((s1,s2,s3,s4)))
            args_hash = hash((sorted_sides, self.matchsticks[idx]))
            if args_hash in self.cache: return self.cache[args_hash] # check

            self.cache[args_hash] = self.rec_makesquare(s1, s2, s3, s4, idx)
            return self.cache[args_hash]

        # if all matchsticks used, check solution
        if idx==-1: return s1==s2==s3

        match = self.matchsticks[idx] # size of next match
        idx -= 1 # decrement idx

        # check all possible groups
        if s1+match <= self.cutoff: # prune impossible combinations w/ cutoff
            if recurse_helper(s1+match, s2, s3, s4, idx): return True
        if s2+match <= self.cutoff:
            if recurse_helper(s1, s2+match, s3, s4, idx): return True
        if s3+match <= self.cutoff:
            if recurse_helper(s1, s2, s3+match, s4, idx): return True
        if s4+match <= self.cutoff:
            return recurse_helper(s1, s2, s3, s4+match, idx)
