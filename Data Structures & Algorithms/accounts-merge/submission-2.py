from collections import defaultdict

class UnionFind:
    # create a union find with rank regrouping (smaller rank merges into larger) and with path compression
    def __init__(self,n):
        # initialize an array with everyone as their own parent
        self.parent = [i for i in range(n)]
        self.rank = [1] * n # initialize ranks
    
    def find(self,i):
        print(self.parent)
        print(i)
        # keep recurisvely going up until u reach the root i.e. parent[i] = i
        if self.parent[i] != i:
            # path compression
            self.parent[i] = self.find(self.parent[i]) 
        return self.parent[i] # matches, return the updated parent

    def union(self,a,b):
        # merge a to b

        # first find their parents
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb:
            return False

        # compare the ranks of their parents
        if self.rank[pa] < self.rank[pb]:
            self.parent[pa] = pb # re-assign pa's parent to be pb
        elif self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
        elif self.rank[pa] == self.rank[pb]:
            self.parent[pa] = pb # just choose one
            self.rank[pb] += 1 # add a rank to pb

        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        # initialize the union find

        # index of accounts -> union find number
        emailToAcc = {}  # email and index of account
        # so like {"john.doe@gmail.com":1, ....}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc: # if this email exists
                    uf.union(i, emailToAcc[e]) # union account i and the account with the email's index (join 2 accounts together)
                else:
                    emailToAcc[e] = i # assign this email to the account    

        # now we have some [0,1,0,0,0... ]etc. tree
        # want to convert that into merged accounts with a list of emails

        emailGroup = defaultdict(list) # index of account -> list of emails'
        # so something like {2:["john.doe@gmail.com","jdoe@gmail.com",... etc.]}
        for e, i in emailToAcc.items():
            leader = uf.find(i) # the account index
            print(leader)
            emailGroup[leader].append(e) # keep appending emails to the index

            
        print(emailGroup)

        # generate the output now
        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emails))

        return res

       