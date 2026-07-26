# Dense-host two-layer spread import for AC5

**Branch:** `research/alternating-core-chain`

The all-`n` superregular-resampling branch proves that the uniform measure on two
edge-disjoint perfect matchings of a dense bipartite host already has the
fixed-rank spread required by AC5.  This note records the exact import in AC5
notation and gives a sparse-hole corollary.  It applies only when a complete AC
menu is represented by the full ordered two-layer matching space of one host;
an arbitrary subfamily, weighted law or history-dependent filter needs its own
comparison theorem.

## Dense two-layer hosts

Let `G=(X,Y;E)` be bipartite with

\[
|X|=|Y|=N,
\]

and let

\[
\Omega_2(G)=
\{(M_1,M_2): M_1,M_2\text{ are edge-disjoint perfect matchings of }G\}.
\]

Assume `Omega_2(G)` is nonempty and let `mu_G` be uniform on it.  Write

\[
d_{\min}=\min_{v\in X\cup Y}d_G(v),
\qquad
L=2d_{\min}-N-3.
\]

A labelled cylinder is a globally compatible set of host edges, each assigned
to one of the two layers.

## AC5u -- dense-host four-cycle switching count -- PROVED

Fix a labelled host edge `e=(i,j)` in layer one and a state containing it.  There
are at least

\[
\boxed{L}
\]

rows `u` such that switching the two layer-one edges on rows `i,u` removes `e`,
uses only host edges and remains disjoint from layer two.

Every state avoiding `e` has at most one reverse predecessor under such a
switch.

### Proof

Before enforcing layer disjointness, the usual neighbourhood intersection has
size at least `d(i)+d(j)-N` and contains `i`.  Delete `i`.  The switch can create
an opposite-layer collision only when the new edge at row `i` equals the
layer-two edge there or the new edge at row `u` equals the layer-two edge there.
Those conditions exclude at most two further uniquely determined rows.  Hence
at least `d(i)+d(j)-N-3>=L` rows remain.  In a state avoiding `e`, any reverse
switch introducing `e` must use the unique row currently matched to column `j`,
so reverse degree is at most one. QED.

## AC5v -- automatic fixed-rank spread -- PROVED

For every globally compatible labelled cylinder `F` of rank `s` with

\[
1\le s\le L,
\]

\[
\boxed{
\Pr_{\mu_G}(F)
\le
\frac1{(L+1)_s}.
}
\]

In particular, for `s<=min{3,L}` and `L>=2`,

\[
\boxed{
\Pr_{\mu_G}(F)
\le
\left(\frac1{L-1}\right)^s.
}
\]

When `L>=3`, the uniform dense-host menu is rank-three spread in AC5's
`K/p` notation with partner scale `p=N` and

\[
\boxed{
K_{\rm dense}=rac{N}{L-1}
=rac{N}{2d_{\min}-N-4}.
}
\]

### Proof

For one edge, double-count the switching graph of AC5u.  Every containing state
has at least `L` outgoing switches and every avoiding state has reverse degree
at most one, giving probability at most `1/(L+1)`.  For a compatible ordered
cylinder, expose its edges successively.  After `t` prescribed edges have been
fixed, discard at most `t` switch rows to preserve them.  The next conditional
probability is at most `1/(L-t+1)`.  Multiplication gives `1/(L+1)_s`.  For
`s<=min{3,L}`, every falling-factorial term is at least `L-1`. QED.

The theorem is state-normalized: no regularity of the number of switches across
flawed states is required.

## AC5w -- sparse-hole dense-menu corollary -- PROVED

Suppose

\[
G=K_{N,N}\setminus Q,
\qquad |Q|=h.
\]

Then

\[
d_{\min}\ge N-h,
\qquad
L\ge N-2h-3.
\]

If

\[
2h<N,
\]

then `Omega_2(G)` is nonempty.  If moreover

\[
N-2h\ge6,
\]

then every compatible labelled cylinder of rank at most three satisfies

\[
\boxed{
\Pr_{\mu_G}(F)
\le
\left(\frac1{N-2h-4}\right)^{|F|}.
}
\]

Equivalently the rank-three AC5 spread constant may be taken as

\[
\boxed{
K_{\rm hole}
=
\frac{N}{N-2h-4}.
}
\]

For `h<=cN` with fixed `c<1/2`, this is bounded by
`(1-2c-o(1))^{-1}` once `N` is large enough for the rank-three condition.

### Proof

Every vertex loses at most `h` incident edges, giving the degree bound and hence
the lower bound for `L`.  Under the uniform complete two-layer measure, one
specified cell appears in exactly one of the two layers with probability `2/N`.
A union bound shows positive probability of avoiding all `h` holes when
`2h<N`; therefore `Omega_2(G)` is nonempty.  The condition `N-2h>=6` gives
`L>=3`.  Apply AC5v. QED.

The total-hole estimate is safe rather than sharp.  Per-row and per-column hole
caps give the stronger direct value of `d_min`.

## AC5x -- direct substitution into the AC5 event audit -- PROVED

Assume `L>=3`, one complete AC menu is exactly `Omega_2(G)`, and every possible
current- or protected-band created triple has a complete labelled-cylinder
inventory of rank two or three.  In AC5l--AC5t, replace the externally supplied
spread constant by

\[
K=K_{\rm dense}.
\]

Then all displayed current-band, protected-band and multistep expectation bounds
remain valid.  In particular AC5t gives a safe improving installation whenever

\[
\Gamma_{\rm cur}
+t\sum_j\Gamma_{{\rm high},j}<t
\]

with `K_dense` substituted into every rank-two and rank-three term.

### Proof

AC5v supplies exactly the cylinder probability bounds used in AC5l.  The rest of
AC5l--AC5t uses only completeness of the event inventory, linearity of
expectation and the augmented protected-band badness variable. QED.

## Corrected AC5 interface

For a menu whose complete states are all ordered edge-disjoint perfect matchings
of one host, AC5 no longer needs a separately constructed spread law.  It is
enough to prove:

1. nonemptiness of the two-layer host space;
2. a minimum-degree or sparse-hole bound with `L>=3`;
3. complete rank-two and rank-three geometric event inventories;
4. the numerical AC5t inequality.

What remains outside this import is equally explicit:

- nonuniform or restricted menu laws;
- filters not representable as host-edge deletion;
- hosts with minimum degree near or below `N/2`;
- lopsided remote-cylinder comparisons needed for witness-tree resampling;
- geometric event inventories whose rank exceeds three.

Thus the superregular all-`n` branch removes one probability-construction
obligation from the dense-host portion of AC5, but does not by itself close the
geometric inventory or local-dependency frontiers.

## Finite check

`scripts/verify_ac_dense_host_spread_import.py` enumerates ordered edge-disjoint
perfect-matching pairs in complete and small hole-deleted bipartite hosts.  It
checks the four-cycle forward-degree bound, unique reverse predecessor and every
compatible cylinder inequality whose rank is at most `min{3,L}`.