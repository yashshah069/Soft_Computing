def cartesian():
    n = int(input("\nEnter number of elements in first set (A): "))
    A = []
    B = []
    print("Enter elements for A:")
    for i in range(0, n):
        ele = float(input())
        A.append(ele)
    m = int(input("\nEnter number of elements in second set (B): "))
    print("Enter elements for B:")
    for i in range(0, m):
        ele = float(input())
        B.append(ele)
    print("A = {"+str(A)[1:-1]+"}")
    print("B = {"+str(B)[1:-1]+"}")
    cart_prod = []
    cart_prod = [[0 for j in range(m)]for i in range(n)]
    for i in range(n):
         for j in range(m):
             cart_prod[i][j] = min(A[i],B[j])
    print("A x B = ")
    for i in range(n):
        for j in range(m):
            print(cart_prod[i][j],end=" ")
        print("\n")
    return
cartesian()

# Enter number of elements(A): 6
# 3
# 5
# 6
# 8
# 9
# 0

# Enter number of elements(B):
# 1
# 2
# 4
# 6
# 7
# 8

# Theory:
# To create a fuzzy relation by taking the Cartesian product of two fuzzy sets, we first need to
# understand the concept of fuzzy sets and Cartesian product.
# Fuzzy Sets:
# • In classical set theory, an element either belongs or does not belong to a set. However,
# in many real-world scenarios, the distinction may not be clear-cut.
# • Fuzzy set theory, introduced by Lotfi Zadeh in 1965, extends classical set theory by
# allowing elements to have degrees of membership ranging between 0 and 1.
# • A fuzzy set Aon a universal set X is characterized by a membership function μA(x),
# which assigns a degree of membership to each element xxx in X. This degree of
# membership represents the extent to which x belongs to A.
# Cartesian Product:
# • The Cartesian product of two sets A and B, denoted as A×BA \times BA×B, is the set
# of all possible ordered pairs (a,b) where a is an element of A and b is an element of B.
# • For example, if A={1,2} and B={a,b}, then A×B={(1,a),(1,b),(2,a),(2,b)}
# Fuzzy Relation:
# • A fuzzy relation between two fuzzy sets A and B on the universal sets X and Y,
# denoted as R, is a fuzzy set defined on the Cartesian product X×YX \times YX×Y.
# • Each element (x,y) in the Cartesian product has a degree of membership in the fuzzy
# relation R, representing the degree to which x is related to y.
# • The membership function μR(x,y) assigns a degree of membership to each ordered
# pair (x,y) in X×YX \times YX×Y.
# Creating Fuzzy Relation by Cartesian Product:
# • To create a fuzzy relation by taking the Cartesian product of two fuzzy sets A and B,
# we compute the degree of membership for each ordered pair (x,y) in X×YX \times
# YX×Y.
# • This can be done by applying a suitable operation (e.g., minimum, product, or
# algebraic sum) to combine the degrees of membership from the fuzzy sets A and B.
# • The resulting fuzzy relation R represents the degree of relation between elements of
# the two sets.