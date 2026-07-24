# Hybrid resonance fibres and repair barriers

This chapter continues
[`docs/29-full-product-host-selection.md`](29-full-product-host-selection.md).
It proves projection-resolved bounds for the full mixed-radix collinearity
equation, sharpens type-`(2,2)` direction multiplicity, gives an exact
alternating-cycle collateral identity, and records a finite obstruction to
monotone repair. It does **not** prove multiplicative closure.

Use the notation of Chapters 27 and 29. For one radix orientation write

\[
F(c,f)=Ac+Bf,
\]

where `A` and `B` are the corresponding positive diagonal scale matrices,
`c in S_m`, and `f in S_n`.

## 1. Joint projection-fibre concentration

The earlier fixed-carry theorem controls one value of the fine determinant.
The next statement controls the complete flattened collinearity equation,
including both hybrid determinants and the fine determinant simultaneously.

### Theorem PX13 — PROVED

Fix an ordered coarse projected triple

\[
(c_0,c_1,c_2)\in S_m^3
\]

and ordered fine points `f_0,f_1 in S_n` such that

\[
F(c_0,f_0)\ne F(c_1,f_1).
\]

Then there are at most two fine points `f_2 in S_n` for which

\[
F(c_0,f_0),\quad F(c_1,f_1),\quad F(c_2,f_2)
\]

are three distinct collinear integer-grid points.

Consequently, for every fixed ordered coarse triple, at most

\[
\boxed{2|S_n|^2=8n^2}
\]

ordered fine triples produce a product collinearity. Symmetrically, for every
fixed ordered fine triple, at most

\[
\boxed{2|S_m|^2=8m^2}
\]

ordered coarse triples produce a product collinearity.

### Proof

Let `ell` be the real line through the distinct points

\[
F(c_0,f_0),\qquad F(c_1,f_1).
\]

For fixed `c_2`, the map

\[
f\longmapsto F(c_2,f)=Ac_2+Bf
\]

is an invertible diagonal affine map of the fine plane. Therefore its inverse
image of `ell` is a real line. Since `S_n` is no-three, that inverse-image line
contains at most two points of `S_n`.

There are `|S_n|^2` ordered choices of `(f_0,f_1)`, giving the first bound. The
second follows after interchanging the factors. \(\square\)

### Corollary PX13a — PROVED

The joint hybrid expression in PX2 cannot concentrate on more than `8n^2`
ordered fine triples after the complete ordered coarse projection is fixed.
This bound does not require separating

\[
\Delta_{iv},\qquad \Delta_{uj},\qquad \Delta_{uv}.
\]

Thus the arithmetic multiplicity part of PC6 is closed at the level of one
fixed complete factor projection. What remains is controlling dependencies
between many different projection fibres during a repair process.

## 2. Direction multiplicity and type-`(2,2)` signatures

### Lemma PX14 — PROVED

Let `S` be a no-three set of `s` points in the real plane. For any fixed
unoriented real direction, at most `s` ordered pairs `(a,b)` of distinct points
of `S` satisfy

\[
b-a\parallel d.
\]

### Proof

Through each point `a` there is exactly one real line of the prescribed
direction. That line contains at most one further point of `S`, since three
points of `S` cannot be collinear. Hence each first endpoint has at most one
ordered partner. \(\square\)

### Theorem PX14a — PROVED

Let `R_22` be the set of ordered pairs of ordered factor secants

\[
((c_0,c_1),(f_0,f_1))
\]

with distinct endpoints satisfying the type-`(2,2)` resonance

\[
\det\bigl(B(f_1-f_0),A(c_1-c_0)\bigr)=0.
\]

Then

\[
\boxed{
|R_{22}|
\le
4mn\bigl(2\min(m,n)-1\bigr).
}
\]

Equivalently, the number of unordered resonant coarse-pair/fine-pair signatures
is at most

\[
\boxed{mn\bigl(2\min(m,n)-1\bigr).}
\]

### Proof

Fix one ordered coarse secant. The vector `A(c_1-c_0)` determines one direction
in the fine plane after applying `B^{-1}`. By PX14, at most `|S_n|=2n` ordered
fine secants have that direction. Thus

\[
|R_{22}|\le |S_m|(|S_m|-1)|S_n|.
\]

Interchanging the factors also gives

\[
|R_{22}|\le |S_n|(|S_n|-1)|S_m|.
\]

Taking the smaller bound and substituting `|S_m|=2m`, `|S_n|=2n` gives the
first display. Reversing the coarse pair and reversing the fine pair account
for four ordered representations of each unordered signature. \(\square\)

