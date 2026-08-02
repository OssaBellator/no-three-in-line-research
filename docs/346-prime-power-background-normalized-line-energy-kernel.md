# Background-normalized coordinates preserve the exact line kernel

Fix a positive inherited scale `s`. For a background line load `h`, define

\[
\rho_1=\binom h2/s^2,\qquad \rho_2=h/s,\qquad \rho_3=1.
\]

## Theorem CMR1942 -- PROVED

The tuple `(rho1,rho2,rho3)` is an exact rational normalized line profile at
scale `s`.

## Theorem CMR1943 -- PROVED

The rank-one kernel is exactly `s^2 k rho1`.

## Theorem CMR1944 -- PROVED

The rank-two kernel is exactly `s C(k,2) rho2`.

## Theorem CMR1945 -- PROVED

The rank-three kernel is exactly `C(k,3) rho3`.

## Theorem CMR1946 -- PROVED

Changing inherited scale changes the normalized coordinates but preserves their
reconstructed absolute kernel.

## Theorem CMR1947 -- PROVED

A response assignment may be scored directly by the reconstructed normalized
kernel coordinates.

## Theorem CMR1948 -- PROVED

Multiplication by a common multiple of the scale and rational denominators gives
an exact integer certificate.

## Corollary CMR1949 -- PROVED

Background normalization is an exact coordinate transfer, not a strictness
proof. All owner, fate, line and provenance labels remain attached to the
normalized row.

The reconstruction and scale-transfer identities are checked in
[`scripts/verify_prime_power_background_normalized_kernel.py`](../scripts/verify_prime_power_background_normalized_kernel.py).
