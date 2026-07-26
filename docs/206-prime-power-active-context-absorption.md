# Active normalized context edges are absorbed or paid

CMR807--CMR813 reduce repeated private reopening to changes outside the current
private union. Not every host change matters to the target scheduler. An active
change either enables a new feasible target-destroying state, disables a state,
or destroys the stored anchor. State feasibility is edgewise: a newly enabled
state uses at least one newly available edge. If the state is nonimproving, the
anchor rule immediately places its complete entering set into the private union.
Therefore one context edge cannot repeatedly enable rejected states without
being physically restored between activations.

Fix one normalized anchor pass with anchor `S`, private union `D`, and current
host `H=\mathcal N_D(H)`. All hosts below have the same labelled vertex sets.

## 1. A newly enabled state uses a newly added edge

### Theorem CMR814 -- PROVED

Let `H'` be a later normalized host containing the same anchor, and let `R` be a
state feasible in `H'` but not in `H`. Then

\[
\boxed{R\cap(E(H')\setminus E(H))\ne\varnothing.}
\]

Every such edge lies outside `D`.

### Proof

If every edge of `R` already belonged to `H`, then the same labelled saturated
state would have been feasible in `H`; layer matching and layer-disjointness are
properties of `R` itself. Thus `R` uses a newly available edge. Both hosts are
normalized and contain no edge of `D`. ∎

This is activation support, not merely symmetric-difference support.

## 2. A rejected activated state absorbs its enabling edge

Suppose `R` is target-destroying relative to the anchor target and
`\Phi(R)\ge\Phi(S)`. Let

\[
A(R)=R\setminus S
\]

be its anchor-entering batch.

### Theorem CMR815 -- PROVED

Every newly added edge of `R` belongs to `A(R)`. Rejecting `R` by CMR786 therefore
adds at least one activation-support edge to the private union, together with the
complete batch `A(R)` of size at least two.

### Proof

The anchor was feasible before the transition, so every anchor edge already
belonged to `H`. An edge of `R` newly added in `H'` cannot belong to `S`; hence it
lies in `R\setminus S`. CMR786 deletes the entire entering batch. ∎

After normalization, the enabling edge is absent again.

## 3. Private-union growth is finite

### Theorem CMR816 -- PROVED

During one anchor epoch, activated nonimproving candidates can enlarge the
private union at most

\[
\boxed{n(n-1)}
\]

times, and the final private union satisfies

\[
\boxed{|D|\le2n^2-2n.}
\]

### Proof

Every activation response is one entering-batch deletion from CMR786. The
batches are pairwise disjoint by CMR793 and each has size at least two. Apply
CMR788. ∎

No routing or state label can evade this absolute edge bound.

## 4. Deactivation is monotone loss or paid return

### Theorem CMR817 -- PROVED

Let a previously feasible nonanchor state become infeasible between consecutive
normalized hosts. Then at least one labelled edge of that state is lost.

Within a segment with no physical restoration, the same labelled edge can be the
first-loss witness at most once. Across several segments, repeated use of that
edge as a loss witness requires intervening restoration and enters CMR777--
CMR784.

### Proof

A state is infeasible only if at least one of its labelled edges is unavailable.
Choose the first newly missing edge. Under a monotone no-restoration mask it
cannot return and be lost again. A later loss after a new availability interval
requires a physical restoration. ∎

State disappearance is therefore monotone progress unless it is explicitly
reopened.

## 5. Repeated activation of one context edge is restoration payment

### Theorem CMR818 -- PROVED

Suppose one exact nonprivate edge `e` enables a target-destroying candidate which
is rejected. Then `e` enters the private union by CMR815 and cannot enable another
normalized candidate while it remains absent.

If `e` supports `r` later activation episodes, it undergoes at least `r-1`
genuine restorations. Their exact labelled nonroot full-token incidence is at
least

\[
\boxed{(r-1)(p+1)(h-1).}
\]

### Proof

The first rejection deletes `e`. Every later feasible state using `e` requires
it to be restored. After each nonimproving activation it is deleted again by the
anchor batch. Apply CMR413 to the resulting restoration occurrences. ∎

An improving activation terminates instead of being privatized.

## 6. Fixed-anchor active-transition bound

Call a normalized transition **active** when it first enables a target-destroying
state, disables the current canonical candidate, or loses an anchor edge.

### Theorem CMR819 -- PROVED

Fix `lambda>=2`. Before strict improvement, contraction, or owner change, at
least one of the following holds.

1. One exact labelled physical edge is restored in at least `lambda` active
   transition histories.
2. The number `J` of active normalized transitions satisfies
   \[
   \boxed{
   J
   \le
   n(n-1)+2\lambda n^2.
   }
   \]

### Proof

Activated nonimproving candidates enlarge `D` and occur at most `n(n-1)` times by
CMR816. Every remaining active transition supplies a first-loss or restoration
witness edge by CMR817 or anchor loss CMR801. For each labelled edge, the number
of maximal absence runs is at most one plus its restoration count. If no edge is
restored `lambda` times, there are at most `lambda` absence runs per edge and at
most `2lambda n^2` such witness slots. Sum the two contributions. ∎

The bound is deliberately coarse but independent of the number of feasible
states and routing skeletons.

## 7. Anchor-normalized context endpoint

### Theorem CMR820 -- PROVED

At one fixed labelled owner, repeated normalized context changes reach at least
one of:

1. strict target-potential improvement;
2. finite private-union growth;
3. finite monotone candidate or anchor loss;
4. one recurrent restored context edge with exact token payment;
5. forced target-pair contraction;
6. exact normalized cycle erasure;
7. owner, factor, wall, or envelope descent.

### Proof

Use CMR814--CMR819 together with the anchor scheduler CMR785--CMR792 and the
normalization alternatives CMR807--CMR813. ∎

## 8. Branch-wide active-context endpoint

### Corollary CMR821 -- PROVED

Along a canonical target-driven prime-power branch, context changes outside
private deletion unions cannot form a new anonymous recurrence class. After the
finite owner, wall, factor, and envelope stocks, every unbounded continuation is
reduced to one exact restored physical edge, and every nonimproving use of that
edge is immediately privatized again.

The remaining global task is therefore concentrated on histories in which the
same physical edge is genuinely restored across owner epochs often enough to
survive bulk redeletion, anchor replacement, normalization, and strict factor
descent.

### Proof

Apply CMR820 in each owner epoch and aggregate owner exits with CMR693, CMR742,
and CMR754. Physical recurrence is owner-independent by CMR777. ∎

No all-`n` theorem is claimed. Activation support, private absorption, loss-run
accounting, and active-transition bounds are checked in
[`scripts/verify_prime_power_active_context_absorption.py`](../scripts/verify_prime_power_active_context_absorption.py).
