# Robust absorption of the target-scale reference cycle

PP3ais--PP3ajl reduce the canonical fresh-helper cascade to one target-scale
relative cycle, then localize the ambient endpoint host by its chord structure.
That chord geometry is useful for a monotone paid conversion.  It is not an
independent obstruction in the robust direct-allocation branch.

The reason is now exact.  By PP3ajm--PP3ajr, the controller-aware base domains of
the retained original source contain the initial domains.  The current target
cycle is itself a source-valid final state.  Its binary support is below the
reserved margin, while excessive unary support produces another free target-size
source star.  Therefore the bare two-state oscillation, sparse chord hub, and
dense chord alternatives are needed only when the initial controller-aware
allocation theorem is unavailable or when a proof insists on one-step potential
descent.

## 1. The current Hamilton state is already an admissible endpoint

Let the original source be `S_0`.  At the first target-cycle boundary write

```text
S_t=O_t dot-union N_t,
L=|N_t|.
```

Under the canonical cascade, `N_t` is the point set of one relative permutation
cycle.  The current state is source-valid by construction, every controller edge
remains in `O_t`, and

```text
L=(alpha+o(1))W,
R=W^2.
```

### Proposition PP3ajs -- PROVED

Assume

```text
0<alpha<sqrt(xi/8)
```

and the marked size satisfies `q=o(W)`.  At the first `alpha W` crossing,

```text
L(L-1)<xi R/4
```

for all sufficiently large `m`.

#### Proof

The hitting-time theorem gives

```text
alpha W <= L < alpha W+q=(alpha+o(1))W.
```

Hence

```text
L(L-1)=(alpha^2+o(1))R<xi R/4.
```

This is PP3aiz, restated as a final-state support bound. ∎

No chord or alternating-host assumption is used.

## 2. Direct completion or another target-size star

Assume the initial controller-aware graphs at margin `gamma+xi` contain the
balanced ownership and global matching required by PP3ho.  By PP3ajq, the same
certificate survives in the retained-original base domains at time `t`.

### Theorem PP3ajt -- PROVED / CONDITIONAL ON THE INITIAL ROBUST ALLOCATION CERTIFICATE

At the target-cycle boundary, exactly one of the following occurs.

1. For every macro and label pair,

   ```text
   d_M^t(i,A)+d_F^t(i,B)+L(L-1) <= xi R.
   ```

   Then the current Hamilton state completes directly.

2. Some final domain loses more than `xi R` values.  Since the binary term is
   below `xi R/4`, more than `3xi R/4` losses are unary.  One point of `N_t` is
   therefore the centre of a final source-star fibre of size

   ```text
   C > 3xi R/(8L).
   ```

3. The initial controller-aware margin/global-allocation certificate was absent.

4. A source, transition, anchor, Hall, or distinguished-endpoint obstruction
   prevented construction of the source-valid path before the boundary.

#### Proof

Alternative 1 is PP3ajq with Proposition PP3ajs.  If the displayed inequality
fails and the original base certificate is present, assign the unary losses to
movement/refill type and to their causing point of `N_t`.  More than `3xi R/4`
unary losses split among at most `2L` classes, giving alternative 2.  The last
two alternatives are precisely the hypotheses not supplied by the direct
interface. ∎

### Corollary PP3aju -- PROVED

If additionally

```text
alpha<3xi/8,
```

then the star in alternative 2 has size greater than `W` for all sufficiently
large `m`.

#### Proof

Since `L=(alpha+o(1))W` and `R=W^2`,

```text
3xi R/(8L)
=
(3xi/(8alpha)+o(1))W
>
W.
```

∎

The earlier convenient condition `alpha<xi/4` is stronger and therefore also
suffices.

## 3. Bare two-state oscillation is not a robust-domain frontier

The bare oscillation host has only the original all-loop state and the current
Hamilton state.  Both are source-valid extreme states, but only the current state
is needed in Theorem PP3ajt.

### Corollary PP3ajv -- PROVED

Under the initial robust allocation certificate, a bare target-scale two-state
reference oscillation cannot be terminal.  The current state either completes
directly or creates another free target-size source star.

The absence of chords does not create an additional case.

#### Proof

Apply PP3ajt--PP3aju to the current state.  The proof does not inspect the rest of
the endpoint host.  Every point of the relative defect is free by PP3aiv. ∎

Thus “bare two-state oscillation” remains relevant only for:

- a one-step paid-potential argument that cannot use final allocation;
- an initial controller-aware margin/global-allocation failure;
- a branch in which the canonical source-valid path was not prepared.

## 4. Sparse and dense chord geometry is likewise optional in the robust branch

### Corollary PP3ajw -- PROVED

Assume the initial robust allocation certificate and a source-valid target-cycle
state.  Whether the normalized cycle host has:

1. no useful chords;
2. `o(L)` chords and an `o(L)` feedback hub;
3. a rooted chord-cycle star;
4. a distinct-signature chord-cycle bank;
5. concentrated Hamilton-backbone support;

has no effect on the direct endpoint PP3ajt.  These structures are not
independent robust-domain obstructions.

#### Proof

The direct proof uses only the final current source, the inherited base
certificate, and the final unary/binary support inequality.  Chord states are
alternative sources that are never invoked. ∎

The chord localization PP3ajf--PP3ajl remains useful and nonredundant in the paid
monotone branch, in branches with no robust base certificate, and when one seeks
a different source-valid endpoint after the current state fails some nonshadow
condition.

## 5. Revised target-cycle endpoint

### Corollary PP3ajx -- PROVED

For the canonical fresh-helper cascade, the robust direct-allocation frontier at
the target-cycle boundary is now exactly:

1. direct completion in the current state;
2. another free target-size source star;
3. failure of the **initial** controller-aware margin or global allocation
   theorem;
4. failure to prepare the source-valid marked path.

The bare two-state core, sparse-chord mobility hub, rooted chord-star family,
distinct-signature cycle bank, and Hamilton-backbone multiplicity are not separate
cases on this branch.

The remaining use of those alternating objects is confined to one-step paid
conversion or to replacing a missing robust allocation certificate.

## 6. Finite diagnostic

The script

```text
scripts/check_target_cycle_robust_absorption.py
```

checks the exact target-cycle binary budget, the remaining unary margin, and the
conservative source-star lower bound.  It reports direct absorption or a
super-target final source star without using chord data.

The no-three-in-line conjecture remains unproved.
