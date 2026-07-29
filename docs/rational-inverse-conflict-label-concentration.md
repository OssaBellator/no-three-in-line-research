# Label concentration inside heavy RI conflict neighborhoods

**Branch:** `research/rational-inverse-expansion`

RI5bv--RI5by show that failure of a requested `q`-component physical subbank returns one closed conflict neighborhood of paid weight at least `W/(q-1)`. This note resolves that neighborhood into one finite physical conflict label.

Let `v` be the returned center and let

\[
N[v]=\{v\}\cup N(v).
\]

Fix a finite ordered conflict-label dictionary

\[
\mathcal L=\{\ell_1,\ldots,\ell_K\}
\]

covering overlap, cross-constraint, owner, occurrence, exterior, blocker and protected-field incompatibilities. For each neighbor `u in N(v)`, assign `u` to the least label occurring on the edge `vu`. Give every component a nonnegative weight `w(u)`.

## RI5bz -- exact labeled neighborhood partition -- PROVED

Define

\[
B_0=\{v\},
\qquad
B_j=\{u\in N(v):\text{the least label on }vu\text{ is }\ell_j\}.
\]

Then the `K+1` buckets form a disjoint partition of `N[v]`, and

\[
\boxed{
 w(N[v])=w(v)+\sum_{j=1}^K w(B_j).
}
\]

### Proof

The center belongs only to `B_0`. Every neighbor has at least one conflict label and therefore exactly one least label. Hence every neighbor belongs to exactly one `B_j`. Summing weights over the partition gives the identity. QED.

## RI5ca -- one heavy physical label -- PROVED

One bucket satisfies

\[
\boxed{
 w(B_j)\ge \frac{w(N[v])}{K+1}.
}
\]

Consequently, when the requested `q`-component bank does not exist, one exact output has weight at least

\[
\boxed{
 \frac{W}{(q-1)(K+1)}.
}
\]

The output is either the center component itself or a cloud of conflicts sharing one least physical label.

### Proof

Pigeonhole the partition from RI5bz over `K+1` buckets, then use RI5bw. QED.

## RI5cb -- label-cloud refinement -- PROVED

Suppose a label bucket `B_j` is returned and its records further carry one of `R_j` finite sublabels, such as a line address, owner, blocker, certificate or occurrence class. Assign every component to its least sublabel. Then one subbucket has weight at least

\[
\boxed{
 \frac{w(B_j)}{R_j}
 \ge
 \frac{W}{(q-1)(K+1)R_j}.
}
\]

Thus any finite refinement of the conflict record preserves an explicit positive fraction of total paid component weight.

### Proof

The least-sublabel assignment partitions `B_j` into at most `R_j` buckets. Pigeonhole. QED.

## RI5cc -- complete labeled-conflict router -- PROVED

For a requested `q`-component physical RI bank, one exact continuation holds:

1. an independent family of size at least `q` gives the bank;
2. one center component has weight at least `W/((q-1)(K+1))`;
3. one least conflict label supports a neighbor cloud of that weight;
4. one finite sublabel refinement supports the bound from RI5cb;
5. or one edge lacks a fixed least label, owner, occurrence, exterior or weight record.

Hence a failed RI subbank no longer returns an unlabeled heavy neighborhood. It returns one quantitatively heavy physical conflict class suitable for overlap destruction, owner concentration, blocker payment or one label-specific capacity ticket.

## Corrected RI6 frontier

The graph-theoretic failure branch is reduced to paying finitely labeled conflict clouds. Remaining work is to prove the actual label dictionaries and payment efficiencies, together with repeated-coset correlations, blocker repair and replenishable-source recurrence.

## Finite check

`scripts/verify_ri_conflict_label_concentration.py` enumerates small labeled neighborhoods, verifies the exact partition and checks the `1/(K+1)` and refined `1/R_j` concentration bounds.