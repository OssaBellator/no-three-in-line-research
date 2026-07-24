# Global-baseline compression for alternating closure

CMR107--CMR112 turn a concentrated prime-power child pencil into an explicit
alternating endpoint bank. The remaining difficulty is that a second-generation
bank is based at a state which may already have larger potential than the
original state. This chapter keeps one fixed global comparison baseline and
proves a branch-and-bound conversion theorem.

Let `Phi(S)` denote the number of real collinear triples in `S`.

## 1. Transfer across a fixed global baseline

Fix a baseline saturated state `S_0`. Let

\[
S_*=X\cup B
\]

be a saturated state in the alternating closure, where `B` is the current
endpoint block. Let `Omega(F)` be a matching bank on the columns and rows of `B`,
and write

\[
S_\pi=X\cup M_\pi,
\qquad \pi\in\Omega(F).
\]

Put

\[
e=\Phi(S_*)-\Phi(S_0),
\qquad
D=\Phi(S_*)-\Phi(X).
\]

### Theorem CMR123 — PROVED

If no state in the bank improves the global baseline,

\[
\Phi(S_\pi)\ge\Phi(S_0)
\qquad\text{for every }\pi\in\Omega(F),
\]

then every bank state satisfies

\[
\boxed{
\Phi(S_\pi)-\Phi(X)\ge D-e.
}
\]

In particular, if the bank destroys an extracted star of size `t`, so that
`D>=t`, then either

\[
e\ge\frac t2,
\]

or every globally nonimproving state has at least `t/2` real triples touching
its replacement matching.

### Proof

The identity

\[
\Phi(S_\pi)-\Phi(X)
=
\bigl(\Phi(S_\pi)-\Phi(S_0)\bigr)
+
\bigl(\Phi(S_0)-\Phi(S_*)\bigr)
+
\bigl(\Phi(S_*)-\Phi(X)\bigr)
\]

is exactly

\[
\Phi(S_\pi)-\Phi(X)
=
\bigl(\Phi(S_\pi)-\Phi(S_0)\bigr)-e+D.
\]

The first term on the right is nonnegative. The final assertion follows from
`D>=t`. ∎

The alternative `e>=t/2` is a paid branch: that state already lies at least
`t/2` above the global minimum target and need not be explored when searching
for a strict improvement over `S_0`.

## 2. A geometric compression lemma

Let `S=X union M` be any saturated two-permutation state. Let `H` be the simple
three-uniform hypergraph whose edges are the real collinear triples in `S` that
touch `M`. Thus

\[
|H|=\Phi(S)-\Phi(X).
\]

A matching in `H` means a family of vertex-disjoint collinear triples.

### Theorem CMR124 — PROVED

Let `s>=7`. If

\[
|H|
\ge
12(s-1)^2(3s-2),
\]

then at least one of the following holds.

1. **Paid disjoint defects.** `H` contains `s` vertex-disjoint collinear
   triples.
2. **Alternating expansion.** There is a point `z` and `2s-1`
   endpoint-disjoint secants through `z` such that one can choose one endpoint
   from each of `s` secants in one fixed permutation layer. Those `s` endpoints
   support a CMR110 alternating matching bank which preserves saturation and
   destroys the `s` corresponding triples in every state.
3. **External line core.** A real line `L` contains more than `2s` points of
   `X`.

### Proof

Assume the first alternative fails. Take a maximal matching in `H`. It has at
most `s-1` edges, and the union of those edges is a vertex cover of `H` of size
at most `3(s-1)`. Hence some point `z` belongs to at least

\[
\frac{|H|}{3(s-1)}
\]

edges.

Form the link graph `G_z`: its vertices are the other selected points and its
edges are the pairs `{P,Q}` for which `{z,P,Q}` is an edge of `H`. If `G_z` has
a matching of size at least `2s-1`, count endpoint incidences by permutation
layer. One layer supplies at least `2s-1` incidences, and each matched pair
supplies at most two incidences. Therefore at least `s` matched pairs have an
endpoint in one fixed layer. Choose one such endpoint from each pair.

The chosen endpoints are distinct and, within one permutation layer, occupy
distinct rows and columns. Forbid their original cells and the cells occupied by
the other layer. The forbidden board has row and column degree at most two, so
CMR110 gives a nonempty matching bank. Moving every chosen endpoint destroys all
`s` original triples through `z`. This is the second alternative.

It remains to suppose that a maximal matching in `G_z` has at most `2s-2`
edges. Its endpoints form a vertex cover of `G_z` of size at most `4s-4`.
Consequently some point `w` has link degree at least

\[
\frac{|H|}{12(s-1)^2}
\ge
3s-2.
\]

There are therefore at least `3s-2` distinct points `u` such that `z,w,u` are
collinear. The line through `z,w` contains at least `3s` selected points.

