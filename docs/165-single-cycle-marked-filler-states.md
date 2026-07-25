# Single-cycle marked filler states

The marked filler arguments PP3xp--PP3yw assume a fixed-rank spread state law on
the selected endpoint block. A canonical law is available without preparing a
separate matching distribution: choose one uniformly random directed Hamilton
cycle on the selected endpoint indices and use its successor map as the endpoint
permutation.

This law moves every endpoint. It also forbids every proper directed cycle in the
permutation, so diagonal cells, transpositions, and directed triangles disappear
identically. Its fixed-rank cylinder probabilities are exact. Consequently the
marked filler source theorem may use a universal single-cycle law, and the
rank-one unary and rank-two binary `Xi` terms are removed before any paid
estimate.

## 1. The single-cycle state family

Let `I` be a set of `b>=4` tied endpoint indices. A **single-cycle state** is a
permutation `pi` of `I` whose cycle decomposition consists of one cycle of length
`b`.

There are

```text
(b-1)!
```

single-cycle states.

### Proposition PP3yx -- PROVED

Every single-cycle state:

1. moves every endpoint index;
2. contains no diagonal arc `i->i`;
3. contains no transposition `i->j, j->i`;
4. contains no directed cycle on a proper subset of `I`.

#### Proof

The cycle decomposition has exactly one cycle, and that cycle uses all `b`
indices. Every cycle of length less than `b`, including lengths one, two, and
three, is absent. ∎

Thus the complete selected endpoint set contributes its available removal credit,
while the lowest-support cyclic insertion patterns are deterministically zero.

## 2. Exact fixed-rank cylinder probabilities

Let `F` be a prescribed compatible set of `r` directed arcs on `I`, meaning that
no two arcs have the same tail or the same head.

### Theorem PP3yy -- PROVED

Assume `0<=r<=b-1`.

1. If `F` contains a directed cycle on a proper subset of `I`, then no
   single-cycle state contains `F`.
2. Otherwise the arcs of `F` form a disjoint union of directed paths and

   ```text
   Pr(F subseteq pi)=1/(b-1)_r,
   ```

   for a uniform single-cycle state `pi`, where

   ```text
   (b-1)_r=(b-1)(b-2)...(b-r).
   ```

In particular, for every fixed `r<=3` and all sufficiently large `b`,

```text
Pr(F subseteq pi) <= (2/b)^r.
```

#### Proof

A proper directed cycle would be a separate cycle in the cycle decomposition and
is therefore impossible.

Otherwise contract every directed path component of `F` to one ordered block.
Each prescribed arc reduces the number of cyclic objects by one, leaving `b-r`
objects. The number of directed cyclic orders of those objects is

```text
(b-r-1)!.
```

Dividing by the total `(b-1)!` single-cycle states gives

```text
(b-r-1)!/(b-1)!=1/(b-1)_r.
```

For fixed `r<=3`, every factor in `(b-1)_r` is at least `b/2` for large `b`. ∎

This is the required fixed-rank spread law with an absolute constant, obtained by
exact counting rather than regularity or a local-lemma distribution theorem.

## 3. Deterministic removal of low-support source classes

Represent an endpoint cell by the directed arc `i->j`, as in PP3iz.

### Corollary PP3yz -- PROVED

Under the single-cycle law:

1. every support-rank-one unary diagonal event has probability zero;
2. every support-rank-two compatible pair event has probability zero, because it
   is a transposition;
3. every support-rank-three compatible triple event has probability zero, because
   it is a directed triangle;
4. a support-rank-three anchored transition remains a directed two-step path and
   has probability

   ```text
   1/((b-1)(b-2)).
   ```

#### Proof

Apply PP3iz and PP3yx--PP3yy. ∎

Thus the only nonunary low-support source class that needs dilution is the
anchored transition class already treated by PP3xw--PP3ya.

## 4. Universal marked source-valid state

Use the slab-optimal pool scales

```text
N=m^(19/20+o(1)),
H=m^(19/40+o(1)),
b=m^(kappa+o(1)),
0<kappa<19/80.
```

Fix a credited endpoint `c`, choose the other `b-1` indices uniformly from the
full pool, and then choose a uniform single-cycle state on the selected block.

### Theorem PP3za -- PROVED

Suppose `c` is simultaneously light for the marked high-support and transition
loads of PP3xt and PP3xz, and suppose its unary data satisfy

```text
d_U(c)=o(N),
theta b=o(1),
```

where `theta` is the full-pool support-rank-two unary density. Then the expected
total number of source-invalid events in the marked single-cycle state is `o(1)`.
Consequently some single-cycle state:

1. moves every selected endpoint, including `c`;
2. is pool-compatible and preserves saturation and the candidate universe;
3. contains no source-invalid pattern.

No separately prepared fixed-rank spread host is required.

#### Proof

