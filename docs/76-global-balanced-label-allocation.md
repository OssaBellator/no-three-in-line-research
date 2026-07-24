# Global balanced refined-label allocation

The coordinate warning PP3-R5 rules out discarding numerical labels after a
single macro oversamples them.  The valid replacement is global: use exactly the
`T=MW` final new rows and exactly the `T` final new columns, assign every row
label to one macro, and choose one perfect matching of all row labels to all
column labels through the refined compatibility graph of the owning macro.

## 1. The global allocation object

Let `E_1,...,E_M` be pairwise disjoint matching pools, each of size `R`.  Put

\[
 T=MW.
\]

Let

\[
 \mathcal A=\{m+1,\ldots,m+T\},
 \qquad
 \mathcal B=\{m+1,\ldots,m+T\}
\]

be the actual final new row and column labels.  For every macro `i` and label
pair `(A,B)`, let

\[
 H_i(A,B)\subseteq E_i
\]

be a source-edge domain.  In the refined source-clean application,
`H_i(A,B)` is the domain from PP3fd: its movement cell is fixed-pair safe, its
refill cell is fixed-pair safe, and its same-edge movement/refill pair has no
fixed source anchor.

Fix `gamma>0` and define the macro compatibility graph

\[
 J_i
 =
 \{(A,B)\in\mathcal A\times\mathcal B:
 |H_i(A,B)|\ge\gamma R\}.
\]

A **balanced ownership map** is a function

\[
 \sigma:\mathcal A\to[M]
\]

with `|sigma^{-1}(i)|=W` for every macro.  Given `sigma`, define the global
bipartite graph

\[
 J_\sigma
 =
 \{(A,B):(A,B)\in J_{\sigma(A)}\}.
\]

## 2. Exact saturation-compatible interface

### Theorem PP3fw -- PROVED

Suppose a balanced ownership map `sigma` is chosen and `J_sigma` has a perfect
matching `pi`.  Suppose also

\[
 \boxed{
 48(2W)^2\le\gamma^2R.
 }
\]

Then every macro `i` admits an internally no-three slot assignment using the
`W` matched label pairs

\[
 \{(A,\pi(A)):A\in\sigma^{-1}(i)\}.
\]

The union of the macro patches has the following properties.

1. Every final new row and every final new column contains exactly two patch
   points.
2. Every selected old source row and column is restored exactly once.
3. Every macro is internally no-three-in-line.
4. If the domains `H_i(A,B)` are the PP3fd refined domains, every patch cell is
   fixed-pair source-safe and every same-edge movement/refill pair is
   fixed-anchor source-safe.

#### Proof

For macro `i`, the perfect matching gives exactly `W` distinct movement labels
and `W` distinct refill labels, with one paired domain of size at least
`gamma R` for every label pair.  Apply PP3ff, with `epsilon` already absorbed
into the refined density `gamma`, to choose `2W` distinct source edges and make
the macro internally no-three.

The source pools are disjoint, so the macro choices do not compete for old
edges.  Every movement label belongs to exactly one fibre of `sigma` and every
refill label occurs exactly once in the perfect matching.  Each label supports
two slots, hence two patch points.  Therefore all `T` final new rows and columns
are saturated; no numerical label is discarded.  The old-coordinate and source-
clean conclusions hold macro by macro. ∎

This is the saturation-compatible form of label oversampling: macros may compete
for a common global label set, but every final label is ultimately used.

## 3. Deterministic minimum-degree endpoint

### Proposition PP3fx -- PROVED

For a balanced ownership map `sigma`, suppose

\[
 \deg_{J_{\sigma(A)}}(A)\ge\frac T2
 \quad\text{for every }A\in\mathcal A
\]

and

\[
 |\{A:(A,B)\in J_{\sigma(A)}\}|
 \ge\frac T2
 \quad\text{for every }B\in\mathcal B.
\]

Then `J_sigma` has a perfect matching.

#### Proof

The two displayed conditions say that `J_sigma` has minimum degree at least
`T/2` on both sides.  Apply PP3ed. ∎

Thus the global allocation problem is separated into balanced ownership of the
movement labels and one ordinary bipartite perfect matching.

## 4. Random balanced ownership

Choose `sigma` uniformly from all balanced ownership maps.  For a refill label
`B`, define

\[
 Z_B(\sigma)
 =
 |\{A:(A,B)\in J_{\sigma(A)}\}|.
\]

Then

\[
 \mathbb E Z_B
 =
 \frac1M
 \sum_{i=1}^M
 |\{A:(A,B)\in J_i\}|.
\]

### Theorem PP3fy -- PROVED FROM THE STANDARD PERMUTATION BOUNDED-DIFFERENCES INEQUALITY

Fix `zeta>0`.  Assume:

1. for every macro `i` and movement label `A`,

\[
 \deg_{J_i}(A)
 \ge
 \left(\frac12+\zeta\right)T;
\]

2. for every refill label `B`,

\[
 \frac1M
 \sum_{i=1}^M
 |\{A:(A,B)\in J_i\}|
 \ge
 \left(\frac12+2\zeta\right)T;
\]

3.

\[
 \boxed{
 T\exp\left(-\frac{\zeta^2T}{8}\right)<1.
 }
\]

Then some balanced ownership map `sigma` satisfies the hypotheses of PP3fx.
Consequently, if the local width inequality of PP3fw holds, the complete set of
`T` new rows and columns supports the source-clean internal macro patches.

#### Proof

Condition 1 gives the left-degree requirement of PP3fx for every possible
ownership map.

Represent a uniform balanced ownership by a random permutation of a multiset
containing `W` copies of every macro label.  For fixed `B`, swapping two assigned
macro labels changes `Z_B` by at most two.  The permutation bounded-differences
inequality therefore gives the conservative tail bound

\[
 \Pr\left(
 Z_B<\mathbb EZ_B-2\zeta T
 \right)
 \le
 \exp\left(-\frac{\zeta^2T}{8}\right).
\]

By condition 2, the event on the left contains `Z_B<T/2`.  Sum over the `T`
refill labels.  Condition 3 makes the union probability below one, so some
balanced ownership has right degree at least `T/2` everywhere.  Apply PP3fx and
then PP3fw. ∎

For fixed positive `zeta`, condition 3 is automatic for all sufficiently large
`T`.

## 5. Failure concentration and graph quantities

### Corollary PP3fz -- PROVED

If the random balanced endpoint PP3fy cannot be applied, at least one of the
following explicit obstructions remains.

1. **Movement-row obstruction:** some macro-label pair `(i,A)` has more than
   `(1/2-zeta)T` incompatible refill labels.
2. **Refill-column obstruction:** some refill label `B` is incompatible, on
   average over macros and movement labels, with at least `(1/2-2zeta)T` of the
   possible owners.
3. **Finite concentration obstruction:** `T` is too small for the displayed
   bounded-differences union bound.

The first two obstructions can be expanded using PP3fs--PP3ft into fixed-pair
boundary shadow and exact same-edge bad-label incidence.  In particular, the
coordinate-budget correction does not destroy the average-shadow strategy; it
moves it from independent per-macro thinning to one global balanced assignment.

## 6. Remaining compatibility after allocation

Theorem PP3fw removes the coordinate-allocation issue and the designated unary
source classes.  It does not by itself remove:

- ordinary fixed-anchor pairs controlled by two distinct source edges;
- patch-only triples meeting two or three macros.

Those classes are exactly the grouped relations of PP3fm--PP3fp.  After a global
allocation is selected, the weighted endpoint PP3fo applies if their total
incident relation mass is at most `1/48-o(1)` at every slot.