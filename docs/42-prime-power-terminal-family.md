# An explicit terminal family for every prime

The finite terminal states in CMR24 can be replaced by one uniform algebraic
construction. This closes the prime-power terminal-family bottleneck.

Let `p` be a prime. Define a permutation `F_p` of the standard residues
`0,...,p-1` by

\[
F_p(0)=1,
\qquad
F_p(x)=[1+x^{-1}]_p\quad(x\ne0).
\]

For `p=2`, this is the transposition of the two residues. For odd `p`, the
nonzero inverse values, translated by one modulo `p`, use every row except one;
the exceptional column `0` is assigned that missing row.

## 1. The completed inverse is an integer no-three permutation

### Theorem CMR33 — PROVED

For every prime `p`, the graph

\[
\Gamma_p=\{(x,F_p(x)):0\le x<p\}
\]

contains no three real collinear points.

### Proof

The assertion is immediate for `p=2`, so assume that `p` is odd. A real
collinear triple would remain collinear after reduction modulo `p`.

Modulo `p`, the graph consists of the exceptional point

\[
E=(0,1)
\]

and the affine conic

\[
x(y-1)=1.
\]

A modular line not containing `E` meets this conic in at most two points.
Therefore any modular triple must consist of `E` and two conic points on one
line through `E`. Such a line has equation

\[
y-1=mx,
\]

so its two conic columns, when they exist, are `x` and `-x` modulo `p`.

Choose the standard representative `1<=x<=p-1`, put

\[
z=[x^{-1}]_p,
\]

and represent the opposite column by `p-x`. The two conic points are

\[
P=(x,[1+z]_p),
\qquad
Q=(p-x,[1-z]_p).
\]

Write

\[
[1+z]_p-1=z-pA,
\qquad
[1-z]_p-1=-z+pB,
\]

where `A=1` exactly when `z=p-1`, and `B=1` exactly when `z>1`.
The determinant of `E,P,Q` is

\[
\begin{aligned}
\Delta(E,P,Q)
&=x([1-z]_p-1)-(p-x)([1+z]_p-1)\\
&=p\bigl(-z+xB+(p-x)A\bigr).
\end{aligned}
\]

There are three cases.

- If `z=1`, the parenthesis equals `-1`.
- If `1<z<p-1`, it equals `x-z`. Equality `x=z` would imply
  `x^2=1` modulo `p`, forcing `x=1` or `x=p-1`, contrary to the case.
- If `z=p-1`, the parenthesis equals `1`.

Thus the determinant never vanishes. Hence the graph has no real collinear
triple. ∎

## 2. A companion-compatible terminal state at every prime power

Let

\[
N=p^k,
\qquad k\ge2,
\qquad a=p^{k-1}.
\]

The terminal columns in the full `N` by `N` grid are the multiples of `a`.
Define

\[
S_{p,k}
=
\{(aj,aF_p(j)):0\le j<p\}
\cup
\{(aj,1+aF_p(j)):0\le j<p\}.
\]

### Theorem CMR34 — PROVED

For every prime `p` and every `k>=2`, the set `S_{p,k}` is an executable
terminal state for the recursive companion bank and contains no real collinear
triple.

Each layer bijects the terminal columns to its prescribed `p`-point row block.
The two row blocks are disjoint, so the state is compatible with the global
saturation constraints.

### Proof

Within either layer, subtract the layer offset and divide both coordinates by
`a`. This identifies the selected points with `Gamma_p`, so CMR33 excludes all
same-layer triples.

For a mixed triple write its three points as

\[
(ax_i,ay_i+b_i),
\qquad b_i\in\{0,1\}.
\]

Its exact determinant is

\[
\Delta=a(aD+E),
\]

where `D` is the determinant of the normalized points `(x_i,y_i)` and

\[
E=(x_2-x_1)(b_3-b_1)-(x_3-x_1)(b_2-b_1).
\]

Two points lie in the same layer. Consequently `E`, up to sign, is the
difference of their two distinct column indices, and therefore

\[
0<|E|\le p-1.
\]

If `D=0`, then the determinant equals `aE` and is nonzero. If `D\ne0`, then
`|aD|>=a>=p>|E|`, so again `aD+E` cannot vanish. ∎

The verifier uses the normalized coordinates `(x,aF_p(x)+b)`: their determinant
is exactly the full terminal determinant divided by the harmless factor `a`.

## 3. Consequence

The terminal block no longer needs a finite prime table or an unrestricted
uniform measure. At every prime base it may be fixed to the explicit state
`S_{p,k}`, while all nonterminal fibres retain the recursive permutation-bank
choices from CMR25--CMR27.

This removes the terminal-existence bottleneck in
[`tracks/all-n-composite-modulus-progress.md`](../tracks/all-n-composite-modulus-progress.md).
The remaining recursive problem is the external and cross-fibre certificate
mass, not terminal existence.

The finite checker is
[`scripts/verify_prime_power_terminal_family.py`](../scripts/verify_prime_power_terminal_family.py).