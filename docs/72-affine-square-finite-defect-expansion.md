# Finite-defect expansion from the affine-square design

PX100 needs many ways to remove a prescribed edge while keeping reverse
congestion bounded.  PX105 gives the exact first shell, and PX109 identifies
the only two-square overlapping moves.  This chapter records a more general
source-count lemma which applies to every mapping that agrees with one affine
root outside a controlled row set.

Let \(p\equiv1\pmod4\) be prime with \(p\ge13\), choose \(i^2=-1\), and let

\[
F(x)=ix+b.
\]

Let \(\mathcal B_i\) be the affine-square \(2-(p,4,3)\) design from PX104.
Suppose \(G\) is any strong complete mapping and put

\[
W=\{x:G(x)\ne F(x)\}.
\]

No assumption is made about how \(G\) was produced.

## Theorem PX110 -- PROVED

For every row \(x\notin W\), at least

\[
\boxed{
p-1-3|W|
}
\]

affine-square blocks \(B\in\mathcal B_i\) satisfy

\[
x\in B,
\qquad
B\cap W=\varnothing.
\]

Every such block is an available PX98 trade support at \(G\), and the trade
removes the current edge

\[
(x,G(x))=(x,F(x)).
\]

Consequently, whenever

\[
|W|\le\frac{(1-\varepsilon)p-1}{3},
\]

every unchanged edge has at least \(\varepsilon p\) one-step trade exits.

### Proof

PX104 gives exactly \(p-1\) affine squares through \(x\).  For a fixed
\(w\in W\), the pair \(\{x,w\}\) lies in exactly three design blocks.  Hence at
most

\[
3|W|
\]

blocks through \(x\) meet \(W\), by the union bound over \(w\).
The remaining blocks are disjoint from \(W\), proving the count.

On one such block \(B\), the maps \(G\) and \(F\) agree at all four rows.  The
root map \(F\) satisfies the PX98 identities on every affine-square support, so
the same four values make the trade available at \(G\).  Since \(x\in B\), its
image changes and the current edge is removed. \(\square\)

The lower bound is intentionally robust.  Different points of \(W\) may charge
the same forbidden block, so the actual number of exits can be larger.

## Corollary PX110a -- PROVED

The total number of affine-square blocks disjoint from \(W\) is at least

\[
\boxed{
\frac{p(p-1)}4-|W|(p-1)
=(p-1)\left(\frac p4-|W|\right).
}
\]

Thus a state differing from an affine root on \(o(p)\) rows retains
\((1-o(1))p^2/4\) commuting root-square trade supports.

### Proof

There are \(p(p-1)/4\) design blocks.  Each point of \(W\) lies in \(p-1\)
blocks, so at most \(|W|(p-1)\) blocks meet \(W\). \(\square\)

## 2. Shell and bridge applications

### First shell

For a one-trade descendant, \(|W|=4\).  PX110 gives at least

\[
p-13
\]

one-step exits removing every edge outside the original support.  This recovers
the source-scale statement after PX105b without using the exact shell degree.

### After one bridge

Start from two adjacent root squares and apply one PX108 bridge.  The resulting
mapping differs from the affine root on exactly nine rows.  Hence every edge
outside those nine rows has at least

\[
\boxed{p-28}
\]

available disjoint-root-square exits.

For \(p\ge37\), this is already a positive linear source family.  The only
remaining difficulty is routing edges on the nine-row nonlinear core.

## 3. Conditioned unchanged-edge exits

Fix a partial matching condition \(F_0\) of size at most two, suppose its rows
lie outside \(W\), and suppose \(F_0\subseteq\operatorname{graph}(G)\).  Because
\(G=F\) outside \(W\), every conditioned edge is the corresponding affine-root
edge.

Let \(x\notin W\) be another row whose affine-root edge is to be removed.  A
root-square trade through \(x\) preserves a conditioned edge unless its support
also contains that conditioned row.  By PX104, the pair consisting of \(x\) and
one conditioned row belongs to exactly three affine squares.  Therefore rank
\(|F_0|\) conditioning excludes at most \(3|F_0|\) further exits, and the source
count remains

\[
\boxed{
p-1-3|W|-3|F_0|.
}
\]

In particular, under rank-two conditioning it is at least

\[
\boxed{p-1-3|W|-6}.
\]

Whenever \(|W|=o(p)\), this is still \(\Omega(p)\), matching the source scale in
PX100.  The reverse-congestion analysis is separate: one target mapping can
have several root-square predecessors, and PX100 still requires a canonical
orientation or weighting which reduces that congestion to \(O(1)\).

## 4. Boundary of the lemma

PX101 proves that constant rank-three spread cannot remain in the regime
\(|W|=o(p)\): almost all affine rows eventually must be rewritten.  PX110 is
therefore not a complete mixing theorem.  Its role is to separate the problem
into two sectors.

1. **Affine exterior.** Every unchanged edge has the required linear supply of
   exact one-step exits for as long as the changed core is smaller than about
   \(p/3\).
2. **Nonlinear core.** Altered edges require bridge and higher-order switchings.
   PX109 gives the complete two-square mechanism; further expansion must grow
   the core while preventing reverse congestion.

A successful global flow can use the affine-square exterior as a reservoir and
concentrate its new argument on the evolving nonlinear core.

## 5. Verification

Run

```bash
python scripts/verify_product_affine_square_finite_defect.py
```

The verifier samples strong mappings obtained from disjoint root-square and
bridge batches at primes \(13,17,29,37\), checks every block counted by the
theorem is an available trade, and verifies the lower bounds for every row
outside the changed set.
