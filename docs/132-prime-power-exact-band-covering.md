# Exact target-specific completion for one intermediate-height band

CMR226 uses the conflict-free matching theorem of
Glock–Joos–Kim–Kühn–Lichev to obtain an almost-perfect matching avoiding one
dyadic direction band. The covering theorem of Joos–Mubayi–Smith upgrades this
to an exact parent permutation after duplicating the row set into main and
reserve copies.

The external theorem used here is:

- F. Joos, D. Mubayi, and Z. Smith,
  [*Conflict-free hypergraph matchings and coverings*](https://doi.org/10.1017/S0963548325100291),
  Combinatorics, Probability and Computing 35 (2026), 230–254;
  preprint [arXiv:2407.18144](https://arxiv.org/abs/2407.18144).

Its mixed-bounded form allows conflicts containing exactly one reserve edge,
which is essential for the duplicated-row model.

Fix a normalized inherited parent board of size `t`, one designated old
endpoint

\[
z_*=(x_*,y_*),
\]

and one dyadic primitive-height band

\[
H\le\max\{|u|,|v|\}<2H.
\]

Let `P` be the source columns and let `Q,R` be disjoint main and reserve copies
of the row set. Main edge `(x,q_y)` and reserve edge `(x,r_y)` both represent
the cell `(x,y)`. Remove both copies of `z_*`.

Let

\[
\mathcal H_1\subseteq P\times Q,
\qquad
\mathcal H_2\subseteq P\times R
\]

be the resulting hosts. Let `\mathcal C` contain the compatible band triples
using three main edges. Let `\mathcal D` contain:

1. every main/reserve pair representing the same original row;
2. every compatible band triple using at least one reserve edge.

## 1. Decoding

### Theorem CMR372 — PROVED

Every `P`-perfect matching in

\[
\mathcal H_1\cup\mathcal H_2
\]

which avoids `\mathcal C\cup\mathcal D` decodes to a target-specific parent
permutation containing no candidate-only triple from the chosen band.

### Proof

A `P`-perfect matching chooses one represented cell in each source column.
Matching inside `Q` and inside `R` prevents row repetition within either copy.
The size-two conflicts prevent one original row from being used in both copies.
Hence the `t` represented rows are distinct and form a permutation. Both target
copies were deleted. Main-only band triples lie in `\mathcal C`, and every
other copy pattern lies in `\mathcal D`. ∎

## 2. Host conditions

### Theorem CMR373 — PROVED

For every fixed `0<\epsilon<1`, the hosts satisfy conditions (H1)–(H4) of the
Joos–Mubayi–Smith theorem with base degree `d=t`, for all sufficiently large
`t`.

### Proof

Every source and row-copy vertex has degree `t`, except vertices incident with
the removed target copies, whose relevant degree is `t-1`. Thus

\[
\delta_P(\mathcal H_1)=t-1,
\quad
\Delta(\mathcal H_1)=t,
\quad
\Delta_2(\mathcal H_1)\le1,
\]

and

\[
\delta_P(\mathcal H_2)=t-1,
\quad
\Delta_R(\mathcal H_2)=t,
\quad
d_{\mathcal H_2}(x,r_y)\le1.
\]

For large `t`, these imply

\[
(1-t^{-\epsilon})t\le t-1,
\qquad
1\le t^{1-\epsilon},
\]

\[
t\le t^{\epsilon^4}(t-1),
\qquad
1\le t^{-\epsilon}(t-1),
\]

which are (H1)–(H4). ∎

## 3. Main-only conflicts

### Theorem CMR374 — PROVED

Fix `\eta>0` and assume

\[
H\ge t^\eta.
\]

Choose a sufficiently small fixed `\epsilon`, below both `\eta/2` and the
constant permitted by the covering theorem for structural parameters
`(1,1,1,3)`. Then `\mathcal C` is `(t,3,\epsilon)`-bounded for all sufficiently
large `t`.

### Proof

Every conflict has size three. CMR223 gives maximum conflict degree below
`3t^2`, which is (C2) for `\ell=3,d=t`. CMR224 gives pair codegree below

\[
\frac{t}{H}\le t^{1-\eta}\le t^{1-\epsilon},
\]

which is (C3). Conditions concerning size-two main conflicts are vacuous. ∎

## 4. Mixed conflicts

### Theorem CMR375 — PROVED

Under the assumptions of CMR374, `\mathcal D` is

\[
(t,3,\epsilon,\epsilon^4)
\]

mixed-bounded in the sense of the Joos–Mubayi–Smith covering theorem, for all
sufficiently large `t`.

### Proof

Every mixed conflict has size two or three and contains at least one reserve
edge, giving (E1). A conflict with `j_2` reserve edges has unavoidability
`O(t^{-j_2})`, since every reserve source degree is at least `t-1`.

For conflicts containing one fixed reserve-side source vertex, the raw and
unavoidability-weighted counts are

\[
\begin{array}{c|c|c}
(j_1,j_2)&\text{raw}&\text{weighted}\\
\hline
(1,1)&O(t^2)&O(t)\\
(2,1)&O(t^3)&O(t^2)\\
(1,2)&O(t^3)&O(t)\\
(0,3)&O(t^3)&O(1).
\end{array}
\]

These give (E2). If main edges are additionally fixed, CMR224 gives

\[
\begin{array}{c|c|c}
(j_1,j_2,j')&\text{raw}&\text{weighted}\\
\hline
(2,1,1)&O(t^2/H)&O(t/H)\\
(2,1,2)&O(1)&O(1/t)\\
(1,2,1)&O(t^2/H)&O(1/H),
\end{array}
\]

while the row-copy type `(1,1,1)` has weighted count `O(1/t)`. These are (E3).
Fixing two reserve-side source vertices similarly gives

\[
\begin{array}{c|c|c}
(j_1,j_2)&\text{raw}&\text{weighted}\\
\hline
(1,2)&O(t^3/H)&O(t/H)\\
(0,3)&O(t^3/H)&O(1/H),
\end{array}
\]

which is (E4).

For conflicts with exactly one reserve edge, a fixed reserve edge lies in at
most `t` row-copy conflicts and fewer than `3t^2` geometric `(2,1)` conflicts,
proving (E5). Fixing one main and one reserve edge leaves fewer than
`t/H\le t^{1-\epsilon}` geometric completions, proving (E6). The positive power
slack follows from `\epsilon<\eta/2`. ∎

## 5. Exact completion of one band

### Theorem CMR376 — PROVED FROM JOOS–MUBAYI–SMITH

For every fixed `\eta>0`, every sufficiently large `t`, and every dyadic band
with

\[
H\ge t^\eta,
\]

there exists a complete target-specific parent permutation containing no
candidate-only collinear triple whose primitive direction lies in that band.

### Proof

Apply the mixed-bounded covering theorem with

\[
p_{\rm JMS}=q_{\rm JMS}=r_{\rm JMS}=1,
\qquad
\ell=3,
\qquad
d=t.
\]

CMR373 verifies the host conditions, CMR374 the main conflicts, and CMR375 the
mixed conflicts. The theorem supplies a `P`-perfect
`\mathcal C\cup\mathcal D`-free matching. Decode it by CMR372. ∎

### Corollary CMR377 — PROVED

CMR226's almost-perfect conclusion is upgraded to exact target-specific
completion for every fixed intermediate-height band `H\ge t^\eta`. The output
may use reserve-row copies internally, but decoding produces an ordinary parent
permutation.

## 6. Remaining band problem

This closes exact completion for **one** dyadic band. It does not yet avoid all
`O(\log t)` intermediate bands simultaneously: their per-cell conflict degrees
accumulate a logarithmic factor, while the covering theorem's (C2) hypothesis
allows only a fixed multiple of `t^2`. Nor does it stop a later repair for
another band from recreating a previously cleaned band.

The remaining intermediate-height task is therefore a band-scheduling or
no-return theorem, with interfaces to the protected-line reserve,
certificate-exchange ancestry, token reintroduction, and the coarse-to-fine
recreation ledger.

No all-`n` theorem is claimed here. Duplicated-row host degrees and finite mixed
conflict counts are checked in
[`scripts/verify_prime_power_exact_band_covering.py`](../scripts/verify_prime_power_exact_band_covering.py).
