# A terminal blocker cover creates a linear Hall wall

CMR1126--CMR1141 reduce rolled-back target banks to a permanent missing-edge
cover.  The principal simultaneous escape banks are perfect matchings of a
balanced board obtained from `K_{n,n}` by forbidding at most two perfect
matchings: the old rematched layer and the fixed opposite layer.  Line-clean banks
forbid only one matching.

If a blocker cover meets every bank state, deleting that cover leaves no perfect
matching.  Hall's theorem then supplies a deficient cut.  Every originally allowed
edge crossing from the deficient source set to the missing target side must belong
to the blocker cover.  Since the original forbidden board has maximum degree at
most two, one row or column contains linearly many blockers.

Let `L,R` be balanced vertex sets of size `n`.  Let `F subseteq L times R` be an
original forbidden set with maximum source and target degree at most `d_0`, and put

\[
G=K_{n,n}\setminus F.
\]

Assume `G` has a perfect matching.  Let `C subseteq E(G)` be a currently unavailable
blocker set.

## 1. Bank coverage is matching destruction

### Theorem CMR1142 -- PROVED

The following are equivalent.

1. Every perfect matching of `G` contains at least one edge of `C`.
2. The graph `G-C` has no perfect matching.

### Proof

A perfect matching avoids `C` exactly when it is a perfect matching of `G-C`. ∎

Thus a permanent cover of the complete bank is an edge set destroying
matchability.

## 2. Canonical Hall-deficient cut

### Theorem CMR1143 -- PROVED

If `C` covers every perfect matching of `G`, there is a nonempty source set
`X subseteq L` such that, with

\[
Y=N_{G-C}(X),
\]

one has

\[
\boxed{|Y|<|X|.}
\]

Choose the inclusion-minimal such `X` and then the canonical first one under the
fixed source ordering.

### Proof

Apply Hall's theorem to the unmatchable graph `G-C`. ∎

Put

\[
x=|X|,
\qquad
y=|Y|,
\qquad
Z=R\setminus Y,
\qquad
z=|Z|=n-y.
\]

Then

\[
\boxed{x+z\ge n+1.}
\]

## 3. Every allowed cross-cut edge is blocked

### Theorem CMR1144 -- PROVED

\[
\boxed{
E(G)\cap(X\times Z)
\subseteq C.
}
\]

### Proof

If an edge from `X` to `Z` belonged to `G-C`, its target would lie in
`N_{G-C}(X)=Y`, contradicting `Z=R-Y`. ∎

The blocker cover therefore contains a complete allowed Hall wall, not merely one
witness edge.

## 4. Quantitative wall bounds

### Theorem CMR1145 -- PROVED

The Hall wall satisfies both lower bounds

\[
\boxed{
|C\cap(X\times Z)|
\ge
x\max\{0,z-d_0\},
}
\]

and

\[
\boxed{
|C\cap(X\times Z)|
\ge
z\max\{0,x-d_0\}.
}
\]

Moreover every source vertex in `X` is incident with at least

\[
\boxed{\max\{0,z-d_0\}}
\]

blocker edges into `Z`, and every target vertex in `Z` is incident with at least

\[
\boxed{\max\{0,x-d_0\}}
\]

blocker edges from `X`.

### Proof

A source vertex has at most `d_0` forbidden neighbours in the whole board, hence
at most `d_0` forbidden neighbours in `Z`.  All its allowed neighbours in `Z` are
blocked by CMR1144.  Sum over `X`.  The target-side proof is symmetric. ∎

## 5. Degree-two banks force a linear blocker wall

### Theorem CMR1146 -- PROVED

Assume `d_0<=2`, as in the simultaneous one-layer escape boards.  Then the blocker
cover has a source-row or target-column vertex of degree at least

\[
\boxed{
\Delta(C)
\ge
\left\lceil\frac{n+1}{2}\right\rceil-2.
}
\]

For a line-clean derangement board with `d_0<=1`,

\[
\boxed{
\Delta(C)
\ge
\left\lceil\frac{n+1}{2}\right\rceil-1.
}
\]

Negative right sides are interpreted as zero in the finite base range.

### Proof

Since `x+z>=n+1`, one of `x,z` is at least `ceil((n+1)/2)`.  If `z` is large, every
source in `X` has blocker degree at least `z-d_0` by CMR1145.  If `x` is large,
every target in `Z` has blocker degree at least `x-d_0`.  Substitute `d_0=2` or
`d_0=1`. ∎

Thus a terminal bank cover always contains a linear matching-vertex wall.

## 6. Sparse blocker covers cannot be terminal

### Corollary CMR1147 -- PROVED

If

\[
\Delta(C)
<
\left\lceil\frac{n+1}{2}\right\rceil-d_0,
\]

then `G-C` has a perfect matching.  Hence the bank contains a candidate avoiding
the complete blocker cover.

### Proof

This is the contrapositive of CMR1146 and its `d_0`-form proof. ∎

For degree-two escape boards, sublinear maximum blocker degree is therefore
insufficient to stop the bank.

## 7. The Hall wall enters existing geometric ledgers

### Theorem CMR1148 -- PROVED

The row or column supplied by CMR1146 contains a set `W` of at least

\[
\left\lceil\frac{n+1}{2}\right\rceil-d_0
\]

distinct unavailable cells.  At every chosen nonroot prefix depth, partitioning
those cells by the varying coordinate gives either:

1. one full token containing at least `ceil(sqrt(|W|))` wall cells; or
2. at least `floor(sqrt(|W|))` pairwise disjoint full-token wall witnesses.

A later return of wall cells enters the physical restoration and bulk-redeletion
ledgers; continuous absence is a persistent row/column Hall wall.

### Proof

Distinct wall edges in one source row or target column have distinct varying
coordinates.  Apply the partition-and-pigeonhole argument of CMR512--CMR515 and
CMR532 at any fixed depth.  Temporal responses are CMR777--CMR821 and CMR1130. ∎

## 8. Terminal blocker endpoint

### Corollary CMR1149 -- PROVED

A permanent blocker cover for a degree-two Hall escape bank reaches at least one
of:

1. a feasible target-destroying completion avoiding the cover;
2. a canonical Hall-deficient cut;
3. a linear unavailable row or column wall;
4. heavy or dispersed full-token wall witnesses;
5. bulk redeletion after blocker return;
6. anchor-loss ancestry, added-core contraction, strict factor/envelope exit, or
   strict potential improvement.

Therefore the terminal blocker obstruction from CMR1141 is no longer an arbitrary
edge cover.  It is a linear Hall wall with exact prefix/token structure.  The
remaining frontier is to resolve a persistent linear wall in the final residual
factor by prefix/carry factorisation, Hall-wall peeling, or a clean completion.

### Proof

Combine CMR1142--CMR1148. ∎

No all-`n` theorem is claimed.  Bank coverage, Hall cuts, cross-cut containment,
quantitative wall bounds, and the linear-degree conclusion are checked in
[`scripts/verify_prime_power_terminal_blocker_hall_wall.py`](../scripts/verify_prime_power_terminal_blocker_hall_wall.py).
