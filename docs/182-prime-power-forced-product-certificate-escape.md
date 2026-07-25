# Forced product certificates can disappear only through deletion, skeleton churn, or entering-edge alternating cycles

CMR636--CMR642 reduce every fully essential mixed obstruction to one fixed
candidate conflict which occurs in every state of a protected/free product
class.  Internal variation of the two factor matchings cannot remove such a
certificate.  This chapter records the exact price of escape.

There are only three mechanisms.

1. A certificate edge is deleted from the current host.
2. The protected/free cross skeleton changes.
3. A factor edge which was essential becomes avoidable after the host gains new
   edges.

The third mechanism has an exact alternating-cycle witness.  If an old
essential edge is omitted by a matching in the enlarged host, then the
alternating-cycle component containing that edge must contain at least one newly
added matching edge.  Several omitted essential edges may lie on one cycle, so
the sharp payment is one entering edge per affected alternating component, not
one entering edge per omitted edge.

Fix one owner-labelled product class with skeleton `S`, factor hosts `H_I,H_J`,
and one forced candidate conflict

\[
T=T_I\sqcup T_J\sqcup T_S.
\]

Every edge of `T_I` is essential in `H_I`, every edge of `T_J` is essential in
`H_J`, and every edge of `T_S` belongs to the fixed skeleton.  The sets
`T_I,T_J,T_S` may be empty, but `|T|=3`.

## 1. Essentiality loss requires a newly added edge

### Theorem CMR643 — PROVED

Let `H` be a balanced bipartite host with a perfect matching, let `e` be
essential in `H`, and let

\[
H'=(H-D)\cup A
\]

be any later host, where `D` is an arbitrary deleted-edge set and

