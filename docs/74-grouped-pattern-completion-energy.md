# Grouped pattern completion energy

PP3fk reduces global completion to an upper bound on the additional bad-event
probability mass incident to every slot.  This chapter writes that mass exactly
as densities of forbidden pair relations and triple relations on the refined
slot domains.  All source anchors witnessing the same forbidden patch pair are
grouped into one event.

## 1. Refined global slot domains

Let `S` be the complete set of macro slots.  For every slot `s`, let `H_s` be its
source-edge domain after the unary restrictions of PP3ea and, when available,
PP3ff.  Thus

\[
 |H_s|\ge\gamma R
\]

for one common `gamma>0`, every slot value is fixed-pair cell-safe, and the
same-edge anchored-pair class may also be absent.

For `e in H_s`, write

\[
 Q_s(e)=\{M_s(e),F_s(e)\}
\]

for the two patch points produced by that slot.

The internal pair/triple events inside each macro are already charged in PP3fj.
The relations below contain only additional source-containing or cross-macro
patterns.

## 2. Grouped forbidden pair relations

For two distinct slots `s,t`, define

\[
 \Gamma_{s,t}\subseteq H_s\times H_t
\]

by putting `(e,f) in Gamma_{s,t}` when the points in
`Q_s(e) union Q_t(f)` create at least one additional forbidden triple of either
of the following forms:

1. one fixed retained source anchor and one point from each slot;
2. two points from one slot and one point from the other, when that pattern is
   not already included in the internal event system of one macro.

A pair `(e,f)` is counted once regardless of how many source anchors or point-type
choices witness it.

### Proposition PP3fm -- PROVED

Under independent uniform slot choices, the grouped pair event

\[
 G_{s,t}=\{(X_s,X_t)\in\Gamma_{s,t}\}
\]

has exact probability

\[
 \boxed{
 \Pr(G_{s,t})
 =
 \frac{|\Gamma_{s,t}|}{|H_s||H_t|}.
 }
\]

Avoiding every `G_{s,t}` removes every additional bad triple controlled by at
most two slots.

#### Proof

The ordered pair `(X_s,X_t)` is uniform on `H_s x H_t`.  By definition,
`Gamma_{s,t}` is exactly the set of value pairs realizing at least one grouped
forbidden pattern.  Grouping witnesses does not change the event. ∎

This is the slot-domain analogue of fixed-core pattern compression PP3cr.

## 3. Grouped forbidden triple relations

For three distinct slots `s,t,u`, define

\[
 \Xi_{s,t,u}\subseteq H_s\times H_t\times H_u
\]

by putting `(e,f,g) in Xi_{s,t,u}` when one selected point from each slot forms
an additional patch-only collinear triple not already charged inside one macro.
Again, a value triple is counted once even if more than one of the eight
movement/refill type choices is collinear.

### Proposition PP3fn -- PROVED

The grouped triple event

\[
 T_{s,t,u}=\{(X_s,X_t,X_u)\in\Xi_{s,t,u}\}
\]

has exact probability

\[
 \boxed{
 \Pr(T_{s,t,u})
 =
 \frac{|\Xi_{s,t,u}|}{|H_s||H_t||H_u|}.
 }
\]

Avoiding all grouped pair and triple events removes every remaining source and
cross-macro triple.

#### Proof

Uniformity gives the displayed density.  Every remaining triple after unary and
internal cleaning uses either two or three controlling slots, and therefore
belongs to the corresponding grouped relation. ∎

## 4. Exact weighted completion endpoint

For a slot `s`, define its grouped external mass

\[
 \Lambda_{\rm ext}(s)
 =
 \sum_{t\ne s}
 \frac{|\Gamma_{s,t}|}{|H_s||H_t|}
 +
 \sum_{\{t,u\}\subseteq S\setminus\{s\}}
 \frac{|\Xi_{s,t,u}|}{|H_s||H_t||H_u|},
\]

where each unordered pair or triple of slots is represented once.

### Theorem PP3fo -- PROVED

Assume the macro width satisfies the hypotheses of PP3fj and

\[
 \boxed{
 \max_s\Lambda_{\rm ext}(s)
 \le
 \frac1{48}
 -
 \frac{5}{8\gamma\sqrt R}.
 }
\]

