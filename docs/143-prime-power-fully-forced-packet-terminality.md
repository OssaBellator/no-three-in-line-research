# Fully forced packet conflicts are terminal in one deletion pass

CMR422--CMR425 reduce lossy packet resets to permanent deletion or fully forced
exchange ancestry. A further monotonicity observation removes repeated fully
forced packet events from the same deletion pass: once an edge is essential, it
remains essential under every later edge deletion that preserves a perfect
matching. Hence a packet triple whose three edges are essential can never be
removed by choosing another perfect matching in the same residual host chain.

The packet schedule therefore has a polynomial completion-or-ancestry endpoint.
It either cleans every packet, or it stops at the first fully forced packet
certificate and hands that certificate to the CMR217 ancestry mechanism.

Let

\[
G_0\supseteq G_1\supseteq\cdots\supseteq G_d
\]

be any nested sequence of balanced bipartite hosts, each with at least one
perfect matching.

## 1. Essentiality is monotone under deletion

### Theorem CMR426 — PROVED

Suppose `e` is essential in `G_i`, and suppose

\[
e\in E(G_j),
\qquad
j\ge i.
\]

Then `e` is essential in `G_j`.

In particular, if every edge of a certificate `Q` is essential in `G_i` and all
of them remain present, then every perfect matching of every later `G_j`
contains `Q`.

### Proof

Every perfect matching of `G_j` is also a perfect matching of `G_i`, because
`G_j\subseteq G_i`. Since `e` belongs to every perfect matching of `G_i`, it
belongs to every perfect matching of `G_j`. Apply the same argument to each edge
of `Q`. ∎

An essential edge cannot itself be deleted while preserving a perfect matching.
Thus the persistence condition is automatic inside a matchability-preserving
deletion pass.

## 2. Fully forced packet terminality

### Corollary CMR427 — PROVED

Let `\mathcal K` be a harmonic packet and let

\[
Q\in\mathcal C_{\mathcal K}
\]

be a packet triple whose three edges are essential in the current residual host
`G_i`. Then:

1. every perfect matching of `G_i` contains `Q`;
2. every later perfect matching in the same deletion pass contains `Q`;
3. no selected-state reset inside that pass can make `\mathcal K` clean.

Consequently the fully forced alternative of CMR422 is a terminal packet
endpoint for the current deletion pass. Continuing packet installations without
changing the host epoch is impossible, not merely inefficient.

### Proof

Essentiality of all three edges means that every perfect matching contains all
three and therefore realizes `Q`. CMR426 preserves this conclusion in every
later matchable residual host. A state clean for `\mathcal K` would avoid every
packet triple, including `Q`, so no such state exists. ∎

Escaping this endpoint requires an operation outside the current deletion pass:
envelope expansion, host decomposition, reserve replacement, or simultaneous
exchange-cycle resampling.

## 3. Polynomial completion-or-ancestry bound

Run the first-dirty packet schedule of CMR421 with the immediate response policy
of CMR422. Stop at the first fully forced packet event. Let `P` be the number of
packets and `T` the number of packet installations performed before stopping or
completion.

### Theorem CMR428 — PROVED

Exactly one of the following occurs.

1. **Packet completion.** Every packet becomes clean after at most
   \[
   \boxed{
   P\bigl(1+t(t-1)\bigr)
   }
   \]
   installations.
2. **Terminal ancestry endpoint.** Before all packets are clean, a fully forced
   packet certificate appears after at most
   \[
   \boxed{
   P\bigl(2+t(t-1)\bigr)
   }
   \]
   installations. This certificate has at most three backward CMR217 ancestry
   links and is terminal for the current deletion pass by CMR427.

### Proof

Before the first fully forced event, every lossy reset is answered by a new
permanent deletion. By CMR423 there are at most `t(t-1)` such responses.

If no fully forced event occurs, the number `B` of lossy reset batches is at
most `t(t-1)`. At most `P` packet losses occur per batch, so CMR421 gives

\[
T\le P+P B\le P\bigl(1+t(t-1)\bigr).
\]

If a first fully forced event occurs, there is at most one additional terminal
lossy batch. Hence

\[
B\le t(t-1)+1
\]

and

\[
T\le P+PB\le P\bigl(2+t(t-1)\bigr).
\]

CMR422 and CMR217 give the ancestry links, and CMR427 gives terminality. ∎

CMR428 is unconditional inside one certificate-directed deletion pass. The
ancestry-width hypothesis of CMR425 is needed only for a larger mechanism which
resolves a forced endpoint and then starts a new host epoch. It is not needed to
bound the packet-installation sequence before the first forced endpoint.

## 4. Revised frontier

The harmonic-packet schedule now has a complete local termination statement:
within one deletion pass it either finishes in polynomially many installations
or reaches one fully forced rank-three ancestry certificate in polynomially
many installations.

Therefore the remaining fixed-envelope problem is no longer packet recurrence.
It is to resolve the terminal fully forced certificate by one of:

1. an incoming-width bound for CMR217 ancestry;
2. simultaneous flipping of several low-overlap CMR216 exchange cycles;
3. a strict envelope or host decomposition forced by a wide ancestry family; or
4. a p-adic signature theorem showing that wide ancestry consumes many distinct
   quotient, carry, or primitive-height resources.

No all-`n` theorem is claimed here. Essentiality persistence, terminal packet
obstruction, and the completion-or-ancestry installation bounds are checked in
[`scripts/verify_prime_power_forced_packet_terminality.py`](../scripts/verify_prime_power_forced_packet_terminality.py).
