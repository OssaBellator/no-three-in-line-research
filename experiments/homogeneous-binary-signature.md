# Homogeneous binary-signature regression

This experiment accompanies
[`docs/128-homogeneous-signature-paid-capacity.md`](../docs/128-homogeneous-signature-paid-capacity.md),
[`scripts/check_homogeneous_binary_signature.py`](../scripts/check_homogeneous_binary_signature.py),
and
[`homogeneous-binary-signature-example.json`](homogeneous-binary-signature-example.json).

Run

```bash
python scripts/check_homogeneous_binary_signature.py \
  experiments/homogeneous-binary-signature-example.json
```

The fixture checks three six-variable signatures.

## Credit-rich signature

The forbidden pairs are

```text
(0,0), (0,1).
```

The exact valid sequences are

```text
111110
111111
```

so the maximum number of cross-oriented variables is six.  In particular the
all-cross assignment verifies PP3qe(1).

## Credit-poor signature

The forbidden pairs are

```text
(0,1), (1,1).
```

The exact valid sequences are

```text
000000
100000
```

so the all-line assignment is valid but at most one variable may use the cross
state.  This verifies the paid-capacity alternative PP3qe(4).

## Local contradiction

The forbidden pairs are

```text
(0,0), (1,1).
```

No length-six sequence is valid.  More generally, no length-three sequence is
valid, because two of three binary states agree.  This verifies PP3qe(3).

The checker also enumerates all sixteen signatures for every length from three
through eight.  It reports a failure if any signature violates the
cross-capacity, credit-poor, or local-contradiction classification.

These are exact finite checks of the homogeneous Boolean classification.  They
do not prove that a geometric rectangle bank has any particular signature; that
input comes from PP3pi and the common-line construction.
