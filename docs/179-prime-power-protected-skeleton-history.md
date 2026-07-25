# Large-core histories pay sparse-interface churn or expand one exact product factor

CMR617--CMR622 decompose every canonical derangement cylinder by its balanced
protected/free cross skeleton.  When the protected core has size `k` and the
free side has size `u=n-k`, every skeleton contains at most `2u` edges and the
state family under one skeleton is an exact product of a protected factor and a
free factor.

This chapter adds the temporal statement.  After exact full-state cycle
erasure, a long cylinder history either changes cross skeleton often or repeats
one skeleton many times.  Skeleton changes pay physical cross-edge churn from
a universe of only `2ku` edges.  Under one repeated skeleton, global state
diversity factors.  Since the free factor has side at most `u`, it has at most
`u!` states, so enough repetition forces many distinct protected-factor
matchings and therefore ordinary matching-state expansion inside one fixed
host.

Fix protected index set `I`, free set `J`, sizes

\[
|I|=k,
\qquad
|J|=u,
\qquad
k+u=n,
\]

and let

\[
\mathfrak S_{k,u}
\]

be the protected/free skeleton family of CMR619.  Put

\[
N_{\mathrm{sk}}(k,u)
=
|\mathfrak S_{k,u}|.
\]

Consider a sequence of cylinder states after exact repeated full states have
been erased as in CMR410--CMR411.

## 1. Finite skeleton stock or exact skeleton recurrence

### Theorem CMR623 — PROVED

For every integer `\lambda>=2`, any simple history of `T` cylinder states
satisfies at least one of the following.

1. **Exact skeleton recurrence.**  One protected/free cross skeleton occurs in
   at least `\lambda` states.
2. **Finite skeleton history.**
   \[
   \boxed{
   T
   \le
   (\lambda-1)N_{\mathrm{sk}}(k,u).
   }
   \]

Using CMR620,

\[
\boxed{
T
\le
(\lambda-1)(u+1)n^{4u}
}
\]

in the second branch.

### Proof

Assign each state its unique cross skeleton.  If no skeleton has multiplicity
`\lambda`, every one appears at most `\lambda-1` times.  Apply CMR619--CMR620.
∎

Thus large-core state history is finite unless one exact sparse interface
recurs.

## 2. Diversity under one fixed skeleton

Fix a skeleton `S` of size `2c`.  By CMR618 its state family is

\[
\operatorname{PM}(H_I(S))
\times
\operatorname{PM}(H_J(S)).
\]

Suppose `L` distinct full states occur with this skeleton.  Let `A` be the
number of distinct protected-factor restrictions and `B` the number of
distinct free-factor restrictions among those states.

### Theorem CMR624 — PROVED

One has

\[
\boxed{L\le AB.}
\]

Consequently

\[
\boxed{
\max\{A,B\}
\ge
\lceil\sqrt L\rceil.
}
\]

More sharply, because the free factor has side `u-c`,

\[
\boxed{
B
\le
|\operatorname{PM}(H_J(S))|
\le
(u-c)!
\le
u!,
}
\]

and therefore

\[
\boxed{
A
\ge
\left\lceil\frac{L}{u!}\right\rceil.
}
\]

### Proof

Every full state is uniquely determined by its pair of factor restrictions,
so at most `AB` distinct pairs occur.  The square-root conclusion follows.
The free host is bipartite of side `u-c`, so it has at most `(u-c)!` perfect
matchings, with equality only for a complete host.  Rearrange. ∎

When `u` is small, repeated skeleton states must diversify predominantly in the
protected factor.

## 3. Protected-factor state expansion

### Theorem CMR625 — PROVED

If one fixed skeleton supports `A` distinct protected-factor matchings, then
there is an ordering of those restrictions whose consecutive transitions have
at least two entering and two leaving factor edges.  Hence the total
protected-factor entering-edge occurrence count is at least

\[
\boxed{2(A-1),}
\]

and the same bound holds for leaving-edge occurrences.

Every such factor edge is a parent-grid edge and carries its exact labelled
full-token incidence from CMR413.

### Proof

Choose one occurrence of every distinct protected restriction and order them
by first occurrence.  Consecutive restrictions are distinct perfect matchings
of the same fixed host `H_I(S)`.  CMR415 gives at least two entering and two
leaving edges for every transition.  Sum over `A-1` transitions. ∎

