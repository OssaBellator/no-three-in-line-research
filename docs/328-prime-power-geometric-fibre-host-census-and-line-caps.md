# Exact geometric host fibres and deterministic line-occupancy caps

CMR1774--CMR1781 correct the thin-host symmetry: residual matching permutations
preserve response denominators but not Euclidean collinearity.  The correction is
finite and explicit.  The raw coordinate-labelled deletion hosts already counted
in CMR1662 are precisely the first geometric fibre expansion of the matching
orbits.

This chapter records the exact fibre sizes through side five and adds two
host-level geometric caps for the rank-two and rank-three line-energy terms.
These caps are coarser than the nested assignment certificates of CMR1790--CMR1797
but require only line occupancy data.

For side `d`, let

\[
H_d=K_{d,d}\setminus(I_d\cup\{(0,1)\}),
\]

let `X` be a partial matching in `H_d`, and put

\[
G_X=H_d\setminus X.
\]

Only executable hosts with at least one perfect matching are retained.

## 1. Raw hosts are the coordinate-labelled matching fibres

### Theorem CMR1798 -- PROVED

The residual `S_{d-2}` matching action partitions the executable raw deletions
into the canonical matching orbits of CMR1662.  For one canonical orbit, its
first exact standard-grid geometric fibre is the set of all coordinate-labelled
raw deletions in that orbit.

### Proof

The matching canonicalization maps every raw deletion to exactly one orbit and
forgets only the residual coordinate permutation.  Restoring all raw deletions
therefore restores every coordinate-labelled embedding represented by the
matching orbit.  Euclidean line data are then computed on those fixed
coordinates. ∎

Additional owner, collision, local-line, root, thin and CRT labels may refine a
raw host further; they never reduce the need to retain its coordinate geometry.

## 2. Exact orbit-size distributions

### Theorem CMR1799 -- PROVED

The executable matching-orbit fibre sizes are:

### Side four

\[
\boxed{
4\text{ fibres of size }1,
\qquad
41\text{ fibres of size }2.
}
\]

Hence

\[
4+41\cdot2=86
\]

coordinate-labelled executable hosts lie above the 45 canonical matching hosts.

### Side five

\[
\boxed{
2\text{ fibres of size }1,
\quad
2\text{ fibres of size }2,
\quad
24\text{ fibres of size }3,
\quad
96\text{ fibres of size }6.
}
\]

Hence

\[
2+2\cdot2+24\cdot3+96\cdot6=654
\]

coordinate-labelled executable hosts lie above the 124 canonical matching hosts.

### Proof

Enumerate every executable raw deletion, compute its canonical residual-permutation
code, and count the members of each code fibre.  The displayed distributions sum
to the raw and canonical counts of CMR1662. ∎

The fibre sizes divide `(d-2)!`, as required by orbit--stabilizer.

## 3. Exact geometric host count through side five

### Corollary CMR1800 -- PROVED

Before provenance refinements, the corrected side-four/five geometric host layer
contains exactly

\[
\boxed{86+654=740}
\]

coordinate-labelled executable hosts.

### Proof

Add the two raw executable counts in CMR1799. ∎

Thus the geometric correction enlarges the matching-level denominator table but
does not create an unbounded computation at fixed side.

## 4. Denominator reuse inside each fibre

### Theorem CMR1801 -- PROVED

All raw hosts in one matching orbit have the same:

1. perfect-matching denominator;
2. contracted prescription numerator after transporting the prescription;
3. rank-one, rank-two and rank-three matching probability table.

Their Euclidean coefficients `a_1,a_2,a_3`, line profiles and labelled offspring
rows may differ.

### Proof

A residual simultaneous coordinate permutation is a bipartite graph isomorphism,
so it bijects perfect matchings and contracted perfect matchings.  CMR1774 shows
that the same map need not preserve collinearity. ∎

Hence one denominator computation may be reused across a fibre, while geometric
numerators are computed separately.

## 5. Response-line occupancy cap

For an embedded host `G`, define

\[
\Lambda(G)
=
\max_{\ell}\,|E(G)\cap\ell|,
\]

