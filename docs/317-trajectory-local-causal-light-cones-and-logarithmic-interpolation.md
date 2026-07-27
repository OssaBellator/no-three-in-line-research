# Trajectory-local causal light cones and logarithmic interpolation

`docs/311` proves sparse immediate causality, while `docs/314` shows that the
union of all possible outputs becomes global after sufficient mixing.  The
possible-output union is too coarse for witness arguments: one realized
trajectory changes only a small number of orbit blocks.

This chapter proves a deterministic trajectory-local light cone and a matching
lower bound from laziness.  Together they isolate a logarithmic-time
interpolation window for the residual three-owner process after parity
preprocessing.

No charge upper bound in that window and no flaw-walk termination theorem are
proved.

## 1. Inserted blocks along one trajectory

Start from a state `x`, apply one labelled targeted deletion, and then run `t`
steps of the lazy combined chain `K_m`.  For a realized trajectory `omega`, let
`I(omega)` be the set of all signed orbit blocks inserted at any transition,
including the initial deletion.

### Proposition PP3bls -- PROVED / TRAJECTORY LOCALITY

Every realized trajectory satisfies

```text
|I(omega)| <= 3(t+1).
```

Moreover, every atomic flaw present in the final state but absent from `x`
contains at least one block from `I(omega)`.

#### Proof

The initial targeted deletion inserts one block in the two-owner case and three
blocks in the three-owner case.  A holding step inserts none, an orientation
flip inserts one, and a successor rotation inserts three.  Hence at most three
blocks are inserted per transition, including the initial deletion.

Suppose a final atomic flaw uses no inserted block.  Every one of its owner
blocks is then an unchanged block from the initial state: a block that had been
removed and later restored would itself count as inserted.  The same three cells
and signed owner descriptors were therefore already present in `x`, contrary to
the assumption that the flaw is new. ∎

The statement concerns one realized path.  Taking the union over every possible
sequence of random moves may still expose the whole state space.

## 2. Pathwise collateral-flaw bound

### Theorem PP3blt -- PROVED / SPARSE REALIZED LIGHT CONE

Along any realized delete-then-mix trajectory of length `t`, both

1. the number of atomic flaws present at the end but absent initially, and
2. the number of distinct atomic flaws that first appear at any time along the
   trajectory,

are bounded by

```text
O((t+1)n^2 log n).
```

#### Proof

By PP3bkr, one fixed signed orbit block belongs to only `O(n^2 log n)` atomic
collinear-triple flaws.  For final new flaws, apply PP3bls and take the union over
at most `3(t+1)` inserted blocks.

For flaws that first appear at an intermediate transition, PP3bkq shows that the
new flaw contains a block inserted at that transition.  Charge every such flaw
to one of its newly inserted blocks and use the same fixed-block bound. ∎

Thus geometric locality survives pathwise for times much larger than one, even
though deterministic possible causality does not.

## 3. Laziness forces logarithmic charge time

For an atomic flaw `A`, let `R_A` be its uniform labelled deletion kernel and put

```text
S_A^(t) = R_A K_m^t.
```

Write `gamma_A(t)` for the uniform-measure action charge of `S_A^(t)`.

### Proposition PP3blu -- PROVED / LAZY HOLD LOWER BOUND

For every `t>=0`,

```text
gamma_A(t) >= 2^(-t) gamma_A(0).
```

Consequently

```text
two-owner flaw:   gamma_A(t) >= 2^(-(t+1)),
three-owner flaw: gamma_A(t) >= 2^(-(t+3)).
```

#### Proof

Choose an output state `y` whose column sum under `R_A` equals
`gamma_A(0)`.  The trajectory that holds at all `t` subsequent chain steps has
probability `2^(-t)`, so

```text
K_m^t(y,y) >= 2^(-t).
```

All transition masses are nonnegative.  The column sum of `R_A K_m^t` at `y`
therefore contains at least the all-hold contribution

```text
2^(-t) sum_(x in A) R_A(x,y)
 = 2^(-t) gamma_A(0).
```

Use the exact immediate charges `1/2` and `1/8` from PP3ble. ∎

This lower bound is elementary but rules out probability-scale charge after only
constant many lazy steps.

## 4. The logarithmic interpolation window

### Corollary PP3blv -- PROVED / FRONTIER SHARPENED

Suppose a delete-then-mix action achieves a three-owner charge bound

```text
gamma_A(t) <= C n^(-3)
```

for a constant `C`.  Then necessarily

```text
t >= 3 log_2 n - O_C(1).
```

For two-owner flaws, probability-scale charge `O(n^-2)` similarly requires

```text
t >= 2 log_2 n - O(1).
```

At any time `t=O(log n)`, however, PP3blt gives the trajectory-local collateral
bound

```text
O(n^2 log^2 n).
```

After parity preprocessing removes the two-owner family, multiplying this
pathwise scale by the stationary three-owner probability `Theta(n^-3)` gives

```text
O(log^2 n / n) = o(1).
```

#### Proof

Combine PP3blu with the assumed charge upper bound and take base-two logarithms.
The trajectory bound is PP3blt with `t=O(log n)`, and the final displayed scale
uses PP3bki. ∎

The final product is not by itself a valid resampling or witness criterion: it
mixes a stationary event probability with a pathwise count, not a proved action
charge.  It identifies the precise missing theorem.

## 5. Revised charge--causality frontier

The endpoints are now separated into three scales:

```text
t=0:
  possible causality O(n^2 log n), charge constant;

t=Theta(log n):
  realized light cone O(n^2 log^2 n),
  probability-scale charge is no longer ruled out by laziness;

t=polynomial worst-case mixing:
  charge near stationary, possible causality global.
```

The next useful result must control **weighted or trajectory-conditioned**
causality rather than the union of possible outputs.  Concrete targets are:

1. prove an upper bound on `gamma_A(t)` for `t=O(log n)` after parity-clean macro
   deletion;
2. bound the expected or exponential moment of the trajectory flaw light cone;
3. formulate a witness-sequence theorem using path probabilities rather than
   possible causal edges;
4. show that consecutive macro deletion outputs remain sufficiently warm to
   avoid restarting from worst-case mixing;
5. combine the owner-intersecting macro from `docs/316` with this logarithmic
   trajectory window.

The current spectral-gap estimate gives a much longer general mixing upper
bound.  Closing the gap between the logarithmic lower scale and that polynomial
upper scale is now the central interpolation problem.
