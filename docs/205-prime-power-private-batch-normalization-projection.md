# Private-batch normalization erases pure reopening cycles

CMR800--CMR806 show that a surviving anchor can re-close every restored private
batch. This operation is canonical. Fix a stored anchor `S` and the disjoint
private union

\[
D=A_1\sqcup\cdots\sqcup A_B,
\qquad D\cap S=\varnothing.
\]

For every same-vertex-set host `H` containing `S`, define

\[
\mathcal N_D(H)=H-D.
\]

This projection removes structural credit from repeated reopening of already
paid private edges while retaining every genuine physical restoration charge.

## 1. Canonical anchor-preserving projection

### Theorem CMR807 -- PROVED

For every host `H` containing `S`,

1. `S` is feasible in `\mathcal N_D(H)`;
2. `\mathcal N_D(H)` contains no edge of `D`;
3.
   \[
   \boxed{
   \mathcal N_D(\mathcal N_D(H))=\mathcal N_D(H).
   }
   \]

### Proof

The anchor avoids `D`, so removing `D` preserves it. The remaining assertions
are immediate from set subtraction. ∎

## 2. Pure private reopening disappears under normalization

### Theorem CMR808 -- PROVED

For every restored subset `R\subseteq D`,

\[
\boxed{
\mathcal N_D(H\cup R)=\mathcal N_D(H).
}
\]

The same conclusion holds whenever two hosts agree outside `D`.

### Proof

Normalization removes all edges of `D` from both hosts. ∎

## 3. Exact pure-reopening cycle erasure

### Theorem CMR809 -- PROVED

Suppose a reset begins at the normalized anchor state

\[
(S,\mathcal N_D(H)),
\]

changes only edges of `D`, and is followed by stored-anchor bulk reclosure. The
final selected state and normalized host equal the initial ones, so the segment
is cycle-erasable.

### Proof

The selected state is again `S`, and CMR808 gives the same normalized host. Apply
the exact-state erasure principle CMR410. ∎

Physical restorations inside the erased segment still retain their CMR797 token
charge; they simply create no new structural state.

## 4. Nonerasable changes use nonprivate edges

### Theorem CMR810 -- PROVED

For anchor-containing hosts `H,H'`, if

\[
\mathcal N_D(H)\ne\mathcal N_D(H'),
\]

then

\[
\boxed{
(E(H)\triangle E(H'))\setminus D\ne\varnothing.
}
\]

### Proof

Both normalized hosts contain no private edge. Their difference must therefore
lie outside `D`. ∎

## 5. Finite context stock or exact recurrence

For each nontrivial transition between normalized hosts, choose the first edge
of the nonprivate symmetric difference.

### Theorem CMR811 -- PROVED

For every integer `lambda>=2`, a history of `J` nontrivial normalized transitions
reaches at least one of:

1. one exact labelled nonprivate edge in at least `lambda` transitions;
2.
   \[
   \boxed{J\le(\lambda-1)2N^2.}
   \]

### Proof

CMR810 gives one witness per transition, from an absolute labelled universe of
size at most `2N^2`. Apply pigeonhole. ∎

## 6. Normalized change or paid restoration

### Theorem CMR812 -- PROVED

Every reset followed by private normalization reaches at least one of:

1. the identical normalized anchor state, hence exact cycle erasure;
2. a nonprivate context-edge change;
3. loss of one stored anchor edge;
4. contraction or owner/envelope change;
5. genuine private-edge restoration with CMR797 token payment.

### Proof

If the anchor survives, compare normalized hosts and use CMR809 or CMR810. If the
anchor fails, use CMR801. Structural exits and restoration payment are the
remaining cases. ∎

## 7. Private-normalization endpoint

### Corollary CMR813 -- PROVED

Repeated resets cannot obtain unbounded structural progress by restoring and
re-closing the same private batches. Every continuation reaches cycle erasure, a
nonprivate context witness, a missing anchor edge, paid physical restoration,
permanent private deletion, contraction, owner descent, envelope expansion, or
strict potential improvement.

### Proof

Combine CMR807--CMR812 with CMR793--CMR806 and CMR777--CMR784. ∎

No all-`n` theorem is claimed. Projection identities, pure-reopening erasure,
nonprivate witness extraction, and recurrence arithmetic are checked in
[`scripts/verify_prime_power_private_batch_normalization.py`](../scripts/verify_prime_power_private_batch_normalization.py).
