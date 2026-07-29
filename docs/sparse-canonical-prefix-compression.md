# Canonical prefix compression for sparse swap words

**Branch:** `research/sparse-algebraic-spread`

SAS5hq--SAS5ht close final structural legality for every finite swap word. When an execution contract also requires every intermediate state to be legal, the original word may be arbitrarily long. This note replaces it by a canonical short implementation of the same final image permutation.

## SAS5hu -- canonical cycle implementation -- PROVED

Let a finite swap word induce a permutation `alpha` on its moved-row support `R`, with `r=|R|`. Write the nontrivial cycle decomposition as

\[
\alpha=C_1\cdots C_s,
\qquad
C_j=(i_{j,1}\ i_{j,2}\ \cdots\ i_{j,\ell_j}).
\]

Each cycle has a transposition implementation of length `ell_j-1`. Concatenating these implementations gives the same final permutation using exactly

\[
\boxed{
L=\sum_j(\ell_j-1)=r-s\le r-1
}
\]

row swaps.

### Proof

A cycle of length `ell` is a product of `ell-1` transpositions sharing one pivot, for example

\[
(i_1\ i_\ell)(i_1\ i_{\ell-1})\cdots(i_1\ i_2)
\]

under the corresponding composition convention. Disjoint cycles commute. Summing the lengths gives `r-s`, and at least one nontrivial cycle gives `s>=1`. QED.

## SAS5hv -- bounded prefix-legality audit -- PROVED

Fix the canonical implementation from SAS5hu. If every intermediate state must be structurally legal, it is enough to inspect its `L<=r-1` noninitial prefix permutations. At each prefix, SAS5hr--SAS5hs require at most

\[
\boxed{2r}
\]

row-local structural tests, or `r` in one layer. Hence the complete two-layer prefix audit uses at most

\[
\boxed{2r(r-1)}
\]

atomic host/collision tests.

### Proof

Every prefix is itself a finite swap word on a subset of `R`, so SAS5hr--SAS5hs apply. There are `L` required noninitial prefixes and at most two tests per moved-support row. QED.

## SAS5hw -- word-length-free execution router -- PROVED

For any proposed finite sparse swap word with final permutation `alpha`, one of the following holds:

1. the canonical `r-s`-swap implementation is legal at every required prefix and reaches the same final state;
2. one least canonical prefix has one exact host-edge or opposite-layer collision atom;
3. the execution contract forbids replacing the original word by an equivalent implementation, and this noncommutation field is returned explicitly;
4. a nonstructural arithmetic, line, boundary, owner, payment or context guard fails.

Thus structural prefix complexity depends polynomially on moved support size and not on the length or recurrence of the original swap word.

### Proof

SAS5hu preserves the final image permutation. Apply the exact structural criterion to each canonical prefix and retain the least failure. If the physical contract distinguishes histories with the same current matching, that history dependence is not structural matching data and must be recorded as the declared noncommutation field. QED.

## Corrected SAS6 frontier

Matching-structural legality, including required intermediate states, now has an `O(r^2)` atomic audit after canonical compression. Remaining work is the nonstructural arithmetic-word, collinearity, boundary, owner, payment and context guards, and proof that selected physical contracts permit the canonical replacement or pay their history dependence.

## Finite check

`scripts/verify_sparse_canonical_prefix_compression.py` decomposes small permutations into pivot transpositions, reconstructs the final permutation, and verifies the `r-s` length and prefix-test bounds.