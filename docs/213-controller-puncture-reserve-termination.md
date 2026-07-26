# Controller-puncture reserve termination

PP3ake--PP3akj show that a captive source-star centre becomes free after deleting
one controller value from the fixed infrastructure.  Repeating that operation
changes the candidate universe, so the old fixed-potential termination theorem
cannot be applied globally without bookkeeping.

The correct bookkeeping is by **puncture epochs**.  Between two punctures the
controller universe is fixed and every paid trade decreases an integer potential.
A puncture can occur only once at each controller point.  Hence the process is
finite until a prescribed controller reserve is exhausted.  Reserve exhaustion
is itself a concrete macro-local concentration, not an unspecified failure of
termination.

## 1. Punctured controller infrastructure

For each macro let

```text
X_i subseteq E_i
```

be its punctured controller set and put

```text
E_i^X=E_i\X_i,
X=union_i X_i.
```

Let `V_X` be the candidate-entry universe whose controllers lie in the active
pools `E_i^X`.  Define the controller-shadow potential

```text
Psi_X(S')
```

by the same formula as PP3ij, but using only entries in `V_X`.

### Proposition PP3akk -- PROVED

For fixed `X`, every controller-preserving paid endpoint, rectangle, cycle, or
tomographic trade has an exact integer change in `Psi_X`.  A strict paid trade
decreases `Psi_X` by at least one, and `Psi_X` is a nonnegative integer.

#### Proof

Once `X` is fixed, the active controller edges and candidate-entry universe are
fixed.  The proof of PP3ij--PP3il applies verbatim to `V_X`. ∎

Thus every epoch with no additional puncture contains only finitely many strict
paid trades.

## 2. Domain cost of a puncture set

Let

```text
b_i=|X_i|.
```

### Proposition PP3akl -- PROVED

For every macro and label pair,

```text
|H_(i,A,B)^ctrl(S\X;E_i^X)|
>=
|H_(i,A,B)^ctrl(S)|-b_i.
```

Consequently, if the original domains have size at least `(gamma+xi)R` and

```text
max_i b_i <= xi R/2,
```

then every punctured retained-original domain has size at least

```text
(gamma+xi/2)R.
```

Every original balanced ownership and global label matching therefore remains
valid at the lower threshold throughout the whole puncture history.

#### Proof

Deleting source points can only improve safety by PP3ajm--PP3ajo.  The only loss
is that the `b_i` punctured values are no longer available as controllers in
macro `i`.  Subtract them and apply PP3ajp. ∎

This is a cumulative statement: isolated punctures do not need separate margin
arguments.

## 3. Finite termination before reserve exhaustion

Fix a reserve parameter `beta>0` and impose

```text
|X_i| < beta R
```

for every macro.  A **puncture step** chooses a captive star centre

```text
p in E_a^X,
```

adds `p` to `X_a`, and then invokes the free-centre conversion PP3akh or PP3aki.

### Theorem PP3akm -- PROVED / CONDITIONAL CONVERSION INTERFACE

Suppose that at every non-ready state before reserve exhaustion, at least one of
the following is available.

1. A strict paid trade for the current fixed universe `V_X`.
2. A captive source-star centre that can be punctured and supplied with the
   marked source-valid host required by PP3akh or PP3aki.
3. An explicit source, transition, anchor, Hall, alternating, endpoint-host, or
   initial-allocation obstruction.

Then after finitely many operations one reaches one of:

1. a ready/directly completable state;
2. an explicit obstruction from item 3;
3. a macro `i` with

   ```text
   |X_i|=ceil(beta R).
   ```

No infinite sequence of paid trades and punctures is possible before this
endpoint.

#### Proof

There are at most `M ceil(beta R)` puncture steps before some macro exhausts its
reserve.  Between two consecutive punctures, `X` is fixed, and Proposition
PP3akk permits only finitely many strict paid trades.  Concatenate the finitely
many epochs. ∎

The theorem is qualitative but exact.  It replaces a moving-controller recurrence
by a finite sequence of fixed-universe monotone epochs.

## 4. Reserve exhaustion is a structured core

For every punctured controller `p`, record:

1. the macro containing `p`;
2. a designated source-star fibre through `p` at the time of puncture;
3. the marked host outcome used after puncturing.

### Corollary PP3akn -- PROVED

If macro `i` exhausts a `beta R` reserve, then it contains a chronological family
of `beta R` distinct original controller points, each of which was the centre of
a designated controller-shadow star when removed from the infrastructure.

If every punctured star had degree at least `W`, the history contains at least

```text
beta R W
```

designated star-incidence units counted with time labels.  Failure to convert
this history is therefore a macro-local controller-centre concentration at scale
`R`, not a target-size isolated star.

#### Proof

A controller point is punctured at most once, so the centres are distinct.  The
recorded designated fibres have their asserted sizes by construction.  Summing
the time-labelled incidence units gives the displayed lower bound. ∎

No claim is made that the unlabelled candidate entries are all distinct across
different times.  Repeated entries are precisely a higher-order controller
ownership/support concentration.

## 5. Robust reserve range

### Corollary PP3ako -- PROVED / CONDITIONAL INITIAL ROBUST-CERTIFICATE INTERFACE

Assume the initial controller-aware domains have margin `gamma+xi` and a valid
balanced ownership/global matching.  For every

```text
0<beta<xi/2,
```

the same certificate survives throughout the entire `beta R` puncture reserve in
each macro.

At every puncture epoch, a source-valid marked state of size `q=o(W)` therefore
has the direct endpoint:

1. completion after final support is charged;
2. a new free source star of degree `omega(W)`;
3. marked-host failure.

The puncture history itself cannot erode the retained-original base certificate.

#### Proof

Apply PP3akl to the cumulative puncture set.  Then use PP3aki and
PP3ajq--PP3ajx at each final state. ∎

## 6. Revised moving-controller frontier

### Corollary PP3akp -- PROVED

A target-size controller-centred star is no longer a terminal object.  Repeated
captive conversions reduce to:

1. fixed-universe paid descent inside puncture epochs;
2. robust direct completion or a new free super-target star;
3. marked source/transition/anchor/Hall/endpoint-host failure;
4. failure of the initial controller-aware allocation theorem;
5. a macro-local `Theta(R)` controller-puncture history core.

The remaining genuinely new issue is therefore not one captive star, but whether
a positive fraction of one macro's controller reserve can be forced to become
successive star centres without yielding a paid or direct completion.

No completion of the no-three-in-line conjecture is claimed.
