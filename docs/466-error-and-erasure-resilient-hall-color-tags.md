# Error-and-erasure resilient Hall color tags

`docs/460` gives Singleton-optimal Hall color tags against erased marker
coordinates.  A geometric marker may also be read incorrectly rather than merely
lost.  This chapter gives the exact error--erasure condition needed to preserve
private Hall targets.

Let a proper residual Hall edge coloring use `M` colors.  Encode each color by a
word in a `p`-ary code `C` of length `n`.  An observation may erase at most `e`
coordinates and alter at most `t` of the remaining coordinates.

## 1. List ambiguity and reverse load

For an observation `omega`, let `L(omega)` be the number of color codewords that
can produce `omega` after the allowed errors and erasures, and put

```text
L_(t,e)=max_omega L(omega).
```

### Theorem PP3ceg -- PROVED / ERROR--ERASURE LIST LOAD

If every source has at least `d` residual Hall actions and chooses uniformly,
then the observed tagged-target load is at most

```text
lambda<=L_(t,e)/d.
```

#### Proof

For each compatible color, proper edge coloring permits at most one incident
source action at a fixed geometric target.  At most `L_(t,e)` colors are
compatible with the observation, and each contributes at most `1/d`. ∎

## 2. Exact private decoding radius

### Theorem PP3ceh -- PROVED / DISTANCE ERROR--ERASURE CRITERION

If the code has minimum Hamming distance `delta` and

```text
2t+e<delta,
```

then every allowed observation has a unique compatible color.  Consequently the
private Hall load remains exactly bounded by `1/d`.

#### Proof

If two distinct codewords were both compatible, remove the `e` erased
coordinates.  Each codeword differs from the observation in at most `t`
remaining positions, so the two codewords differ in at most `2t+e` positions in
total, contradicting their distance. ∎

## 3. Optimal field-coordinate tags

### Theorem PP3cei -- PROVED / SINGLETON-OPTIMAL ERROR--ERASURE TAGS

Suppose `M=p^k`.  Any `p`-ary tag correcting `t` errors and `e` erasures must
have

```text
n>=k+2t+e.
```

When `n=k+2t+e<=p`, a length-`n` Reed--Solomon evaluation code attains equality.

#### Proof

Correction requires distance at least `2t+e+1`.  The Singleton bound gives
`p^k<=p^(n-delta+1)`, hence `n>=k+delta-1>=k+2t+e`.  Reed--Solomon evaluation of
polynomials of degree below `k` has size `p^k` and distance `n-k+1=2t+e+1`. ∎

Thus the marker-coordinate cost is exactly the message dimension plus twice the
error budget plus the erasure budget.

## 4. Exact audit

Run

```bash
python scripts/check_error_erasure_hall_tags.py
```

The stored code uses `49` colors over `F_7`, length `5`, one error, and one
erasure.  It verifies distance `4`, Singleton optimality, and all `5,880`
corrupted observations by exact finite enumeration.
