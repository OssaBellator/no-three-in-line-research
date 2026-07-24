# PFR and inverse-additive structure for hyperbola cycles

This chapter converts multiplicative structure in a hyperbola cycle into executable row-column-preserving trades. The key point is that an inverse theorem is only useful here if its structured output can be installed as a repair bank.

Throughout, let

\[
X=\{x_0,\ldots,x_{k-1}\}\subseteq \mathbb F_p^*
\]

be the distinct column parameters of one hyperbola layer

\[
H_a=\{(x,a/x):x\in\mathbb F_p^*\}.
\]

Indices are cyclic modulo `k`. For a shift `s`, define

\[
R_s=\{x_{i+s}x_i^{-1}:i\in\mathbb Z_k\},
\qquad q_s=|R_s|.
\]

The full quotient set is

\[
X/X=\{yx^{-1}:x,y\in X\}.
\]

## 1. Window sets, quotient sets, and energy

### Theorem I1 — PROVED

The window-ratio sets satisfy

\[
\boxed{X/X=\bigcup_{s\in\mathbb Z_k}R_s.}
\]

Consequently,

\[
\boxed{|X/X|\le \sum_s q_s.}
\]

Let

\[
E_\times(X)
=
|\{(u,v,w,z)\in X^4:uv^{-1}=wz^{-1}\}|
\]

be the multiplicative energy. Then

\[
\boxed{
E_\times(X)
\ge
\sum_{s\in\mathbb Z_k}\frac{k^2}{q_s}.
}
\]

### Proof

Every ordered pair `(x_i,x_j)` has a unique cyclic offset `s=j-i`, proving the union identity.

For a fixed `s`, let

\[
\nu_s(r)=|\{i:x_{i+s}x_i^{-1}=r\}|.
\]

Then

\[
\sum_r\nu_s(r)=k,
\qquad
|\operatorname{supp}\nu_s|=q_s.
\]

Cauchy-Schwarz gives

\[
\sum_r\nu_s(r)^2\ge \frac{k^2}{q_s}.
\]

Each term counts an ordered multiplicative-energy quadruple

\[
(x_{i+s},x_i,x_{j+s},x_j).
\]

Different shifts give disjoint indexed quadruple families, because the first ordered pair determines its offset. Summing over `s` proves the energy bound. `square`

## 2. Small quotient sets produce a common-ratio trade bank

For `g\in\mathbb F_p^*`, define

\[
r_X(g)=|\{x\in X:gx\in X\}|.
\]

### Theorem I2 — PROVED

Let

\[
K=\frac{|X/X|}{|X|}.
\]

There is a nonidentity ratio `g` and a family of at least

\[
\boxed{
\frac{k-1}{6K}
}
\]

pairwise disjoint pairs

\[
\{x,gx\}\subseteq X.
\]

Each pair supports an independent rectangle switch in the hyperbola layer. Under arbitrary simultaneous switches from this family, every selected point remains in

\[
\boxed{H_a\cup H_{ag}\cup H_{a/g}.}
\]

### Proof

The total number of ordered nonidentity quotient representations is

\[
\sum_{g\ne1}r_X(g)=k(k-1).
\]

There are at most `|X/X|-1` represented nonidentity ratios. Hence some `g\ne1` satisfies

\[
r_X(g)
\ge
\frac{k(k-1)}{|X/X|-1}
\ge
\frac{k-1}{K}.
\]

Form the graph on `X` with an undirected edge `\{x,gx\}` whenever both endpoints lie in `X`. It has maximum degree at most two. Every undirected edge is represented by at most two directed pairs counted by `r_X(g)`, so the graph has at least `r_X(g)/2` edges. A graph of maximum degree two has a matching containing at least one third of its edges. Thus there are at least `r_X(g)/6` disjoint pairs.

For one pair, the current cells are

\[
(x,a/x),
\qquad
(gx,a/(gx)).
\]

Swapping their rows produces

