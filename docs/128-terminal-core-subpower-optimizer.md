# Exact terminal-core optimization is subpower

PX265 leaves a terminal nested block of order

\[
m=O(\Delta_0+\log\log N).
\]

PX270--PX272 compress any matching infeasibility inside that block to a Hall
rectangle. Even when no uniform absorber theorem is available, the terminal
optimization problem itself is small enough to solve exactly: every one-block
or coupled two-block matching state can be enumerated in `N^(o(1))` time.

This does not prove that every terminal core has an improving state. It turns
failure into an explicit finite obstruction certificate rather than an
unanalysed asymptotic remainder.

## 1. One-block exact optimizer

Let `F` be the terminal forbidden graph on an order-`m` block. For
`1<=r<=3`, let `C_r` be a finite weighted family of compatible rank-`r`
partial matchings. Aggregate duplicate certificates by adding their weights
and define

\[
\Phi(\pi)
=
\sum_{r=1}^3
\sum_{E\in\mathcal C_r}
w(E)\mathbf 1_{E\subseteq\pi}.
\]

### Theorem PX273 -- PROVED

The minimum of `Phi` over every perfect matching avoiding `F` can be computed
exactly in

\[
\boxed{O(m!\,m^6)}
\]

arithmetic operations after `O(m^6)` certificate preprocessing.

The same enumeration decides whether there is a strict improvement over a
given current state and returns an explicit minimizing permutation when one
exists.

### Proof

The number of rank-`r` partial matchings in a complete `m x m` bipartite grid is

\[
\binom mr^2r!.
\]

For `r<=3`, their total number is `O(m^6)`. Aggregate the supplied weighted
family in a lookup table. Enumerate the at most `m!` permutations, discard
those meeting `F`, and evaluate every surviving state against the table.
All operations are exact when the weights are integer or rational. \(\square\)

The algorithm may be accelerated by branch-and-bound or subset dynamic
programming, but no acceleration is needed for the asymptotic conclusion.

## 2. Coupled two-block optimizer

Consider the sequential two-block setting of PX253. The second forbidden graph
may depend on the first selected permutation. Let the total certificate rank
across both blocks be at most three.

### Theorem PX274 -- PROVED

The exact minimum over all legal sequential pairs `(pi_1,pi_2)` can be computed
in

\[
\boxed{O((m!)^2m^6)}
\]

operations when both terminal blocks have order at most `m`.

### Proof

There are at most `m!` first-block states. For each one, construct its residual
second forbidden graph and enumerate at most `m!` second-block states. A
rank-at-most-three certificate on the disjoint union of two `m x m` grids is
specified by at most three of `2m^2` cells, so the aggregated table has
`O(m^6)` entries. Evaluate each legal pair exactly. \(\square\)

The proof does not assume independence and applies directly to the coordinate
star-field skeleton of PX252--PX255.

## 3. Subpower terminal complexity

### Corollary PX275 -- PROVED

Assume fixed initial forbidden degree and

\[
\boxed{m=O(\log\log N).}
\]

Then

\[
\boxed{m!\,m^6=N^{o(1)}}
\]

and

\[
\boxed{(m!)^2m^6=N^{o(1)}.}
\]

The same conclusion holds for any fixed number of sequential terminal blocks.

### Proof

Stirling's estimate gives

\[
\log(m!)=O(m\log m)
=O(\log\log N\,\log\log\log N)
=o(\log N).
\]

Polynomial factors in `m` and a fixed power of `m!` do not change the
conclusion. \(\square\)

## 4. Auditable obstruction certificates

### Corollary PX276 -- PROVED

If the exact terminal optimizer finds no strict improvement, it can output an
auditable obstruction certificate of size `N^(o(1))` containing:

1. the terminal forbidden graph or sequential forbidden-graph rule;
2. the aggregated rank-at-most-three certificate table;
3. the current potential value;
4. the complete list of legal terminal states and their exact values, or an
   equivalent replayable enumeration transcript.

Thus a failure of terminal absorption is a finite, subpower-size object which
can be classified or passed to a computer-assisted lemma.

### Proof

The data table has `O(m^6)` entries and the enumeration has at most `m!` or
`(m!)^2` states. Apply PX275. \(\square\)

PX273--PX276 do not assert that the obstruction list is empty. They reduce the
terminal-core frontier to an exact finite classification problem whose total
size is asymptotically negligible compared with the ambient product instance.

## 5. Verification

Run

```bash
python scripts/verify_product_terminal_core_optimizer.py
```

The verifier checks the exact partial-matching counts, compares the optimizer
with direct evaluation on random small weighted instances, tests the dependent
two-block enumeration, and verifies the subpower logarithmic estimates.
