# A recursive-compatible bank for binary stars

The full prefix rematching bank CMR75 is powerful but leaves the original
recursive reciprocal parameter space. Binary stars can also be neutralized by a
smaller bank that changes only one nonroot reciprocal node map and therefore
preserves the recursive algebraic form.

Assume

\[
p\equiv1\pmod4,
\qquad p\ge5,
\]

and use the corrected balanced recursive class from CMR67. Fix a nonroot
layer-prefix node `(s,a,ell)` with `s>=1`. Its current child-digit map is

\[
F_{b,c}(\xi)=b+c\tau(\xi),
\]

where `c` is a nonsquare and `tau` is completed inversion.

Fix two distinct child digits `xi_1,xi_2`, and let

\[
\eta_i=F_{b,c}(\xi_i).
\]

Define

\[
\Omega(\xi_1,\xi_2)
=
\{F_{b',c'}\in\mathcal B_p:
F_{b',c'}(\xi_i)\ne\eta_i\text{ for }i=1,2\}.
\]

## 1. Exact state count and cylinder law

### Theorem CMR96 — PROVED

\[
|\Omega(\xi_1,\xi_2)|
=
h(p-2)+1,
\qquad h=(p-1)/2.
\]

For a uniform state from this family:

1. a prescribed output at one child digit has probability at most
   \[
   \frac{h}{h(p-2)+1}<\frac1{p-2};
   \]
2. compatible prescribed outputs at two or more distinct child digits have
   probability at most
   \[
   \frac1{h(p-2)+1}.
   \]

### Proof

For one forbidden cell `(xi_i,eta_i)`, each nonsquare `c'` determines exactly
one shift

\[
b'=\eta_i-c'\tau(\xi_i),
\]

so exactly `h` maps contain that cell. The two forbidden-cell families intersect
in exactly one map: two distinct input-output prescriptions determine `(b',c')`,
and the current map is that solution. Inclusion-exclusion gives

\[
ph-(2h-1)=h(p-2)+1.
\]

A new one-cell prescription is contained in at most `h` maps. Two prescriptions
at distinct inputs determine at most one map, and additional prescriptions
cannot increase the count. Divide by the family size. ∎

## 2. Executability inside the recursive state

Write every column in the node as

\[
x=a+p^s\xi+p^{s+1}q.
\]

Its current row has a unique form

\[
y=P_{\ell,s}(a)+p^sF_{b,c}(\xi)+p^{s+1}H_x.
\]

For `F'` in the bank, replace it by

\[
y'=P_{\ell,s}(a)+p^sF'(\xi)+p^{s+1}H_x.
\]

### Theorem CMR97 — PROVED

Every state in `Omega(xi_1,xi_2)`:

1. preserves both row and column counts;
2. remains disjoint from the opposite layer;
3. changes every point whose child digit is `xi_1` or `xi_2`;
4. remains a valid recursive balanced-reciprocal state with only one node
   parameter changed.

### Proof

For each fixed child digit, the unchanged descendant maps biject its columns to
all rows with the prescribed lower row prefix and child row digit. Since `F'` is
a permutation of the `p` child digits, the new child row fibres remain disjoint
and cover the identical parent row fibre. Thus the changed layer remains a
permutation.

Because `s>=1`, the two layer row prefixes `P_{0,s}(a)` and `P_{1,s}(a)` are
already distinct modulo `p^s`. Changing the next row digit cannot create an
opposite-layer collision.

The two forbidden outputs ensure that every column in the targeted child
subblocks receives a different row digit. All local and descendant maps still
belong to the recursive construction. ∎

The restriction `s>=1` is automatic for a binary p-adic cluster, because its
maximum pair valuation is strictly larger than its minimum pair valuation.

## 3. Extracting a heavy child-pair star

For one layer-prefix block, partition its assigned binary-star triples by the
unordered pair of child digits occupied by their closest endpoints.

### Theorem CMR98 — PROVED

Some child-digit pair carries at least

\[
\frac{B_{s,a,\ell}}{\binom p2}
\]

assigned old triples. Every state in the corresponding CMR96 bank destroys all
of those triples.

Combining with CMR77, some recursive-compatible node bank at scale `s` destroys
at least

\[
\frac{B_s}{2p^s\binom p2}
=
\frac{B_s}{p^{s+1}(p-1)}
\]

old binary-star certificates in every state.

### Proof

The closest endpoints have exact column-difference valuation `s`, so their
child digits are distinct. There are `binom(p,2)` possible unordered pairs.
Averaging gives the first bound.

CMR97 changes every point in both selected child subblocks, so neither old
closest endpoint cell remains. Hence every old triple assigned to that pair is
absent. The global bound follows from the heavy-block extraction CMR77. ∎

## 4. Rank by distinct child digits

Remove the old full node block `A` and put `Z=S\setminus A`. For a prospective
triple using cells from a replacement node state, define its **node rank** to be
the number of distinct child input digits among its replacement cells.
Let `U_r` count compatible real-collinear certificates of node rank `r`, with
the remaining points in `Z`.

### Theorem CMR99 — PROVED

For a uniform recursive-compatible node state,

\[
\mathbb E\bigl[\Phi(S_{F'})-\Phi(Z)\bigr]
\le
\frac{h}{h(p-2)+1}U_1
+
\frac{U_2+U_3}{h(p-2)+1}.
\]

Consequently some node state improves the total triple potential whenever

\[
D(A)
>
\frac{h}{h(p-2)+1}U_1
+
\frac{U_2+U_3}{h(p-2)+1},
\]

where `D(A)=Phi(S)-Phi(Z)`.

### Proof

A node-rank-one prescription fixes one output of the local map and occurs in at
most `h` allowed states. Any prescription using at least two distinct child
inputs determines the local map uniquely and occurs in at most one state.
Apply CMR96 and sum certificate probabilities.

The potential identity

\[
\Phi(S_{F'})-\Phi(S)
=
-D(A)+\bigl(\Phi(S_{F'})-\Phi(Z)\bigr)
\]

then gives the improvement criterion. ∎

This bank can be iterated indefinitely without leaving the recursive reciprocal
class. Its only weak collateral class is `U_1`, consisting of certificates
confined to one child subblock. Those are precisely finer-scale objects. Thus a
lexicographic or reverse-scale potential may charge `U_1` downward, while all
cross-child collateral already receives the natural quadratic parameter-space
spread.

The exact parameter and saturation checks are in
[`scripts/verify_prime_power_recursive_compatible_bank.py`](../scripts/verify_prime_power_recursive_compatible_bank.py).
