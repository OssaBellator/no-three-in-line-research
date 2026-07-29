# Bounded-denominator integral gain potential

This note records BDA5dt--BDA5dx. It turns a rational local gain certificate into a canonical integer-weight account suitable for occurrence tickets and exact mass debits.

## Contract

Let `G=(V,E)` be a finite directed physical source graph. Every edge `u->v` has a retained positive rational gain `g_uv`. Assume positive rational weights `q_v` satisfy

`q_v g_uv <= q_u`

on every edge. Integer occurrence mass obeys `m' <= g_uv m` on a legal transfer.

## Theorem block

### BDA5dt — common-denominator integerization

Let `L` be the least common multiple of the denominators of all `q_v`. Then `Q_v=Lq_v` are positive integers and satisfy

`Q_v g_uv <= Q_u`

on every edge.

### BDA5du — primitive canonical normalization

Dividing all `Q_v` by their common gcd gives a unique primitive positive integer potential up to the fixed vertex ordering and the original rational ray.

### BDA5dv — integer weighted-mass monotonicity

Every legal integer transfer satisfies

`Q_v m' <= Q_u m`.

Thus the potential-weighted source account is integer-valued and nonincreasing edge by edge.

### BDA5dw — exact threshold ticket bound

If every selected restoration consumes at least `J` units of primitive weighted mass, then an account of size `P` pays at most `floor(P/J)` such restorations.

### BDA5dx — local failure return

A zero or omitted vertex weight, a changed gain, failure of one edge inequality, nonintegral occurrence multiplicity outside the declared expansion, splitting, or source-less creation is returned as an exact local obstruction/reset.

## Proof

Multiplication by the positive common denominator preserves every edge inequality. Gcd normalization preserves the inequalities and makes the integer ray primitive. Combining `m'<=g_uv m` with `Q_vg_uv<=Q_u` proves weighted monotonicity. The threshold bound is integer division.

## Finite audit

Run `python scripts/verify_bda_integral_gain_potential.py`.

The deterministic audit checks 6,000 finite systems, 26,800 vertices, 53,940 certified edges and transfers, 269,090 primitive integer-weight units, and 1,529 sampled exact local factor violations.

## Scope

The theorem does not construct the physical rational weights or edge damping factors. It only makes an existing rational certificate integral and occurrence-faithful. BDA6 and the no-three-in-line conjecture are not proved.