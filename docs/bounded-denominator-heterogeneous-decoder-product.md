# Heterogeneous products of clean radial decoders

**Branch:** `research/bounded-denominator-absorbers`

BDA4e extracts row-column-compatible families of clean co-anchored adjacent radial pairs. BDA5a--BDA5e decode one pair, but the local blocker patterns may differ from pair to pair. This note shows that such heterogeneity causes no further compatibility loss: the local decoder envelopes are already separated by the BDA4e row/column condition.

## Decoder envelopes

For a clean radial pair \(R\), let \(E(R)\) be the union of:

- its five active cells;
- the four opposite-diagonal cross cells from its two rectangle roles; and
- every blocker-layer cell changed by the BDA5e fallback.

Every cell in \(E(R)\) uses a row and a column already used by the five-cell radial support of \(R\). Thus two radial pairs whose original supports use disjoint row and column sets also have row-column-disjoint decoder envelopes.

Let \(\Omega(R)\) be the nonempty menu of all local BDA5e decoder states:

- an empty-diagonal switch for each role with blocker count zero;
- a full-diagonal phase flip for each role with blocker count two;
- the size-two coupled derangement when both roles have blocker count one.

Each state in \(\Omega(R)\) preserves both permutation layers and destroys the two paid radial triples of \(R\).

## BDA5f — heterogeneous simultaneous decoder — PROVED

Let \(\mathcal F\) be a family of clean co-anchored adjacent radial pairs whose five-cell supports are pairwise disjoint in rows and columns. Choose an arbitrary state

\[
s_R\in\Omega(R)
\qquad(R\in\mathcal F).
\]

Then the union of the local states \(s_R\) is a valid two-layer state. It:

1. preserves every row and column in each permutation layer;
2. preserves inter-layer disjointness;
3. destroys both paid radial triples of every represented pair.

Consequently, every product choice

\[
\boxed{
\prod_{R\in\mathcal F}\Omega(R)
}
\]

is a valid global decoder bank. No decoder-type regularization or loss of paid weight is required.

### Proof

BDA5a and BDA5e prove the three assertions inside one decoder envelope. Every changed cell uses only rows and columns from that pair's original five-cell support. The BDA4e compatibility hypothesis makes those row and column sets disjoint for different pairs. Hence local changes cannot share a cell, row, or column across envelopes, and a blocker-layer replacement in one envelope cannot meet an active-layer cell in another. The union therefore preserves both matchings and their disjointness.

Every local state removes at least one role endpoint from each of the two paid radial triples, so every represented paid triple is destroyed. Since the local choices were arbitrary, the full Cartesian product is valid. \(\square\)

## BDA5g — exact heterogeneous product collateral — PROVED

Give every pair \(R\) a uniform independent choice from its menu \(\Omega(R)\). Let \(D\) be the total distinct paid weight destroyed by the family.

For a candidate collateral triple \(C\), let \(J(C)\subseteq\mathcal F\) be the set of decoder envelopes meeting its cells. Because the envelopes are cell-disjoint and \(C\) has three cells,

\[
\boxed{|J(C)|\le3.}
\]

Let \(m_C\) be the number of local state tuples on \(J(C)\) that create \(C\). Then its exact creation probability is

\[
\boxed{
\Pr(C\text{ is created})
=
\frac{m_C}
{\prod_{R\in J(C)}|\Omega(R)|}.
}
\]

Let \(F\) be collateral independent of all decoder choices, and for \(r=1,2,3\) put

\[
T_r
=
\sum_{\substack{C:\ |J(C)|=r}}
 w_C
 \frac{m_C}
 {\prod_{R\in J(C)}|\Omega(R)|}.
\]

If

\[
\boxed{
D>F+T_1+T_2+T_3,
}
\]

then one heterogeneous product state strictly lowers the paid triple potential.

### Proof

A collateral triple depends only on the local states in the envelopes meeting its cells. Under the uniform product measure, every tuple on \(J(C)\) has probability \(1/\prod_{R\in J(C)}|\Omega(R)|\), proving the exact probability formula. Linearity of expectation gives expected collateral \(F+T_1+T_2+T_3\), while BDA5f destroys paid weight \(D\) in every state. If the displayed inequality holds, some state has collateral below \(D\). \(\square\)

## Consequence for BDA6

BDA4e and BDA5f now compose without an intermediate occupancy classification:

\[
\text{bounded row/column load}
\Longrightarrow
\text{compatible clean radial family}
\Longrightarrow
\text{valid heterogeneous decoder product}.
\]

The remaining global work is therefore entirely in the named outputs:

- prove the BDA5g normalized collateral inequality;
- localize a failed inequality through BDA3c--BDA3e;
- handle clean-support failure and the affine anchor chains returned by BDA4e;
- break every recurrent finite-profile cycle.

Local blocker occupancy and variation of decoder type are no longer obstructions.

## Finite check

`scripts/verify_bda_heterogeneous_decoder.py` enumerates all nine blocker-count patterns on up to three row-column-disjoint radial envelopes. It checks every local menu, all heterogeneous product states, preservation of both partial matchings and inter-layer disjointness, destruction of the two paid triples, and the exact product-event probability formula.