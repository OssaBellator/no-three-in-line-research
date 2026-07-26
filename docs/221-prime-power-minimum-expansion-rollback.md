# Same-value host expansions are exactly rollbackable

CMR926--CMR933 show that new minimum states under host expansion use added
physical edges.  For a minimum-anchor proof, this yields a stronger scheduler
rule.  If an expansion lowers the minimum potential, it is a strict improvement.
If it does not, the old minimum states remain feasible and the entire added batch
can be removed again.

For an arbitrary same-vertex-set transition, factor through the intersection
host.  If an old minimum survives the restriction part, every subsequent
same-value addition rolls back to the intersection.  If no old minimum survives,
the old canonical state has a concrete lost-edge witness.  The intersection may
have an empty feasible family; that is automatically the second case.

## 1. Pure expansion is improvement or rollback

Let `H\subseteq H'` and assume both feasible families are nonempty.

### Theorem CMR934 -- PROVED

Exactly one of the following holds.

1. `m(H')<m(H)`.
2. `m(H')=m(H)`, every old minimum remains minimum in `H'`, and deleting
   \[
   A=H'\setminus H
   \]
   restores
   \[
   \boxed{
   \mathcal F(H'-A)=\mathcal F(H),
   \qquad
   m(H'-A)=m(H').
   }
   \]

### Proof

CMR927 gives `m(H')\le m(H)`.  Under equality the old face embeds in the new
one.  Removing exactly the added edges returns the host, feasible family, and
minimum value to their original forms. ∎

## 2. Canonical expansion scheduler

### Theorem CMR935 -- PROVED

A minimum-anchor scheduler may accept a pure expansion only when it lowers the
minimum.  Otherwise it deletes all added edges and retains the old canonical
minimum.  The normalized host and retained value are unchanged.

### Proof

Apply CMR934. ∎

## 3. Pure restoration cycles are erasable

Suppose a batch `A` of absent edges is restored, no other edge changes, and the
minimum does not decrease.

### Theorem CMR936 -- PROVED

After canonical rollback, the selected minimum state, minimum value, and host are
exactly those before restoration.  The segment is cycle-erasable.

The restorations retain their exact CMR413 token incidence but receive no new
structural credit.

### Proof

The temporary host is `H\cup A`; CMR935 returns it to `H` with the old canonical
minimum. ∎

## 4. Arbitrary transitions reduce through the intersection

Let

\[
K=H_0\cap H_1,
\qquad
D=H_0\setminus H_1,
\qquad
A=H_1\setminus H_0.
\]

### Theorem CMR937 -- PROVED

Assume `m(H_1)\ge m(H_0)`.  Exactly one of the following holds.

1. Some old minimum survives in `K`.  Then `\mathcal F(K)` is nonempty and
   \[
   m(K)=m(H_0)=m(H_1).
   \]
   Deleting `A` from `H_1` returns to `K` while preserving the minimum.
2. No old minimum survives in `K`.  Then the canonical old minimum contains an
   edge of `D`.  This includes the case `\mathcal F(K)=\varnothing`.

### Proof

In case 1, CMR926 gives `m(K)=m(H_0)`.  Since expansion gives
`m(H_1)\le m(K)` and the hypothesis gives the reverse lower bound, all three
values agree.  Apply CMR934 to `K\subseteq H_1`.

In case 2, the canonical old minimum is infeasible in `K`, so it contains an
edge of `H_0\setminus K=D`; no minimum value for `K` is needed when its feasible
family is empty. ∎

## 5. Canonical no-improvement transition

### Theorem CMR938 -- PROVED

Every same-vertex-set transition with no strict minimum decrease can be replaced
by one of:

1. a monotone restriction from `H_0` to `K` preserving an old minimum, with all
   added edges rolled back;
2. a minimum-loss event with one canonical lost edge of the old minimum;
3. contraction or owner/vertex-set exit.

No pure added-edge batch remains in the normalized no-improvement history.

### Proof

Apply CMR937 and roll back `A` in its first case. ∎

## 6. Monotone same-value restrictions have finite depth

Consider a normalized same-owner segment using branch 1 of CMR938 repeatedly.

### Theorem CMR939 -- PROVED

The hosts form a nested decreasing chain.  Every strict transition deletes a
previously available edge.  If the states have cardinality `k`, the number of
strict transitions is at most

\[
\boxed{|U|-k.}
\]

For saturated two-layer side `n`, this is at most `2n^2-2n`.

### Proof

The final nonempty host contains a feasible minimum state of `k` edges.  Because
the hosts are nested, those `k` edges survive every earlier host as well.  Hence
at most `|U|-k` distinct edges can be deleted along the chain. ∎

The common minimum core grows monotonically by CMR930.

## 7. Nonerasable transitions pay minimum-loss ancestry

At every branch-2 transition of CMR938, store the old canonical minimum and its
first lost edge.

### Theorem CMR940 -- PROVED

For `J` minimum-loss transitions and every `\lambda\ge2`, either one exact edge is
the witness at least `\lambda` times or

\[
\boxed{J\le(\lambda-1)|U|.}
\]

Repeated use of one witness is covered by one continuous absence run or requires
genuine restoration between loss generations.

### Proof

There is one witness in the finite edge universe for every transition.  Apply
pigeonhole and the physical absence-run identity. ∎

## 8. Expansion-rollback endpoint

### Corollary CMR941 -- PROVED

Every minimum-anchor same-vertex-set history reaches at least one of:

1. strict potential improvement;
2. exact rollback of a same-value added batch;
3. a finite monotone same-value restriction pass;
4. a lost edge of the old canonical minimum and forward ancestry;
5. recurrent loss/restoration with exact token payment;
6. minimum-core contraction;
7. factor, wall, owner, or envelope exit.

Thus restoration-only activity needs no independent capacity bound: if it fails
to improve the minimum, it is exactly rollbackable.  The remaining dynamic
obstruction is mixed loss/restoration ancestry across owner or vertex-set changes
and its geometric conversion into target-load, reserve, quotient/carry, or
envelope progress.

No all-`n` theorem is claimed.  Expansion rollback, empty intersections,
minimum survival, monotone restriction depth, lost-edge witnesses, and recurrence
arithmetic are checked in
[`scripts/verify_prime_power_minimum_expansion_rollback.py`](../scripts/verify_prime_power_minimum_expansion_rollback.py).
