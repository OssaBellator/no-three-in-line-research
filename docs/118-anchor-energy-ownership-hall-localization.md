# Anchor-energy localization of ownership Hall failures

The direct score \(\rho_i(A)\) contains the same-slot anchor row mass

\[
U_i(A)=\sum_Bu_i(A,B).
\]

A large value may obstruct movement-label ownership. The product factorization
PP3dv gives a global divisor-energy bound, while PP3mn turns ownership failure
into a high-score rectangle. Combining them rules out middle-sized anchor Hall
cores at the slab-optimal exponents.

## 1. Total same-slot anchor mass

Let \(E_1,\ldots,E_M\) be the disjoint active matching pools, each of size \(R\),
so

\[
\sum_i|E_i|=MR\le m.
\]

Let the movement and refill label sets each have size \(T\). Put

\[
\mathfrak U
=
\sum_{i=1}^M\sum_A\sum_Bu_i(A,B).
\]

Let

\[
D_m=\max_{1\le n\le m^2}\tau(n)=m^{o(1)}.
\]

### Proposition PP3od -- PROVED

One has

\[
\mathfrak U
\le
2mD_m\sum_i|E_i|
=
O(m^2D_m).
\]

#### Proof

Fix a controller edge \(e=(x,y)\) and retained source anchor \(p=(u,v)\). By
PP3dv, a same-slot certificate has

\[
(A-v)(B-u)=(x-u)(y-v)>0.
\]

For fixed \(e,p\), PP3dw gives at most
\(\tau(|(x-u)(y-v)|)\le D_m\) label pairs. Sum over at most \(2m\) source
anchors and over all edges in the disjoint active pools. Counting witness
multiplicity dominates the union counts \(u_i(A,B)\). ∎

The transposed identity is

\[
\mathfrak U
=
\sum_{i,B}V_i(B),
\qquad
V_i(B)=\sum_Au_i(A,B).
\]

## 2. Hall rectangle versus anchor energy

Fix a threshold \(u>0\). Declare movement label \(A\) anchor-acceptable for
macro \(i\) when

\[
U_i(A)\le u.
\]

### Theorem PP3oe -- PROVED

If this capacitated ownership host has no balanced matching, then there is a Hall
set \(X\) satisfying

\[
u|X|(T-|X|)
<
W\mathfrak U.
\]

The same statement holds for the refill ownership host defined by
\(V_i(B)\le u\).

#### Proof

By PP3mn, failure gives an unacceptable rectangle \(X\) by \(Y\) with

\[
|X||Y|>\dfrac{|X|(T-|X|)}W.
\]

Every pair in the rectangle has anchor mass above \(u\), so

\[
\mathfrak U
>
u|X||Y|
>
\dfrac{u|X|(T-|X|)}W.
\]

Rearrange. The refill statement is transposed. ∎

Thus total divisor energy controls the size profile of every anchor-only
ownership Hall set.

## 3. Slab-optimal quantitative localization

Use

\[
M=m^{1/20+o(1)},
\quad
R=m^{19/20+o(1)},
\quad
W=m^{19/40+o(1)},
\quad
T=m^{21/40+o(1)}.
\]

Fix any constant

\[
0<\zeta<\dfrac1{40}
\]

and take

\[
u=m^{-1/40+\zeta}RT.
\]

This is \(o(RT)\).

### Corollary PP3of -- PROVED

If movement anchor ownership at threshold \(u\) fails, its Hall set \(X\)
satisfies

\[
\min\{|X|,T-|X|\}
=
O(m^{1/2-\zeta+o(1)}).
\]

The same conclusion holds for refill anchor ownership.

#### Proof

PP3od and PP3oe give

\[
|X|(T-|X|)
<
\dfrac{W\mathfrak U}{u}
=
O(m^{41/40-\zeta+o(1)}).
\]

Let \(s=\min\{|X|,T-|X|\}\). Since \(s\le T/2\),

\[
|X|(T-|X|)\ge\dfrac{sT}{2}.
\]

Divide by \(T=m^{21/40+o(1)}\). ∎

The exponent \(1/2-\zeta\) is smaller than the total label exponent \(21/40\).
Therefore no positive-density anchor Hall rectangle survives.

## 4. Revised anchor ownership alternatives

### Corollary PP3og -- PROVED

At the threshold of PP3of, each of the movement and refill anchor ownership hosts
has one of the following forms.

1. A balanced ownership exists.
2. A small exceptional label cluster of size
   \[
   O(m^{1/2-\zeta+o(1)})
   \]
   has insufficient acceptable macro capacity.
3. One or more macros reject all labels outside a set of size
   \[
   O(m^{1/2-\zeta+o(1)}).
   \]

#### Proof

Apply PP3of. If \(|X|\) is the small side, use the Hall set itself. If
\(T-|X|\) is small, every macro in the nonempty complement
\([M]\setminus N_M(X)\) rejects all labels of \(X\), hence all but
\(O(m^{1/2-\zeta+o(1)})\) labels. ∎

Thus same-slot anchor energy no longer supports a diffuse or middle-scale
ownership obstruction. The remaining anchor cases are a sublinear exceptional
label cluster or a nearly dead macro column, both explicit targets for local
label trades or macro replacement.