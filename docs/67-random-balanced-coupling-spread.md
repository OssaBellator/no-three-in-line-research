# Random balanced coupling spread

In PP3dr, an ordinary pair controlled by two source edges has probability
`O(R^-2)`, but a movement/refill pair controlled by one edge has probability
`O(R^-1)`.  The pair's two new-coordinate labels need not be coupled
canonically.  Randomizing that balanced coupling supplies one additional factor
`1/W`.

## 1. Mixture over refill couplings

Fix the movement slot map

\[
 \alpha:S\to[W]
\]

with two slots above every movement row.  Choose `beta:S->[W]` uniformly from
all balanced maps with two preimages for every refill column.  For the chosen
`beta`, sample the slot-edge assignment from the internally clean conditional
distribution `D_int,beta` of PP3dq.

Every sampled state is saturated and internally no-three-in-line.  The cylinder
bound of PP3dq is uniform in `beta`.

### Proposition PP3ds -- PROVED

For every slot `s` and refill label `b`,

\[
 \Pr(\beta(s)=b)=\frac1W.
\]

#### Proof

The balanced maps are invariant under permutations of the `W` labels.  Every
label appears in exactly two of the `2W` slots, so all labels have probability
`2/(2W)=1/W` at a fixed slot. ∎

## 2. Same-source-edge pair spread

### Theorem PP3dt -- PROVED

Under the mixed distribution over `beta` and `D_int,beta`:

1. every prescribed movement or refill cell has probability at most

\[
 \frac{2\sqrt e}{R};
\]

2. every prescribed pair controlled by two distinct source edges has probability
at most

\[
 \frac{4e}{R^2};
\]

3. every prescribed movement/refill pair controlled by one source edge has
probability at most

\[
 \boxed{
 \frac{2\sqrt e}{RW}.
 }
\]

#### Proof

The first two estimates hold for each fixed `beta` by PP3dr and therefore also
for their mixture.

Fix a source edge `e`, a movement row label `a`, and a refill column label `b`.
The corresponding pair can occur only if `e` is assigned to one of the two slots
in `alpha^{-1}(a)` and that slot receives refill label `b`.  For one such slot,
PP3dq bounds the conditional probability of `X_s=e` by `sqrt(e)/R`, uniformly
in `beta`.  Proposition PP3ds gives probability `1/W` for the required refill
label.  Sum over the two movement slots. ∎

At `W=Theta(sqrt(R))`, the exceptional pair class has probability
`O(R^(-3/2))`.

## 3. Higher coupling cylinders

### Corollary PP3du -- PROVED

Suppose a prescribed pattern fixes `q` distinct slot-edge assignments and fixes
`h` refill labels on distinct slots, where no refill label is demanded more than
twice.  Its probability under the mixed distribution is at most

\[
 \boxed{
 e^{q/2}R^{-q}
 \frac{2^h}{(2W)_h}.
 }
\]

#### Proof

For a uniform balanced map, the probability of the prescribed refill labels is
at most `(2)_1^h/(2W)_h=2^h/(2W)_h`, with repeated-label requirements only
reducing the numerator through falling factorials.  Conditional on the map,
PP3dq gives the slot-edge factor. ∎

This form allows exact cross-macro profiles to charge both source-edge rank and
new-label rank.

## 4. Remaining aggregate obstruction

Random coupling removes the pointwise rank-one spike, but a complete macro
support contains as many as `R W^2` possible same-edge movement/refill label
pairs.  Multiplying their count by the `O(1/(RW))` marginal still gives an
`O(W)` worst-case aggregate before geometric savings.

Therefore PP3dt closes fixed-rank spread but not support compression by itself.
A final preparation theorem must show that only a small fraction of the `W^2`
label pairs per source edge can lie on relevant source or cross-macro lines, or
must remove the concentrated pairs with protected trades.