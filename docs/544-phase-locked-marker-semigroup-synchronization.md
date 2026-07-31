# Phase-locked marker semigroup synchronization

The marker Apéry certificate in `docs/537` realizes every length at least 18, but
a global schedule may also prescribe the phase of one marker type.  This chapter
shows that the stored lengths four and seven still realize every sufficiently
large side under an arbitrary modulo-three phase demand.

Write

```text
N=4a+7b,
```

and require `b congruent t (mod 3)`.

## 1. Phase locking as a translated semigroup

### Theorem PP3cng -- PROVED / PHASE-LOCKED MARKER REDUCTION

For `t in {0,1,2}`, a nonnegative solution with `b congruent t (mod 3)` exists
if and only if

```text
N-7t is in <4,21>.
```

#### Proof

Write `b=t+3c`.  Then

```text
N=4a+7t+21c,
```

with `a,c>=0`, which is exactly the stated translated numerical semigroup
condition. ∎

## 2. Exact locked conductors

### Theorem PP3cnh -- PROVED / LOCKED APERY CONDUCTOR TABLE

The Apéry set of `<4,21>` modulo four is

```text
(0,21,42,63),
```

so its conductor is 60.  Consequently the phase-`t` schedule exists for every

```text
N>=60+7t,
```

and the preceding length `59+7t` is impossible for that phase.

#### Proof

The displayed values are the least semigroup elements in residues
`0,1,2,3 mod 4`.  The conductor formula gives `63-4+1=60`.  Translation by `7t`
gives the phase threshold.  Since 59 is the Frobenius number of `<4,21>`, the
translated predecessor is excluded. ∎

## 3. Arbitrary phase selectors

### Theorem PP3cni -- PROVED / UNIFORM THREE-PHASE MARKER SCHEDULE

Let `t(N)` be any function from the positive integers to `{0,1,2}`.  For every
`N>=74` there are nonnegative integers `a,b` satisfying

```text
4a+7b=N,
b congruent t(N) (mod 3).
```

The bound 74 is the maximum of the three exact thresholds `60,67,74`.

#### Proof

Apply `PP3cnh` with the demanded phase.  The largest phase threshold occurs at
`t=2`. ∎

## 4. Stored exact audit

The audit `scripts/check_phase_locked_marker_semigroup.py` reconstructs the
Apéry table, checks the sharp predecessor failure in all three phases, and
enumerates every locked representation through length 1000.  It also verifies
three unrelated phase-selector functions from the uniform threshold 74 onward.

## 5. Prime-patching consequence

Boundary marker selection can absorb one external modulo-three phase request
without losing all-length eventuality.  This is a genuine cross-frontier
compatibility statement: a threshold or shell phase may choose the seven-block
count modulo three, while the boundary still realizes every sufficiently large
side.  It does not yet identify the geometric phase selector arising in the
full construction.