where the maximum is over nonaxis real lines and the line trace is viewed as grid
cells.  Put `(t)_+=max(t,0)`.

### Theorem CMR1802 -- PROVED

Every response perfect matching `Q` of side `d` satisfies

\[
\boxed{
3\Psi(Q)
\le
(\Lambda(G)-2)_+\binom d2.
}
\]

Consequently,

\[
\boxed{
\Psi(Q)
\le
\left\lfloor
\frac{(\Lambda(G)-2)_+\binom d2}{3}
\right\rfloor.
}
\]

### Proof

Every response pair lies on one nonaxis line because a perfect matching has
distinct source and target coordinates.  If a line contains `k` response points,
each of its `C(k,2)` response pairs has exactly `k-2` possible third response
points on that line.  Therefore

\[
3\Psi(Q)
=
\sum_{\{x,y\}\subseteq Q}
(k_{\ell(x,y)}-2).
\]

Every response point lies in `G`, so `k_ell<=Lambda(G)`.  Bound each of the
`C(d,2)` pair summands and use integrality. ∎

This is a host-specific replacement for the ambient rank-three mass
`C(d,3)`.

## 6. Background load cap for the rank-two term

For fixed background set `B`, define

\[
H_B(G)
=
\max
\left\{
|B\cap\ell(x,y)|:
\{x,y\}\text{ is a compatible response pair in }G
\right\},
\]

with maximum zero when no compatible pair exists.

### Theorem CMR1803 -- PROVED

Every response perfect matching satisfies

\[
\boxed{
\sum_{\{x,y\}\subseteq Q}a_2(\{x,y\})
\le
H_B(G)\binom d2.
}
\]

### Proof

By CMR1782, `a_2({x,y})=|B cap ell(x,y)|`.  Every one of the `C(d,2)` response
pairs has coefficient at most `H_B(G)`. ∎

Exact nested assignments or rook marginals may replace this maximum whenever it
is too coarse.

## 7. Coarse deterministic fibre certificate

Let `L_1` be any assignment upper bound for the rank-one score

\[
a_1(x)=\sum_{\ell\ni x}\binom{|B\cap\ell|}{2}.
\]

Define

\[
T_3(G)
=
\left\lfloor
\frac{(\Lambda(G)-2)_+\binom d2}{3}
\right\rfloor.
\]

### Theorem CMR1804 -- PROVED

Every response perfect matching in the geometric fibre satisfies

\[
\boxed{
\Psi(B\cup Q)-\Psi(B)
\le
L_1+H_B(G)\binom d2+T_3(G).
}
\]

If the right-hand side is strictly below destroyed current load `D`, every
response in the host is a strict improvement.

### Proof

Apply the rank-one assignment bound, CMR1803 to the rank-two term, and CMR1802 to
the rank-three term in the exact decomposition CMR1782. ∎

This certificate uses only one assignment problem plus two finite geometric host
statistics.

## 8. Geometric fibre census endpoint

### Corollary CMR1805 -- PROVED

The corrected thin-host computation through side five now has the following
finite form.

1. Expand the 45 side-four matching classes into 86 raw geometric hosts.
2. Expand the 124 side-five matching classes into 654 raw geometric hosts.
3. Reuse matching denominators inside each orbit fibre.
4. Compute `a_1`, `H_B(G)` and `Lambda(G)` on each raw host and provenance
   refinement.
5. Apply the coarse certificate of CMR1804 or the sharper marginal/nested
   certificates of CMR1788--CMR1797.
6. Quotient further only through verified automorphisms of the complete geometric
   signature.

The first geometric host layer therefore contains exactly 740 finite cases, not
169 matching representatives and not an unbounded family.  The remaining work
is to attach the actual background and recurrent provenance data and certify the
surviving rows.  No all-`n` theorem is claimed.

Exact fibre distributions, all 740 raw hosts, response-line occupancy caps and
background rank-two bounds are checked in
[`scripts/verify_prime_power_geometric_fibre_host_census.py`](../scripts/verify_prime_power_geometric_fibre_host_census.py).
