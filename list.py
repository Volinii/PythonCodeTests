#推导
ls=[1,2,3,5]
a=[r+1 for r in ls]
print(a)
a=[r for r in ls if r%2==0]
print(a)
ls=[[1,2,3],[3,2,1]]
g=(sum(r)for r in ls)
print(next(g))