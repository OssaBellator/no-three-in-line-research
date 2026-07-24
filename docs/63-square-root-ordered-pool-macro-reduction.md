# Square-root ordered-pool macro reduction

PP3df supplies `m^0.05` ordered pools of size `m^0.475`, but that formulation
asks one local variable to install essentially linear width in its pool size.
The cross-pool threshold PP3cz permits many more variables.  Balancing these two
facts gives a sharper target: a local macro state only needs square-root width in
an ordered matching pool.

## 1. The balanced exponents

Put

\[
 \rho=\frac{19}{40}=0.475,
 \qquad
 \beta=\frac{19}{80}=0.2375,
 \qquad
 \mu=\frac{23}{80}=0.2875.
\]

Then

\[
 \beta=\frac\rho2,
 \qquad
 \mu+\beta=\frac{21}{40}=0.525,
 \qquad
 \mu<\frac13.
\]

Also

\[
 \mu+\rho=\frac{61}{80}<1,
 \qquad
 2\rho=\frac{19}{20}<1.
\]

### Proposition PP3dg -- PROVED

For all sufficiently large `m`, every perfect matching layer contains

\[
 M=\lfloor m^\mu\rfloor
\]

pairwise disjoint monotone matching pools, each of size

\[
 R=\lfloor m^\rho\rfloor,
\]

all having one common orientation.  After at most one global row reflection they
may all be assumed increasing.

#### Proof

The extraction criterion PP3de requires

\[
 2MR+R^2\le m.
\]

The two terms have orders

\[
 m^{\mu+\rho}=m^{61/80}
 \qquad\text{and}\qquad
 m^{2\rho}=m^{19/20},
\]

both `o(m)`.  Hence the criterion holds for sufficiently large `m`.  The common
orientation and reflection conclusion are part of PP3de--PP3df. ∎

The total source-edge budget is only

\[
 MR=m^{61/80+o(1)}=o(m).
\]

## 2. A precise local hypothesis

Call a state family on an increasing `R`-edge pool a **square-root compressed
macro family** if it has the following properties.

1. **Equal margins.** Every state has one point on each old pool row and column
   and exactly two points on each of `W` newly installed rows and columns.
2. **Width.**

\[
 W\ge c\sqrt R
\]

   for an absolute constant `c>0`.
3. **Internal and source cleaning.** Every retained state is internally
   no-three-in-line and clean against the fixed source points assigned to that
   macro variable.
4. **Positive state density.** The retained state family has density at least an
   absolute constant `delta>0` inside a reference equal-margin bank, or has
   equivalent fixed-rank cell and pair spread bounds.
5. **Compressed cross potential.** For independently sampled states from two
   distinct macro families, the expected number of patch-only triples meeting
   both variables is at most `C/m`; for three distinct macro families it is at
   most `C/m`, where `C` is absolute.

The fifth condition is the probabilistic form of genuine support compression.
The complete product of width-two micro-rungs does not satisfy it merely because
its intervals are grouped into one variable; PP3dc records that limitation.

## 3. Conditional prime-gap-scale completion

### Theorem PP3dh -- PROVED UNDER THE SQUARE-ROOT COMPRESSED MACRO HYPOTHESIS

Suppose every sufficiently large increasing `R`-edge matching pool admits a
square-root compressed macro family, uniformly for

\[
 R=m^{19/40+o(1)}.
\]

Suppose also that the opposite-layer and retained-core preparation step leaves
total expected source-containing defect `o(1)` across the selected macro
variables, for example through PP3cv, PP3cp plus protected trades, or an exact
PP2l estimate.

Then every sufficiently large saturated source supports an extension of width

\[
 \Omega(m^{21/40})=\Omega(m^{0.525})
\]

with no new collinear triple.

#### Proof

Use PP3dg to select

\[
 M=m^{23/80+o(1)}
\]

disjoint increasing pools of size `R=m^{19/40+o(1)}`.  Install one macro family
on each pool.  The total width is at least

\[
 MW
 \ge
 cM\sqrt R
 =
 m^{23/80+19/80+o(1)}
 =
 m^{21/40+o(1)}.
\]

Equal margins preserve saturation, while the local hypotheses exclude all
within-variable and prepared source-containing triples.

The expected number of patch-only triples meeting two macro variables is at
most

\[
 C\binom M2/m
 =
 O(m^{2\mu-1})
 =
 O(m^{-34/80}),
\]

and the corresponding three-variable expectation is at most

\[
 C\binom M3/m
 =
 O(m^{3\mu-1})
 =
 O(m^{-11/80}).
\]

Both tend to zero because `mu<1/3`.  Adding the assumed `o(1)` source-containing
defect gives total expected defect `o(1)`.  Hence some state assignment has no
new triple. ∎

Combined with PP4b, a width with a fixed positive constant times `m^0.525`
would meet the published prime-gap exponent after the usual constant and
rounding slack.  The theorem above records the exact local geometric input
needed to obtain that width from matching-first ordered pools.

## 4. Why this target is sharper

The previous `m^0.05`-pool formulation required width `Theta(R)` from each
`R=m^0.475` pool.  PP3dh requires only

\[
 W=Theta(\sqrt R).
\]

The number of variables rises to `m^0.2875`, but remains below the
`m^(1/3)` cross-variable threshold.  Thus:

- source matching pools exist universally by PP3dg;
- the source-edge budget is sublinear;
- the total width reaches the prime-gap exponent exactly;
- generic cross-variable first moment is asymptotically harmless once the local
  supports are genuinely compressed.

## 5. Remaining local theorem

The branch is now reduced to one local construction problem on an ordered
matching pool:

> Given
> `x_1<...<x_R` and `y_1<...<y_R`, construct an equal-margin finite-state family
> adding `Omega(sqrt(R))` new rows and columns, with internal no-three geometry,
> source cleaning, positive fixed-rank spread, and the compressed cross potential
> in PP3dh.

Monotone endpoint order is guaranteed.  What is not yet proved is that order
alone supports the required convex, algebraic, tomographic, or trade-based macro
geometry.  This is strictly narrower than the earlier arbitrary-reservoir or
independent-template preparation problems.