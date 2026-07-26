# An inclusion-minimal terminal blocker cover is an exact unit Hall wall

CMR1142--CMR1149 turn every terminal cover of a degree-two response bank into a
Hall-deficient unavailable wall.  Minimize that blocker cover by inclusion.  The
minimality is much stronger than linear wall concentration.

For a Hall witness `X`, every allowed edge from `X` to the missing target side is
blocked.  If a minimal cover contained any edge outside that cut, restoring that
edge would leave the same Hall deficiency and would not recover a perfect
matching.  Therefore the cover is exactly one allowed Hall cut.  Its deficiency is
exactly one: if the deficiency were at least two, restoring one cut edge could
increase the Hall neighbourhood by at most one and still could not recover a
perfect matching.

Thus every blocker edge is essential in the graph obtained by restoring it alone.
The deficiency-one unit-wall factorisation CMR727--CMR747 applies immediately.

Let `G=(L,R;E)` be any finite balanced bipartite graph with a perfect matching.
Let `C subseteq E` be inclusion-minimal subject to `G-C` having no perfect
matching.  Inclusion-minimal means

\[
G-(C\setminus\{e\})
\]

has a perfect matching for every `e in C`.

## 1. Minimal blocker cores exist

### Theorem CMR1150 -- PROVED

Every finite blocker cover contains an inclusion-minimal blocker subcover.

### Proof

Repeatedly delete a blocker edge whenever its deletion still leaves a blocker
cover.  The finite process stops at an inclusion-minimal subcover. ∎

All conclusions below apply to that canonical subcover after fixed-order tie
breaking.

## 2. A Hall witness determines the complete minimal cover

Let `X subseteq L` be any Hall-deficient set in `G-C`, and put

\[
Y=N_{G-C}(X),
\qquad
Z=R\setminus Y.
\]

### Theorem CMR1151 -- PROVED

\[
\boxed{
C=E(G)\cap(X\times Z).
}
\]

### Proof

CMR1144 gives

\[
E(G)\cap(X\times Z)\subseteq C.
\]

Suppose `c in C` lies outside that cross-cut.  Restoring only `c` does not add an
edge from `X` to `Z`, so the neighbourhood of `X` remains `Y`.  The same Hall
inequality `|Y|<|X|` persists, and `G-(C\setminus\{c\})` is still unmatchable,
contradicting inclusion-minimality. ∎

Thus a minimal blocker cover contains no irrelevant edge.

## 3. The Hall deficiency is exactly one

### Theorem CMR1152 -- PROVED

For the sets of CMR1151,

\[
\boxed{|X|-|Y|=1.}
\]

### Proof

The deficiency is positive.  If it were at least two, restoring one blocker edge
could add at most one new target to `N(X)`.  The restored graph would still satisfy

\[
|N(X)|\le |Y|+1<|X|,
\]

so it would remain unmatchable.  This contradicts inclusion-minimality for every
edge of `C`. ∎

Hence `|Z|=n-|Y|=n-|X|+1`.

## 4. Every blocker is an essential restored edge

For `e in C`, put

\[
G_e=(G-C)+e.
\]

### Theorem CMR1153 -- PROVED

The graph `G_e` has a perfect matching, and every perfect matching of `G_e`
contains `e`.  Equivalently, `e` is essential in `G_e`.

### Proof

Matchability is the inclusion-minimality condition.  Removing `e` from `G_e`
returns `G-C`, which is unmatchable.  Therefore no perfect matching of `G_e` can
omit `e`. ∎

So a single blocker restoration cannot be treated as a free optional edge.

## 5. Every blocker has a private bank matching

### Theorem CMR1154 -- PROVED

For every `e in C`, choose one perfect matching `M_e` of `G_e`.  Then

\[
\boxed{e\in M_e}
\]

and the matchings `M_e` are pairwise distinct as `e` varies.

### Proof

Essentiality gives `e in M_e`.  The graph `G_e` contains no other edge of `C`, so
`M_e cap C={e}`.  If `e ne f`, a matching cannot have both intersections `{e}` and
`{f}` with `C`; hence `M_e ne M_f`. ∎

The minimal wall therefore carries a private restoration bank indexed by its
physical blocker edges.

## 6. Exact unit-wall product after one restoration

Fix `e=(u,v) in C`.  The graph `G_e-e=G-C` has matching number one below full,
and the Hall wall of CMR1151--CMR1152 has unit deficiency.

### Theorem CMR1155 -- PROVED

The essential-edge unit-wall theorems CMR727--CMR740 apply to `G_e`.  In
particular, after fixing `e`, every perfect matching factors exactly as

\[
\boxed{
\operatorname{PM}(G_e)
\cong
\{e\}
\times
\operatorname{PM}(G_A)
\times
\operatorname{PM}(G_B),
}
\]

where the two residual factor sides `a,b` satisfy

\[
\boxed{a+b=n-1.}
\]

### Proof

CMR1153 makes `e` essential and CMR1152 supplies the deficiency-one Hall wall.
Apply CMR727--CMR740. ∎

Every positive wall child has strictly smaller side.

## 7. The complete minimal-blocker factor tree is finite

### Theorem CMR1156 -- PROVED

Following blocker restorations and exact unit-wall splits cannot generate an
unbounded same-side tree.  Starting at side `n`, the complete tree has at most

\[
\boxed{n}
\]

splits and at most

\[
\boxed{2n+1}
\]

nodes.  Its total owner-edge stock is bounded by

\[
\boxed{
\sum_{j=1}^{n}j^2.
}
\]

### Proof

Every split replaces side `m` by children whose side sum is `m-1`.  Apply
CMR741--CMR747. ∎

Minimal blocker walls therefore enter an already finite structural recursion.

## 8. Minimal blocker endpoint

### Corollary CMR1157 -- PROVED

A terminal blocker cover for a selected response bank reaches at least one of:

1. removal of redundant blockers until an inclusion-minimal cover remains;
2. an exact allowed Hall cut;
3. unit Hall deficiency;
4. one essential restored blocker edge;
5. a private perfect matching indexed by that blocker;
6. exact unit-wall factorisation into strict lower-side hosts;
7. finite wall-tree recursion, blocker bulk redeletion, anchor-loss ancestry, or
   strict potential improvement.

Thus the terminal blocker endpoint of CMR1141 is structurally closed: once
minimal, it is an exact unit-wall product rather than an arbitrary permanent edge
inventory.  The remaining terminal prime-power obstruction is the loaded-line or
fixed-core certificate surviving inside the final strict wall/child factor, plus
the prime-field and thin-regime endpoints.

### Proof

Combine CMR1150--CMR1156. ∎

No all-`n` theorem is claimed.  Minimal-cover exactness, unit deficiency,
essential restoration, private matchings, and wall-tree arithmetic are checked in
[`scripts/verify_prime_power_minimal_blocker_unit_wall.py`](../scripts/verify_prime_power_minimal_blocker_unit_wall.py).
