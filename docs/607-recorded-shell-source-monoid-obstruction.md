# Recorded shell source-monoid obstruction

`docs/601` showed that each recorded shell action has even cycle-coordinate sum.
A possible escape would be to compose recorded actions, idle slots, simultaneous
controls, repetitions, or the stored startup buffer.  This chapter closes that
escape.

The recorded generators are

```text
(1,0,1), (1,1,0), (0,1,1).
```

The idle action is `(0,0,0)`, and five times the stored fractional startup buffer
is `(2,0,2)`.

## 1. Parity closure

### Theorem PP3cun — PROVED / SOURCE MONOID PARITY

Every nonnegative integer combination of the recorded actions has even
coordinate sum.  Adding idle operations, simultaneous compositions, repeated
periods, or the scaled startup buffer preserves that parity.

#### Proof

Each generator has even coordinate sum, and parity is additive.  The startup
buffer vector is itself twice an integral vector. ∎

### Theorem PP3cuo — PROVED / BOUNDED COMPOUND AUDIT

The checker enumerates coefficients `0,...,8` for the three recorded controls and
idle.  The resulting `729` distinct compound cycle vectors all have even
coordinate sum.  None of the three unit odd actions is present.

The enumeration is a diagnostic; `PP3cun` is the unbounded proof.

### Theorem PP3cup — PROVED / GENUINELY NEW ACTION REQUIRED

No operation built solely from the recorded clean-macro primitives crosses the
missing index-two lattice coset.  Any odd-sum cycle action must therefore be a
new source operation, not a repackaging or compound of the recorded catalogue.

No shell ledger row is promoted.

## Exact audit

```bash
python scripts/check_shell_recorded_closure_parity.py
```
