def minmax():
    r1 = int(input("Enter number of rows of first relation (R1): "))
    c1 = int(input("Enter number of columns of first relation (R1): "))
    rel1=[[0 for i in range(c1)]for j in range(r1)]
    print("Enter the elments for R:")
    for i in range(r1):
        for j in range(c1):
            rel1[i][j]=float(input())

    r2 = int(input("Enter number of rows of second relation (R2): "))
    c2 = int(input("Enter number of columns of second relation (R2): "))
    rel2=[[0 for i in range(c2)]for j in range(r2)]
    print("Enter the elments for R:")
    for i in range(r2):
        for j in range(c2):
            rel2[i][j]=float(input())
    print("\nR1 = ")
    for i in range(r1):
        for j in range(c1):
            print(rel1[i][j],end=" ")
        print("\n")
    print("\nR2 = ")
    for i in range(r2):
        for j in range(c2):
            print(rel2[i][j],end=" ")
        print("\n")

    col=0
    comp=[]
    for i in range(r1):
        comp.append([])
        for j in range(c2):
            l=[]
            for k in range(r2):
                l.append(min(rel1[i][k],rel2[k][j]))
            comp[i].append(max(l))
    print("\nR1 composition R2 =")
    for i in range(r1):
        for j in range(c2):
            print(comp[i][j],end=" ")
        print("\n")
    return
minmax()

# Enter number of rows of first relation (R1): 2
# Enter number of columns of first relation (R1): 2    
# Enter the elments for R:
# 2
# 4
# 6
# 7
# Enter number of rows of second relation (R2): 2      
# Enter number of columns of second relation (R2): 3   
# Enter the elments for R:
# 4
# 6
# 7
# 3
# 8
# 7

# Theory:
# In fuzzy logic, max-min composition is a fundamental operation used to combine two fuzzy
# relations to produce a new fuzzy relation. This operation is particularly useful in fuzzy
# inference systems and fuzzy control systems for reasoning and decision-making processes.
# Let's delve into the theory behind max-min composition:
# 1. Fuzzy Relations:
# o A fuzzy relation represents a mapping between elements from two sets, where
# each element is associated with a degree of membership or truthfulness.
# o Let R1 and R2 be two fuzzy relations defined as R1={(x,y,μ1(x,y))} and
# R2={(y,z,μ2(y,z))}, where x, y, and z are elements from their respective
# universes, and μ1 and μ2 are membership functions representing the degree of
# membership between the elements.
# 2. Max-Min Composition:
# o Max-min composition is a method of combining two fuzzy relations to obtain a
# new fuzzy relation.
# o Given R1 and R2 , the max-min composition RRR is defined as:
# R=R1∘R2={(x,z,μ(x,z))}
# where the degree of membership μ(x,z)\mu(x, z)μ(x,z) is calculated as the
# maximum of the minimum degrees of membership over all intermediate
# elements: μ(x,z)=max(min(μ1(x,y),μ2(y,z))) for all y in the universe of
# discourse.
# 3. Interpretation:
# o Max-min composition represents the fuzzy relation between the elements xxx
# and zzz considering the intermediate element y.
# o It captures the maximum degree of compatibility between xxx and zzz based on
# the minimum degree of compatibility with the intermediate element y.
# 4. Applications:
# o Max-min composition is widely used in fuzzy inference systems, fuzzy control
# systems, pattern recognition, and decision-making processes.
# o It allows for reasoning and making decisions in uncertain and imprecise
# environments, where traditional binary logic may not be suitable.