# Every dirty side-five joint state has an ambient strict target response

CMR1286--CMR1293 close the side-four selected-execution base by complete finite
search.  The same response mechanism remains tractable at side five.  Every dirty
ordered saturated state has a physical target cell, a disjoint forbidden extension
and a response matching of strictly smaller physical triple potential.

The search can be organized without enumerating the same bank repeatedly.  For
each fixed opposite matching `O` and each cell `e notin O`, precompute the minimum
potential over all response states obtained from all disjoint forbidden extensions
through `e`.  Every target in every ordered state then consults this finite table.

## 1. Complete side-five state stock

### Theorem CMR1294 -- PROVED BY COMPLETE FINITE ENUMERATION

There are

\[
\boxed{5280}
\]

ordered pairs of physically disjoint perfect matchings of `K_{5,5}` and

\[
\boxed{2040}
\]

distinct physical saturated states.

The ordered-state potential distribution is

\[
\begin{array}{c|rrrrrrrrrrrrrrrr}
\Phi&0&1&2&3&4&5&6&7&8&9&10&11&12&13&14&15\\
\hline
\#&64&192&960&1200&904&616&560&336&96&64&32&104&80&32&24&16.
\end{array}
\]

The physical-state distribution is

\[
\begin{array}{c|rrrrrrrrrrrrrrrr}
\Phi&0&1&2&3&4&5&6&7&8&9&10&11&12&13&14&15\\
\hline
\#&32&76&360&440&322&264&252&140&30&28&12&32&32&8&8&4.
\end{array}
\]

Hence 64 ordered states are clean and 5216 are dirty.

### Proof

Enumerate the `5!=120` perfect matchings.  Relative to each fixed matching there
are `!5=44` disjoint permutation matchings, giving `120*44=5280` ordered states.
Deduplicate physical unions and test the 152 collinear three-cell subsets of the
`5 x 5` board by the integer determinant.  The tables are the complete counts. ∎

The maximum physical potential in this state class is fifteen.

## 2. Side-five response-bank stock

Fix disjoint perfect matchings `O,F`.  The response graph

\[
G_{O,F}=K_{5,5}\setminus(O\cup F)
\]

is 3-regular.

### Theorem CMR1295 -- PROVED BY COMPLETE FINITE ENUMERATION

Across all 5280 ordered disjoint pairs `(O,F)`, the response bank has size either

\[
\boxed{12\text{ or }13.}
\]

More precisely, 2400 pairs have twelve response matchings and 2880 pairs have
thirteen.

### Proof

For every ordered disjoint pair, enumerate the 120 perfect matchings and retain
those disjoint from `O union F`.  The displayed distribution is exhaustive. ∎

In particular every forbidden extension has a nonempty complete response bank, as
also follows from regular bipartite matchability.

## 3. Fixed-opposite target-response table

For a fixed perfect matching `O` and a cell `e notin O`, define

\[
\mu_5(O,e)
=
\min
\left\{
\Phi(O\cup R):
\begin{array}{l}
F\text{ is a perfect matching},\\
e\in F,\ F\cap O=\varnothing,\\
R\in\operatorname{PM}(K_{5,5}\setminus(O\cup F))
\end{array}
\right\}.
\]

### Theorem CMR1296 -- PROVED

The table `mu_5(O,e)` is defined for all

\[
\boxed{120\cdot20=2400}
\]

fixed-opposite, nonopposite-cell pairs.  A minimizing response always omits `e` and
is physically disjoint from `O`.

### Proof

CMR1198 supplies at least one disjoint forbidden extension through every
`e notin O`, and CMR1295 supplies a nonempty response bank.  Every response avoids
both `F` and `O`, hence omits `e` and preserves layer disjointness. ∎

This table is independent of the old targeted-layer matching and can be reused by
all states with the same fixed opposite layer.

## 4. Every dirty state has a lower response

### Theorem CMR1297 -- PROVED BY COMPLETE FINITE ENUMERATION

For every one of the 5216 dirty ordered side-five states `S=O union M`, there is a
physical target cell `e` such that, after taking the other layer as fixed opposite,

