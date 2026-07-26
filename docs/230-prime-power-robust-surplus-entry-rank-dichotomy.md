# Robust surplus is a secant-star bank or an entering-pair line load

CMR990--CMR1005 convert a minimum-robust target escape into new-triple
incidences and stabilize recurrent edge/triple signatures. This chapter uses the
number of genuinely new physical cells in each new triple. Rank-one new triples
are controlled by lines through one entering cell and old common cells. Higher-
rank new triples contain an entering pair and therefore concentrate directly on
one selected line of the bank state.

Let `S,Q` be saturated labelled two-layer states on the same side-`n` board. Put

\[
A=|Q|\setminus |S|,
\qquad
a=|A|,
\]

where vertical bars on a state mean its physical cell set. Let

\[
\mathcal N=\mathcal T(Q)\setminus\mathcal T(S),
\qquad
N=|\mathcal N|.
\]

Every cell of `A` has one selected layer label in `Q`. For a new triple `U`,
define its physical entry rank

\[
\rho(U)=|U\cap A|.
\]

## 1. Exact entry-rank partition

### Theorem CMR1006 -- PROVED

Every new triple has entry rank one, two, or three. If

\[
N_r=|\{U\in\mathcal N:\rho(U)=r\}|,
\]

then

\[
\boxed{N=N_1+N_2+N_3.}
\]

### Proof

A new physical triple cannot use only cells already selected in `S`, because then
it would also be a triple of `S`. Thus `\rho(U)>=1`; a triple has three cells. ∎

## 2. Half the surplus has rank one or at least two

### Theorem CMR1007 -- PROVED

Put `H=N_2+N_3`. Then

\[
\boxed{\max\{N_1,H\}\ge\left\lceil\frac N2\right\rceil.}
\]

In a robust episode with destroyed load `D` and positive gap `g`, CMR991 gives

\[
\boxed{\max\{N_1,H\}\ge
\left\lceil\frac{D+g}{2}\right\rceil.}
\]

### Proof

The two nonnegative integers `N_1,H` sum to `N`; use CMR991 for the second
statement. ∎

## 3. Rank-one triples concentrate at one entering cell

Assume `N_1>0`, so `a>=1`. Assign every rank-one triple to its unique cell of
`A`.

### Theorem CMR1008 -- PROVED

Some entering physical cell `x\in A`, with its unique selected labelled edge
`e_x\in Q`, supports at least

\[
\boxed{d_x\ge\left\lceil\frac{N_1}{a}\right\rceil}
\]

rank-one new triples.

Let

\[
C=|S|\cap |Q|
\]

be the common physical cells. For every real line `L` through `x`, put

\[
r_L=|C\cap L|.
\]

Then the exact supported-triple count is

\[
\boxed{d_x=\sum_{L\ni x}\binom{r_L}{2}.}
\]

### Proof

Average the unique assignments over the `a` entering cells. A rank-one triple
through `x` consists of `x` and two common cells. Those two cells determine one
line through `x`. Conversely, every two common cells on one line through `x`
form a new triple with `x`, because `x` is absent from `S`. Distinct lines through
`x` partition the common cells other than `x`. ∎

## 4. Rank-one line load or a disjoint secant-star bank

### Theorem CMR1009 -- PROVED

Fix an integer `R>=3`. For the entering cell supplied by CMR1008, at least one of
the following holds.

1. **Old target-line concentration.** Some line through `x` satisfies `r_L>=R`.
   The old state `S` then contains at least
   \[
   \boxed{\binom{R}{3}}
   \]
   collinear triples on that line.
2. **Cell-disjoint secant-star bank.** There are at least
   \[
   \boxed{
   s_x
   \ge
   \left\lceil
   \frac{d_x}{\binom{R-1}{2}}
   \right\rceil
   }
   \]
   distinct lines through `x`, each carrying a chosen pair of common cells. The
   chosen outside pairs are pairwise cell-disjoint, and together with `x` form
   `s_x` distinct secant-star arms.

### Proof

If the first branch fails, every line contributes at most
`\binom{R-1}{2}` to the sum in CMR1008. Hence at least the displayed number of
lines have positive contribution. Choose one pair from each. Two distinct lines
through `x` have no second common point, so the outside pairs are disjoint. In the
first branch, any three of the `R` common cells are selected in `S` and collinear. ∎