\[
(x,a/(gx))\in H_{a/g},
\qquad
(gx,a/x)\in H_{ag}.
\]

Disjoint pairs use disjoint rows and columns, so their switches are independent. `square`

### Interpretation

Constant quotient doubling does not merely imply abstract additive structure. It gives a linear-size binary repair bank with a fixed algebraic alphabet of three hyperbola channels.

## 3. Near-minimal quotient sets complete to subgroup absorbers

Choose a generator `\gamma` of `\mathbb F_p^*` and write

\[
X=\gamma^A,
\qquad
A\subseteq\mathbb Z/(p-1)\mathbb Z.
\]

Then

\[
|X/X|=|A-A|.
\]

Let `H` be the stabilizer of `A-A`, and let `t` be the number of `H`-cosets meeting `A`.

Kneser's theorem gives

\[
|A-A|\ge 2|A+H|-|H|=(2t-1)|H|.
\]

Since `|A|\le t|H|`, we obtain the following.

### Theorem I3 — PROVED

If

\[
|X/X|<2|X|,
\]

then `X` is contained in at most

\[
\boxed{
\left\lfloor\frac{1}{2-|X/X|/|X|}\right\rfloor
}
\]

cosets of a multiplicative subgroup, which may be trivial in the general statement.

In particular, if

\[
\boxed{|X/X|<\frac32|X|,}
\]

then `X` is contained in a single coset `x_0K` of a multiplicative subgroup `K`; for `|X|>1`, this subgroup is nontrivial.

More quantitatively, if

\[
|X/X|\le(1+\delta)|X|,
\qquad 0\le\delta<\frac12,
\]

then

\[
X\subseteq x_0K,
\qquad
|X|\le |K|\le(1+\delta)|X|.
\]

Thus at most `\delta|X|` additional hyperbola points are needed to complete `X` to the full multiplicative-coset absorber on `x_0K`.

### Proof

Kneser and `|A|\le t|H|` imply

\[
\frac{|A-A|}{|A|}
\ge
\frac{(2t-1)|H|}{t|H|}
=
2-\frac1t.
\]

Rearranging gives the bound on `t`. If the quotient ratio is below `3/2`, then `t=1`. In that case `A` lies in one `H`-coset and

\[
|A|\le |H|\le |A-A|.
\]

Translating back through discrete logarithms proves the quantitative statement. `square`

### Geometric consequence

Completing the coset installs the exact multiplicative orbit block

\[
\{(x,a/(ux)):x\in x_0K\},
\qquad u\in K,
\]

whose states preserve the same row and column sets and remain single hyperbola channels.

## 4. Robust inverse theorem from many low-complexity windows

A cycle can have a large full quotient set while still having many shifts with small `q_s`. The energy inequality then supplies a structured subset.

Assume a set `S\subseteq\mathbb Z_k` of shifts satisfies

\[
|S|\ge\sigma k,
\qquad
q_s\le Q\quad(s\in S).
\]

Theorem I1 gives

\[
E_\times(X)
\ge
\frac{\sigma}{Q}k^3.
\]

Apply the Balog-Szemeredi-Gowers theorem in the cyclic logarithm group. A quantitative form due to Reiher and Schoen says that if energy is at least `|A|^3/K_0`, then for every fixed `\varepsilon>0` there is `A'\subseteq A` with

\[
|A'|\ge(1-\varepsilon)K_0^{-1/2}|A|
\]

and

\[
|A'-A'|\le C_\varepsilon K_0^4|A'|.
\]

Here `K_0=Q/\sigma`.

### Theorem I4 — PROVED FROM BSG

For every fixed `\varepsilon>0`, there is `c_\varepsilon>0` such that the following holds for sufficiently large `k`.

If at least `\sigma k` shifts satisfy `q_s\le Q`, then there are a ratio `g\ne1` and at least

\[
\boxed{
c_\varepsilon
\left(\frac{\sigma}{Q}\right)^{9/2}k
}
\]

