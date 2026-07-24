# Superregular resampling and exact conflict-free matching

**Branch:** `research/superregular-resampling`

This is an independent endpoint track. It seeks to upgrade the spread perfect-matching results SR1–SR5 to a local-load theorem in a dense superregular host. It does not depend on the carry-cycle analysis.

## Proved inputs

- SR1: a uniform perfect matching of a dense superregular pair is fixed-rank `O(1/N)`-spread;
- SR2: the two-clone blow-up preserves superregularity;
- SR3: an all-rank spread measure exists in the dense superregular regime;
- SR4: two edge-disjoint spread perfect matchings give exact degree two;
- SR5: a global conflict-mass union bound works when total weighted conflict mass is below one;
- D1–D4: the complete-clone permutation space has a local-load LLL endpoint.

The gap is that spread in an arbitrary host does not imply the Lu–Szekely negative-dependency graph.

## SRR1 — Stationary local resampling oracle — DENSE-HOST STATIONARITY PROVED; LOCALITY OPEN

### Target statement

Let `G=(X,Y)` be an `(epsilon,d)`-superregular balanced bipartite graph with `d>=delta N`. Construct a probability measure `mu` on perfect matchings and, for every forbidden partial matching `F` of size at most three, a randomized map

\[
\mathcal R_F:M\mapsto M'
\]

such that:

1. if `F subseteq M`, then `F` is not contained in `M'`;
2. `M'` is a perfect matching of `G`;
3. `mu` is stationary under the resampling operation;
4. the symmetric difference `M triangle M'` is supported on `O_delta(1)` alternating cycles and has `O_delta(1)` edges in expectation;
5. for every event `B` whose matching vertices are disjoint from a controlled neighbourhood of `F`, resampling `F` does not increase the probability of `B` by more than `1+o(1)`.

A version using an exact heat-bath update on a bounded alternating-cycle gadget is preferred.

[`complete-host-resampling-oracle.md`](complete-host-resampling-oracle.md)
proves all five properties for `K_{N,N}`. The oracle swaps the matched
columns of the distinguished forbidden row and one uniformly random other
row; it is a symmetric stationary kernel supported on one four-cycle and
has an exact `1+O(1/N)` remote-event bound. The note also fixes the
stationarity convention: stationarity must refer to the all-state kernel,
since conditional regeneration to `mu` would contradict guaranteed flaw
removal. The missing-edge remote-event comparison remains open.

[`superregular-switching-criterion.md`](superregular-switching-criterion.md)
proves SRR1b: an exact stationary oracle exists whenever the flaw-removing
switching graph is left-regular and has reverse degree no larger than its
forward degree. This reduces the general host problem to a balanced
alternating-cycle switching theorem plus the remote-neighbourhood bound.

[`superregular-hall-resampling.md`](superregular-hall-resampling.md) proves
SRR1c: degree regularity can be removed entirely for the stationarity and
flaw-removal clauses.  Such a reversible kernel exists exactly when the
allowed switching graph satisfies Hall's condition on the flawed side.
The fractional Hall flow also identifies the remaining quantitative
problem: find feasible switching weights with a dispersed
remote-neighbourhood load.

[`dense-host-stationary-resampling.md`](dense-host-stationary-resampling.md)
proves SRR1d. For a host edge \(e=(i,j)\), a flawed perfect matching has
at least \(d(i)+d(j)-N-1\) host-valid four-cycle partners. Although this
degree varies with the state, every output has at most one reverse
predecessor, so state-by-state normalization gives an exact symmetric
uniform-stationary flaw-removal kernel. This settles the stationarity,
host-preservation, and bounded-switch clauses whenever the lower bound
is positive. It deliberately leaves the conditioned remote-cylinder
correlation required by SRR2 open.

[`deleted-matching-locality.md`](deleted-matching-locality.md) proves
SRR2a for the first nontrivial missing-host family. If the unavailable
cells form a matching \(Q\) of rank \(t\), inclusion--exclusion gives
the exact extension count after every partial matching. For
vertex-disjoint rank-\(f,b\) cylinders, their correlation ratio is at
most

\[
\frac{(N)_b}{(N-f)_b}
\cdot
\frac1{(1-t/(N-f))(1-t/(N-b))}.
\]

