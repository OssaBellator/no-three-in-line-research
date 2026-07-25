# Terminal Hall cores and near-threshold matching deficiency

PX265 reduces every nested decoder branch to a terminal block whose order is
comparable with its accumulated forbidden degree. The sharp Hall threshold
PX200 guarantees a perfect matching at order `m>=2Delta`, but did not describe
what failure looks like below that threshold.

This chapter gives the exact obstruction. Every failure contains a complete
forbidden rectangle. Its two sides have size at most `Delta`, and the matching
deficiency is at most `2Delta-m`. At the sharp order `m=2Delta-1`, the only
possible obstruction is a saturated forbidden `K_(Delta,Delta)` core.

Let `F subseteq L times R`, where `|L|=|R|=m`, and assume every row and column
of `F` has degree at most `Delta`. Let

\[
G=K_{m,m}\setminus F
\]

be the allowed graph, let `nu(G)` be its maximum-matching order, and put

\[
\delta(G)=m-\nu(G).
\]

## 1. Exact Hall-rectangle localization

### Theorem PX270 -- PROVED

If `delta(G)>0`, then there are nonempty sets `S subseteq L` and `B subseteq R`
such that

\[
\boxed{S\times B\subseteq F}
\]

and

\[
\boxed{|S|+|B|=m+\delta(G).}
\]

Moreover,

\[
\boxed{|S|\le\Delta,
\qquad
|B|\le\Delta,}
\]

so

\[
\boxed{\delta(G)\le2\Delta-m.}
\]

Consequently

\[
\boxed{\nu(G)\ge 2m-2\Delta}
\]

whenever the right-hand side is positive.

### Proof

By the deficiency form of Hall's theorem, choose `S subseteq L` with

\[
|S|-|N_G(S)|=\delta(G).
\]

Put

\[
B=R\setminus N_G(S).
\]

No allowed edge joins `S` to `B`, so `S times B subseteq F`. Also

\[
|S|+|B|
=|S|+m-|N_G(S)|
=m+\delta(G).
\]

Because `S` and `B` are nonempty, every row of `S` contains all `|B|`
forbidden cells of its rectangle, giving `|B|<=Delta`; symmetrically
`|S|<=Delta`. The deficiency bound follows immediately, and
`nu(G)=m-delta(G)`. \(\square\)

This recovers PX200 when `m>=2Delta`: positive deficiency would force
`delta(G)<=0`.

## 2. Sharp-threshold classification

### Theorem PX271 -- PROVED

Assume

\[
\boxed{m=2\Delta-1.}
\]

Then `G` has no perfect matching if and only if there are sets

\[
S\subseteq L,
\qquad
B\subseteq R,
\qquad
|S|=|B|=\Delta,
\]

with

\[
\boxed{S\times B\subseteq F.}
\]

In that case every vertex of `S union B` has forbidden degree exactly `Delta`,
so the `K_(Delta,Delta)` core is saturated and has no forbidden edge incident
with `S` or `B` outside the core.

### Proof

If `G` has no perfect matching, PX270 gives

\[
1\le\delta(G)\le2\Delta-(2\Delta-1)=1.
\]

Thus `delta(G)=1` and

\[
|S|+|B|=m+1=2\Delta.
\]

Since each side has size at most `Delta`, both have size exactly `Delta`.
Every vertex in the complete forbidden rectangle already has forbidden degree
`Delta`, proving saturation.

Conversely, if such a rectangle exists, the `Delta` rows of `S` have allowed
neighbourhood contained in `R minus B`, which has order `Delta-1`. Hall's
condition fails. \(\square\)

Thus the extremal example in PX200 is not merely sharp; it is the unique
obstruction form at the sharp order.

## 3. Near-threshold compression

### Corollary PX272 -- PROVED

Write

\[
m=2\Delta-r,
\qquad r\ge1.
\]

Then every allowed graph has deficiency

\[
\boxed{\delta(G)\le r.}
\]

A maximum matching therefore covers at least

\[
\boxed{m-r}
\]

rows and the same number of columns. Equivalently, after deleting at most `r`
rows and at most `r` columns, one obtains an allowed balanced perfect matching.
Every failure certificate is supported by one complete forbidden rectangle
with at most `2Delta` incident row/column vertices.

### Proof

The deficiency estimate is PX270. Delete the unmatched rows and columns of a
maximum matching. The remaining matching is perfect between the retained row
and column sets. \(\square\)

The retained row and column sets need not correspond to the same endpoint-label
subset. Thus PX272 is an exact terminal matching skeleton, not yet a principal
row-column-preserving absorber. The remaining terminal problem is to convert
this compressed Hall core into an executable principal or coupled-block move.

## 4. Verification

Run

```bash
python scripts/verify_product_terminal_hall_core.py
```

The verifier exhausts all bipartite forbidden graphs through order four,
checks the deficiency form of Hall's theorem, verifies the complete-rectangle
localization, and confirms the sharp `K_(Delta,Delta)` classification.
