#!/usr/bin/env python3
"""Verify PX142--PX144: edge lattice and two-point leftovers."""
from itertools import combinations, product


def bareiss_det(matrix):
    a=[row[:] for row in matrix]
    n=len(a); sign=1; previous=1
    for k in range(n-1):
        if a[k][k]==0:
            pivot=next((r for r in range(k+1,n) if a[r][k]),None)
            if pivot is None: return 0
            a[k],a[pivot]=a[pivot],a[k]; sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                a[i][j]=(a[i][j]*pivot-a[i][k]*a[k][j])//previous
        previous=pivot
        for i in range(k+1,n): a[i][k]=0
    return sign*a[-1][-1]


def rank_mod(matrix,q):
    a=[[value%q for value in row] for row in matrix]
    rows=len(a); cols=len(a[0]); rank=0
    for col in range(cols):
        pivot=next((r for r in range(rank,rows) if a[r][col]),None)
        if pivot is None: continue
        a[rank],a[pivot]=a[pivot],a[rank]
        inv=pow(a[rank][col],-1,q)
        a[rank]=[(x*inv)%q for x in a[rank]]
        for r in range(rows):
            if r==rank or a[r][col]==0: continue
            factor=a[r][col]
            a[r]=[(x-factor*y)%q for x,y in zip(a[r],a[rank])]
        rank+=1
        if rank==rows: break
    return rank


def incidence(p):
    columns=[]
    for x,y in product(range(p),repeat=2):
        col=[0]*(4*p)
        for part,value in enumerate((x,y,(x-y)%p,(x+y)%p)):
            col[part*p+value]=1
        columns.append(col)
    return [[columns[c][r] for c in range(p*p)] for r in range(4*p)]


def canonical_minor(p):
    matrix=incidence(p)
    rows=list(range(p))+list(range(p,2*p-1))+list(range(2*p,3*p-1))+list(range(3*p,4*p-1))
    columns=[]
    for x in (0,1,2):
        columns.extend(x*p+y for y in range(p))
    columns.extend(x*p for x in range(3,p))
    assert len(rows)==len(columns)==4*p-3
    return [[matrix[r][c] for c in columns] for r in rows]


def moments(p,sets):
    r,c,d,s=sets
    linear_r=(sum(d)+sum(s)-2*sum(r))%p
    linear_c=(sum(s)-sum(d)-2*sum(c))%p
    quadratic=(sum(x*x for x in d)+sum(x*x for x in s)-2*sum(x*x for x in r)-2*sum(x*x for x in c))%p
    return linear_r,linear_c,quadratic


def direct_two_completion(p,sets):
    r,c,d,s=map(tuple,sets)
    for pairing in ((0,1),(1,0)):
        edges=[]
        for index,row in enumerate(r):
            column=c[pairing[index]]
            edges.append((row,column,(row-column)%p,(row+column)%p))
        if {e[2] for e in edges}==set(d) and {e[3] for e in edges}==set(s):
            return True
    return False


def verify_prime(p):
    matrix=incidence(p)
    assert rank_mod(matrix,p)==4*p-6
    for q in (2,3,5,7,11,13):
        if q!=p:
            assert rank_mod(matrix,q)==4*p-3
    assert abs(bareiss_det(canonical_minor(p)))==p**3

    for x,y in product(range(p),repeat=2):
        assert moments(p,((x,),(y,),((x-y)%p,),((x+y)%p,)))==(0,0,0)

    valid=0
    for r in combinations(range(p),2):
        for c in combinations(range(p),2):
            for d in combinations(range(p),2):
                for s in combinations(range(p),2):
                    if moments(p,(r,c,d,s))!=(0,0,0): continue
                    valid+=1
                    inv2=pow(2,-1,p)
                    rc=sum(r)*inv2%p; cc=sum(c)*inv2%p
                    a=(r[1]-r[0])*inv2%p; b=(c[1]-c[0])*inv2%p
                    dc=sum(d)*inv2%p; sc=sum(s)*inv2%p
                    u=(d[1]-d[0])*inv2%p; v=(s[1]-s[0])*inv2%p
                    assert dc==(rc-cc)%p and sc==(rc+cc)%p
                    assert (u*u+v*v-2*(a*a+b*b))%p==0
                    direct=direct_two_completion(p,(r,c,d,s))
                    criterion={u*u%p,v*v%p}=={(a-b)**2%p,(a+b)**2%p}
                    assert direct==criterion
    print(f"p={p}: lattice rank, determinant, moments, and {valid} two-point leftovers verified")


def main():
    for p in (3,5,7,11):
        if p<=7:
            verify_prime(p)
        else:
            matrix=incidence(p)
            assert rank_mod(matrix,p)==4*p-6
            assert abs(bareiss_det(canonical_minor(p)))==p**3
            print(f"p={p}: lattice rank and determinant verified")
    print("PX142--PX144 verified")


if __name__=="__main__":
    main()
