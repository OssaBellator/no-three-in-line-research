# The order-three absorber barrier

PX144 reduces a two-point lattice-admissible leftover to the normal form

\[
R_0=\{\pm1\},
\qquad
C_0=\{\pm b\},
\qquad
D_0=\{\pm u\},
\qquad
S_0=\{\pm v\},
\]

with

\[
u^2+v^2=2(1+b^2).
\]

PX146--PX147 show that absorber order two is not universal, but every type
through prime order nineteen has absorber order at most three. This chapter
shows that order three is also not universal. The first finite obstruction
appears at order twenty-three, and a complete symbolic template census proves
that such obstructions must occur for every sufficiently large prime.

## 1. The first order-four type

Use unsigned normalised representatives

\[
1\le b,u,v\le\frac{p-1}{2}.
\]

## Theorem PX152 -- PROVED FINITE

At prime order

\[
p=23,
\]

there are exactly forty-one lattice-admissible but directly noncompletable
normalised two-point types. Exactly thirteen of them have no order-two
absorber:

\[
\begin{aligned}
&(1,1,7),(1,5,5),(1,7,1),\\
&(2,5,10),(2,10,5),\\
&(3,5,8),(3,8,5),\\
&(7,2,2),\\
&(8,5,6),(8,6,5),\\
&(10,3,3),\\
&(11,5,9),(11,9,5).
\end{aligned}
\]

Twelve of these thirteen types have an order-three absorber. The unique
order-three exception is

\[
\boxed{(b,u,v)=(1,5,5).}
\]

This type has the following explicit order-four absorber. Put

\[
M_0=\{(2,0),(4,5),(13,13),(15,7)\}
\]

and

\[
M_1=\{(22,0),(1,1),(2,7),(4,22),(13,5),(15,13)\}.
\]

Every pair denotes the host edge

\[
e(x,y)=(x,y,x-y,x+y)
\]

over \(\mathbb F_{23}\). Then both sets are matchings and

\[
V(M_1)
=
V(M_0)\mathbin{\dot\cup}
\bigl(
\{\pm1\}_R
\cup\{\pm1\}_C
\cup\{\pm5\}_D
\cup\{\pm5\}_S
\bigr).
\]

Consequently the minimum absorber order of this leftover is exactly four.

### Proof

The verifier exhausts all unsigned triples on the lattice circle, rejects the
directly completable types using PX144, and performs a complete order-two
search. For each of the thirteen exceptions it then searches directly for the
five-edge side of an order-three absorber: the eight required leftover vertices
must be covered, while the three additional vertices in every part must form a
three-edge matching. This is an exact required-vertex backtracking search.

It finds order-three absorbers for twelve types and proves that no such matching
exists for \((1,5,5)\). The displayed order-four certificate is checked by
direct vertex-set comparison. \(\square\)

## 2. Abstract order-three templates

An order-three absorber consists of a three-edge matching \(M_0\) and a
five-edge matching \(M_1\). Label the rows and columns of \(M_0\) by

\[
A_1,A_2,A_3,
\qquad
B_1,B_2,B_3.
\]

Its difference and sum labels are

\[
A_i-B_i,
\qquad
A_i+B_i.
\]

The five labels available to \(M_1\) in each part are therefore

\[
\begin{aligned}
R&:\quad 1,-1,A_1,A_2,A_3,\\
C&:\quad b,-b,B_1,B_2,B_3,\\
D&:\quad u,-u,A_1-B_1,A_2-B_2,A_3-B_3,\\
S&:\quad v,-v,A_1+B_1,A_2+B_2,A_3+B_3.
\end{aligned}
\]

After fixing the row order, an abstract template is determined by three
permutations assigning the column, difference and sum labels to those five
rows. Hence there are exactly

\[
(5!)^3=1,728,000
\]

templates.

For one template, each of its five edges supplies the two equations

\[
r-c-d=0,
\qquad
r+c-s=0.
\]

These are ten homogeneous integer linear equations in the six internal
variables

\[
A_1,A_2,A_3,B_1,B_2,B_3
\]

and the four external coordinates

\[
1,b,u,v.
\]

Write the resulting matrix as

\[
[A_T\ B_T],
\]

where \(A_T\) contains the six internal columns.

## Theorem PX153 -- PROVED FINITE/SYMBOLIC

For every one of the \(1,728,000\) abstract order-three templates,

\[
\boxed{
\operatorname{rank}_{\mathbb Q}[A_T\ B_T]
-
\operatorname{rank}_{\mathbb Q}A_T
=2.
}
\]

The complete internal/full rank distribution is

