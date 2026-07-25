# Laminar fine-to-coarse sweeps have a geometric token-reintroduction budget

CMR347 shows that repeated visits to one token are paid by initial endpoint
stock plus edge reintroductions. CMR350 shows that arbitrary rematching resets
can restore the entire state, so no bound is possible without a scheduling
hypothesis. The natural prime-power schedule is laminar: at each prefix depth,
process pairwise disjoint blocks once, then move to the next coarser depth.
Within such a sweep, token-compatible reintroduction is bounded by the old row
stock, not by the size of the candidate board.

Work in one fixed inherited envelope of normalized size

\[
t=p^h.
\]

By CMR172, each permutation layer has its initial envelope row set throughout
the envelope epoch. Normalize that row set to `[t]`. Fix a row-prefix token

\[
\tau=(b,c,\theta),
\qquad
0\le b<h.
\]

Only the row condition matters for reintroduction, so put

\[
U_\tau=
\{(x,y)\in[t]^2:y\equiv c\pmod{p^b}\}.
\]

A rematching reuses the currently occupied rows on its selected columns. An old
occupied edge which becomes unoccupied is **vacated**. In a residual parent
host, every token edge reintroduced solely because of this rematching is a
vacated token edge; occupation by the other layer can only reduce the actual
reintroduction count.

## 1. One rematching is paid by vacated rows

### Theorem CMR378 — PROVED

Let one permutation layer be rematched on a column set `B`, using exactly its
current row set `R_B`. The number of token-compatible host edges reintroduced by
the move is at most

\[
\boxed{
|R_B\cap(c+p^b\mathbb Z)|.
}
\]

In particular, a complete rematching of the whole envelope reintroduces at most

\[
\boxed{\frac{t}{p^b}}
\]

token edges in one layer.

### Proof

The only edges made newly available by changing the occupied matching are old
occupied edges which the new matching vacates. Every old edge is determined by
its occupied row. At most one old edge is associated with each row of `R_B`,
and it belongs to `U_\tau` exactly when that row is congruent to `c` modulo
`p^b`. This proves the first bound.

The normalized envelope row set is `[t]`, which contains exactly `t/p^b` rows
in the chosen residue class. ∎

## 2. One prefix depth has no multiplicity loss

### Theorem CMR379 — PROVED

Fix one prefix depth `a`. Let `B_1,\ldots,B_m` be pairwise disjoint depth-`a`
column blocks, and rematch each selected block at most once in one permutation
layer. Then the total number of token-compatible edges reintroduced across all
those moves is at most

\[
\boxed{\frac{t}{p^b}}.
\]

For an old-cell-clean two-layer sweep at that depth, the total is at most

\[
\boxed{\frac{2t}{p^b}}.
\]

### Proof

The current row sets over pairwise disjoint column blocks are disjoint because
a permutation layer uses each row once. Apply CMR378 and sum. The intersections
of those row sets with one residue class are disjoint subsets of the
`t/p^b` envelope rows in that class. The two layers are counted separately. ∎

No descendant row-balance hypothesis is used here; only disjointness of the
current row sets is needed.

## 3. Complete laminar sweep

A **one-pass laminar sweep** is a repair schedule in which, for each depth
`a=0,1,\ldots,h-1`, every selected depth-`a` block is rematched at most once per
layer, and selected blocks at the same depth are pairwise disjoint.

### Theorem CMR380 — PROVED

For one layer, a one-pass laminar sweep reintroduces at most

\[
\boxed{
\frac{ht}{p^b}
}
\]

token-compatible edges. For an old-cell-clean two-layer sweep, the total is at
most

\[
\boxed{
\frac{2ht}{p^b}.
}
\]

### Proof

Apply CMR379 at each of the `h` possible prefix depths and sum. ∎

The estimate counts reintroductions with multiplicity, exactly as required by
CMR347.

## 4. Repeated-token visits in a laminar sweep

### Corollary CMR381 — PROVED UNDER THE SWEEP HYPOTHESIS

Consider a CMR349 certificate-directed deletion process interleaved with one
old-cell-clean two-layer laminar sweep. Then

\[
\boxed{
J_\tau
\le
\frac{t^2}{p^b}
+
\frac{2ht}{p^b}
+
X_\tau+F_\tau.
}
\]

After the initial token-edge stock is exhausted, the additional token-paid
visits caused by the whole sweep number at most

\[
\boxed{\frac{2ht}{p^b}.}
\]

At the cubic-root deep threshold `p^b\ge t^{2/3}`, this additional amount is at
most

\[
\boxed{2h\,t^{1/3}.}
\]

### Proof

CMR349 gives

\[
J_\tau\le \frac{t^2}{p^b}+I_\tau+X_\tau+F_\tau.
\]

CMR380 bounds the reintroduction term by `2ht/p^b`. The final specialization is
immediate. ∎

## 5. Revised coarse-to-fine endpoint

The CMR350 two-step return remains a genuine obstruction to unrestricted
resampling. However, the canonical no-repeat-per-depth sweep has a finite and
scale-sensitive recreation budget. For deep tokens, the reintroduction cost is
only `O(h t^(1/3))` at the cubic threshold, while CMR371 supplies
`Omega_p(t^(2/3)/log t)` occupied deep tokens and an `Omega(t^(1/3))`
simultaneous elimination capacity.

The remaining scheduling theorem must compare these quantities across many
tokens and prevent repeated full sweeps inside one envelope epoch. Witness
escapes and fully forced ancestry remain separate terms.

No all-`n` theorem is claimed here. The disjoint-row accounting and all scale
specializations are checked in
[`scripts/verify_prime_power_laminar_reintroduction.py`](../scripts/verify_prime_power_laminar_reintroduction.py).
