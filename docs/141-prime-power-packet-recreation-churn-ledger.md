# Packet recreation is supported by returned-edge churn

CMR413--CMR417 show that exact state cycles are erasable and that every genuinely
new selected parent state pays returned-edge and full-token incidence mass.  The
remaining packet-scheduling question is whether a later exact covering can
recreate conflicts from an earlier clean packet.  Such recreation has an exact
support: every newly present old-packet triple contains an edge returned by the
latest reset.

This chapter converts packet no-return into a churn ledger.  It does not yet
bound total churn, but it removes packet recreation as an independent source of
complexity.

Let `H,H'` be two represented-cell hosts on the same parent board and put

\[
R=H'\setminus H.
\]

For a family `\mathcal C` of candidate-only triples, call `H`
`\mathcal C`-clean when no member of `\mathcal C` is contained in `H`.

## 1. Universal recreation support

### Theorem CMR418 — PROVED

Assume `H` is `\mathcal C`-clean.  Every conflict

\[
C\in\mathcal C,
\qquad
C\subseteq H',
\]

contains at least one returned edge:

\[
\boxed{C\cap R\ne\varnothing.}
\]

Consequently, if

\[
\Delta(\mathcal C)
=
\max_e|\{C\in\mathcal C:e\in C\}|,
\]

then the number of conflicts from `\mathcal C` present in `H'` is at most

\[
\boxed{|R|\Delta(\mathcal C).}
\]

### Proof

If `C\subseteq H'` and `C\cap R=\varnothing`, then every edge of `C` already
belongs to `H`; hence `C\subseteq H`, contradicting cleanliness.  For the count,
assign each recreated conflict to one returned edge it contains and use the
maximum conflict degree. ∎

The theorem applies to any host reset.  It does not require the new selected
matching to be old-cell-clean.

## 2. One harmonic packet

Let `\mathcal K` be one harmonic packet with

\[
W(\mathcal K)
=
\sum_{K\in\mathcal K}\frac1K
<\frac32,
\]

and let `\mathcal C_{\mathcal K}` be its represented candidate-only triple
system.

### Corollary CMR419 — PROVED

If `H` is clean for the packet and a reset returns `R`, then the number of packet
triples recreated in `H'` is at most

\[
\boxed{
2(t-1)^2W(\mathcal K)|R|
<
3t^2|R|.
}
\]

In particular, the packet remains clean whenever no returned edge belongs to
any packet triple.

### Proof

Apply CMR418 and the harmonic conflict-degree bound CMR386.  The final statement
is the zero-incidence case. ∎

Thus packet protection can be formulated entirely as a restriction on the old
matching edges vacated by later resets.

## 3. Several previously clean packets

Let `\mathcal K_1,\ldots,\mathcal K_P` be pairwise disjoint harmonic packets.
For `A\subseteq[P]`, put

\[
\mathcal K_A=\bigcup_{q\in A}\mathcal K_q,
\qquad
W_A=\sum_{K\in\mathcal K_A}\frac1K.
\]

The degree estimate CMR386 does not require `W_A<3/2`; only the exact covering
theorem does.

### Theorem CMR420 — PROVED

Consider a reset history.  Immediately before reset `j`, let `A_j` be the set of
packets which are clean, let `R_j` be the returned-edge set, and let `N_j` be the
number of triples from those packets which are present immediately after the
reset.  Then

\[
\boxed{
N_j
\le
2(t-1)^2W_{A_j}|R_j|.
}
\]

Hence, with

\[
C=\sum_j|R_j|,
\qquad
W_*=\sum_{q=1}^P W(\mathcal K_q),
\]

one has

\[
\boxed{
\sum_jN_j
\le
2(t-1)^2W_*C.
}
\]

If the packets partition dyadic heights from `H_0` through `t-1`, then

\[
W_*
\le
\sum_{K=H_0}^{t-1}\frac1K
\le
1+\log\frac{t}{H_0}
\le
1+\log t.
\]

### Proof

Before reset `j`, the host is clean for the union conflict system

\[
\mathcal C_{\mathcal K_{A_j}}.
\]

Apply CMR418.  CMR386 bounds the maximum degree of that union by

\[
2(t-1)^2W_{A_j}.
\]

Since `W_{A_j}\le W_*`, summation gives the second inequality.  The harmonic-sum
estimate follows from the integral bound. ∎

The sum counts recreated triple occurrences with reset multiplicity.  It is
therefore suitable for a dynamic ledger even when the same geometric triple is
recreated more than once.

## 4. First-dirty packet scheduling

Fix an order of the packets.  At each step, choose the first packet which is not
currently clean and install one of its exact covering states from CMR388.  A
packet **loss** is a transition in which a packet was clean immediately before a
reset and is not clean immediately afterward.

### Corollary CMR421 — PROVED

For every reset in the first-dirty schedule, exactly one of the following holds.

1. The targeted dirty packet becomes clean and no earlier clean packet is lost.
2. At least one earlier packet is lost, and every lost packet has a recreated
   triple containing a returned edge.

Let `L` be the total number of packet losses and `T` the number of packet
installations.  Then

\[
\boxed{T\le P+L}
\]

and

\[
\boxed{
L
\le
\sum_jN_j
\le
2(t-1)^2W_*C.
}
\]

Consequently,

\[
\boxed{
T
\le
P+2(t-1)^2W_*C.
}
\]

### Proof

The installed state is clean for its target packet by CMR388.  If no earlier
packet is lost, the first-dirty index advances.  Otherwise CMR418 gives the
returned-edge witness for each lost packet.

Each installation is a dirty-to-clean transition for its target packet.  Every
packet can undergo one initial cleaning, giving at most `P` such transitions.
Every later cleaning of the same packet must follow an earlier clean-to-dirty
loss.  Thus `T\le P+L`.  Each loss contributes at least one recreated triple, so
`L\le\sum_jN_j`; apply CMR420. ∎

This is a conditional termination reduction rather than a complete termination
theorem.  Once cumulative returned-edge churn `C` is bounded by a monotone global
quantity, the entire first-dirty packet schedule has a polynomial length bound.
Together with CMR417, both distinct-state expansion and packet recreation are now
paid by the same churn variable.

The remaining frontier is therefore narrower:

1. prove a global upper bound on cumulative churn from target-load destruction,
   reserve depletion, or envelope expansion; or
2. show that any excess churn opens enough fully forced exchange ancestry to
   permit simultaneous resampling.

No all-`n` theorem is claimed here.  Recreation support, harmonic degree charges,
packet-loss accounting, and first-dirty schedule inequalities are checked in
[`scripts/verify_prime_power_packet_recreation_churn.py`](../scripts/verify_prime_power_packet_recreation_churn.py).
