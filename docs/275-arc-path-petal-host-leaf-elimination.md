# Arc- and path-petal conditional hosts are exact finite cycle spaces

The dense current-support endpoint still lists residual endpoint-host failure in the
fixed-axis arc-petal and fixed-centre path-petal branches.  At the actual petal call
there is no residual matching host to regularize: one has already selected a finite
filler block and conditioned a directed Hamilton cycle on one prescribed arc or one
prescribed two-arc path.

The conditioned cycle spaces have exact positive cardinalities.  The complete source
and insertion objective is then an average over that explicit finite set.  Failure
of the paid inequality can only be carried by one of its displayed nonnegative
source or cost terms.  Conditional Hall, alternating-component, non-superregular,
coordinate-shortage, and role-host alternatives are not produced at this stage.

This chapter removes those stale petal-host leaves.  It does not pay centre-core,
local petal, global support-ranked, or source concentration at the removal-credit
scale.

## 1. Exact arc-conditioned cycle space

Let `V` be a filler block of size `b>=3` and prescribe one directed arc `x->y`.

### Proposition PP3bbo -- PROVED

The number of directed Hamilton cycles on `V` containing `x->y` is exactly

```text
(b-2)!.
```

For every additional compatible directed forest `F` with `u` arcs, the conditional
probability that a uniform arc-conditioned Hamilton cycle contains `F` is

```text
1/(b-2)_u,
```

unless `F` together with `x->y` contains a proper directed cycle, in which case the
probability is zero.

#### Proof

Contract the prescribed arc to one ordered object.  The resulting `b-1` cyclic
objects have `(b-2)!` directed cyclic orders.  Contracting `u` further compatible
arcs gives the falling-factorial ratio.  A proper directed cycle cannot be contained
in a Hamilton cycle on all `b` vertices. ∎

This is the exact cycle law used in PP3add and PP3ade.

## 2. Exact path-conditioned cycle space

Prescribe a directed path `x->y->z` on three distinct vertices of a filler block of
size `b>=3`.

### Proposition PP3bbp -- PROVED

The number of directed Hamilton cycles containing the path is exactly

```text
(b-3)!.
```

For every additional compatible `u`-arc forest, the conditional inclusion
probability is

```text
1/(b-3)_u,
```

unless a proper directed cycle is formed, in which case it is zero.

#### Proof

Contract the two-arc path to one ordered object.  There are `b-2` cyclic objects and
therefore `(b-3)!` directed cyclic orders.  Further compatible contractions give the
probability formula. ∎

This is the exact cycle law used in PP3acy.

## 3. Filler-block existence is already supplied

### Proposition PP3bbq -- PROVED

At every arc- or path-petal call produced by the dense current-support row:

1. the marked scale is at most `W`;
2. the permanent matching block and source layer are explicit;
3. the required quadratic helper reservoir is automatic;
4. selected-controller and role-domain losses are linear;
5. every positive local source, transition, anchor, old-grid, and insertion event is
   represented in the complete support table.

Consequently the petal call reaches a nonempty finite block on which PP3bbo or
PP3bbp applies.  It cannot terminate before conditioning through coordinate shortage,
raw Hall failure, role-host failure, or an untyped distinguished-endpoint condition.

#### Proof

Items 1--5 are PP3baa, PP3bai--PP3bak, and PP3bao--PP3bap.  Raw explicit-host
alternatives are eliminated by PP3bal, and internal coordinate cover is eliminated
by PP3baq.  The petal itself fixes only one arc or one path inside the supplied
block, so PP3bbo or PP3bbp gives a nonempty conditioned cycle space. ∎

## 4. Exhaustive arc-petal endpoint

Let `B` be a comparable-cost arc-petal bank and use the notation of PP3ade.  For one
petal `e`, define

```text
Q_arc(e)=sum_u S_e,u/(b-2)_u
         +(a(e)+J_e^core+J_e^var)/R_*.
```

### Theorem PP3bbr -- PROVED

Exactly one of the following occurs.

1. The bank average of `Q_arc(e)` is below one, and PP3ade gives a source-valid
   strict paid decrease.
2. At least one displayed nonnegative class has bank-average mass at its normalized
   unit scale: source-invalid patterns, local arc cost, centre-core insertion,
   variable bounded-support insertion, or another explicitly typed paid term.

There is no residual endpoint-host alternative.

#### Proof

By PP3bbq every petal has the exact nonempty cycle space PP3bbo.  The expression
`Q_arc` is the full nonnegative first-moment objective of PP3ade.  If its average is
below one, apply that theorem.  Otherwise the average is at least one; since it is a
finite sum of named nonnegative classes, one class carries its corresponding share
of the unit threshold.  No other event is omitted from the complete support table. ∎

## 5. Exhaustive path-petal endpoint

For a comparable-cost path-petal bank use the notation of PP3acy and put

```text
Q_path(e)=sum_u S_e,u/(b-3)_u
          +(beta_L(e)+J_e^core+J_e^var)/R_*.
```

### Theorem PP3bbs -- PROVED

Exactly one of the following occurs.

1. The bank average of `Q_path(e)` is below one, and PP3acy gives a source-valid
   strict paid decrease.
2. One displayed source, local path, centre-core, variable insertion, or other typed
   paid class has normalized bank-average mass at unit scale.

There is no residual endpoint-host alternative.

#### Proof

Use PP3bbq and the exact path-conditioned space PP3bbp, then repeat the nonnegative
objective argument of PP3bbr with PP3acy. ∎

## 6. Revised petal frontier

### Corollary PP3bbt -- PROVED

For dense current support, arc- and path-petal banks no longer have independent:

- conditional Hall failure;
- alternating-component failure;
- non-superregular host failure;
- coordinate shortage;
- role-host failure; or
- residual endpoint-host failure.

Their exhaustive frontier is paid completion or a finite named weighted
concentration: source mass, local petal cost, centre-core cost, bounded-support
variable cost, or another already typed current-potential term.

Together with PP3bbh--PP3bbn, the dense current row is now free of host-existence and
raw multiplicity frontiers.  Its remaining work is payment or conversion of the
finite named weighted concentrations.  The dense source row and the global
prime-minus-one seed theorem remain separate.  The no-three-in-line conjecture
remains unproved.

## 7. Finite diagnostic

Run

```bash
python scripts/check_petal_conditioned_cycle_spaces.py \
  experiments/petal-conditioned-cycle-spaces-example.json
```

The checker enumerates directed Hamilton cycles on a finite block, verifies the exact
arc- and path-conditioned counts, checks compatible forest cylinder counts, and
rejects `host_failure` as a petal endpoint outcome.