This is historical-free geometry inside one transition: all arms occur
simultaneously in `Q` and all outside cells occur in `S`.

## 5. Quantitative rank-one robust endpoint

### Corollary CMR1010 -- PROVED

If the rank-one branch of CMR1007 holds in a robust episode, then some entering
cell satisfies

\[
\boxed{
d_x
\ge
\left\lceil
\frac{\lceil(D+g)/2\rceil}{a}
\right\rceil.
}
\]

For every `R>=3`, this gives either the old target-line load
`\binom{R}{3}` or a cell-disjoint secant-star bank of size at least

\[
\boxed{
\left\lceil
\frac{
\left\lceil\lceil(D+g)/2\rceil/a\right\rceil
}{\binom{R-1}{2}}
\right\rceil.
}
\]

### Proof

Combine CMR1007--CMR1009. ∎

## 6. Higher-rank triples concentrate on one entering pair

Assume `H=N_2+N_3>0`, so `a>=2`. For every rank-two or rank-three new triple,
choose the first unordered pair of its entering physical cells in a fixed order.

### Theorem CMR1011 -- PROVED

Some entering physical pair `Z\subseteq A` supports at least

\[
\boxed{
t_Z
\ge
\left\lceil
\frac{H}{\binom a2}
\right\rceil
}
\]

distinct new triples.

All their third cells are distinct and lie on the unique real line `L_Z` through
`Z`. The state `Q` therefore contains at least `t_Z+2` selected physical cells on
`L_Z`, and

\[
\boxed{
\Phi(Q)\ge\binom{t_Z+2}{3}.
}
\]

If `t_Z>=1`, the line `L_Z` is nonaxis.

### Proof

There are at most `\binom a2` entering pairs. Average the canonical pair
assignments. A fixed pair determines its real line, and distinct triples have
distinct third cells. Hence `Q` contains the pair and all `t_Z` third cells on
that line, producing every three-cell subset as a collinear triple. A horizontal
or vertical line contains at most two cells of a saturated two-layer state—one
from each permutation layer—so a line containing at least three selected cells
is nonaxis. ∎

## 7. Gap control for the entering-pair branch

### Theorem CMR1012 -- PROVED

If `S` has minimum value `m` and `\Phi(Q)=m+g`, then every entering-pair
multiplicity satisfies

\[
\boxed{
\binom{t_Z+2}{3}\le m+g.
}
\]

Consequently, for every integer `T>=1`, if

\[
m+g<\binom{T+2}{3},
\]

then no entering pair supports `T` higher-rank new triples and

\[
\boxed{
H\le(T-1)\binom a2.
}
\]

### Proof

The first inequality is CMR1011 and `\Phi(Q)=m+g`. If every pair has
multiplicity at most `T-1`, sum over the at most `\binom a2` pairs. ∎

Thus a diffuse higher-rank branch has an explicit quadratic entering-pair bound,
while a concentrated branch forces cubic line energy in the bank state.

## 8. Entry-rank endpoint

### Corollary CMR1013 -- PROVED

Every minimum-robust target-surplus episode reaches at least one of:

1. an old target line with explicit load `\binom{R}{3}`;
2. a cell-disjoint secant-star bank through one entering cell;
3. one entering pair supporting many new triples on one nonaxis line;
4. the explicit high-rank bound of CMR1012;
5. one recurrent exact edge/triple/pair signature from CMR998--CMR1005;
6. selected-state churn, matching-preserving deletion, essential contraction,
   protected-line/reserve payment, factor descent, envelope expansion, or strict
   potential improvement.

The rank-one branch now feeds directly into the secant-star and protected-line
machinery. The higher-rank branch produces a fixed compatible joint pair and an
exact line-load certificate rather than an anonymous surplus count.

### Proof

Combine CMR1006--CMR1012 with the robust-surplus and augmented-signature
endpoints CMR990--CMR1005. ∎

No all-`n` theorem is claimed. Entry-rank partition, line-clique decomposition,
secant-star extraction, entering-pair concentration, line energy, and gap bounds
are checked in
[`scripts/verify_prime_power_robust_surplus_entry_rank.py`](../scripts/verify_prime_power_robust_surplus_entry_rank.py).
