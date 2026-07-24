# Weighted slot-mass endpoint

The global occurrence theorem PP3ei uses one common upper bound on event
probabilities and charges every event equally.  Cross-macro rank-three events can
be much rarer than pair events, so raw occurrence may overpay badly.  This
chapter replaces occurrence by the total bad-event probability mass incident to
each slot.

## 1. A probability-mass local lemma

Let independent slot variables support a finite family `A` of bad events.  Assume
every event depends on at most three slots.  For a slot `s`, define

\[
 \lambda_s
 =
 \sum_{E\in\mathcal A:\,s\in\operatorname{vbl}(E)}\Pr(E),
 \qquad
 \lambda=\max_s\lambda_s.
\]

Events are adjacent when their slot sets intersect.

### Theorem PP3fi -- PROVED FROM THE ASYMMETRIC LOCAL LEMMA

Suppose

\[
 \max_{E\in\mathcal A}\Pr(E)\le\frac14
 \qquad\text{and}\qquad
 \boxed{\lambda\le\frac1{12}}.
\]

Then there is a slot assignment avoiding every event in `A`.

#### Proof

For each event put

\[
 x_E=2\Pr(E).
\]

Then `0<=x_E<=1/2`.  For a fixed event `E`,

\[
 \sum_{F\sim E}x_F
 \le
 2\sum_{s\in\operatorname{vbl}(E)}\lambda_s
 \le
 6\lambda
 \le
 \frac12.
\]

For numbers in `[0,1]`, the product is at least one minus their sum.  Hence

\[
 \prod_{F\sim E}(1-x_F)
 \ge
 1-\sum_{F\sim E}x_F
 \ge
 \frac12.
\]

Therefore

\[
 x_E\prod_{F\sim E}(1-x_F)
 \ge
 2\Pr(E)\cdot\frac12
 =
 \Pr(E).
\]

The asymmetric Lovasz local lemma applies. ∎

This criterion is insensitive to how many events meet one slot when their total
probability mass is small.

## 2. Exact internal mass budget

Use the source-clean square-root macro model of PP3dz with `n=2W` slots and slot
domains of size at least `gamma R`.  Keep one pair event for each slot pair and
one triple event for each slot triple, as in PP3dl.

### Proposition PP3fj -- PROVED

The internal bad-event mass incident to one slot is at most

\[
 \boxed{
 \lambda_{\rm int}
 \le
 \frac{5(n-1)}{\gamma^2R}
 +
 \frac{8\binom{n-1}{2}}{\gamma^2R}.
 }
\]

If

\[
 W\le\frac{\gamma\sqrt R}{16},
\]

then

\[
 \boxed{
 \lambda_{\rm int}
 \le
 \frac1{16}
 +
 \frac{5}{8\gamma\sqrt R}.
 }
\]

Consequently, for sufficiently large `R`, all source-containing and cross-macro
events may be added provided their total incident probability mass at every slot
is at most

\[
 \boxed{
 \eta_R
 =
 \frac1{48}
 -
 \frac{5}{8\gamma\sqrt R}.
 }
\]

#### Proof

A slot belongs to `n-1` internal pair events and `binom(n-1,2)` internal triple
events.  Apply the probability bounds `5/(gamma^2R)` and `8/(gamma^2R)` from
PP3dz.

Since `n=2W<=gamma sqrt(R)/8`,

\[
 \frac{8\binom{n-1}{2}}{\gamma^2R}
 \le
 \frac{4n^2}{\gamma^2R}
 \le
 \frac1{16},
\]

and

\[
 \frac{5(n-1)}{\gamma^2R}
 \le
 \frac{5}{8\gamma\sqrt R}.
\]

Subtract this upper bound from the PP3fi threshold `1/12`; the constant part is
`1/12-1/16=1/48`. ∎

Unlike PP3ej, the additional budget is a probability mass, not an event count.
For example, `R^2` events of probability `O(R^-3)` cost only `O(R^-1)`.

## 3. Global completion endpoint

### Theorem PP3fk -- PROVED

Consider all macro slots simultaneously.  Assume:

1. every macro uses the refined source-clean domains of PP3ea, or the stronger
   fixed-pair and same-edge-anchor-clean domains of PP3ff;
2. the internal pair and triple events are those of PP3dl;
3. every additional source-containing or cross-macro bad event depends on at most
   three slots and has probability at most `1/4`;
4. for every slot `s`, the sum of probabilities of all additional events
   containing `s` is at most `eta_R` from PP3fj.

Then one simultaneous slot assignment is saturated and no-three-in-line.

#### Proof

At each slot, the total incident event mass is at most

\[
 \lambda_{\rm int}+\eta_R\le\frac1{12}.
\]

Apply PP3fi to the union of the internal and additional events.  Avoiding the
internal events gives distinct selected source edges and internally no-three
macro patches.  Domain restrictions remove their designated unary source
classes.  Avoiding the additional events removes every remaining source and
cross-macro triple.  Equal-margin bookkeeping gives saturation. ∎

This endpoint permits arbitrary grouping of geometric certificates into one bad
event whenever the grouped event still depends on at most three slots.  In
particular, all retained anchors producing the same forbidden pair pattern may
be charged once through the probability of that pair-pattern event.

## 4. Conditional fixed-rank spread

### Theorem PP3fl -- PROVED FROM THE PUBLISHED LLL-DISTRIBUTION THEOREM

Under the hypotheses of PP3fi, condition the product distribution on avoiding all
bad events.  A cylinder fixing `q` slot values has probability at most

\[
 \boxed{
 \Pr(B\mid\text{avoid})
 \le
 e^{q/3}\Pr(B).
 }
\]

Thus, when every slot domain has size at least `gamma R`,

\[
 \boxed{
 \Pr(B\mid\text{avoid})
 \le
 \frac{e^{q/3}}{(\gamma R)^q}.
 }
\]

#### Proof

Use the asymmetric activities `x_E=2Pr(E)` from PP3fi.  A `q`-slot cylinder meets
events whose total probability mass is at most `q lambda<=q/12`, and hence whose
total activity is at most `q/6`.

For `0<=x<=1/2`,

\[
 -\log(1-x)\le2x.
\]

The LLL-distribution inflation factor is therefore at most

\[
 \prod_{E\sim B}(1-x_E)^{-1}
 \le
 \exp\left(2\sum_{E\sim B}x_E\right)
 \le
 e^{q/3}.
\]

Multiply by the unconditioned cylinder probability. ∎

The weighted endpoint therefore preserves stronger fixed-rank spread than the
raw occurrence theorem while allowing heterogeneous event probabilities.

## 5. Revised remaining theorem

After PP3ff removes fixed-pair cells and same-edge anchored pairs, define for each
slot `s`:

\[
 \Lambda_{\rm ord}(s)
 =
 \sum_{E\ni s:\,E\text{ ordinary source-anchor}}\Pr(E),
\]

\[
 \Lambda_{\rm cross}(s)
 =
 \sum_{E\ni s:\,E\text{ cross-macro}}\Pr(E).
\]

The active global bottleneck is now the explicit inequality

\[
 \boxed{
 \Lambda_{\rm ord}(s)+\Lambda_{\rm cross}(s)
 \le
 \frac1{48}-o(1)
 \quad\text{for every slot }s.
 }
\]

This is strictly weaker than bounding the number of external events by `O(R)`.
It asks for weighted pattern compression: common events may be numerous if they
are correspondingly rare.  Failure identifies a slot carrying constant total
external conflict probability, which can then be attacked through source-pattern
compression, interval ordering, divisor/carry structure, or protected trades.