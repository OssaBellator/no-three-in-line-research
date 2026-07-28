# Owner-local atomic collateral and the trajectory light cone

The current parity-repair and clean-macro actions rotate the outgoing targets of
three source owners.  The remaining atomic frontier is caused by three-owner
collateral, so this chapter records the exact deterministic locality available
before any probabilistic drift or weighted-charge estimate is applied.

No negative-drift, expansion, or no-three-in-line theorem is claimed.

## 1. Owner-support locality

A signed Hamilton state assigns to each owner `i` one signed target assignment

```text
(i -> rho(i), e_i).
```

For a source triple `T`, the successor rotation changes the targets of exactly
the three owners in `T`; all signs may either be retained or changed only on
`T` in the locally coupled action.

### Proposition PP3boz -- PROVED / EXACT OWNER-SUPPORT LOCALITY

Let `x` and `y` be signed Hamilton states related by one successor rotation on
`T`, with all owners outside `T` retaining their signed assignments.  Then:

1. every two-owner atomic count supported on a pair disjoint from `T` is
   identical in `x` and `y`;
2. every three-owner atomic count supported on a triple disjoint from `T` is
   identical in `x` and `y`;
3. every parity predicate between two owners outside `T` is identical in `x`
   and `y`.

#### Proof

The four selected cells of an owner depend only on that owner's source, target,
and sign.  All of these data are unchanged outside `T`.  Therefore the complete
point configuration on any owner support disjoint from `T` is unchanged, so its
atomic collinearity count is unchanged.  The two-owner parity predicate is also
a function only of the two displayed signed assignments, giving the third
claim. ∎

## 2. Exact number of mutable support slots

### Corollary PP3bpa -- PROVED / SUPPORT-SLOT CENSUS

For one three-owner rotation, the only atomic support slots that can change are
those meeting `T`.  Their exact numbers are

```text
two-owner supports:   C(m,2)-C(m-3,2) = 3m-6,
three-owner supports: C(m,3)-C(m-3,3) = (3m^2-15m+20)/2.
```

#### Proof

Subtract the supports contained entirely in the `m-3` untouched owners from all
owner pairs and triples. ∎

The statement is about potentially mutable support slots.  Most such slots can
still have zero geometric change for a particular rotation.

## 3. Deterministic atomic-collateral envelope

A two-owner support contains eight cells.  At most

```text
C(8,3)-2C(4,3)=48
```

mixed-owner cell triples can occur on it.  A three-owner support has at most

```text
4^3=64
```

atomic triples, one cell chosen from each owner orbit.

### Theorem PP3bpb -- PROVED / ONE-STEP ATOMIC ENVELOPE

For any locally coupled three-owner successor rotation,

```text
|Delta Z_2| <= 48(3m-6),
|Delta Z_3| <= 64(C(m,3)-C(m-3,3)),
```

and hence

```text
|Delta Z| <= 96m^2-336m+352.
```

#### Proof

By PP3boz, only supports meeting `T` can change.  On each mutable two-owner
support, both the old and new atomic counts lie between zero and 48, so their
absolute difference is at most 48.  The analogous bound is 64 for a three-owner
support.  Multiply by the support counts in PP3bpa and add:

```text
48(3m-6)+64(3m^2-15m+20)/2
 = 96m^2-336m+352.
```

∎

This worst-case envelope is intentionally geometry-blind.  Its role is to make
the collateral scale explicit: one repair can alter only `O(m^2)` atomic event
slots, rather than the full `Theta(m^3)` three-owner family.

## 4. A trajectory-local causal light cone

Let a repair trajectory use source triples `T_1,...,T_k`, and let

```text
R = T_1 union ... union T_k,
r = |R| <= min(m,3k).
```

### Theorem PP3bpc -- PROVED / TRAJECTORY OWNER LIGHT CONE

Between the initial and final states, every atomic support disjoint from `R` is
unchanged.  Consequently the number of support slots that can differ is at most

```text
C(m,2)-C(m-r,2)
```

for two-owner supports and

```text
C(m,3)-C(m-r,3)
```

for three-owner supports.  The total atomic-count difference obeys

```text
|Z_final-Z_initial|
 <= 48[C(m,2)-C(m-r,2)]
  + 64[C(m,3)-C(m-r,3)].
```

In particular, when `r<=3k` and `k=o(m)`, only `O(km^2)` atomic slots lie in the
trajectory light cone.

#### Proof

Apply PP3boz at every step.  An owner support disjoint from the union `R` is
disjoint from every rotated source triple, so its displayed assignments and
atomic count never change.  Count the supports meeting `R` and apply the same
per-support atomic maxima as in PP3bpb. ∎

## 5. Revised drift interface

The result separates locality from drift.

1. Parity repair can create three-owner collateral, but it cannot create it on
   owner supports outside the rotated-owner light cone.
2. A logarithmic repair trajectory touches at most `O(log m)` owners if owner
   reuse is controlled, leaving only `O(m^2 log m)` potentially changed atomic
   slots.
3. Weighted Hall capacities and heat-kernel trajectories therefore need not pay
   for the full cubic flaw universe on each path; they need a bound on the local
   light cone and its predecessor merging.
4. The remaining hard step is sign and magnitude: prove negative compensated
   drift, or exhibit a bounded cancellation word, inside this deterministic
   support envelope.

The next theorem identifier after this chapter is `PP3bpd`.
