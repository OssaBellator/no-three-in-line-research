# Clean-macro fibre shells and the exact `m=10` cycle gate

`docs/346` proves complete clean-macro reachability through `m=10`, and
`docs/348` shows that the distance-five layer is a union of complete clean
orientation fibres over 1,260 Hamilton cycles.  This chapter gives the exact
cycle-coordinate recursion behind that phenomenon.

No asymptotic bound on the macro horizon is claimed.

## 1. Eligibility masks on one clean fibre

For a parity-clean Hamilton cycle `rho`, let `Omega(rho)` be its affine root
cube.  For a source-owner triple `T`, define

```text
E_rho(T) subseteq Omega(rho)
```

to be the clean orientations for which `T` intersects at least one current
three-owner flaw support.  These are exactly the source orientations from which
the fibre-randomised clean macro may rotate `T`.

Write `rho^T` for the rotated successor cycle and

```text
d_min(eta)=min_(f in Omega(eta)) d(eta,f),
```

where `d` is the clean-macro distance to validity.  Target fibre regeneration
means that only `d_min(rho^T)`, not the source orientation's induced target
orientation, enters the recursion.

### Theorem PP3bqx -- PROVED / EXACT FIBRE-SHELL RECURSION

For a nonvalid clean state `(rho,e)`,

```text
d(rho,e)
 = 1 + min_(T: e in E_rho(T)) d_min(rho^T).
```

Consequently, for every integer `k>=1`, the orientations at distance at most
`k` are exactly

```text
C_k(rho)
 = V(rho)
   union
   union_(T: d_min(rho^T)<=k-1) E_rho(T),
```

where `V(rho)` is the set of line-valid orientations in the fibre.

#### Proof

A legal first macro step must use a triple whose owner set intersects a current
flaw, which is exactly membership in `E_rho(T)`.  After rotating, the macro may
regenerate any clean target orientation, so the least remaining distance is
`d_min(rho^T)`.  Minimising over legal first triples gives the first formula.
The sublevel identity is the same statement rewritten as `d<=k`. ∎

Thus every distance layer can be computed as a union of root-cube eligibility
masks indexed only by neighbouring cycle minima.

## 2. Complete-fibre shell criterion

Assume `rho` has no valid orientation.  Define the lower-shell coverage

```text
C_<h(rho)
 = union_(T: d_min(rho^T)<=h-2) E_rho(T)
```

and the closing-shell coverage

```text
C_h(rho)
 = union_(T: d_min(rho^T)<=h-1) E_rho(T).
```

### Corollary PP3bqy -- PROVED / WHOLE-FIBRE EXTREMALITY CRITERION

Every orientation in `Omega(rho)` has exact macro distance `h` if and only if

```text
C_<h(rho)=empty,
C_h(rho)=Omega(rho).
```

Therefore the global clean-macro horizon is the largest fibre-shell index
attained by any Hamilton cycle.  Orientation enumeration is unnecessary once
the eligibility masks and neighbouring cycle minima are known.

#### Proof

By PP3bqx, `C_<h` is precisely the set of orientations at distance at most
`h-1`, and `C_h` is precisely the set at distance at most `h`. ∎

This gives an exact structural interpretation of the audited horizon sequence
`3,4,5`: it is the maximum closing-shell index at `m=8,9,10`.  It does not yet
bound that index as `m` grows.

## 3. The exact fifth shell at `m=10`

For `h=5`, the lower gate consists of triples whose target cycle has minimum
distance at most three.  The closing gate consists of triples whose target cycle
has minimum distance four.

### Theorem PP3bqz -- VERIFIED FINITELY / COMPLETE `m=10` CYCLE-GATE CENSUS

Exactly 1,260 parity-clean Hamilton cycles satisfy

```text
union_(T: d_min(rho^T)<=3) E_rho(T) = empty,

union_(T: d_min(rho^T)=4) E_rho(T) = Omega(rho).
```

Their complete fibres contain exactly 535,072 signed states, so this shell
criterion recovers the full distance-five layer from `docs/348` with no
state-level exceptions.

For these 1,260 cycles:

```text
active triples into the distance-four cycle layer: 70 to 118,
minimum per-root closing-gate multiplicity:         70 to 118.
```

Summed over the supporting cycles, the two quantities are respectively

```text
123,852,
123,374.
```

No distance-five cycle has a nonempty gate into cycle minimum distance at most
three, and none fails complete coverage by its distance-four neighbours.

#### Verification

The checker repeats the exact `m=9` and `m=10` root-cube reachability ledgers.
It then constructs the eligibility union for every source cycle, grouped by the
minimum macro distance of the rotated target cycle.  The shell-five identities,
triple counts, and root multiplicities are compared with hard-coded regression
totals. ∎

The result localises the remaining horizon question.  The fifth step is caused
by a cycle gate: every active rotation from an extremal cycle lands no closer
than the fourth cycle layer, while the fourth-layer neighbours collectively
cover the entire source fibre.  A future asymptotic argument must bound this
cycle-shell depth or exhibit an invariant that decreases under at least one
eligible rotation.

Compile and run with

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic -fopenmp \
  scripts/check_clean_macro_fibre_shell_m10.cpp \
  -o /tmp/check_clean_macro_fibre_shell_m10

OMP_NUM_THREADS=8 /tmp/check_clean_macro_fibre_shell_m10
```

The next theorem identifier after this chapter is `PP3bra`.
