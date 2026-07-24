# A linear reserve of lower-height parent lines

CMR233 gives an exact parent permutation avoiding the candidate-only top-height
slice.  Its matching-space local-load proof has enough slack to forbid a linear
number of previously discovered real-line matchings at the same time.  This
turns one-step height descent into an iterative lower-height signature reserve.

Fix an odd parent block of size `t`, put

\[
H_t=\left\lceil\frac{49t}{100}ight\rceil,
\qquad
q_t=\left\lfloor\frac t{100}ight\rfloor,
\]

and let `E(L)` denote the non-diagonal parent-board cells on a nonaxis real line
`L`.

## 1. Exact cleaning with a forbidden-line reserve

### Theorem CMR237 — PROVED

Assume

\[
\boxed{t\ge175.}
\]

Let `L_1,...,L_q` be distinct nonaxis real lines, where

\[
0\le q\le q_t,
\]

and let

\[
D\subseteq\bigcup_{i=1}^q E(L_i).
\]

There is a parent permutation which

1. avoids every old diagonal cell;
2. avoids every cell of `D`;
3. contains no compatible candidate-only board triple of primitive height at
   least `H_t`;
4. preserves saturation and inherited layer disjointness.

### Proof

Apply the matching-space local lemma CMR219 on the complete parent matching
board.  Use the following canonical bad events.

- Every old diagonal cell is a singleton event.
- Every cell of `D` is a singleton event.
- Every candidate-only triple of primitive height at least `H_t` is a rank-three
  event.

A real line cuts the board in a partial matching.  Hence each source row or
target column is incident with at most one cell from each `E(L_i)`.  The total
singleton load at every board vertex is therefore at most

\[
\frac{1+q}{t}
\le
\frac1t+rac1{100}.
\]

CMR231 bounds the rank-three top-slice load by

\[
\frac{2\left((t^2-1)/4-(49t/100)(49t/100-1)\right)}{(t-1)(t-2)}.
\]

Thus the complete local load is at most

\[
\frac1t+rac1{100}
+
\frac{2\left((t^2-1)/4-(49t/100)(49t/100-1)\right)}{(t-1)(t-2)}.
\]

This is below `1/24` precisely when

\[
178t^3-31125t^2+53450t-30000>0.
\]

The cubic is increasing and positive for every `t>=175`.  CMR219 therefore
supplies a perfect matching avoiding all displayed bad events.  The inherited
opposite-layer row fibre is disjoint, so the resulting parent permutation
preserves layer disjointness. ∎

## 2. Iterated lower-height extraction

### Theorem CMR238 — PROVED

Let an inherited parent block of odd size `t>=175` lie in a globally minimal
positive-potential saturated state.  At least one of the following holds.

1. Some parent state is covered by a rank-one or rank-two certificate, yielding
   an executable anchored alternating continuation by CMR201.
2. There are
   
   \[
   q_t+1
   \]
   
   distinct candidate-only real-line signatures
   
   \[
   L_1,\ldots,L_{q_t+1}
   \]
   
   all having primitive height strictly below `H_t`, and one parent permutation
   avoids every candidate cell on
   
   \[
   L_1,\ldots,L_{q_t}.
   \]

### Proof

Start with no forbidden line.  Apply CMR237.  The resulting parent permutation
moves the designated old target endpoint, so global minimality forces at least
one new triple touching the replacement block.

If a covering certificate has rank one or two, the first alternative holds.
Otherwise it is a candidate-only rank-three certificate.  CMR237 excludes the
top slice, so its real line `L_1` has primitive height below `H_t`.

Add all cells of `E(L_1)` to the forbidden set and apply CMR237 again.  Continue
inductively.  At stage `j<=q_t`, the forbidden set is contained in `j` distinct
line matchings, so CMR237 remains applicable.  Every newly obtained
candidate-only certificate uses a new line because no cell of any earlier line
is available, and its height is below `H_t`.

After the first `q_t` lines have been forbidden, one final application produces
a parent permutation avoiding all of them.  Its required covering certificate
is either anchored or supplies the distinct lower-height line `L_{q_t+1}`. ∎

### Corollary CMR239 — PROVED

For every large inherited odd parent, a frozen candidate-only obstruction cannot
be concentrated entirely in the top primitive-height slice.  It contains a
linear reserve of at least

\[
\left\lfloor\frac t{100}ight\rfloor+1
\]

distinct lines below height `0.49t`, unless an anchored alternating continuation
has already appeared.

The conclusion is exact and uses complete parent permutations, not
almost-perfect matchings.

## 3. Revised height endpoint

The current exact height decomposition is now:

- the candidate-only slice above `0.49t` is exactly cleanable;
- while cleaning it, a linear family of previously discovered lines may also be
  forbidden;
- hence every anchored-free frozen parent exposes linearly many distinct
  candidate-only signatures below `0.49t`.

The next target is to repeat the argument on an intermediate-height band.  The
available tools are the bounded-conflict almost-perfect matching CMR226, the
half-plus-`t^{1/5}` line resilience CMR236, and a reserve or switching completion
which keeps the already extracted lower-height lines forbidden.

No all-`n` theorem is claimed here.  The cubic threshold and the linear reserve
arithmetic are checked in
[`scripts/verify_prime_power_linear_height_reserve.py`](../scripts/verify_prime_power_linear_height_reserve.py).