\[
A\subseteq E(H')\setminus E(H)
\]

is the set of genuinely new edges relative to `H`.

If `H'` has a perfect matching `N` with

\[
e\notin N,
\]

then

\[
\boxed{N\cap A\ne\varnothing.}
\]

### Proof

If `N\cap A` were empty, then every edge of `N` would belong to `H`.  Thus `N`
would be a perfect matching of `H` avoiding the essential edge `e`, a
contradiction. ∎

Deleting old edges alone cannot destroy essentiality; some genuinely entering
edge is necessary.

## 2. Alternating-cycle support for essentiality loss

Fix any old perfect matching `M` of `H`.  Since `e` is essential,

\[
e\in M.
\]

### Theorem CMR644 — PROVED

Under the hypotheses of CMR643, the component of

\[
M\triangle N
\]

containing `e` is an alternating cycle and contains at least one edge of

\[
N\cap A.
\]

More generally, let

\[
R\subseteq E_{\mathrm{ess}}(H)\setminus N
\]

be any set of old essential edges omitted by `N`.  Every alternating-cycle
component of `M\triangle N` which meets `R` contains at least one edge of
`N\cap A`.  Hence, if `\chi(R;M,N)` is the number of such components, then

\[
\boxed{
\chi(R;M,N)
\le
|N\cap A|.
}
\]

### Proof

The symmetric difference of two perfect matchings is a disjoint union of even
alternating cycles.  Let `C` be a component containing an omitted essential
edge.  If `C` contained no edge of `N\cap A`, then every `N`-edge of `C` would
belong to `H`.  Flipping `M` along `C` would therefore give a perfect matching
of `H` omitting the essential `M`-edge on `C`, contradiction.

Distinct alternating components are edge-disjoint, so the newly added witness
edges selected from them are distinct. ∎

One new edge may unlock several essential edges only when they occur on the
same alternating cycle.

## 3. Exact forced-certificate escape trichotomy

Consider a later state with the same selector/envelope owner.  Its skeleton and
factor hosts may have changed.

### Theorem CMR645 — PROVED

If the later state does not contain the forced certificate `T`, then at least
one of the following holds.

1. **Certificate-edge deletion.**  Some edge of `T` is absent from the later
   host.
2. **Skeleton change.**  The later protected/free cross skeleton differs from
   `S`.
3. **Factor essentiality loss.**  The skeleton is still `S`, every edge of `T`
   remains present in the later host, but a later factor matching omits at least
   one edge of `T_I\cup T_J`.  For every affected alternating component, CMR644
   supplies a genuinely new factor edge.

### Proof

Assume branches 1 and 2 fail.  Then all certificate edges remain present and
the skeleton still supplies every edge of `T_S`.  If both later factor
matchings contain `T_I` and `T_J`, the later full state contains all of `T`,
contrary to hypothesis.  Hence one factor matching omits an old essential
certificate edge, giving branch 3 and CMR644. ∎

Internal matching variation inside unchanged factor hosts is therefore
incapable of escaping the certificate.

## 4. Finite owner-labelled escape-witness stock

Assign every escape event one canonical witness of the first applicable type:

1. one deleted certificate edge;
2. one physical edge in the skeleton symmetric difference;
3. one newly added factor edge on the lexicographically first affected
   alternating component.

### Theorem CMR646 — PROVED

At one fixed owner in a residual board of side `n`, the number of possible
owner-labelled physical witness edges is at most

\[
\boxed{3n^2.}
\]

For every integer `\lambda\ge2`, a history of `J` forced-certificate escape
events satisfies at least one of:

1. one exact owner-labelled witness edge occurs in at least `\lambda` escape
   events;
2. the escape history is finite:
   \[
   \boxed{
   J\le3(\lambda-1)n^2.
   }
   \]

### Proof

Each witness type is a physical parent-board edge, giving at most `n^2` choices
per type.  If no labelled witness occurs `\lambda` times, every one contributes
at most `\lambda-1` events.  Sum over the three labelled universes. ∎

The type label prevents a deletion occurrence from being confused with an
entering-edge or skeleton-churn occurrence on the same physical cell.

## 5. Exact token and churn payment

Assume the inherited parent has side

\[
m=p^g.
\]

### Theorem CMR647 — PROVED

Every forced-certificate escape event carries at least one owner-labelled
physical edge occurrence.  Consequently `J` escape events carry at least

\[
\boxed{
J(p+1)(g-1)
}
\]

labelled nonroot full-token incidences, counted with multiplicity.

More specifically:

1. repeated certificate-edge deletion/reappearance enters the absence-run and
   reintroduction ledger CMR519;
2. repeated skeleton witnesses enter the cross-edge churn ledger
   CMR626--CMR627;
3. repeated entering-edge witnesses enter the matching-state expansion and
   packet/full-token recreation ledgers CMR413--CMR421.

### Proof

CMR413 assigns exactly `(p+1)(g-1)` labelled nonroot token incidences to every
physical parent edge occurrence.  CMR645 gives at least one such occurrence per
escape.  The three refinements are precisely the cited existing ledgers for the
three witness types. ∎

The statement counts occurrences; CMR646 isolates recurrence rather than
claiming repeated use is fresh physical stock.

## 6. Forced-product certificate endpoint

### Corollary CMR648 — PROVED

A forced product certificate from CMR639--CMR642 reaches at least one of the
following endpoints.

1. **Persistent forced class.**  The skeleton and factor hosts retain the
   certificate, so every state in the product class remains dirty.
2. **Finite escape history.**  The bound of CMR646 holds.
3. **Certificate-edge deletion/reintroduction.**  A fixed certificate edge is
   removed or repeatedly restored.
4. **Skeleton churn.**  Cross-interface changes pay CMR626--CMR627.
5. **Entering-edge alternating cycle.**  Essentiality loss is witnessed by an
   alternating cycle containing a genuinely new factor edge.
6. **Recurrent owner-labelled witness.**  One exact deletion, skeleton, or
   entering-edge witness recurs and enters the corresponding existing temporal
   ledger.

### Proof

If the certificate never disappears, use branch 1.  Otherwise apply CMR645 to
all escape events and CMR646.  Route recurrent witnesses by CMR647. ∎

## 7. Revised frontier

Forced product certificates now have an exact escape ledger.

- Staying inside unchanged factor hosts and skeletons cannot remove them.
- Deletion pays a certificate edge.
- Skeleton change pays sparse-interface churn.
- Essentiality loss pays a newly entering edge on an alternating cycle.
- Repeated escape uses a finite owner-labelled witness universe.

The remaining product-factor frontier is pure-factor recursion after all mixed
certificates have been deleted, contracted, or isolated.  The next target is an
exact inheritance theorem showing how candidate-conflict potential, protected
matching ownership, and full-token labels restrict to the contracted factor
hosts without recreating a previously paid mixed certificate anonymously.

No all-`n` theorem is claimed.  Essentiality-loss support and alternating-cycle
component payment are checked in
[`scripts/verify_prime_power_forced_product_escape.py`](../scripts/verify_prime_power_forced_product_escape.py).
