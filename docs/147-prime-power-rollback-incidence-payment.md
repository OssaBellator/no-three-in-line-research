# Sparse rollback has exact token incidence and packet recreation cost

CMR439--CMR443 show that every final essential edge admits a rollback footprint
of size at most `t`, while a large minimum footprint forces strict host
factorization.  This chapter pays the complementary cheap-rollback branch in
the ledgers already developed for full tokens and harmonic packets.

A restored edge occupies exactly one full-prefix cell at every nonroot depth and
for every direction label.  Thus rollback has an exact linear labelled token
cost.  Moreover, any conflict from a family which was clean before rollback
must use at least one restored edge, so the harmonic recreation bounds apply
without a selected-state transition.

Let

\[
t=p^h,
\qquad
G\subseteq K_{t,t},
\qquad
R\subseteq E(K_{t,t})\setminus E(G),
\]

and write `G+R` for the host obtained by restoring the edges of `R`.

## 1. Exact full-token incidence of rollback

For every nonroot depth `1\le b<h`, prefix pair `(a,c)` modulo `p^b`, and
direction `\theta\in\mathbb P^1(\mathbb F_p)`, let

\[
U_{(b,a,c,\theta)}^{(2)}
=
\{(x,y):x\equiv a\pmod{p^b},\ y\equiv c\pmod{p^b}\}.
\]

Define the labelled rollback incidence

\[
\mathcal I(R)
=
\sum_{\theta}
\sum_{b=1}^{h-1}
\sum_{a,c\bmod p^b}
|R\cap U_{(b,a,c,\theta)}^{(2)}|.
\]

### Theorem CMR444 — PROVED

For every finite restored-edge set `R`,

\[
\boxed{
\mathcal I(R)
=
(p+1)(h-1)|R|.
}
\]

### Proof

Fix one edge `(x,y)\in R`.  At each depth `b`, it belongs to exactly one prefix
pair,

\[
(a,c)=(x\bmod p^b,y\bmod p^b),
\]

and the full-token edge universe is repeated for all `p+1` direction labels.
Hence the edge contributes exactly `(p+1)(h-1)` labelled incidences.  Sum over
the distinct edges of `R`. ∎

This is the rollback analogue of the edge-incidence identity CMR413.

## 2. Cheap rollback payment

### Corollary CMR445 — PROVED

Let `e` be essential in the final host of a deletion pass and let `R_e` be a
minimum rollback set.  Then

\[
\boxed{
\mathcal I(R_e)
=
(p+1)(h-1)\kappa(e)
\le
(p+1)(h-1)t.
}
\]

For every threshold `q`, the cheap branch `\kappa(e)<q` has

\[
\boxed{
\mathcal I(R_e)
<
(p+1)(h-1)q.
}
\]

If `E_*` is the final essential core and one minimum rollback set is chosen for
each `e\in E_*`, then

\[
\boxed{
\sum_{e\in E_*}\mathcal I(R_e)
\le
(p+1)(h-1)t^2.
}
\]

### Proof

Apply CMR444 and the bounds

\[
\kappa(e)\le t,
\qquad
\sum_{e\in E_*}|R_e|\le t^2
\]

from CMR439 and CMR443. ∎

Thus every minimum rollback footprint for the whole essential core fits inside
an `O_p(t^2\log t)` labelled full-token budget.

## 3. Universal rollback recreation support

Let `\mathcal C` be any family of candidate edge sets and suppose `G` is
`\mathcal C`-clean: no member of `\mathcal C` is contained in `G`.  Put

\[
\Delta(\mathcal C)
=
\max_e|\{C\in\mathcal C:e\in C\}|.
\]

### Theorem CMR446 — PROVED

Every conflict

\[
C\in\mathcal C,
\qquad
C\subseteq G+R,
\]

contains a restored edge.  Consequently,

\[
\boxed{
|\{C\in\mathcal C:C\subseteq G+R\}|
\le
|R|\Delta(\mathcal C).
}
\]

### Proof

If `C\subseteq G+R` and `C\cap R=\varnothing`, then every edge of `C` already
belongs to `G`, contradicting cleanliness.  Assign each recreated conflict to
one restored edge it contains and use the maximum degree. ∎

This is the host-expansion form of CMR418.  Unlike the selected-state version,
there is no entering/leaving orientation issue: the support is literally the
restored set `R`.

## 4. Harmonic packet rollback cost

Let `\mathcal K` be a harmonic packet, with represented candidate-only triple
system `\mathcal C_{\mathcal K}` and weight

\[
W(\mathcal K)=\sum_{K\in\mathcal K}\frac1K.
\]

### Corollary CMR447 — PROVED

If `G` is clean for `\mathcal K`, restoring `R` creates at most

\[
\boxed{
2(t-1)^2W(\mathcal K)|R|
}
\]

packet triples.  In particular, if `W(\mathcal K)<3/2`, then the number is less
than

\[
\boxed{3t^2|R|.}
\]

For a union of packets which are all clean in `G`, with total harmonic weight
`W_A`, the corresponding bound is

\[
\boxed{
2(t-1)^2W_A|R|.
}
\]

If one minimum rollback set is chosen for each final essential edge, the total
recreation incidence over any fixed clean packet union is at most

\[
\boxed{
2(t-1)^2W_A t^2.
}
\]

### Proof

Apply CMR446 and the harmonic conflict-degree estimate CMR386,

\[
\Delta(\mathcal C_{\mathcal K})
\le
2(t-1)^2W(\mathcal K).
\]

The packet-union statement uses the same degree estimate with total weight
`W_A`.  Sum the resulting bound over the rollback sets and apply CMR443. ∎

The theorem counts recreated triple occurrences.  It does not assert that all
packets remain simultaneously clean after rollback.

## 5. Combined terminal endpoint

Let `Q` be a fully forced terminal certificate and choose a prescribed edge
`e\in Q`.  For every threshold `q`, CMR441 and CMR442 now give the following
exact alternative.

1. **Cheap common-epoch escape.** Restore fewer than `q` deleted edges and choose
   a perfect matching avoiding `Q`.  Its labelled full-token rollback cost is
   less than
   \[
   (p+1)(h-1)q,
   \]
   and every previously clean packet union of weight `W_A` gains at most
   \[
   2(t-1)^2W_A(q-1)
   \]
   represented triples.
2. **Strict factorization.** A minimum rollback set of size at least `q` is a
   forced matching in the avoiding host and factors the residual problem to side
   at most `t-q`.

Thus temporal lifting is no longer an unpriced existence operation.  It is
quantitatively integrated into both the full-token and harmonic-packet ledgers.
The remaining cheap-rollback task is qualitative: turn the restored-edge
support into target-load destruction, protected-reserve depletion, prefix or
line-clean continuation, or strict envelope expansion.

Repeated compatible local ancestor resets still lack a canonical final
essential edge to which the rollback number can be attached.

No all-`n` theorem is claimed here.  Exact labelled incidence, recreation
support, harmonic arithmetic, and threshold alternatives are checked in
[`scripts/verify_prime_power_rollback_incidence.py`](../scripts/verify_prime_power_rollback_incidence.py).
