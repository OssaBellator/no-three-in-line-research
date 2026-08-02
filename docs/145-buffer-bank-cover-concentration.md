# Buffer-bank cover concentration and exact child sectors

PX346--PX350 give a quadratic terminal buffer bank.  If no bank state improves,
every valid buffer pair must create at least one external triple.  Because an
external triple uses at most two inserted cells, its occurrence depends on one
or two buffer variables.  A simple cylinder cover then forces either linearly
many one-buffer obstructions or quadratically many two-buffer obstructions.

The dependency patterns are exact.  They are not new terminal extreme rays:
they are coordinate rank-one fields, support-three directed paths, generic
rank-one candidate fields, or mixed rank-two shadows already decoded earlier.

## 1. One- and two-variable blocker cover

Let `Omega` be either buffer bank from PX347.  Assume every state in `Omega`
is nonimproving.  Since every state destroys at least one designated old
certificate and has no internal support-three creation, every state contains at
least one external created triple.

Let:

- `A` be the first-buffer labels `a` supporting at least one external blocker
  whose inserted cells depend only on `a`;
- `B` be the analogous second-buffer labels `b`;
- `P` be the ordered pairs `(a,b)` supporting a blocker whose occurrence
  depends on both buffer variables.

### Theorem PX351 -- PROVED

The valid bank is covered by

\[
\boxed{
\Omega
\subseteq
(A\times[n])
\cup
([n]\times B)
\cup
P.
}
\]

Consequently

\[
\boxed{
|\Omega|
\le
n|A|+n|B|+|P|.
}
\]

Under the `|Omega|>=n^2/4` hypothesis of PX347, at least one of

\[
\boxed{
|A|\ge\frac n{16},
\qquad
|B|\ge\frac n{16},
\qquad
|P|\ge\frac{n^2}{8}
}
\]

holds.

### Proof

Choose one external created triple from every nonimproving bank state.  PX349
classifies it by whether its inserted-cell occurrence determines one or both
buffer variables.  A one-variable blocker places the state in the
corresponding cylinder; a two-variable blocker places its exact pair in `P`.
The cardinality bound follows.  If the first two alternatives fail, their
cylinders cover fewer than `n^2/8` pairs, so `P` must contain at least
`n^2/8` pairs. \(\square\)

The constants are deliberately slack and independent of the exact valid-bank
shape.

## 2. Exact dependency types for a one-core cycle

For

\[
u\to a\to b\to u,
\]

write

\[
U_a=(x_u,y_a),\qquad
M_{a,b}=(x_a,y_b),\qquad
V_b=(x_b,y_u).
\]

### Theorem PX352 -- PROVED

Every external blocker has one of the following dependency types.

1. `a` only: one inserted cell `U_a` and two fixed points.
2. `b` only: one inserted cell `V_b` and two fixed points.
3. `(a,b)`: either the rank-one cell `M_(a,b)`, or one of the three inserted
   pairs
   \[
   \{U_a,M_{a,b}\},\quad
   \{M_{a,b},V_b\},\quad
   \{U_a,V_b\}
   \]
   together with one fixed point.

There are no other types.

### Proof

The three inserted cells have dependency sets `{a}`, `{a,b}`, and `{b}`.
An external triple contains one or two inserted cells.  Take unions of the
corresponding dependency sets. \(\square\)

Thus linear one-variable concentration is a coordinate family of positive
rank-one spoke cells, while quadratic two-variable concentration is either a
generic rank-one field on the buffer grid or one of three mixed rank-two
shadows.

## 3. Exact dependency types for a two-core cycle

For

\[
u\to a\to v\to b\to u,
\]

write

\[
U_a=(x_u,y_a),\quad A_v=(x_a,y_v),
\qquad
V_b=(x_v,y_b),\quad B_u=(x_b,y_u).
\]

### Theorem PX353 -- PROVED

Every external blocker has one of the following types.

1. `a` only:
   - rank one at `U_a` or `A_v`; or
   - the support-three directed-path pair `{U_a,A_v}` with one fixed point.
2. `b` only: the symmetric three types.
3. `(a,b)`: one of the four cross pairs obtained by choosing one `a`-cell and
   one `b`-cell, together with one fixed point.

There is no two-variable rank-one cell in the two-core bank.

### Proof

The inserted dependency sets are `{a},{a},{b},{b}`.  A one-cell external
triple is rank one.  A two-cell triple depends on one variable exactly when
both cells lie on the same side; otherwise it depends on `(a,b)`.  The
same-side pair is the directed path `u to a to v` or `v to b to u`.
\(\square\)

## 4. Quantitative child extraction

### Theorem PX354 -- PROVED REDUCTION

If the first alternative of PX351 holds, then one of at most three exact
one-buffer types occurs on at least `n/48` first-buffer labels.  The outcome is
either:

1. a coordinate row/column family of at least `n/48` positive rank-one
   candidate cells; or
2. a support-three directed-path family of at least `n/48` positive weighted
   pairs.

The same conclusion holds for the second-buffer alternative.

If the two-buffer alternative holds, one of at most four exact dependency
types occurs on at least `n^2/32` buffer pairs.  The outcome is either:

1. a generic rank-one candidate-cell field of quadratic size; or
2. a mixed rank-two shadow of quadratic size.

### Proof

Use PX352--PX353 and pigeonhole over the displayed finite type lists.  In the
one-core one-variable case there is only one type on each side, which is
stronger.  In the two-core case there are three types per side.  There are at
most four two-variable types in either bank. \(\square\)

### Corollary PX355 -- PROVED REDUCTION

Every nonimproving actual terminal buffer bank produces one of the already
established decoder inputs:

- a coordinate heavy-cell field for PX245--PX252;
- a rank-two support-three directed-path field for PX205--PX231;
- a generic rank-one field for the heavy-cell avoidance dichotomy;
- a mixed `(1,1)` rank-two shadow for PX253--PX259.

Therefore geometrically realizable terminal obstruction rays have been
replaced by four explicit growing child sectors.  The remaining frontier is
to attach the exact destruction credit of those decoders to the buffer-bank
cover, not to enumerate an abstract constant cone.

## 5. Verification

Run

```bash
python scripts/verify_product_buffer_cover_concentration.py
```

The verifier checks the cylinder-cover inequality at the sharp integer
thresholds, exhausts all one-/two-cell dependency unions in both buffer banks,
and verifies the `3`- and `4`-type pigeonhole constants.
