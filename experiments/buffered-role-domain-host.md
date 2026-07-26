# Buffered role-domain square-root host diagnostic

Run

```text
python scripts/check_buffered_role_domain_host.py \
  experiments/buffered-role-domain-host-example.json
```

The stored model has twelve marked roles and a square-root-critical helper reservoir

```text
s=12,
N=144=s^2.
```

Each role forbids at most `3s=36` helpers.  The buffered theorem first seeks an
independent set of size

```text
b=(3+1)s=48.
```

Inside the stored 48-helper buffer, the role-domain sizes are

```text
[12, 12, 14, 21, 28, 35, 42, 48, 48, 48, 48, 48].
```

Thus the two tightest roles retain exactly `s` choices, but Hall still assigns all
twelve roles pairwise distinct helpers.  One valid assignment is

```text
[36, 43, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0].
```

For comparison, failure of an independent 48-set has exact simple-support thresholds

```text
rank-two threshold   4.5638297872340425,
rank-three threshold 14.088344125809435.
```

The complete rank-two and rank-three examples have respectively 10,296 edges and
487,344 triples; the rank-two graph has a matching of size 72.  These finite numbers
illustrate the asymptotic `Omega(s^2)` and `Omega(s^3)` dense alternatives.

The expected output is

```text
marked roles 12
helper reservoir 144
domain loss constant 3
excluded per role 36
buffer size 48
allowed counts in buffer [12, 12, 14, 21, 28, 35, 42, 48, 48, 48, 48, 48]
minimum allowed 12
role matching size 12
role assignment [36, 43, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
rank-two failure threshold 4.5638297872340425
complete rank-two support 10296
rank-two matching size 72
rank-three failure threshold 14.088344125809435
complete rank-three support 487344
outcome buffered_role_domain_square_root_host
```

This verifies PP3awk in a tight finite role-domain model and checks the exact
falling-factorial thresholds used by PP3awj--PP3awl.
