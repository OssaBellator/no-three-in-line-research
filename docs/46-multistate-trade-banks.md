# Multistate equal-margin trade banks

The binary formulation in PP3be--PP3bg is exact, but it discards most of the
state space supplied by a sheared parabolic bank.  This chapter keeps an
arbitrary finite state set for every local variable.  It gives an exact
rank-at-most-three forbidden-box CSP, together with first-moment and
bounded-dependency local-lemma endpoints.

## 1. Equal-margin finite-state variables

Fix a set `F subseteq [n]^2`.  For each variable `i=1,...,r`, let `Omega_i` be a
nonempty finite state set and let

\[
 A_i^a\subseteq[n]^2\qquad(a\in\Omega_i).
\]

Assume:

1. `F` is disjoint from every variable support
   `U_i=union_{a in Omega_i} A_i^a`;
2. the supports `U_i` are pairwise disjoint;
3. all states of one variable have the same row-incidence vector and the same
   column-incidence vector.

For an assignment `alpha in product_i Omega_i`, put

\[
 T_\alpha=F\cup\bigcup_i A_i^{\alpha_i}.
\]

### Proposition PP3bh -- PROVED

If one assignment produces exactly two points in every row and column, then
every assignment does.

#### Proof

Changing one coordinate `alpha_i` replaces one local state by another with the
same row and column incidence vectors.  Therefore every row and column sum is
unchanged.  Connect any two assignments by changing one coordinate at a time.
∎

This includes a full sheared-rung family, a finite family of matching-reservoir
states, a grouped collection of rectangle orientations, or any finite
line-sum-preserving tomographic state family.

## 2. Exact forbidden boxes

For a candidate point `z in U_i`, define its selection set

\[
 \Sigma_i(z)=\{a\in\Omega_i:z\in A_i^a\}.
\]

Let `tau` be a collinear triple in `F union union_i U_i`.  For each variable
meeting `tau`, put

\[
 \Sigma_i(\tau)
 =
 \bigcap_{z\in\tau\cap U_i}\Sigma_i(z).
\]

If one intersection is empty, the triple can never be selected.  Otherwise the
triple is present exactly when

\[
 \alpha_i\in\Sigma_i(\tau)
\]

for every variable for which `Sigma_i(tau)` is a proper subset of `Omega_i`.
Variables with `Sigma_i(tau)=Omega_i` impose no restriction.  The resulting
Cartesian product of proper state subsets is the **bad box** of `tau`.  A
collinear triple that is selected independently of every variable gives the
empty bad box.

Duplicate bad boxes are identified.  Let `B` be the resulting family.

### Theorem PP3bi -- PROVED

The following are equivalent.

1. Some assignment `alpha` makes `T_alpha` no-three-in-line.
2. No empty bad box exists and some assignment avoids every box in `B`.

Every bad box involves at most three variables.

#### Proof

A triple with an empty local intersection is impossible.  For every other
triple, the definition of its bad box records exactly the state choices under
which all three points are selected.  Thus an assignment avoids all collinear
triples if and only if it avoids all bad boxes.  A triple has three points and
the variable supports are disjoint, so it can constrain at most three
variables. ∎

This is the finite-state analogue of PP3bf.  It is an exact CSP, not a
probabilistic relaxation.

## 3. Product-distribution first moment

Choose the local states independently from arbitrary probability measures
`mu_i` on `Omega_i`.  For a bad box `B`, let

\[
 p(B)=
 \prod_{(i,S)\in B}\mu_i(S).
\]

### Proposition PP3bj -- PROVED

If there is no empty bad box and

\[
 \boxed{\sum_{B\in\mathcal B}p(B)<1,}
\]

then a valid saturated no-three assignment exists.

#### Proof

Let `Z` count the bad boxes hit by the random assignment.  Linearity of
expectation gives

\[
 \mathbb E Z=\sum_{B\in\mathcal B}p(B)<1.
\]

Since `Z` is a nonnegative integer, some assignment has `Z=0`.  PP3bh gives
saturation and PP3bi gives the no-three property. ∎

The measures need not be uniform.  This permits weighting a sheared parameter
family toward matching-admissible or externally sparse states.

## 4. Bounded-dependency local lemma

Two bad-box events are independent when their variable sets are disjoint.  Let
`D` be the maximum degree of the bad-box dependency graph and let

\[
 p=\max_{B\in\mathcal B}p(B).
\]

### Theorem PP3bk -- PROVED FROM THE STANDARD LOCAL LEMMA

If there is no empty bad box and

\[
 \boxed{3p(D+1)\le1,}
\]

then a valid saturated no-three assignment exists.

#### Proof

The bad-box events live in a product probability space and the graph joining
events with a shared variable is a dependency graph.  The displayed inequality
implies

\[
 p\le\frac1{3(D+1)}<\frac1{e(D+1)}.
\]

The symmetric Lovasz local lemma therefore gives positive probability that no
bad-box event occurs.  Apply PP3bh and PP3bi. ∎

The constant `3` is used so the criterion can be checked with exact rational
arithmetic; replacing it by `e` gives the usual slightly sharper form.

### Corollary PP3bl -- PROVED

Suppose every variable occurs in at most `Delta` distinct bad boxes.  If
`Delta=0`, every assignment is valid.  Otherwise it is sufficient that

\[
 \boxed{3p(3\Delta-2)\le1.}
\]

#### Proof

A rank-at-most-three box shares a variable with at most
`3(Delta-1)` other boxes.  Hence `D+1<=3Delta-2`, and PP3bk applies. ∎

This is the first endpoint in the prime-patching track whose capacity improves
directly with the number of local states.  If every bad box fixes one state in
three `q`-state variables, then `p=q^{-3}` and the criterion permits variable
occurrence on the order of `q^3`.

## 5. Exact solver

The script

```bash
python scripts/solve_multistate_trade_bank.py \
  experiments/four-state-trade-bank-n4.json
```

validates equal margins and disjoint supports, constructs every exact bad box,
reports uniform first-moment and local-lemma quantities, solves the CSP by
domain propagation and backtracking, and independently checks the returned
grid with integer determinants.

The remaining asymptotic target is to populate the local state sets with a
positive-density family of matching-admissible sheared rungs and prove that the
resulting bad-box probabilities and variable occurrences pass PP3bj, PP3bk, or
PP3bl.