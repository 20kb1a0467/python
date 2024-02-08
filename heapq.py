import heapq
a=[1,3,5,8,9]
b=[13,6,2,1]
c=heapq.merge(a,b,reverse=True)
print(*c)

#n smallest elements

a=[1,3,5,8,9]
c=heapq.nsmallest(2,a)
print(*c)

#n largest elements
a=[1,3,5,8,9]
c=heapq.nlargest(2,a)
print(*c)
