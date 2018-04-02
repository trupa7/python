import numpy as np

A=np.array([1,2,3])

# for i in A:
#     print(i)
#
# print(A**2)
# print(A+A)
# print(np.sqrt(A))
#
#
# a=np.array([1,2])
# b=np.array([2,1])
#
# dot=0
#
# for e,f in zip(a,b):
#     dot +=e*f
# #sum
# print(dot)
#
# print(np.sum(a*b))
# print((a*b).sum())
# print(np.dot(a,b))
# print(a.dot(b))
# #sqrt amng
# print(np.sqrt((a*a).sum()))
# print(np.linalg.norm(a))
# #cosangal
# print(a.dot(b)/(np.linalg.norm(a)*np.linalg.norm(b)))

#creating matrix

# A=np.zeros(10)
# B=np.zeros((10,10))
# print(A)
# print(B)
# #random matrix
# R=np.random.random((10,10))
# print(R)
# print("mean",R.mean())
# print("var",R.var())#variant

#matrix multipication

B=np.array([[1,2],[3,4]])
# #inverse
# Binv=np.linalg.inv(B)
# print(Binv)
# print(Binv.dot(B))
# #deteminate
# print(np.linalg.det(B))
# print("Diagonal",np.diag(B))
# print("Diagonal metrix",np.diag([1,2]))
# print("diagonal sum",np.diag(B).sum())
# print("diagonal sum by trace",np.trace(B))

#outer /inner product

# a=np.array([1,2])
# b=np.array([3,4])
# print("outer product",np.outer(a,b))
# print("inner product",np.inner(a,b))

#covariant

# X=np.random.rand(100,3)
# cov=np.cov(X.T)
# print(cov.shape)

#eigenvalues adn eigen vectors

# print(np.linalg.eigh(cov))

#linear system
# b=np.array([1,2])
# print(np.linalg.inv(B).dot(b))
# print(np.linalg.solve(B,b))

#word problem

C = np.array([[1,1],[1.5,4]])
a = np.array([2200,5050])
p=np.linalg.solve(C,a)
print('children and adults',p)

