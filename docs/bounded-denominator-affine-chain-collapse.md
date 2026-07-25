# Fixed-cell collapse of the five affine anchor chains

**Branch:** `research/bounded-denominator-absorbers`

BDA4e returns a high-load row or column together with one of five exact support roles. The branch map currently treats this as a one-dimensional affine anchor chain and leaves a second coordinate concentration open. In the actual two-layer union, however, every row and every column contains exactly two current cells. After the five-role split, one of those two cells carries a fixed fraction of the incident paid record weight. Fixing that role cell determines both anchor coordinates and collapses the chain to one radial line.

## Setup

Retain the BDA4e radial-pair support

$$
\mathcal R_h(P)
=
\{P,\ P+hu\,d,\ P+hv\,d,\ P+(h+q)u\,d,\ P+(h+q)v\,d\},
$$

where

$$
d=(a,b),
$$

and every displayed support cell is current in the two-layer union. Give the records nonnegative paid weights.

For a heavy row or column, BDA4e chooses one of the five roles

$$
0,\quad (0,u),\quad(0,v),\quad(1,u),\quad(1,v).
$$

The root role `0` is the anchor `P`. A role `(s,w)` is the support cell

$$
P+(h+s q)w\,d.
$$

## BDA5ap -- exact current-cell localization of high coordinate load -- PROVED

Let a row or column have incident paid record weight `H`. One of the five roles carries weight at least `H/5`. Inside that role class, one exact current cell carries weight at least

$$
\boxed{
\frac{H}{10}.
}
$$

In the unweighted form, if the coordinate has load `L`, one exact current cell and one role occur in at least

$$
\boxed{
\left\lceil\frac{L}{10}\right\rceil
}
$$

records.

### Proof

The five role classes partition the incident records, giving the `1/5` role bound. A row of the union contains one cell from each permutation layer, and the layers are disjoint, so it contains exactly two current cells. The same is true for a column. The selected role cell of every record lies at the heavy coordinate and therefore is one of those two cells. Weighted or unweighted pigeonhole gives the extra factor two. QED.

## BDA5aq -- fixed-cell radial-chain identity -- PROVED

Fix the exact current cell `Q` and selected role from BDA5ap.

1. For the root role,
   $$
   \boxed{P(h)=Q.}
   $$
2. For a role `(s,w)`,
   $$
   \boxed{
   P(h)=Q-(h+s q)w\,d.
   }
   $$

Consequently every support cell of every retained record lies on the one fixed real line

$$
\boxed{
\ell_Q=Q+\mathbb R d.
}
$$

More precisely, a support role `(t,z)` equals

$$
\boxed{
Q+\bigl((h+tq)z-(h+s q)w\bigr)d
}
$$

in the nonroot case, while the root support is obtained by taking `z=0`.

### Proof

The selected role cell equals `Q`. Solving `Q=P+(h+s q)w d` gives the anchor identity. Substituting it into every other support role gives the displayed scalar multiple of `d` from `Q`. The root case is immediate. QED.

## BDA5ar -- affine-chain terminal router -- PROVED

Every BDA4e high-row or high-column output of incident weight `H` returns one exact fixed-cell radial profile of weight at least

$$
\boxed{
H/10.
}
$$

The profile records:

- one current cell `Q`;
- one of the five support roles;
- the primitive radial direction `d`;
- the exact denominator, residue, scale class and blocker/decoder decorations;
- the anchor law from BDA5aq;
- and a family of current co-anchored pair records whose complete supports lie on `ell_Q`.

Thus the five affine anchor chains do not require a second independent row/column concentration. They terminate as one of:

1. a fixed-anchor profile `P=Q`;
2. a translated radial chain `P(h)=Q-(h+s q)w d` through one fixed current role cell.

The remaining interface is payment and recurrence for the resulting fixed-cell radial fan, not determination of the second anchor coordinate.

### Proof

Apply BDA5ap and then BDA5aq. All arithmetic and decoder labels were fixed before BDA4e and survive the two finite pigeonhole steps. QED.

## Consequence

The branch frontier phrase “terminate the five affine anchor chains” is now narrowed. High coordinate load always produces a fixed current cell and one exact radial line at loss `1/10`. On the alternating-core branch this is a same-cell current-incidence fan suitable for the AC3g/AC3k reuse routers or for direct pivot aggregation once factor-conservative payment is verified.

## Finite check

`scripts/verify_bda_affine_chain_collapse.py` checks the ten-bucket weighted and unweighted pigeonholes, every root/nonroot anchor identity, and every support-role collinearity with the fixed cell and radial direction.