This is a linear-in-the-other-factor multiplicity bound for the entire
weighted-direction obstruction. It does not prevent a selected state from
using many such signatures simultaneously.

## 3. Exact alternating-cycle collateral

Let `Q` be a degree-two product-host state and let `C` be an alternating cycle
between selected and unselected host edges. Put

\[
A=C\cap Q,
\qquad
B=C\setminus Q,
\qquad
R=Q\setminus A.
\]

The toggled state is

\[
Q'=R\cup B.
\]

For a set `R`, define

\[
t_R(x)
=
\#\{\{r_1,r_2\}\subseteq R:r_1,r_2,x\text{ are collinear}\},
\]

and

\[
s_R(x,y)
=
\#\{r\in R:r,x,y\text{ are collinear}\}.
\]

Let `T(X)` denote the number of collinear triples contained in `X`.

### Theorem PX15 — PROVED

The exact change in triple potential is

\[
\begin{aligned}
T(Q')-T(Q)
={}&
\sum_{b\in B}t_R(b)-\sum_{a\in A}t_R(a)\\
&+\sum_{\{b,b'\}\subseteq B}s_R(b,b')
 -\sum_{\{a,a'\}\subseteq A}s_R(a,a')\\
&+T(B)-T(A).
\end{aligned}
\]

### Proof

Triples contained entirely in `R` occur in both states and cancel. Partition
every remaining triple according to whether it contains one, two, or three
moving cells. The one-moving-cell terms give the first line, the two-moving-cell
terms give the second line, and triples entirely in the removed or inserted
half-cycle give the final difference. \(\square\)

PX15 gives an exact decoder for any proposed cycle-selection rule. It also
shows why one-cell shadow alone is insufficient: pair collateral and internal
cycle triples can reverse the sign.

## 4. Monotone repair is false

Define

\[
\Phi(Q)=T(Q).
\]

A natural first repair claim would say that every state with `Phi(Q)>0` has an
alternating-cycle neighbour with smaller `Phi`.

### Claim PX16 — REFUTED

Take

\[
\sigma_0=(0,1),\qquad \sigma_1=(1,0),
\]

\[
\tau_0=(0,2,1),\qquad \tau_1=(1,0,2),
\]

and the crossed `cf` factor-product host of side six.

Exhaustive enumeration gives:

- `546` degree-two factor-compatible states;
- `20,944` unordered single-alternating-cycle adjacencies;
- `2` no-three states;
- `10` states with exactly one bad triple and no neighbour of smaller triple
  count.

Every one of those ten traps requires a temporary increase to at least two bad
triples before any no-three state can be reached. Thus even though the repair
state graph is connected and contains solutions, pure monotone descent in
`Phi` can fail.

## 5. A natural second-order refinement also fails

For every host line `ell` containing at least three host cells, define

\[
q_\ell(Q)=|Q\cap\ell|,
\]

and put

\[
E_2(Q)
=
\sum_{\ell}\binom{q_\ell(Q)}2.
\]

This counts selected pairs lying on potentially dangerous host lines.

### Claim PX17 — REFUTED

Lexicographic descent in

\[
(\Phi(Q),E_2(Q))
\]

is not guaranteed. The same side-six host contains four bad states that are
local minima for this lexicographic potential under every single
alternating-cycle toggle.

One explicit state decomposes into the permutation layers

\[
\pi_0=(1,0,2,3,5,4),
\]

\[
\pi_1=(2,4,5,1,0,3).
\]

Its unique bad triple is

\[
(2,2),\qquad(3,1),\qquad(4,0).
\]

The finite certificate checks every degree-two state and every single-cycle
adjacency, rather than sampling moves.

## 6. Verification

Run

```bash
python scripts/verify_product_hybrid_repair.py
```

The script checks PX13 on all factor pairs in the `2 x 3`, `3 x 2`, and
`3 x 3` cases and all four radix orientations. It checks PX14 for every
saturated no-three factor pair through side five. It then exhausts the complete
side-six repair graph and verifies the numerical certificates in PX16 and PX17.

## 7. Updated boundary

The product branch now has:

- exact saturation for the full degree-two product-host state space;
- exact determinant and four-type resonance classification;
- fixed-carry and complete projection-fibre concentration;
- a sharp direction-multiplicity bound for type `(2,2)`;
- a connected alternating-cycle repair graph;
- an exact cycle collateral identity.

The remaining obstruction is no longer a missing elementary multiplicity
bound. It is a **global repair theorem** that coordinates many projection
fibres while allowing controlled temporary increases in the defect potential.
The side-six barrier shows that any successful theorem must permit bounded
uphill moves, use a nonlocal resampling operation, or introduce an enlarged
host with additional offsets or digit maps.
