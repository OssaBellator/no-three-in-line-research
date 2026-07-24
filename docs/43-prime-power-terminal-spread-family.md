# A two-parameter spread family of terminal states

This chapter strengthens CMR33--CMR34 from one fixed terminal state to a
quadratic-size family with exact cylinder bounds.

Let `p` be an odd prime and put

\[
h=(p-1)/2.
\]

Let `B_p={1,...,h}` and let `C_p` be the set of nonzero quadratic nonsquares
modulo `p`. Both sets have size `h`. For `b` in `B_p` and `c` in `C_p`, define

\[
F_{b,c}(0)=b,
\qquad
F_{b,c}(x)=[b+cx^{-1}]_p\quad(x\ne0).
\]

## 1. Every parameter pair is no-three

### Theorem CMR35 — PROVED

For every odd prime `p` and every parameter pair `(b,c)`, the map `F_{b,c}` is
a permutation and its integer graph contains no real collinear triple.

### Proof

The nonzero columns map through inversion, multiplication by `c`, and
translation by `b`, so they use every row except `b`; column zero uses that
missing row.

A real triple would remain collinear modulo `p`. Modulo `p`, the graph consists
of the exceptional point

\[
E=(0,b)
\]

and the conic

\[
x(y-b)=c.
\]

A modular triple must therefore contain `E` and the two conic points on one
line through `E`. Write their columns as `x` and `-x`, and put

\[
z=[cx^{-1}]_p.
\]

The two points are

\[
P=(x,[b+z]_p),
\qquad
Q=(p-x,[b-z]_p).
\]

Write

\[
[b+z]_p-b=z-pA,
\qquad
[b-z]_p-b=-z+pD,
\]

where `A=1` exactly when `z>=p-b`, while `D=1` exactly when `z>b`. Direct
expansion gives

\[
\Delta(E,P,Q)=p(-z+xD+(p-x)A).
\]

Since `b<=h<p-b`, there are three ranges.

- If `z<=b`, the parenthesis is `-z`.
- If `b<z<p-b`, it is `x-z`. Equality would imply `x^2=c` modulo `p`,
  impossible because `c` is a nonsquare.
- If `z>=p-b`, it is `p-z`.

Every value is nonzero. ∎

## 2. Exact cylinder bounds

Choose `(b,c)` uniformly from the `h^2` parameter pairs.

### Theorem CMR36 — PROVED

For one terminal layer, any prescribed cell has probability at most `1/h`.
Any compatible prescription on at least two distinct columns has probability
at most `1/h^2`, and the latter bound remains valid for every higher-rank
prescription.

### Proof

At column zero, prescribing a row fixes `b` and leaves at most `h` choices for
`c`, giving probability at most `1/h`.

At a nonzero column, for each possible `b` the cell equation determines at most
one value

\[
c=(y-b)x.
\]

Again at most `h` parameter pairs survive.

For two distinct prescribed columns, the two equations determine both
parameters. If one column is zero, its row fixes `b` and the other cell fixes
`c`. If both are nonzero, subtraction of

\[
y_i=b+cx_i^{-1}
\]

determines `c`, because the inverse column residues are distinct, and then
`b` is determined. Thus at most one parameter pair survives. Additional cells
cannot increase that number. ∎

## 3. Two-layer terminal bank

At `N=p^k`, put `a=p^(k-1)`. Choose independent parameter pairs for the two
layers and select

\[
\{(j,aF_{b_0,c_0}(j)):0\le j<p\}
\]

and

\[
\{(j,1+aF_{b_1,c_1}(j)):0\le j<p\}.
\]

### Corollary CMR37 — PROVED

Every state is companion-compatible and contains no real collinear triple. The
bank has `h^4` states. For a compatible prescription using `r_0` cells in the
first layer and `r_1` cells in the second, its probability is at most

\[
\psi(r_0)\psi(r_1),
\]

where

\[
\psi(0)=1,
\qquad
\psi(1)=1/h,
\qquad
\psi(r)=1/h^2\quad(r\ge2).
\]

### Proof

CMR35 excludes same-layer triples. Reduction modulo `p` excludes mixed triples
because the two terminal row blocks have different row residues. The cylinder
law is the product of the independent single-layer bounds from CMR36. ∎

This gives the recursive bank a nontrivial spread base measure at every odd
prime. It does not give full rank-`r` decay beyond rank two, but every terminal
triple prescription using at least two cells in one layer has probability
`O(p^-2)`.

The finite checker is
[`scripts/verify_prime_power_terminal_spread.py`](../scripts/verify_prime_power_terminal_spread.py).
