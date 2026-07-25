# Exact target-specific completion for one intermediate-height band

CMR226 applies the conflict-free matching theorem of Glock--Joos--Kim--Kühn--
Lichev to obtain an almost-perfect matching avoiding one dyadic direction band.
The covering theorem of Joos--Mubayi--Smith upgrades this to an exact parent
permutation after the row set is duplicated into a main copy and a reserve copy.
The only additional conflicts are row-copy collisions and geometric triples
using at least one reserve edge.

The external theorem used here is:

- F. Joos, D. Mubayi, and Z. Smith,
  [*Conflict-free hypergraph matchings and coverings*](https://doi.org/10.1017/S0963548325100291),
  Combinatorics, Probability and Computing 35 (2026), 230--254;
  preprint [arXiv:2407.18144](https://arxiv.org/abs/2407.18144).

Its more general mixed-bounded form allows conflicts containing exactly one
reserve edge.  This is essential for the duplicated-row model.

Fix a normalized inherited parent board of size `t` and one designated old
endpoint

\[
z_*=(x_*,y_*).
\]

Fix a dyadic primitive-height band

\[
H\le \max\{|u|,|v|\}<2H.
\]

Let `P` be the set of source columns.  Let `Q` and `R` be disjoint main and
reserve copies of the row set.  A main edge `(x,q_y)` and a reserve edge
`(x,r_y)` both represent the grid cell `(x,y)`.  Remove the two copies of
`z_*` from the hosts.

Let

\[
\mathcal H_1\subseteq P\times Q,
\qquad
\mathcal H_2\subseteq P\times R
\]

be the resulting complete bipartite graphs minus those target copies.

Define the main conflict system `mathcal C` to consist of all compatible
candidate-only collinear triples in the chosen band using three main edges.
Define the mixed conflict system `mathcal D` to contain:

1. every disjoint pair consisting of a main edge and a reserve edge representing
   the same original row;
2. every compatible collinear triple in the chosen band whose three edge copies
   include at least one reserve edge.

## 1. Decoding a conflict-free covering

### Theorem CMR355 — PROVED

Every `P`-perfect matching in

\[
\mathcal H_1\cup\mathcal H_2
\]

which avoids `mathcal C cup mathcal D` decodes to a target-specific parent
permutation containing no candidate-only collinear triple from the chosen
height band.

### Proof

A `P`-perfect matching chooses exactly one represented cell in every source
column.  Matching inside `Q` and inside `R` prevents repeated rows within one
copy.  The size-two row-copy conflicts prevent a row used in `Q` from also being
used in `R`.  Thus the `t` chosen edges represent `t` distinct original rows and
form a permutation.

Both copies of `z_*` were removed, so the designated endpoint is omitted.  A
band triple using only main edges belongs to `mathcal C`; every other copy pattern
belongs to `mathcal D`.  Hence no represented band triple survives. ∎

## 2. Host degree conditions

### Theorem CMR356 — PROVED

For every fixed `epsilon` with `0<epsilon<1`, the hosts `mathcal H_1,mathcal H_2`
satisfy conditions (H1)--(H4) of the Joos--Mubayi--Smith theorem with base
degree

\[
d=t
\]

for all sufficiently large `t`.

### Proof

Every source and row-copy vertex has degree `t`, except the four vertices
incident with the removed target copies, whose relevant degree is `t-1`.
Consequently

\[
\delta_P(\mathcal H_1)=t-1,
\qquad
\Delta(\mathcal H_1)=t,
\qquad
\Delta_2(\mathcal H_1)\le1.
\]

For sufficiently large `t`,

\[
(1-t^{-\epsilon})t\le t-1
\]

and `1<=t^(1-epsilon)`, proving (H1)--(H2).

Similarly

\[
\delta_P(\mathcal H_2)=t-1,
\qquad
\Delta_R(\mathcal H_2)=t,
\qquad
d_{\mathcal H_2}(x,r_y)\le1.
\]

Thus

\[
t\le t^{\epsilon^4}(t-1)
\]

and

\[
1\le t^{-\epsilon}(t-1)
\]

for all sufficiently large `t`, proving (H3)--(H4). ∎

## 3. Main-only band conflicts are bounded

### Theorem CMR357 — PROVED

Fix `eta>0` and assume

\[
H\ge t^\eta.
\]

Choose a sufficiently small fixed

\[
0<\epsilon<\eta/2.
\]

Then `mathcal C` is `(t,3,epsilon)`-bounded for all sufficiently large `t`.

### Proof

Every conflict has size three.  CMR223 gives maximum conflict degree below

\[
3t^2,
\]

which is condition (C2) with `ell=3` and `d=t`.  CMR224 gives pair codegree below

\[
\frac{t}{H}
\le
t^{1-\eta}
\le
t^{1-\epsilon}
\]

for sufficiently large `t`, which is (C3).  Conditions (C4)--(C5) concern
size-two conflicts and are vacuous.  Removing one edge and using only the main
copy can only reduce these degrees. ∎

## 4. Mixed conflicts are mixed-bounded

### Theorem CMR358 — PROVED

Under the assumptions of CMR357, `mathcal D` is

\[
(t,3,\epsilon,\epsilon^4)
\]

mixed-bounded in the sense of Section 4.3 of Joos--Mubayi--Smith, for all
sufficiently large `t`.

### Proof

Every conflict has size two or three and contains at least one reserve edge, so
(E1) holds.  Every reserve source degree is at least `t-1`; hence a conflict with
`j_2` reserve edges has unavoidability at most

\[
(t-1)^{-j_2}=O(t^{-j_2}).
\]

We record the required raw counts.  Constants are harmless because
`epsilon<eta/2` and the mixed-bounded inequalities have positive power slack.

For conflicts containing a fixed reserve-side source vertex `x`, the row-copy
and geometric types have the following counts:

\[
\begin{array}{c|c|c}
(j_1,j_2)&\text{raw count}&\text{unavoidability-weighted count}\\
\hline
(1,1)&O(t^2)&O(t)\\
(2,1)&O(t^3)&O(t^2)\\
(1,2)&O(t^3)&O(t)\\
(0,3)&O(t^3)&O(1).
\end{array}
\]

These prove (E2).

For (E3), fix `j'` main edges as well as the reserve source `x`.  The only
nonvacuous geometric estimates are obtained by summing CMR224 over the possible
reserve cell at `x`:

\[
\begin{array}{c|c|c}
(j_1,j_2,j')&\text{raw count}&\text{weighted count}\\
\hline
(2,1,1)&O(t^2/H)&O(t/H)\\
(2,1,2)&O(1)&O(1/t)\\
(1,2,1)&O(t^2/H)&O(1/H).
\end{array}
\]

The row-copy type `(1,1,1)` has weighted count `O(1/t)`.  Since
`H>=t^eta`, these satisfy the powers required by (E3).

For (E4), fix two reserve-side source vertices.  Summing the pair-codegree bound
over their row choices gives

\[
\begin{array}{c|c|c}
(j_1,j_2)&\text{raw count}&\text{weighted count}\\
\hline
(1,2)&O(t^3/H)&O(t/H)\\
(0,3)&O(t^3/H)&O(1/H),
\end{array}
\]

which satisfy (E4).

It remains to check conflicts with exactly one reserve edge.  For a fixed
reserve edge, at most `t` main edges form a row-copy conflict, proving (E5) for
`(1,1)`.  CMR223 gives fewer than `3t^2` geometric `(2,1)` conflicts through a
fixed reserve edge, proving (E5) there.  Finally, fixing one main edge and one
reserve edge leaves fewer than `t/H<=t^(1-epsilon)` geometric completions by
CMR224, which is (E6). ∎

## 5. Exact completion of one dyadic band

### Theorem CMR359 — PROVED FROM JOOS--MUBAYI--SMITH

For every fixed `eta>0`, every sufficiently large `t`, and every dyadic band
with

\[
H\ge t^\eta,
\]

there exists a complete target-specific parent permutation which contains no
candidate-only collinear triple whose primitive direction lies in that band.

### Proof

Apply the mixed-bounded form of the Joos--Mubayi--Smith covering theorem with
structural parameters

\[
p_{\rm JMS}=q_{\rm JMS}=r_{\rm JMS}=1,
\qquad
\ell=3,
\qquad
d=t.
\]

The size condition is automatic for large `t`.  CMR356 verifies the host
conditions, CMR357 verifies the main conflict conditions, and CMR358 verifies
the mixed conflict conditions.  The theorem supplies a `P`-perfect
`mathcal C cup mathcal D`-free matching.  Decode it using CMR355. ∎

### Corollary CMR360 — PROVED

CMR226's almost-perfect conclusion is upgraded to exact target-specific
completion for every fixed intermediate-height band

\[
H\ge t^\eta.
\]

The output may use a vanishing fraction of reserve-row copies internally, but
after row-copy decoding it is an ordinary parent permutation.

## 6. Remaining band problem

This theorem closes exact completion for **one** dyadic band.  It does not yet
avoid all `O(log t)` intermediate bands simultaneously: the per-cell conflict
degree accumulates a logarithmic factor, while condition (C2) permits only a
fixed multiple of `t^2`.  Nor does it prevent a later repair for another band
from recreating a previously cleaned band.

The remaining intermediate-height task is therefore a band scheduling or
no-return theorem, not an exact-completion theorem for one band.  The natural
interfaces are the protected-line reserve, certificate-exchange ancestry, and
the coarse-to-fine recreation ledger.

No all-`n` theorem is claimed here.  The duplicated-row host degrees and finite
mixed-conflict counts are checked in
[`scripts/verify_prime_power_exact_band_covering.py`](../scripts/verify_prime_power_exact_band_covering.py).
