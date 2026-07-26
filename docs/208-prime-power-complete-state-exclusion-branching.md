# Single-edge branching excludes one state without losing completeness

CMR785--CMR821 define a useful anchor-preserving normalization: reject a
nonimproving candidate by deleting its whole entering batch. That operation
preserves the anchor and gives strong private-edge accounting, but it may also
remove other untested states. It is therefore one valid structural branch, not a
complete search of the original feasible family.

There is an exact completeness-preserving replacement. To exclude one selected
state, branch on deleting one of its labelled edges. Because all feasible states
have the same cardinality, every different state omits at least one edge of the
rejected state and survives in at least one branch. Empty branches are discarded.
The union of viable children is exactly the original family minus the one
rejected state.

Let `\mathcal F` be a nonempty family of labelled saturated two-layer states,
each of cardinality `2n`, and fix one state

\[
Q\in\mathcal F.
\]

For a labelled edge `f`, write

\[
\mathcal F-f=\{R\in\mathcal F:f\notin R\}.
\]

## 1. Exact state-exclusion identity

### Theorem CMR830 -- PROVED

One has

\[
\boxed{
\mathcal F\setminus\{Q\}
=
\bigcup_{f\in Q}(\mathcal F-f).
}
\]

### Proof

The state `Q` belongs to no branch because it contains every `f\in Q`. Let
`R\in\mathcal F` be different from `Q`. Since `|R|=|Q|=2n`, the inclusion
`Q\subseteq R` would force equality. Hence some edge `f\in Q\setminus R` exists,
and `R\in\mathcal F-f`. ∎

Equal cardinality is the only property needed for the identity.

## 2. Viable branches preserve every alternative state

Call the branch `f` viable when `\mathcal F-f` is nonempty.

### Theorem CMR831 -- PROVED

After discarding empty branches,

\[
\boxed{
\mathcal F\setminus\{Q\}
=
\bigcup_{\substack{f\in Q\\\mathcal F-f\ne\varnothing}}
(\mathcal F-f).
}
\]

Every alternative state `R\ne Q` certifies at least one viable branch, namely any
`f\in Q\setminus R`.

### Proof

The branch containing `R` is nonempty because it contains `R`. Apply CMR830. ∎

No matching-feasibility assumption is made for a branch which is empty.

## 3. Nonimproving state rejection preserves all improving states in the union

Let `\Phi` be the real-triple potential and suppose `Q` is a candidate with

\[
\Phi(Q)\ge\Phi(S_0)
\]

for the current baseline state `S_0`.

### Theorem CMR832 -- PROVED

Replacing `\mathcal F` by the collection of viable child families

\[
\{\mathcal F-f:f\in Q,\ \mathcal F-f\ne\varnothing\}
\]

removes `Q` but preserves every other state, including every state of potential
strictly below `\Phi(S_0)`, in at least one child branch.

### Proof

This is CMR831 applied to the subset of improving states. ∎

Thus single-edge branching is completeness-preserving even though the aggressive
entering-batch branch need not be.

## 4. Every branch has polynomial deletion depth

Follow one root-to-leaf branch of repeated state exclusions. At each step delete
one edge of the rejected state and retain only a viable child.

### Theorem CMR833 -- PROVED

Along one branch, all deleted labelled edges are distinct and the branch depth is
at most

\[
\boxed{2n^2-2n.}
\]

### Proof

A rejected state is feasible under the current mask, so every edge chosen from it
is currently present and has not been deleted earlier on the branch. Hence branch
deletions are distinct. The two labelled layer hosts contain at most `2n^2`
edges, while every viable leaf contains a saturated state of `2n` edges. ∎

The depth is polynomial although the number of branches may still be large.

## 5. A fixed improving witness determines one surviving branch

### Theorem CMR834 -- PROVED

Suppose an improving state `R_*\in\mathcal F` exists. For every rejected state
`Q\ne R_*`, choose the first edge

\[
f(Q)\in Q\setminus R_*.
\]

Then the branch which deletes `f(Q)` preserves `R_*`. Repeating this choice gives
a viable deletion path of length at most `2n^2-2n` on which `R_*` survives every
rejection.

### Proof

The chosen edge is absent from `R_*`, so deleting it preserves `R_*` and makes the
child viable. Distinctness and the length bound are CMR833. ∎

This is an existential completeness statement, not an algorithm for locating an
unknown improving witness.

## 6. Relation to aggressive anchor-batch normalization

### Theorem CMR835 -- PROVED

For a rejected state `Q` and anchor `S`, the CMR786 entering-batch child

\[
\mathcal F-A(Q),
\qquad A(Q)=Q\setminus S,
\]

is contained in every single-edge child `\mathcal F-f` with `f\in A(Q)`:

\[
\boxed{
\mathcal F-A(Q)
\subseteq
\mathcal F-f.
}
\]

Hence the anchor-batch pass is a valid simultaneous-deletion subbranch of the
complete state-exclusion tree, but generally not the union of all viable
children.

### Proof

Every state avoiding all edges of `A(Q)` avoids each particular `f\in A(Q)`. ∎

The private-batch and normalization ledgers remain valid on that subbranch.

## 7. Terminal leaves and forced prescriptions

### Theorem CMR836 -- PROVED

At a viable leaf of the complete branching process, at least one of the following
holds.

1. A state of strictly smaller potential has been retained.
2. No further selected state is rejected under the chosen scheduler criterion.
3. The surviving family has a fixed labelled edge or pair, which contracts by the
   essential-core or labelled-pair factorisation.
4. The scheduler changes target, owner, factor, or envelope.

If a physical target occurs in every surviving state of a leaf, the labelled-pair
normalisation CMR790 may be applied inside that leaf, but the resulting
contraction is a leaf-local statement.

### Proof

The first two alternatives describe the stopping rule. A prescription common to
all surviving states is essential in that family and contracts by the existing
exact restriction bijections. Target and owner changes are the remaining
scheduler exits. The final sentence records the scope of CMR790--CMR791. ∎

No leaf-local forcedness is promoted to the original family without the union of
branches.

## 8. Completeness-corrected anchor endpoint

### Corollary CMR837 -- PROVED

A nonimproving candidate has two distinct valid responses.

1. **Aggressive normalization branch.** Delete its complete anchor-entering batch.
   This preserves one anchor, gives private deletion and return payment, and may
   discard other states.
2. **Complete exclusion branching.** Create the viable single-edge deletion
   children from CMR831. Their union preserves every state except the rejected
   candidate, and every root-to-leaf path has depth at most `2n^2-2n`.

Therefore the private-batch theory is a rigorous structural subbranch, while a
complete existence argument must either control the width of the CMR831 branch
tree or prove that one aggressive branch retains a desired improving state.

### Proof

Combine CMR830--CMR836 with CMR785--CMR821. ∎

No all-`n` theorem is claimed. Exact union identities, viable-branch coverage,
branch depth, witness-preserving paths, and aggressive-branch containment are
checked in
[`scripts/verify_prime_power_complete_state_exclusion.py`](../scripts/verify_prime_power_complete_state_exclusion.py).
