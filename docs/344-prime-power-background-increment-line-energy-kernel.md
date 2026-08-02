# Background additions have exact nonnegative line-energy increments

Adding one background point to a line changes its load from `h` to `h+1` while
the response occupancy `k` is fixed.

## Theorem CMR1926 -- PROVED

The exact one-point increment is

\[
\Delta K(h,k)=K(h+1,k)-K(h,k)=kh+\binom k2.
\]

## Theorem CMR1927 -- PROVED

The rank-one increment is exactly `kh`, the number of new background-pair
incidences with one response point.

## Theorem CMR1928 -- PROVED

The rank-two increment is exactly `C(k,2)`, one new background choice for every
response pair on the line.

## Theorem CMR1929 -- PROVED

The pure rank-three response term is unchanged by adding a background point.

## Theorem CMR1930 -- PROVED

Every background increment is nonnegative.

## Theorem CMR1931 -- PROVED

For any sequence of point additions, the increments telescope exactly to the
complete kernel difference.

## Theorem CMR1932 -- PROVED

Rationally weighted increments admit exact integer certificates after a common
denominator is cleared.

## Corollary CMR1933 -- PROVED

Background growth can be audited line by line through exact nonnegative
increments. This does not imply that the accumulated kernel remains below the
parent budget.

The identities and telescoping checks are implemented in
[`scripts/verify_prime_power_background_increment_kernel.py`](../scripts/verify_prime_power_background_increment_kernel.py).
