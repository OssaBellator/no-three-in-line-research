# Exact first-generation destruction coefficients

PX235--PX239 separate old-certificate deletion from prospective-recreation
suppression.  This chapter evaluates the old-deletion term for the three
first-generation decoder outcomes used by PX189--PX190: clean stars, loaded
lines, and radial cores.

The clean-star and radial guarantees are linear in the moved block order.  A
loaded line is substantially stronger: its old line shadow is cubic in the line
occupancy and can dominate any genuinely linear creation ledger.

## 1. Endpoint-disjoint old stars

Let the current state contain distinct old triples

\[
\{z,P_j,Q_j\},
\qquad 1\le j\le s,
\]

where the pairs `P_j,Q_j` are endpoint-disjoint.  Suppose the moved matching
block contains one chosen endpoint from every pair and every chosen endpoint is
forced off its current cell.

### Theorem PX240 -- PROVED

Every allowed rematching destroys all `s` designated star triples.  Therefore
its old block shadow satisfies

\[
\boxed{D_A\ge s.}
\]

### Proof

Every designated old triple contains its chosen moved endpoint.  The exact
current cell of that endpoint is forbidden, so the old three-point set is absent
from every replacement state.  Endpoint-disjointness makes the `s` designated
triples distinct.  Apply PX235. \(\square\)

This theorem concerns an **old** star.  For the prospective star produced after
a fixed rectangle switch, the corresponding `s` units belong instead to the
cancellation term `Gamma_A(W)` of PX236--PX237.

## 2. Exact loaded-line deletion

Let a real line `L` contain exactly `ell` current selected points.  Let `A` be a
subset of `s` of those points, all of whose current cells are forbidden in the
replacement bank.

### Theorem PX241 -- PROVED

The number of old certificates on `L` destroyed by every allowed rematching is
exactly

\[
\boxed{
D_L(\ell,s)
=
\binom{\ell}{3}-\binom{\ell-s}{3}.
}
\]

Consequently

\[
\boxed{
D_A\ge D_L(\ell,s)
\ge
s\binom{\ell-s}{2}.
}
\]

### Proof

The old line supports `binom(ell,3)` three-point certificates.  Exactly
`ell-s` old points of `L` remain outside the moved block, so exactly
`binom(ell-s,3)` old line triples avoid `A` and survive the deleting step.
Every other old line triple meets `A` and is destroyed by PX235.

The lower bound counts only destroyed triples containing exactly one moved
point and two unmoved line points. \(\square\)

Replacement points may create new triples on the same line.  Those are new
certificates and belong to the positive creation ledger; they do not change the
exact old-shadow count.

## 3. Movable loaded-line subblocks

Assume the selected state is decomposed into two permutation layers and lies in
`q` channels.  Label each selected point by its layer and channel, giving at
most `2q` types.

### Theorem PX242 -- PROVED

A loaded line containing `ell` selected points contains a movable row-column
matching block of one fixed layer and channel of order

\[
\boxed{
s\ge\left\lceil\frac{\ell}{2q}\right\rceil.
}
\]

Moving this block destroys at least

\[
\boxed{
\binom{\ell}{3}
-
\binom{\ell-\lceil\ell/(2q)\rceil}{3}
}
\]

old line certificates.

For `ell>=8`, one has the convenient lower bounds

\[
\boxed{
D_L(\ell,s)
\ge
\frac{s\ell^2}{32}
\ge
\frac{\ell^3}{64q}.
}
\]

### Proof

Some layer-channel type occurs at least `ceil(ell/(2q))` times.  Points in one
permutation layer occupy distinct rows and columns, so they form a movable
matching block.  PX241 gives the exact deletion count.

Since `s<=ell/2+1` is not needed, use instead the selected block size
`s=ceil(ell/(2q))` when applying the lower bound; moving additional points only
increases deletion.  For `q>=1`,

\[
\ell-s
\ge
\frac\ell2-1.
\]

When `ell>=8`,

\[
\binom{\ell-s}{2}
\ge
\frac{\ell^2}{32}.
\]

Now apply `D_L>=s binom(ell-s,2)` and `s>=ell/(2q)`. \(\square\)

Thus a genuinely loaded line carries a cubic old-defect reservoir, not merely
one unit per moved endpoint.

## 4. Radial cores

Let `A={a_1,...,a_s}` be a movable endpoint block.  Suppose there are distinct
old triples

\[
R_j=\{a_j,u_j,v_j\},
\qquad 1\le j\le s,
\]

assigned injectively to the moved endpoints.  This includes the radial-core
situation of PX190, where every retained endpoint lies on an old radial triple.

### Theorem PX243 -- PROVED

Every allowed rematching destroys all assigned radial certificates, and hence

\[
\boxed{D_A\ge s.}
\]

More generally, if moved endpoint `a_j` is assigned `rho_j` old certificates
and the assigned certificate families are disjoint, then

\[
\boxed{D_A\ge\sum_{j=1}^s\rho_j.}
\]

### Proof

Every assigned old certificate contains a current cell of `A`, which is
forbidden in every replacement.  Distinct assigned certificates therefore lie
in the exact old shadow counted by PX235. \(\square\)

## 5. First-generation sign theorem

Let `B_s` denote the complete expected positive ledger after deterministic
insertions and prospective exclusions:

\[
B_s
=
F_W
+
\mathcal C(s,\Delta)
\sum_{r=1}^3\frac{W_r^{\rm ext}}{(s)_r}.
\]

### Corollary PX244 -- PROVED

A first-generation decoder state strictly improves whenever one of the following
holds.

1. **Old clean star or radial core:** `B_s<s`.
2. **Loaded line:**
   
   \[
   \boxed{
   B_s
   <
   \binom{\ell}{3}-\binom{\ell-s}{3}.
   }
   \]
3. **Layer-channel loaded line with `ell>=8`:** it is sufficient that
   
   \[
   \boxed{
   B_s<\frac{s\ell^2}{32}.
   }
   \]

If the non-line creation ledger has the linear form `B_s<=b s`, then every
loaded-line outcome with

\[
\boxed{\ell>\sqrt{32b}}
\]

strictly improves.

### Proof

Insert the destruction bounds PX240--PX243 into the unified sign criterion
PX239.  The final statement follows from `D_L>=s ell^2/32`. \(\square\)

The last criterion is the first strict-sign statement in the recursive
rematching program which does not require a large linear destruction
coefficient: sufficiently loaded lines beat every fixed linear creation
constant automatically.

## 6. Updated frontier

The exact destruction ledger is now complete for all first-generation outcomes.

- old clean stars and radial cores supply linear deletion;
- prospective stars and radial lines supply cancellation credit through PX237;
- loaded lines supply cubic deletion in their occupancy;
- packet-selected blocks use PX235 for old deletion and PX238 for recurrence
  suppression.

The remaining sign problem is concentrated in the genuinely linear cases:
clean stars, radial cores, and small loaded lines.  There one must improve the
external linear coefficient or prove that a failed sign inequality extracts a
larger loaded line or another higher-credit batch.

## 7. Verification

Run

```bash
python scripts/verify_product_first_generation_destruction.py
```

The verifier checks the exact loaded-line formula, the layer-channel extraction
bound, the cubic lower envelope, and the clean-star/radial injection counts.