The exact cylinder bounds PP3yy are of the same orders used in PP3xq, PP3xx, and
PP3yd, so all their marked and unmarked estimates remain valid after changing the
absolute spread constant. The high-support and transition expectations are
`o(1)` by the hypotheses and PP3xt--PP3xz. The unary expectation is

```text
O(d_U(c)/N+theta b)=o(1)
```

by PP3yd. Diagonal, transposition, and directed-triangle terms are exactly zero by
PP3yz. Add the nonnegative source-invalid counts and average over the block and
single-cycle choices. Since the expectation tends to zero, one state has no
source-invalid event. Pool compatibility and candidate-universe preservation are
PP3tg. ∎

Combined with PP3yf--PP3yi, a large credited resource bank therefore has an exact
source alternative: a source-valid single-cycle marked filler through a credited
endpoint, or an `Omega(H)` unary-forbidden resource matching.

## 5. Reduced dynamic-Xi paid expression

Use the support-ranked `Xi` weights of PP3yj. A rank-one unary `Xi` pattern is a
diagonal arc, while a rank-two binary `Xi` pattern is the transposition on two tied
indices.

### Proposition PP3zb -- PROVED

For every single-cycle state,

```text
A_1 contribution = 0,
B_2 contribution = 0.
```

For a marked endpoint `c`, the remaining marked paid loads are bounded, up to one
absolute constant, by

```text
M_A^cyc(c)=D_A,2(c)/N,
```

and

```text
M_B^cyc(c)=D_B,3(c)/N^2 + D_B,4(c)b/N^3.
```

The remaining unmarked terms are

```text
U_A^cyc=A_2 b/N^2,
```

and

```text
U_B^cyc=B_3 b/N^3 + B_4 b^2/N^4.
```

#### Proof

The first statement is PP3yx and the corrected classifications PP3ys--PP3yt.
For the remaining support ranks, repeat PP3yk with the exact one-edge and two-edge
cylinder probabilities from PP3yy. ∎

The formulas remove the two support ranks that are most resistant to thinning.

## 6. Paid single-cycle completion

Let `R_c>0` be the exact removal credit obtained by moving the marked endpoint.

### Theorem PP3zc -- PROVED

Under the source hypotheses of PP3za, a source-valid strict dynamic improvement
exists whenever

```text
M_A^cyc(c)+M_B^cyc(c)+U_A^cyc+U_B^cyc < R_c-o(R_c),
```

after restoring the fixed cylinder constants.

For a credited resource bank of size `H`, if

```text
A_2/N + B_3/N^2 + B_4 b/N^3 = o(H)
```

and

```text
A_2 b/N^2 + B_3 b/N^3 + B_4 b^2/N^4 = o(1),
```

then all but `o(H)` source-light credited endpoints support a strict
pool-compatible decrease of `Xi`.

#### Proof

The first statement combines PP3za and PP3zb in one first-moment objective and
uses the exact dynamic identity PP3kx.

For the bank statement, weighted support-incidence double counting gives total
marked load

```text
O(A_2/N+B_3/N^2+B_4 b/N^3).
```

The displayed hypothesis makes this `o(H)`. Markov's inequality leaves only
`o(H)` endpoints with nonvanishing marked load, while the second display controls
the unmarked cost. Intersect with the `H-o(H)` source-light endpoints and apply
the first statement. ∎

## 7. Revised captive-centre certificate

### Corollary PP3zd -- PROVED

When a captive centre is tested with single-cycle filler states, alternatives 7
and 9 of PP3yr are impossible:

```text
D_A,1(c) large,
D_B,2(c) large.
```

A failed centre therefore carries one of only nine remaining explicit cores:

1. unary source degree;
2. anchored transition degree;
3. rank-four anchored-pair degree;
4. rank-four inserted-triple degree;
5. rank-five inserted-triple degree;
6. rank-six inserted-triple degree;
7. rank-two unary `Xi` weight;
8. rank-three binary `Xi` weight;
9. rank-four binary `Xi` weight.

#### Proof

The two omitted classes have zero probability in every single-cycle state by
PP3zb. Apply the finite large-term argument PP3yr to the reduced paid expression.
∎

Thus rank-one local state cost and rank-two transposition cost are no longer
frontiers in the marked filler branch.

## 8. Revised marked-filler endpoint

The large resource-bank branch now has the following exact split.

1. A unary-light credited endpoint admits a universal source-valid single-cycle
   filler state.
2. Unary failure yields an `Omega(H)` resource-disjoint unary matching.
3. Diffuse support-ranked `Xi` weight excluding `A_1` and `B_2` yields a strict
   dynamic decrease.
4. A fixed captive centre that still fails carries one of the nine support cores
   in PP3zd.

The prepared-spread-host hypothesis, rank-one unary `Xi` core, and rank-two binary
transposition core are no longer separate marked-filler obstructions.