Then one simultaneous saturated no-three assignment exists.  Its conditioned
fixed-rank cylinders satisfy the spread bound of PP3fl.

#### Proof

Use one grouped event for every nonempty relation `Gamma` and `Xi`.  Propositions
PP3fm and PP3fn show that their total incident probability mass at slot `s` is
exactly `Lambda_ext(s)`.  Apply PP3fk and then PP3fl. ∎

The theorem charges each forbidden value pattern once, rather than once per
source anchor, point-type witness, or geometric triple description.

## 5. Completion multiplicities

For an ordered slot pair, define

\[
 d_{s,t}(e)
 =
 |\{f\in H_t:(e,f)\in\Gamma_{s,t}\}|,
\]

and its average

\[
 \bar d_{s,t}
 =
 \frac1{|H_s|}\sum_{e\in H_s}d_{s,t}(e).
\]

For an ordered slot triple, define

\[
 c_{s,t,u}(e,f)
 =
 |\{g\in H_u:(e,f,g)\in\Xi_{s,t,u}\}|,
\]

and

\[
 \bar c_{s,t,u}
 =
 \frac1{|H_s||H_t|}
 \sum_{e\in H_s}\sum_{f\in H_t}c_{s,t,u}(e,f).
\]

### Corollary PP3fp -- PROVED

One has

\[
 \Pr(G_{s,t})
 =
 \frac{\bar d_{s,t}}{|H_t|}
 \le
 \frac{\bar d_{s,t}}{\gamma R},
\]

and

\[
 \Pr(T_{s,t,u})
 =
 \frac{\bar c_{s,t,u}}{|H_u|}
 \le
 \frac{\bar c_{s,t,u}}{\gamma R}.
\]

Consequently it is sufficient that, for every slot `s`,

\[
 \boxed{
 \sum_{t\ne s}\bar d_{s,t}
 +
 \sum_{\{t,u\}\subseteq S\setminus\{s\}}
 \bar c_{s,t,u}
 \le
 \gamma R
 \left(
 \frac1{48}
 -
 \frac{5}{8\gamma\sqrt R}
 \right).
 }
\]

#### Proof

Double-count the relation entries by their first one or two coordinates and use
`|H_t|,|H_u|>=gamma R`.  Substitute into PP3fo. ∎

This is the exact completion-energy form of the remaining theorem.  A constant
completion bound is useful but not required; large codegrees may be tolerated if
they occur for few first-coordinate values.

## 6. Coarse interaction-graph corollary

Suppose each slot has nonempty pair relations with at most `D_2` partner slots
and nonempty triple relations with at most `D_3` partner-slot pairs.  Suppose
also

\[
 \max_{s,t}\bar d_{s,t}\le\kappa_2,
 \qquad
 \max_{s,t,u}\bar c_{s,t,u}\le\kappa_3.
\]

### Corollary PP3fq -- PROVED

The hypotheses of PP3fo hold whenever

\[
 \boxed{
 D_2\kappa_2+D_3\kappa_3
 \le
 \gamma R
 \left(
 \frac1{48}
 -
 \frac{5}{8\gamma\sqrt R}
 \right).
 }
\]

This separates two possible compression mechanisms:

1. **support sparsity:** few other slots or slot pairs can interact with a fixed
   slot;
2. **completion sparsity:** many interactions are allowed, but their average
   completion multiplicities are small.

## 7. Failure concentration

### Corollary PP3fr -- PROVED

If the grouped weighted endpoint fails, some slot `s` satisfies

\[
 \sum_{t\ne s}\bar d_{s,t}
 +
 \sum_{\{t,u\}}\bar c_{s,t,u}
 >
 \gamma R
 \left(
 \frac1{48}
 -
 \frac{5}{8\gamma\sqrt R}
 \right).
\]

Thus failure produces one explicit high-energy slot star.  Its mass may be
further decomposed into:

- ordinary fixed-anchor pair patterns;
- cross-macro two-slot patterns;
- cross-macro three-slot patterns.

This star is the correct target for interval reordering, pattern sparsification,
carry/divisor dispersion, or a protected trade.  Raw anchor multiplicity is not
itself charged; only distinct forbidden value relations contribute.