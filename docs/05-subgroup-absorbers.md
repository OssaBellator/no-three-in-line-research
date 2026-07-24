# Affine terminal configurations and subgroup absorbers

## 1. Finite protected direction sets

For a primitive direction \(d=(u,v)\), define the toroidal line coordinate

\[
\lambda_d(x,y)=vx-uy\pmod n.
\]

If every fibre contains at most two selected points, then every real line in direction \(d\) contains at most two points.

## 2. Two affine layers

Choose \(m,c\pmod n\) and define

\[
S_{m,c}=
\{(x,mx):x\in\mathbb Z_n\}
\cup
\{(x,mx+c):x\in\mathbb Z_n\}.
\]

### Theorem A1 — PROVED

Let \(D\) be a finite set of nonaxis primitive directions. If

\[
\gcd(m,n)=1,
\qquad
\gcd(v-mu,n)=1
\quad((u,v)\in D),
\]

then \(S_{m,c}\) is saturated and contains no real collinear triple in any direction of \(D\).

### Proof

Both affine maps are permutations. For a protected direction, \(\lambda_d\) restricts to an affine bijection on each layer, so every toroidal fibre receives one point from each layer. ∎

## 3. Arithmetic existence

### Theorem A2 — PROVED

If every prime divisor \(q\mid n\) exceeds \(|D|+1\), a suitable \(m\) exists.

For each prime divisor, avoid residue \(0\) and at most one slope residue per protected direction, then combine choices by the Chinese remainder theorem.

This solves the finite-direction terminal problem for sufficiently rough moduli, including all sufficiently large primes.

## 4. Order-two offset for \(n=2N\)

When \(N\) is odd, the layers

\[
y=mx,
\qquad
y=mx+N
\pmod n
\]

admit a relaxed protected-fibre condition. For \(q_d=v-um\):

\[
\begin{cases}
\gcd(q_d,n)=1,&u\text{ even},\\
\gcd(q_d,N)=1,&u\text{ odd}.
\end{cases}
\]

This allows a controlled factor two for odd horizontal component.

## 5. Coset-cycle absorbers

Let \(H\le\mathbb Z_n\) have odd order \(h\). Let \(C=u_0+H\) be a coset in one affine layer. Replace

\[
\{(u,mu+\varepsilon N):u\in C\}
\]

by

\[
\{(u,m(u+t)+\varepsilon N):u\in C\},
\qquad t\in H.
\]

### Theorem A3 — PROVED

If

\[
\gcd(h,v-um)=1
\]

for every protected direction, then every shift state:

- uses the same columns and rows;
- has identical protected toroidal line sums;
- is disjoint from the original state for \(t\ne0\);
- does not collide with the other affine layer.

The cosets supply \(n/h\) pairwise independent installed absorbers, with at least \(h^{n/h}\) global protected states.

## 6. Arithmetic limitation

For prime \(n\), there is no nontrivial proper subgroup, so this route gives global rather than linearly many local absorbers. This is a limitation of the method, not a counterexample to the conjecture.