Thus a fixed sparse interface does not hide free global motion: it pays
ordinary matching-state expansion inside one exact protected host.

## 4. Skeleton-change churn

The physical cross-edge universe is

\[
E_\times
=
(I\times J)\cup(J\times I),
\]

so

\[
\boxed{|E_\times|=2ku.}
\]

Let `R` be the number of consecutive history transitions at which the cross
skeleton changes.

### Theorem CMR626 — PROVED

Every skeleton-changing transition has cross-edge symmetric difference at
least two.  Therefore the total cross-edge churn, counted with multiplicity,
satisfies

\[
\boxed{
\sum_{t:\,S_t\ne S_{t+1}}
|S_t\triangle S_{t+1}|
\ge
2R.
}
\]

For every integer `\lambda>=2`, at least one of the following holds.

1. **Recurrent cross edge.**  One physical edge of `E_\times` belongs to at
   least `\lambda` skeleton-change symmetric differences.
2. **Finite skeleton-change count.**
   \[
   \boxed{
   R
   \le
   (\lambda-1)ku.
   }
   \]

### Proof

Every skeleton has even cardinality `2c`.  Two distinct skeletons therefore
have nonempty even symmetric difference, hence size at least two.

If no cross edge occurs in `\lambda` changed-transition differences, every
edge of the `2ku`-edge universe occurs at most `\lambda-1` times.  Combine the
upper incidence bound `2ku(\lambda-1)` with the lower bound `2R`. ∎

This is a physical-edge stock statement for interface changes.

## 5. Exact labelled interface churn

Assume the inherited parent has side `m=p^g`.

### Theorem CMR627 — PROVED

A skeleton-changing history with total physical cross-edge churn `C_\times`
has exact labelled nonroot full-token churn incidence

\[
\boxed{
(p+1)(g-1)C_\times.
}
\]

In particular, `R` skeleton changes carry at least

\[
\boxed{
2R(p+1)(g-1)
}
\]

labelled churn incidences.

### Proof

CMR413 assigns exactly `(p+1)(g-1)` nonroot token labels to every parent edge.
Apply this with multiplicity to every edge occurrence in the skeleton symmetric
differences and use CMR626. ∎

The statement is an occurrence ledger; if one physical edge recurs often,
CMR626 isolates it instead of declaring the occurrences fresh stock.

## 6. Combined large-core history endpoint

### Corollary CMR628 — PROVED

Let a canonical cylinder have protected size `k` and free size `u`.  After
exact full-state cycle erasure, every state history reaches at least one of the
following endpoints.

1. **Finite skeleton history.**  The CMR623 bound holds.
2. **Sparse-interface churn payment.**  Skeleton changes pay CMR626--CMR627,
   or one exact cross edge recurs.
3. **Free-factor diversity.**  Under one skeleton, the free factor of side at
   most `u` carries at least `\lceil\sqrt L\rceil` distinct states.
4. **Protected-factor expansion.**  Under one skeleton, the protected factor
   carries at least
   \[
   \left\lceil\frac{L}{u!}\right\rceil
   \]
   distinct matchings and the entering/leaving payment of CMR625.

When `u<=q`, the skeleton stock is at most `(q+1)n^{4q}`, every interface has
at most `2q` edges, and the free factor has side at most `q`.

### Proof

Apply CMR623.  Account for skeleton changes by CMR626--CMR627.  In a recurrent
skeleton class, apply CMR624--CMR625.  Use CMR621 for the threshold form. ∎

## 7. Revised frontier

Large protected-core histories now have both static and temporal normal forms.

- Static states factor over sparse protected/free skeletons.
- Frequent skeleton changes pay cross-edge churn.
- Repeated skeletons force factor-state diversity.
- Small free side gives a genuine lower-dimensional matching factor.

The remaining geometric step is to attach candidate-conflict potential to the
two product factors: show that protected-factor expansion, free-factor
recursion, or sparse-interface churn yields a clean state, protected-reserve
depletion, deletion ancestry, full-token return, or envelope expansion.

No all-`n` theorem is claimed.  Skeleton multiplicity, product diversity,
factor-state expansion, cross-edge churn, and labelled incidence are checked in
[`scripts/verify_prime_power_protected_skeleton_history.py`](../scripts/verify_prime_power_protected_skeleton_history.py).
