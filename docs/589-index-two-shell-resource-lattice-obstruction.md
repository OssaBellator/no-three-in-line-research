# Index-two shell resource lattice obstruction

`docs/583` derived the actual action-to-cycle incidence matrix of the stored
`docs/517` shell schedule:

```text
A = ((1,1,0),
     (0,1,1),
     (1,0,1)).
```

Earlier identity-debt shell benchmarks treat the three resource coordinates as
independently serviceable unit debts.  This chapter compares the two resource
types exactly.

## 1. Integer image of the action lattice

### Theorem PP3csl -- PROVED / INDEX-TWO CYCLE LATTICE

The determinant of `A` is two.  Its integer image is exactly

```text
{y in Z^3 : y_1+y_2+y_3 is even}.
```

#### Proof

The exact inverse is

```text
A^(-1)y = 1/2 *
          ( y_1-y_2+y_3,
            y_1+y_2-y_3,
           -y_1+y_2+y_3 ).
```

All three numerators have the same parity as `y_1+y_2+y_3`.  Hence the inverse
is integral exactly for even coordinate sum.  The determinant gives index two.
∎

### Theorem PP3csm -- PROVED / UNIT-CYCLE TYPE MISMATCH

None of the three unit cycle-resource vectors has an integral action preimage.
Their preimages are respectively

```text
( 1/2, 1/2,-1/2),
(-1/2, 1/2, 1/2),
( 1/2,-1/2, 1/2).
```

Therefore the identity-incidence unit-debt model cannot be identified with the
`docs/517` cycle-resource model by an integral relabelling of actions.

#### Proof

Substitute the three unit vectors into the inverse formula. ∎

## 2. Stored period remains valid

### Theorem PP3csn -- PROVED / EVEN-LATTICE PERIOD CERTIFICATE

The stored action counts `(5,7,3)` map to cycle totals `(12,10,8)`, which lie in
the even-sum image lattice.  The action buffer `(2/5,0,0)` maps to cycle reserve
`(2/5,0,2/5)`.  Thus the exact `docs/517` schedule remains valid even though the
identity-debt interpretation does not.

#### Proof

Direct matrix multiplication gives both vectors. ∎

## 3. Exact audit

Run

```bash
python scripts/check_shell_index_two_resource_lattice.py
```

## 4. Frontier consequence

The shell source bridge is now typed precisely.  Future clean-macro resources
must be shown to live in the even-sum cycle lattice or must include a fractional
or additional action capable of crossing the missing coset.  The identity shell
benchmark cannot be promoted through this bridge.