Together with SRR1d's pathwise noncreation, this proves the required
\(1+o(1)\) remote locality for fixed \(f,b\) whenever \(t=o(N)\).

## SRR2 — Resampling dependency theorem

### Target statement

Using SRR1, prove an algorithmic or lopsided local lemma for canonical forbidden submatchings of sizes two and three. A sufficient form is:

If

\[
\max_v
\sum_{A\ni v}\Pr_\mu(A)
\le c_0
\]

for a sufficiently small absolute constant `c_0`, then a perfect matching avoiding every forbidden event exists.

The dependency graph should be indexed by overlapping matching vertices, possibly enlarged by the bounded resampling neighbourhood from SRR1.

SRR1b and SRR1c show that stationarity and flaw removal follow from,
respectively, switching balance or the exact Hall condition, but not the
remote-event estimate. SRR2 still requires the lopsided/remote locality
estimate recorded in those criteria. SRR3b proves that estimate for
same-layer remote partial matchings in the complete two-layer space, and
SRR3c proves it for remote events entirely in the untouched layer;
SRR3d handles globally row-column-compatible mixed events. Thus the
complete-host locality calculation is finished for single-layer flaws.
SRR3e supplies the general compatible-cylinder count and finishes it for
mixed-layer flaws as well. SRR1d and SRR3f close the stationary
flaw-removal part for sufficiently dense missing-edge hosts; the
missing-host remote-cylinder comparison remains.

SRR2a resolves that comparison when the missing cells form a partial
matching of sublinear rank. Arbitrary missing-edge geometry and the
two-layer conditioned measure remain open.

[`sparse-hole-locality.md`](sparse-hole-locality.md) proves SRR2b for an
arbitrary missing set \(Q\) of sublinear total size. Rook-polynomial
inclusion--exclusion gives the exact cylinder count, while a union bound
gives the same remote inflation estimate as SRR2a with \(t=|Q|\).
Together with SRR1d this supplies at least \(N-2t-1\) stationary
four-cycle choices and all five one-layer oracle properties whenever
\(t=o(N)\). The unresolved one-layer host range may therefore be
assumed to have a linear or larger number of holes; arbitrary geometry
alone is no longer an obstruction in the sparse-hole regime.

[`two-layer-sparse-hole-locality.md`](two-layer-sparse-hole-locality.md)
proves SRR3g. A general two-layer cylinder has a crude independent-layer
upper count, while every globally compatible cylinder has the SRR3e
lower count. Their ratio bounds the conditional probability of using
one specified missing cell. A union bound and conditioning comparison
then give \(1+o(1)\) remote locality for two edge-disjoint matchings
whenever the arbitrary missing set has size \(t=o(N)\). Together with
SRR3f's \(N-2t-3\) stationary choices, this completes the two-layer
oracle throughout the sparse-hole regime.

The same note proves SRR3h, the explicit bound
\[
\varepsilon_Q(a,b)\leq\frac{9|Q|}{N-a-b}.
\]
Hence arbitrary hole geometry of size \(|Q|\leq cN\), \(c<1/9\), still
has \(O_c(1)\) fixed-rank remote inflation and linearly many stationary
switches. This is a genuine linear-hole extension, although the
inflation is not \(1+o(1)\) at fixed positive \(c\) and the
quadratically many holes of a general superregular host remain open.

SRR3i identifies the sharp asymptotic range of this particular
crude-cylinder method. For fixed ranks and \(|Q|/N\to c\), its error
tends to \(2ec\), giving bounded remote inflation for
\(c<1/(2e)\). Separately, exact cell marginals show that the two-layer
host space is nonempty for every arbitrary \(|Q|<N/2\), with
\(N-2|Q|-3\) stationary switches when positive. The gap between
\(1/(2e)\) correlation control and \(1/2\) switching feasibility now
pinpoints the missing conditional counting improvement.

## SRR3 — Two-layer exact-cover extension

### Target statement

Apply SRR2 sequentially or jointly to two edge-disjoint perfect matchings. The resulting theorem should select a simple 2-factor of the row-column graph while avoiding:

- duplicate cells across layers;
- all collinear candidate triples;
- optional unavailable-cell constraints already encoded by the host.

The local-load hypothesis should scale as the natural spread probabilities `O(N^{-2})` and `O(N^{-3})` for pair and triple events.

### Complete-host stationary component proved