pairwise disjoint pairs `\{x,gx\}\subseteq X`.

Consequently the cycle contains a common-ratio binary repair bank of that size, and every bank state lies inside three hyperbola channels.

### Proof

The energy estimate and the quantitative BSG theorem produce `X'\subseteq X` with

\[
|X'|\ge c_1K_0^{-1/2}k,
\qquad
|X'/X'|\le C_\varepsilon K_0^4|X'|.
\]

Apply Theorem I2 to `X'`. The resulting matching has size at least

\[
\frac{|X'|-1}{6C_\varepsilon K_0^4}
\ge
c_\varepsilon K_0^{-9/2}k.
\]

Substitute `K_0=Q/\sigma`. `square`

## 5. General PFR-level structure

For a constant `K`, the hypothesis

\[
|X/X|\le K|X|
\]

becomes a small-difference-set statement for the logarithm set `A\subseteq\mathbb Z/(p-1)\mathbb Z`.

After standard Ruzsa inequalities convert small difference to small doubling, current general abelian-group Freiman-Ruzsa theory covers `A` by at most

\[
\exp\bigl(C_\eta\log(2K)^{1+\eta}\bigr)
\]

translates of a convex coset progression, with dimension at most

\[
C_\eta\log(2K)^{1+\eta}
\]

and size at most

\[
\exp\bigl(C_\eta\log(2K)^{1+\eta}\bigr)|A|
\]

for every fixed `\eta>0`.

This is useful as a classification theorem, but it is weaker geometrically than Theorems I2 and I3:

- a progression is not automatically an installed row-column absorber;
- interval boundaries prevent unrestricted translation states;
- a progression cover can be sparse inside each progression.

The correct use of PFR here is therefore:

1. classify a frozen core into a bounded-rank multiplicative progression;
2. use quotient multiplicities to extract executable common-ratio rectangles;
3. use near-minimal cases to complete to genuine subgroup-coset absorbers.

Polynomial bounds are known in bounded-torsion abelian groups, but the logarithm group `\mathbb Z/(p-1)\mathbb Z` has exponent growing with `p`; the bounded-torsion theorem does not apply uniformly.

## 6. Structured/dispersed dichotomy

For a cycle column set `X`, define

\[
K_\times(X)=\frac{|X/X|}{|X|}.
\]

The inverse-additive output is now an exact dichotomy.

### Structured regime

If `K_\times(X)=O(1)`, Theorem I2 supplies `\Omega(k)` disjoint same-ratio rectangle trades.

If `K_\times(X)<3/2`, Theorem I3 completes the cycle columns to one exact multiplicative subgroup absorber with fewer than `k/2` added points.

If many individual windows have bounded `q_s`, Theorem I4 supplies a linear common-ratio bank even without assuming the full quotient set is small.

### Dispersed regime

If none of these conclusions holds, then:

- `|X/X|` is large;
- only a small fraction of shifts can have small `q_s`;
- no ratio occurs on a linear family of disjoint column pairs.

This is the regime in which sum-product or incidence estimates should control collateral. It is now separated cleanly from the algebraically structured regime.

## 7. Next exact target

The next bridge should be a common-ratio bank conversion theorem:

> Given `m` disjoint hyperbola rectangle trades with one ratio `g`, and an outside configuration with bounded line occupancy and displacement multiplicity, prove that either a positive fraction of the bank can be flipped to reduce the triple potential, or the outside points concentrate on a bounded family of `g`-invariant secant orbits.

This is more concrete than applying PFR directly to the whole no-three-in-line configuration.

## References

- C. Reiher and T. Schoen, *Note on the Theorem of Balog, Szemeredi, and Gowers*, arXiv:2308.10245.
- W. T. Gowers, B. Green, F. Manners, and T. Tao, *Marton's Conjecture in abelian groups with bounded torsion*, arXiv:2404.02244.
- R. Raghavan, *Improved Bounds for the Freiman-Ruzsa Theorem*, arXiv:2512.11217.