\[
\boxed{
\mu_5(O_e,e)<\Phi(S).
}
\]

The best potential-change distribution is

\[
\begin{array}{c|rrrrrrrrrrrrrr}
\min_Q(\Phi(Q)-\Phi(S))
&-1&-2&-3&-4&-5&-6&-7&-8&-9&-10&-11&-12&-13&-15\\
\hline
\#
&316&1268&1176&836&728&360&152&76&56&64&72&88&16&8.
\end{array}
\]

Thus every dirty ordered state has an ambient response improving by at least one.

### Proof

For every dirty ordered state, enumerate its physical collinear triples and their
three cells.  For a cell in one layer, query the precomputed table with the other
layer fixed.  The minimum over all target-cell queries has the displayed negative
distribution, covering all 5216 dirty states. ∎

No extrapolation from smaller sides is used.

## 5. Canonical side-five policy

Fix total orders on target triples, target cells, forbidden extensions and response
matchings.

### Theorem CMR1298 -- PROVED

Every dirty ordered side-five state has a unique canonical first lower response.
Repeated accepted canonical responses reach a clean side-five state after at most

\[
\boxed{\Phi(S)\le15}
\]

steps.

### Proof

CMR1297 makes the improving response set nonempty.  Fixed-order tie breaking makes
the policy deterministic.  Every accepted response lowers the nonnegative integer
potential by at least one, and CMR1294 bounds the initial value by fifteen. ∎

## 6. Restricted-host lowering expansion

Let `H` be a restricted host whose selected minimum is a dirty side-five state `S`,
and let `Q` be its canonical ambient improving response.  Put

\[
A=Q\setminus E(H).
\]

### Theorem CMR1299 -- PROVED

Exactly one of the following occurs.

1. `A` is empty and `Q` is a feasible strict improvement.
2. `A` is nonempty and adding it makes a lowering expansion:
   \[
   \min_{R\in\mathcal F(H\cup A)}\Phi(R)
   \le\Phi(Q)<\Phi(S).
   \]
   Canonical expansion normalization accepts a lower minimum or contracts an added
   minimum-core edge after minimum-preserving peels.

### Proof

Identical to CMR1290: the expanded host retains `S` and makes the strictly lower
ambient state `Q` feasible.  Apply CMR942--CMR952. ∎

Thus side-five response unavailability is structural contraction, not a positive
same-side terminal.

## 7. Finite side-five execution and credit descent

### Theorem CMR1300 -- PROVED

Along a selected side-five owner, every canonical dirty response gives strict
potential decrease, added-core contraction or structural descent.  There are at
most fifteen accepted potential decreases and at most ten labelled-edge
contractions before the two-layer residual state cardinality is exhausted.

Every accepted response strictly decreases the all-ones live-credit potential of
CMR1256.

### Proof

Use CMR1298 for potential decreases.  A saturated side-five joint state has ten
labelled edges, and every exact contraction removes at least one residual edge.
The credit statement is the equality between physical potential and live-credit
count. ∎

As at side four, extra retired credits may be essential; no conservative one-parent
row-sum claim is made.

## 8. Side-five endpoint

### Corollary CMR1301 -- PROVED

The selected-execution finite matching base now closes through side five.

1. Sides one and two are rigid/clean bases.
2. Every dirty side-three response is clean.
3. Every dirty side-four state has an ambient lower response.
4. Every dirty side-five state has an ambient lower response.
5. Restricted unavailability at sides four and five gives lowering-expansion
   improvement or added-core contraction.

The first unclassified finite matching side is six.  The uniform proof still
requires line/height/carry or spectral control for arbitrary side, fixed-interface
and product owners; finite bases do not replace that theorem.

No all-`n` theorem is claimed.  The 5280 ordered states, 2040 physical states,
response-bank sizes, 2400 target-response table entries, complete lower-response
distribution and restricted lowering expansion are checked in
[`scripts/verify_prime_power_side_five_finite_improvement.py`](../scripts/verify_prime_power_side_five_finite_improvement.py).
