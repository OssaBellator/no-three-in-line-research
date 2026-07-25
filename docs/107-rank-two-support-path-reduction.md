# Rank-two support paths and the unique superlinear sector

PX201--PX204 organize replacement collateral by matching rank and endpoint-index
support. For the difficult two-replacement/one-background term `T_2`, the three
possible support sizes are two, three, and four. PX203 identifies support two as
a transposition pair. This chapter classifies all three sectors exactly and
shows that support three is already at most linear after square-root thinning
whenever selected-line occupancy is bounded.

Use the notation

\[
e_{ij}=(x_i,y_j)
\]

from PX201 and forbid every diagonal cell `e_(ii)`. Regard a rank-two compatible
partial matching as a directed graph on endpoint indices: the cell `e_(ij)` is
the arc `i->j`. Compatibility says that every vertex has indegree and outdegree
at most one.

## 1. Exact directed-graph classification

### Theorem PX205 -- PROVED

Every diagonal-free compatible rank-two partial matching has exactly one of the
following forms.

1. **Support two:** one directed two-cycle

   \[
   \{e_{ij},e_{ji}\}.
   \]

2. **Support three:** one directed path of length two

   \[
   \{e_{ij},e_{jk}\}
   \]

   on distinct indices `i,j,k`, up to renaming the path direction.

3. **Support four:** two arcs whose source set and target set are disjoint. On a
   fixed four-element support, choose two source vertices, take the complementary
   two vertices as targets, and choose one of the two bijections between them.

Consequently the exact numbers of possible patterns on `t` endpoint indices are

\[
\boxed{N_{2,2}=\binom t2,}
\]

\[
\boxed{N_{2,3}=t(t-1)(t-2),}
\]

and

\[
\boxed{N_{2,4}=12\binom t4
=\frac{t(t-1)(t-2)(t-3)}2.}
\]

### Proof

The support-two statement is PX203.

Suppose the support has size three. The two source indices are distinct and the
two target indices are distinct. Since their union has size three, their
intersection has size one. The common index cannot be a source twice or a target
twice, so it is the target of one arc and the source of the other. The arcs form
a directed path. Conversely every directed path of length two is compatible and
uses three indices. Its middle vertex and ordered endpoints determine it, giving
`t(t-1)(t-2)` paths.

Suppose the support has size four. Two source indices and two target indices have
union size four, so the sets are disjoint. On a fixed support, choose the source
set in `binom(4,2)=6` ways and then choose one of the two bijections to the target
set. This gives twelve patterns. \(\square\)

## 2. Weighted anchor bounds

As in PX203a, weight a compatible pair by the number of background anchors that
complete its two candidate cells to a collinear triple. Let `L_Z` be the maximum
number of background anchors on any candidate secant line, and let `W_(2,u)` be
the total weight in support sector `u`.

### Theorem PX206 -- PROVED

The three weighted sectors satisfy

\[
\boxed{W_{2,2}\le L_Z\binom t2,}
\]

\[
\boxed{W_{2,3}\le L_Zt(t-1)(t-2),}
\]

and

\[
\boxed{W_{2,4}\le12L_Z\binom t4.}
\]

Assume `t>=1024`, choose the square-root-thinned set from PX201, and suppose its
order `s` satisfies `s>=8Delta`. Under the uniform allowed matching measure, the
three expected `T_2` contributions obey

\[
\boxed{
\mathbb E T_{2,2}
\le128e^{4\Delta}L_Z,
}
\]

\[
\boxed{
\mathbb E T_{2,3}
\le256e^{4\Delta}L_Z\sqrt t
\le512e^{4\Delta}L_Zs,
}
\]

and

\[
\boxed{
\mathbb E T_{2,4}
\le128e^{4\Delta}L_Zt.
}
\]

### Proof

Every candidate pair lies on one scalar line and therefore has weight at most
`L_Z`. Multiply the exact pattern counts from PX205 by this weight bound.

PX203a gives

\[
\mathbb E T_{2,u}
\le
256e^{4\Delta}
\frac{W_{2,u}}{t^{1+u/2}}.
\]

For `u=2`, substitute `W_(2,2)<=L_Z binom(t,2)`.

For `u=3`, substitute the directed-path count and use

\[
\frac{t(t-1)(t-2)}{t^{5/2}}
\le\sqrt t.
\]

PX201 gives `s>=sqrt(t)/2`, yielding the second displayed comparison.

For `u=4`, use

\[
12\binom t4
=\frac{t(t-1)(t-2)(t-3)}2
\le\frac{t^4}{2}.
\]

Substitution gives the final bound. \(\square\)

The constants are not sufficient for strict descent, especially because the
spread constant `e^(4Delta)` is deliberately crude. The theorem is nevertheless
an asymptotic separation:

- support two is bounded independently of block order;
- support three is at most linear in the thinned order;
- support four alone can remain of order `t=s^2`.

## 3. Updated rank-two frontier

A depth-two mass theorem no longer needs a new estimate for support three merely
to remove a superlinear obstruction. The directed-path sector is already on the
same linear scale as the guaranteed destroyed mass.

The unique potentially superlinear rank-two sector consists of two disjoint
source-to-target arcs on four endpoint indices. Equivalently, the next decoder
only has to control weighted background collisions between candidate cells whose
row-index set and column-index set are disjoint.

A useful next theorem can therefore take either form.

1. **Support-four counting:** prove `W_(2,4)=O(t^3)` after the PX195 extraction and
   bounded-line alternative.
2. **Support-four decoder:** show that `W_(2,4)>>t^3` forces a common anchor pencil,
   a large endpoint-disjoint star, or another executable bounded-support batch.
3. **Constant improvement:** sharpen the bounded-forbidden spread constant on the
   actual union-of-few-matchings graphs enough that the linear support-three term
   is paid by the destroyed mass.

The first two are structural; the third is quantitative. None is proved here.

## 4. Verification

Run

```bash
python scripts/verify_product_rank_two_support.py
```

The verifier exhausts rank-two compatible partial matchings through order ten,
checks the directed-cycle/path/disjoint-arc classification and exact sector
counts, and verifies the square-root expectation scales used in PX206.
