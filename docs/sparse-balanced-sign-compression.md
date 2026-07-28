# Sparse balanced sign compression

This note records SAS5jg--SAS5jk. It combines coordinatewise bipartite cancellation into an exact boundary-compression criterion.

## Contract

For every exact boundary coordinate `j`, retain all positive and negative unit occurrences and the complete allowed-pair graph. Let `P_j` and `N_j` be the two unit counts, `m_j` the maximum matching size, and `delta_j = min(P_j,N_j)-m_j` the matching deficiency.

## Theorem block

### SAS5jg — exact residual formula

After maximum allowed pairing, the unpaired variation at coordinate `j` is

`R_j = P_j + N_j - 2m_j = |P_j-N_j| + 2 delta_j`.

### SAS5jh — global balanced compression

The total unpaired boundary variation is `R = sum_j R_j`. Exact compression to the zero boundary vector occurs precisely when every coordinate has `P_j=N_j` and every matching deficiency is zero.

### SAS5ji — canonical obstruction

If `R>0`, the least coordinate with `R_j>0` is canonical. It gives either a count imbalance or, when the counts agree, a positive Hall deficiency with a canonical deficient subset.

### SAS5jj — heavy-coordinate localization

For a coordinate dictionary of size `d`, some coordinate satisfies `R_j >= R/d`. In the balanced case the residual therefore localizes to one exact Hall-deficient pair graph.

### SAS5jk — reset boundary

Omitted occurrence identity, incomplete compatibility, cross-coordinate pairing, repeated use of one unit, or use of a disallowed pair returns reset.

## Proof

The coordinate identity follows from the maximum matching size. Summing gives the global formula. Every summand is nonnegative, which proves the exact zero criterion and the averaging alternative.

## Remaining physical work

The result leaves the concrete pair-graph Hall inequalities, output lower bounds, and the implication from a zero boundary vector to final balanced algebraic compression open.