If at least `s` of those line points belong to `M`, choose `s` of them and pair
each with two further unused points on the line. This gives `s` vertex-disjoint
collinear triples touching `M`, contradicting the failure of the first
alternative. Hence the line contains fewer than `s` points of `M`, and therefore
more than `2s` points of `X`. This is the third alternative. ∎

The theorem uses only saturation into two permutation layers and real
collinearity. It does not use a modular-to-real implication.

## 3. Conversion of a globally frozen endpoint bank

Suppose an extracted alternating bank has size `t>=7` and destroys `t` current
star triples. Keep the original state `S_0` as the global comparison baseline.

### Corollary CMR125 — PROVED

Put

\[
s(t)=\left\lfloor\left(\frac{t}{72}\right)^{1/3}\right\rfloor.
\]

If `s(t)>=7`, then at least one of the following holds.

1. Some endpoint-bank state has potential strictly below `Phi(S_0)`.
2. The chosen parent state has excess at least `t/2` over `S_0`.
3. Some globally nonimproving endpoint state contains `s(t)` vertex-disjoint
   real triples touching its replacement matching.
4. Some globally nonimproving endpoint state exposes a new alternating bank of
   size `s(t)`.
5. Some globally nonimproving endpoint state has an external line containing
   more than `2s(t)` points outside its replacement matching.

### Proof

If the first alternative fails, apply CMR123. If the parent excess is at least
`t/2`, the second alternative holds. Otherwise every endpoint state has at least
`t/2` triples touching its replacement matching.

Since

\[
\frac t2
\ge
36s(t)^3
>
12(s(t)-1)^2(3s(t)-2),
\]

CMR124 applies to any endpoint state and gives one of the final three
alternatives. ∎

The threshold `s(t)>=7` is guaranteed once

\[
t\ge72\cdot7^3=24696.
\]

Smaller banks form an absolute finite residual class rather than a scale-growing
obstruction.

## 4. Descending closure size

### Corollary CMR126 — PROVED

Follow only branches which

- do not improve the fixed global baseline;
- have parent excess below half the current star size;
- do not terminate in a paid disjoint-defect family or an external line core.

Then the successive alternating bank sizes satisfy

\[
t_{j+1}
\le
\left(\frac{t_j}{72}\right)^{1/3}
<
t_j^{1/3}.
\]

Hence every such branch reaches a bank of size below `24696` after
`O(log log t_0)` expansions. More explicitly, it is enough that

\[
3^j
\ge
\frac{\log t_0}{\log 24696}.
\]

### Proof

CMR125 supplies a new bank of exactly `s(t_j)` endpoints whenever none of the
other alternatives holds. Restricting an extracted star to exactly that many
pairs preserves the degree-two forbidden-board property. The displayed
recurrence follows. Iteration gives `t_j<=t_0^{3^{-j}}`, which proves the stated
bound. ∎

This is a genuine termination statement for uncharged alternating expansion:
an unbounded closure chain is impossible. The unresolved issue is to aggregate
the paid alternatives over all starting nodes and scales, and to eliminate the
absolute bounded residual class.

## 5. Paying external line cores

For a finite point set `X`, let

\[
\mathcal L_s(X)
=
\{L:|L\cap X|>2s\}.
\]

### Theorem CMR127 — PROVED

\[
\boxed{
|\mathcal L_s(X)|
\le
\frac{\Phi(X)}{\binom{2s+1}{3}}.
}
\]

At a low-excess closure node with parent excess `e<t/2`, this gives

\[
|\mathcal L_s(X)|
<
\frac{\Phi(S_0)+t/2}{\binom{2s+1}{3}}.
\]

### Proof

Every line in `L_s(X)` contains at least `binom(2s+1,3)` collinear triples of
`X`. A triple determines a unique real line, so the triple populations belonging
to distinct lines are disjoint. Summing them proves the first inequality.

Removing the endpoint block cannot create triples, so

\[
\Phi(X)\le\Phi(S_*)=\Phi(S_0)+e<\Phi(S_0)+t/2.
\]

This proves the second inequality. ∎

Thus the third CMR124 alternative is not an unstructured failure: it consumes a
heavy real-line signature already paid by the outside triple potential.

## 6. Remaining endpoint

The alternating concentration-conversion problem is reduced to two explicit
finite-accounting tasks:

1. sum the disjoint-defect and heavy-line payments over the family of starting
   prime-power nodes without repeated charging;
2. resolve or enumerate the absolute endpoint-bank residual class below
   `24696`.

No all-`n` theorem is claimed here. The global-baseline transfer and compression
inequalities are checked in
[`scripts/verify_prime_power_global_baseline_closure.py`](../scripts/verify_prime_power_global_baseline_closure.py).
