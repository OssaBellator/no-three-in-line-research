# Exact selected geometry and correction burden of the eleven-host hard core

CMR1998--CMR2005 identify the positive-minimum raw hosts as exact blockers of all
zero-rank-three side-four responses.  This chapter reconstructs the selected
collinear geometry and determines the exact rank-three occurrence-deletion burden
under the deterministic selector policy.

## 1. The two selected responses

Let

\[
Q_1=(3,0,1,2),\qquad Q_4=(3,2,1,0).
\]

### Theorem CMR2006 -- PROVED

The lexicographically selected rank-three minimizer is:

1. `Q_1` on nine hard-core hosts;
2. `Q_4` on the remaining two hosts.

No third response is selected on the hard core.

### Proof

CMR2003 leaves only the two positive base responses.  On the nine two-response hosts,
`Q_1` has one triple and `Q_4` has four, so `Q_1` is the unique minimizer.  On the two
one-response hosts only `Q_4` survives. ∎

## 2. Literal line support

### Theorem CMR2007 -- PROVED

The selected rank-three triples have exactly two possible line supports:

1. for `Q_1`, the three response points
   `[(1,0),(2,1),(3,2)]` lie on
   \[
   x-y-1=0
   \]
   and create exactly one triple;
2. for `Q_4`, all four response points
   `[(0,3),(1,2),(2,1),(3,0)]` lie on
   \[
   x+y-3=0
   \]
   and create exactly four triples.

### Proof

Substitution verifies both line equations.  Three collinear points determine one
triple.  Four collinear points determine `binom(4,3)=4` triples.  Direct determinant
enumeration confirms that these are all selected rank-three triples. ∎

### Corollary CMR2008 -- PROVED

The selected-support distribution over the eleven hosts is

\[
\boxed{9\text{ on }x-y-1=0,\qquad2\text{ on }x+y-3=0.}
\]

## 3. Exact selected-response correction lower bound

Fix a selected response and consider a scalar correction that acts only by deleting
rank-three primitive occurrence units from that selected response, without changing
the response itself.

### Theorem CMR2009 -- PROVED

The minimum number of rank-three occurrence units that must be removed to make the
selected response rank-three-free is exactly its literal selected triple count.
Thus it is one on the nine `Q_1` hosts and four on the two `Q_4` hosts.

### Proof

Every selected collinear response triple contributes one distinct rank-three
primitive occurrence.  Rank-three freedom requires all such occurrences to be
removed, giving the lower bound.  Deleting every such occurrence attains the bound. ∎

The theorem is deliberately scoped to occurrence deletion.  A structural transfer,
changed response, nonuniform weighting, or finer labelled state split is a different
certificate surface.

## 4. Deterministic hard-core burden

### Theorem CMR2010 -- PROVED

The total independent selected-response correction burden across the eleven hard-core
hosts is

\[
\boxed{9\cdot1+2\cdot4=17.}
\]

### Proof

Sum the exact hostwise minima of CMR2009. ∎

## 5. Comparison with independent uniform correction

Every hard-core host has uniform slack `S_3=-3`, so CMR1982 assigns uniform
rank-three correction requirement

\[
1-S_3=4.
\]

### Theorem CMR2011 -- PROVED

Independent uniform correction of the eleven hosts requires 44 rank-three numerator
units, while deterministic selected-response occurrence deletion requires 17 units.
The exact arithmetic difference is

\[
\boxed{44-17=27.}
\]

### Proof

Uniform correction contributes `11*4=44`.  CMR2010 gives 17 for the deterministic
selected responses. ∎

This is a comparison of two different response policies, not an improvement of a
fixed uniform theorem.  The selector may be used only where deterministic response
choice is allowed.

## 6. Two-host irreducible raw geometry

### Theorem CMR2012 -- PROVED

The two hosts with minimum four have only one available response, `Q_4`.  Therefore
no response selection rule on the same raw allowed-edge set can reduce their literal
rank-three load below four.

### Proof

Their exact catalogue response lists contain one record.  That response is `Q_4`,
whose literal rank-three count is four by CMR2007. ∎

Consequently these two hosts require correction, altered routing, or a changed state
or operation even before background terms are added.

## 7. Executable endpoint

### Corollary CMR2013 -- PROVED

`scripts/check_prime_power_rank_three_hard_core_correction.py` reconstructs every
selected response, enumerates its literal collinear triples, verifies common line
support, computes the exact selected occurrence-deletion minimum, and checks the
17/44/27 burden identities.

The canonical correction-manifest digest is

\[
\texttt{86902404bef228440c2ed6e1e940f3b45ffd8e0a3a193abd8a21fe9327d6ab62}.
\]

Its built-in mutation suite rejects ten independently corrupted manifests.

Neither the one-triple nor the four-triple correction count includes background,
return, selector, interface, or labelled recurrent contributions.
