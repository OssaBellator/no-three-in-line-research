# Prime-minus-one alternating-star seed census

## Status

This note keeps AC as the sole active research track and proves AC5nk--AC5np. It exhausts one precisely defined seed family: two modular-hyperbola permutation layers, one legal two-row rectangle switch in one layer, one inserted candidate, and at least seven real secant pairs through that candidate in the other layer.

The census does not classify arbitrary AC seeds or arbitrary two-permutation configurations.

## Seed family

For an odd prime `p`, put `n=p-1` and

\[
H_c=\{(x,y)\in[1,n]^2:xy\equiv c\pmod p\}.
\]

Choose distinct channels `a,b`. A seed address consists of:

1. the anchor layer `H_a`;
2. the switch layer `H_b`;
3. two switch rows `x_1<x_2`;
4. one of the inserted rectangle cells as candidate `z`;
5. the complete real secant-pair set of `H_a` through `z`.

The switch is retained only when both inserted cells avoid `H_a`. Since one hyperbola contains no real collinear triple, the secant pairs through `z` are automatically endpoint-disjoint.

## AC5nk -- exact finite seed census -- PROVED

The complete census gives:

\[
\begin{array}{c|c|c}
p&\text{maximum secant pairs}&\text{seed addresses with at least seven pairs}\\\hline
11&4&0\\
13&4&0\\
17&5&0\\
19&7&56\\
23&7&144\\
29&8&600\\
31&8&216\\
37&10&2512.
\end{array}
\]

Thus `p=19` is the first tested prime for which this exact hyperbola-rectangle seed family reaches the `t>=7` alternating-star threshold.

This is a finite statement about the displayed primes and seed family. It does not assert a monotone formula in `p` or rule out different seeds on smaller boards.

## AC5nl -- complete two-layer bank guardrail -- PROVED

For every retained seed, a bank state contains:

- every unchanged point of both original hyperbola layers;
- the two inserted switch cells;
- the seven replacement anchor cells;
- none of the seven selected old anchor endpoints or two removed switch cells.

Every evaluated state therefore has exactly `2(p-1)` points. Omitting the unchanged part of the switched layer is not an approximation: it changes the physical configuration and is rejected by the cardinality and state-equality checks.

This guardrail is included because collateral values computed from only the replacement block can be drastically smaller than the true full-state potential.

## AC5nm -- canonical improving transfer seeds -- PROVED

Take the lexicographically first retained seven-pair seed and the lexicographically first endpoint from each pair. Exhaust the complete allowed matching bank.

The full-state results are:

\[
\begin{array}{c|c|c|c|c}
p&|\Omega(F)|&\Phi_{\rm current}&\min\Phi_{\rm bank}&\#\text{ improving states}\\\hline
19&1101&66&50&408\\
23&1300&80&54&1172\\
29&1289&120&113&26.
\end{array}
\]

Hence this canonical seed gives a strict physical improvement at each of `p=19,23,29`, although the improving proportion decreases sharply by `p=29`.

These are transfer examples, not a uniform theorem for all seeds or primes.

## AC5nn -- explicit nonimproving p=31 seed -- PROVED

At `p=31`, use

\[
H_1,\qquad H_2,
\]

switch the `H_2` cells

\[
(4,16),(16,4)\longrightarrow(4,4),(16,16),
\]

and take candidate `z=(16,16)`. The canonical seven secant pairs are

\[
\begin{aligned}
&(1,1)-(30,30),\quad (4,8)-(19,18),\quad (6,26)-(26,6),\\
&(8,4)-(18,19),\quad (10,28)-(14,20),\\
&(12,13)-(24,22),\quad (13,12)-(22,24).
\end{aligned}
\]

The exact forbidden-position bank has 1088 states. The current potential is 106, while the least bank potential is 108. Therefore

\[
\boxed{
\text{all 1088 legal alternating-star states are nonimproving.}
}
\]

This is a concrete physical AC1 input rather than a synthetic failure model.

## AC5no -- exact AC1 normalized rank at p=31 -- PROVED

Let `X` be the current state after removing the seven selected endpoints and the two switch cells, and let `Z` add the two inserted cells. The exact potentials are

\[
\Phi(S)=106,\qquad \Phi(X)=73,\qquad \Phi(Z)=88.
\]

Thus

\[
D_\star=33,\qquad F_\star=15,\qquad G=D_\star-F_\star=18.
\]

The occurrence-faithful bank certificate counts are

\[
T_1=179,\qquad T_2=112,\qquad T_3=20.
\]

Their normalized values are

\[
\frac{T_1}{7}=\frac{179}{7},\qquad
\frac{T_2}{(7)_2}=\frac{8}{3},\qquad
\frac{T_3}{(7)_3}=\frac{2}{21}.
\]

The unique heaviest normalized rank is rank one. In particular

\[
\frac{179}{7}>\frac{18}{384},
\]

so the concrete seed satisfies the AC1a heavy-rank conclusion with a large margin.

## AC5np -- explicit heavy-anchor concentration -- PROVED

Inside the rank-one family, the canonical anchor-block address `(5,6)` represents the physical cell

\[
\boxed{(12,12)}.
\]

It lies in exactly 20 rank-one certificate occurrences, more than any other anchor-block cell. Thus the p=31 nonimproving seed returns an explicit one-anchor concentration rather than an anonymous large `T_1` value.

The next arithmetic/geometric task is to classify those 20 exact lines through `(12,12)` as a paid star, quotient/carry pattern, bounded-denominator chamber or a precise AC1 obstruction.

## Deterministic audit

Run:

```text
python scripts/verify_ac_prime_seed_census.py
```

Expected ledger:

- tested primes: `11,13,17,19,23,29,31,37`;
- first tested seven-pair prime: `19`;
- seed counts at `19,23,29,31,37`: `56,144,600,216,2512`;
- canonical improving-state counts at `19,23,29,31`: `408,1172,26,0`;
- p=31 bank size: `1088`;
- p=31 current/best potential: `106/108`;
- p=31 certificate counts: `179,112,20`;
- p=31 heavy rank: `1`;
- p=31 heavy anchor: `(12,12)`, degree `20`.

## Remaining frontier

1. Classify the 20 exact p=31 heavy-anchor certificates by quotient, carry, denominator and current-payment labels.
2. Search the other 215 p=31 seven-pair seed addresses and all endpoint orientations for additional AC1 models.
3. Determine whether the improving-seed frequency admits a uniform lower bound or necessarily vanishes on some arithmetic classes.
4. Convert successful seeds into complete terminal paths, as already done for one p=19 seed.
5. Prove a uniform seed-existence and AC1/AC2 continuation theorem beyond the finite census.

AC6 and the general no-three-in-line conjecture remain open.