| \(\operatorname{rank}A_T\) | \(\operatorname{rank}[A_T\ B_T]\) | Templates |
|---:|---:|---:|
| 0 | 2 | 8 |
| 1 | 3 | 288 |
| 2 | 4 | 4,504 |
| 3 | 5 | 39,360 |
| 4 | 6 | 204,864 |
| 5 | 7 | 613,632 |
| 6 | 8 | 865,344 |

Thus every order-three template imposes exactly two independent affine
consistency conditions on the external parameters \((b,u,v)\). Whenever the
template is feasible, its parameter set is contained in an affine line.

### Proof

The verifier enumerates the three permutations and computes both ranks modulo

\[
q=1,000,000,007.
\]

Every matrix entry has absolute value at most two. By Hadamard's inequality,
every square minor of size at most ten has absolute determinant at most

\[
(2\sqrt{10})^{10}
=102,400,000
<q.
\]

Therefore a minor is nonzero over the integers if and only if it is nonzero
modulo \(q\). The modular ranks are exactly the rational ranks, not merely lower
bounds. The exhaustive distribution is the displayed table. The usual
solvability criterion for

\[
A_Tz=-B_T(1,b,u,v)^{\mathsf T}
\]

shows that the rank difference is the number of independent consistency
conditions on the external vector. \(\square\)

## 3. Order three fails asymptotically

## Theorem PX154 -- PROVED

For every prime

\[
\boxed{p>102,400,000,}
\]

there is a lattice-admissible two-point leftover in the strong-complete host
which has no absorber of order at most three.

Consequently no universal two-point absorber theorem can use the constant
order three. Any universal bounded-order theorem, if true, must allow order at
least four.

### Proof

First count signed parameter triples

\[
(b,u,v)\in(\mathbb F_p^*)^3
\]

on the lattice circle

\[
u^2+v^2=2(1+b^2).
\]

For every nonzero \(b\) with \(1+b^2\ne0\), the standard quadratic character
count gives

\[
\#\{(u,v)\in\mathbb F_p^2:u^2+v^2=2(1+b^2)\}
=p-\chi(-1)
\ge p-1.
\]

Removing the solutions with \(u=0\) or \(v=0\) deletes at most four pairs.
There are at least \(p-3\) admissible values of \(b\). Hence the number of
signed nonzero lattice triples is at least

\[
(p-3)(p-5).
\]

A directly completable triple satisfies

\[
\{u^2,v^2\}
=
\{(1-b)^2,(1+b)^2\}.
\]

For each \(b\), there are at most eight ordered signed choices of \((u,v)\).
Thus the number of signed lattice-admissible, directly noncompletable triples is
at least

\[
(p-3)(p-5)-8(p-1)
=
\boxed{p^2-16p+23.}
\]

Now fix an order-three template. For primes exceeding the Hadamard bound, its
integer ranks remain the ranks from PX153 after reduction modulo \(p\). Its two
independent affine consistency equations have at most \(p\) solutions in
\((b,u,v)\). Therefore all \((5!)^3\) templates together cover at most

\[
1,728,000p
\]

signed parameter triples.

For \(p>102,400,000\),

\[
p^2-16p+23>1,728,000p.
\]

Hence some lattice-valid, directly noncompletable signed triple satisfies no
order-three template.

Finally, any absorber of smaller positive order can be padded to order three by
adding common host edges disjoint from both of its matchings. PX139 gives
positive residual degree after deleting a bounded number of vertices when
\(p\) is this large. Therefore the uncovered type has no absorber of order one,
two or three. \(\square\)

The numerical threshold is deliberately crude. It comes from using one prime
modulus large enough to certify every possible template minor and a union bound
over all labelled templates. The structural conclusion is the important one:
order-three absorber families occupy only finitely many affine-line sections of
the two-dimensional lattice circle.

## 4. Revised absorption target

The finite and asymptotic results change the completion problem.

1. Order two is insufficient from prime seventeen onward.
2. Order three first fails at prime twenty-three.
3. Order three fails for every sufficiently large prime by PX154.
4. Order four is sufficient for the first exceptional type.

The next useful target is therefore one of the following.

- Prove that every two-point lattice leftover has an absorber of order at most
  four.
- Find the first order-four obstruction and determine whether the minimum order
  is unbounded.
- Replace individual two-point absorbers by a collective absorber which handles
  many lattice-circle packets simultaneously.

The last option may be better aligned with the pseudorandom leftover from
PX141, because collective absorption can use cancellations among the three
moment conditions from PX143.

## 5. Verification

Compile and run

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_order_three_absorber_barrier.cpp \
  -o /tmp/verify_product_order_three_absorber_barrier
/tmp/verify_product_order_three_absorber_barrier
```

The verifier reproduces the complete prime-23 order-two and order-three census,
checks the explicit order-four certificate, and exhausts all \(1,728,000\)
abstract order-three templates with exact rank certification.
