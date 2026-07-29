# Structural admissibility of arbitrary finite matching-swap words

**Branch:** `research/sparse-algebraic-spread`

SAS5hi--SAS5hp give exact host and opposite-layer tests for one swap, disjoint two-swap squares and two swaps sharing one row.  Any finite word of row transpositions acts only by permuting the current matched columns on its moved-row support.  This note records the resulting complete structural criterion.

Let `pi` be a perfect matching from rows to columns in a bipartite host `G`.  Let a finite word of row swaps have moved-row support `R`.  Its induced permutation of the original images is the unique permutation

\[
\alpha:R\longrightarrow R
\]

such that the final first-layer matching satisfies

\[
\pi'(i)=\pi(\alpha(i))\qquad(i\in R),
\]

while `pi'(i)=pi(i)` outside `R`.  Delete fixed points of `alpha` from `R`, so every retained row changes image.

## SAS5hq -- arbitrary swap words are exact image permutations -- PROVED

The final map `pi'` is a bijection on the column set.  Its restriction to `R` uses exactly the original column set `pi(R)`, with no repetitions, and no column outside `pi(R)` changes owner.

### Proof

Each row swap composes the current row-to-image assignment with a transposition on the row indices.  A finite product of transpositions is a permutation `alpha`.  Permuting the distinct images `pi(R)` preserves their multiplicities and leaves every image outside the support unchanged. QED.

## SAS5hr -- exact one-layer word criterion -- PROVED

The final state `pi'` is a perfect matching of `G` if and only if

\[
\boxed{
(i,\pi(\alpha(i)))\in E(G)
\qquad(i\in R).
}
\]

Thus a moved support of size `r` has exactly `r` potentially new host tests.  Intermediate word states need separate checks only when the execution contract requires them to be legal; final-state legality depends solely on `alpha`.

### Proof

SAS5hq gives bijectivity.  Outside `R` all edges are original host edges.  On `R`, the displayed edges are exactly the final edges, so their host membership is necessary and sufficient. QED.

## SAS5hs -- exact two-layer word criterion -- PROVED

Let `(pi,rho)` be two edge-disjoint perfect matchings of the same host, and change only `pi`.  The final state `(pi',rho)` is structurally legal if and only if

\[
\boxed{
(i,\pi(\alpha(i)))\in E(G),
\qquad
\pi(\alpha(i))\ne\rho(i)
\quad(i\in R).
}
\]

No other host or duplicate-cell condition can change.

### Proof

The host part is SAS5hr.  Rows outside `R` are unchanged and already layer-disjoint.  At a moved row `i`, the new first-layer cell coincides with the second layer exactly when the displayed equality holds. QED.

## SAS5ht -- complete structural obstruction alphabet -- PROVED

Fix the ordered moved-row support, the induced permutation `alpha`, the original images `pi(R)` and, in two layers, `rho(R)`.  Order the following tests lexicographically by row and test type:

1. missing final host edge `(i,pi(alpha(i)))`;
2. opposite-layer collision `pi(alpha(i))=rho(i)`.

The least failed test is a complete exact structural obstruction address.  The alphabet has at most `2|R|` atoms, or `|R|` in one layer.

Consequently every finite sparse swap word has one continuation:

1. all final structural tests pass;
2. one exact host/collision atom is returned;
3. an intermediate-state legality requirement fails at one separately addressed prefix;
4. or a nonstructural arithmetic, line, boundary, owner, payment or context guard fails.

### Proof

SAS5hr--SAS5hs are necessary and sufficient.  Ordering their finite conjunction gives the least witness.  Prefix legality is the same theorem applied to each required prefix permutation. QED.

## Corrected SAS6 legality frontier

Underlying matching structure is now closed for every finite swap word, including arbitrary overlaps.  Remaining legality work is exclusively prefix requirements and nonstructural arithmetic-word, collinearity, boundary, payment, owner and context guards.

## Finite check

`scripts/verify_sparse_arbitrary_swap_words.py` enumerates small permutations and transposition words, verifies the induced image permutation, checks the exact one- and two-layer structural criteria, and confirms the `2|R|` atomic obstruction bound.
