# Bounded-denominator integral gain restoration bank

This note records BDA5dy--BDA5ec. It composes the primitive integer gain potential with the paid restoration bank.

## Contract

Let a finite physical source graph have primitive positive integer vertex weights `q_v`. Every legal edge `u -> v` carries a retained rational gain `a_e/b_e` satisfying
`a_e q_v <= b_e q_u`.
An occurrence-faithful transfer sends input raw mass `m` to output raw mass at most `floor(a_e m/b_e)`. Initial raw mass and every exogenous deposit are named by vertex. A selected restoration consumes raw mass at one exact vertex.

## Theorem block BDA5dy--BDA5ec

### BDA5dy — integral potential mass

The potential mass `sum_v q_v m_v` is an integer. Every legal edge transfer weakly decreases it.

### BDA5dz — exact transfer debit

For a transfer carrying input `m` and output `m'`, the nonnegative integer
`q_u m - q_v m'`
is the exact dissipated debit.

### BDA5ea — cumulative restoration account

Cumulative restoration potential plus remaining live potential is at most initial potential plus named deposited potential.

### BDA5eb — threshold ticket bound

If every selected restoration consumes at least `J` units of potential, then at most
`floor((P_initial + P_deposit)/J)`
selected restorations occur.

### BDA5ec — local failure return

A failed edge inequality, output above the retained gain, source-less mass, splitting, changed primitive weights or unrecorded deposits return the exact local factor/lineage obstruction.

## Proof

Multiply the raw transfer inequality by `q_v` and use `a_e q_v <= b_e q_u`. All quantities are integral. Summing the exact edge debits, restoration consumptions and named deposits gives the cumulative account and threshold bound.

## Finite audit

Run `python scripts/verify_bda_integral_gain_restoration_bank.py`.

## Scope

The theorem does not construct the physical integer weights or damping factors and does not prove BDA6 or the no-three-in-line conjecture.