[`complete-two-layer-resampling.md`](complete-two-layer-resampling.md)
proves SRR3a on the ordered space of two edge-disjoint perfect matchings
of \(K_{N,N}\). A four-cycle switch in one layer has at most two
cross-layer collision rows; canonical deletion leaves exactly \(N-3\)
forward choices and reverse degree at most one. SRR1b therefore gives an
exact stationary reversible flaw-removal kernel preserving the simple
two-layer exact cover. SRR3b adds a pathwise noncreation theorem and an
exact \(1+O(1/N)\) inflation bound for vertex-disjoint partial matchings
in the resampled layer. SRR3c gives a derangement-ratio
\(1+O_s(1/N)\) bound for rank-\(s\) remote events in the untouched layer.
SRR3d combines the two counts for mixed-layer, globally compatible
events. SRR3e extends the result to globally compatible mixed-layer flaws
and events. The complete-host remote theorem is therefore proved for the
canonical pair/triple conflicts; its superregular missing-edge
remote-event extension remains open.

### Dense missing-edge stationary component proved

[`dense-host-stationary-resampling.md`](dense-host-stationary-resampling.md)
also proves SRR3f on ordered pairs of edge-disjoint host matchings. A
flawed state has at least
\(d(i)+d(j)-N-3\) host- and cross-layer-valid partner rows. Unique
reverse predecessors again permit state-dependent symmetric weights,
giving an exact uniform-stationary one-four-cycle oracle whenever this
quantity is positive. Minimum degree \(\delta N\) gives the explicit
bound \((2\delta-1)N-3\). The other layer is unchanged pathwise and a
remote same-layer partial matching cannot be created, but arbitrary-host
conditional correlations are not yet controlled.

The same switching count proves SRR3j. If
\(L_2=2d_{\min}-N-3\geq1\), the *uniform* two-layer host measure has
labelled edge marginal at most \(1/(L_2+1)\), and every compatible
rank-\(s\) cylinder, \(s\leq L_2\), has probability at most
\(1/(L_2+1)_s\). Thus dense hosts already have the natural uniform
fixed-rank \(O(N^{-1})\)-spread. This deliberately does not infer
negative dependency: the remaining SRR2 gap is the conditioned
remote-cylinder ratio, not cylinder rarity.

## SRR4 — Superregular local-load endpoint

### Target statement

There are constants `epsilon_0,delta,c>0` such that every `(epsilon,delta)`-superregular candidate host with `epsilon<=epsilon_0` and maximum normalized conflict load at most `c` contains two edge-disjoint perfect matchings whose union is no-three-in-line.

An explicit geometric corollary should bound the permitted number of residual collinear triples incident with each row or column.

## Alternative route: conflict-free exact-cover theorem

Instead of SRR1, one may prove a specialization of conflict-free hypergraph matching/covering theory:

- host edges are row-column cells;
- desired object is an exact perfect matching or two disjoint perfect matchings;
- forbidden configurations are matchings of size two or three;
- superregularity supplies the exact-cover reservoir.

The theorem must achieve exact coverage, not merely an almost-perfect conflict-free matching.

## Regression tests and obstructions

- four-cycle host, where opposite compatible edges are positively correlated;
- near-disconnected superregular-looking examples with hidden forced edge pairs;
- duplicate-cell conflicts across two layers;
- preservation of stationary measure after repeated resampling;
- comparison against the exact complete-permutation constant `1/24`.

The four-cycle positive-correlation example and the complete-host oracle
are exhaustively checked by `scripts/verify_complete_resampling.py`.
The state-dependent one- and two-layer kernels in complete and
one-edge-deleted dense hosts are checked by
`scripts/verify_dense_host_resampling.py`. Deleted-matching extension
counts and remote-cylinder ratios are checked by
`scripts/verify_deleted_matching_locality.py`. Arbitrary sparse-hole
rook counts and locality are checked by
`scripts/verify_sparse_hole_locality.py`. Two-layer sparse-hole
conditioning is checked by
`scripts/verify_two_layer_sparse_hole_locality.py`.

## Completion criterion

This branch is complete when the superregular extension of SRR1 and
SRR2–SRR4, or an equivalent conflict-free exact-cover theorem, is proved
with constants and supplies a directly usable replacement for D1 in a
dense superregular host.
