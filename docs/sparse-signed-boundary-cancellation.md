# Sparse signed boundary cancellation and compression

This note records SAS5iw--SAS5ja.  It extends the nonnegative boundary-profile quotient to signed additive ledgers by separating exact coordinate cancellation from residual boundary mass.

## Contract

Each retained ledger has a signed integer boundary vector `z_l in [-B,B]^d`.  Outputs add exactly.  For coordinate `j`, let `P_j` and `N_j` be total positive and negative magnitudes, let

`Z_j=P_j-N_j`,

and define total variation and net boundary mass by

`V=sum_j(P_j+N_j)`,
`M=sum_j |Z_j|`.

## Results

### SAS5iw — finite signed profile quotient

There are at most `(2B+1)^d` exact signed boundary signatures.  Aggregating equal signatures preserves both the total vector `Z` and the variation data.

### SAS5ix — exact cancellation identity

The number of coordinatewise positive/negative cancellation pairs is

`C=sum_j min(P_j,N_j)=(V-M)/2`.

After these pairs are removed, every coordinate has only one sign and the residual vector is exactly `Z`.

### SAS5iy — barrier/cancellation dichotomy

For any `0<theta<1`, either

`M>=theta V`

and some coordinate satisfies `|Z_j|>=theta V/d`, or

`C>(1-theta)V/2`.

### SAS5iz — balanced compression interface

In the cancellation branch, coordinatewise opposite-sign units provide exact neutral pairing tickets.  In the barrier branch, the least heavy signed coordinate is a retained boundary obstruction for the existing barrier ledger.

### SAS5ja — reset conditions

Nonadditive output, omitted coordinates, illegal opposite-sign pairing, dynamic coordinate dictionaries or untracked cancellation side effects return a classification/compression reset.

## Proof

For each coordinate,

`P_j+N_j-|P_j-N_j|=2 min(P_j,N_j)`.

Summing proves the cancellation identity.  If `M>=theta V`, pigeonhole gives a coordinate of magnitude at least `M/d`.  Otherwise substitution into `C=(V-M)/2` gives the cancellation alternative.

## Finite audit

Run:

`python scripts/verify_sas_signed_boundary_cancellation.py`

The deterministic audit checks:

- 10,000 signed output systems;
- 49,771 ledger vectors;
- 45,338 distinct signed signatures;
- 251,210 variation units;
- 102,716 net boundary units;
- 74,247 exact cancellation pairs;
- 5,278 barrier and 4,722 cancellation epochs.

## Scope

This theorem is an exact algebraic compression interface.  It does not prove that opposite-sign boundary units can be physically paired without violating sparse-word legality, nor does it prove core shareability or the output lower bound.  SAS6 and the no-three-in-line conjecture remain open.
