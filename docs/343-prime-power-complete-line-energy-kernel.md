# The complete line-energy kernel keeps all three response ranks coupled

For one real line with `h` background points and `k` response points define

\[
K(h,k)=k\binom h2+\binom k2h+\binom k3.
\]

## Theorem CMR1918 -- PROVED

`K(h,k)` is the complete local new-triple kernel on the line.

## Theorem CMR1919 -- PROVED

Its three terms are respectively the rank-one, rank-two and rank-three response
contributions.

## Theorem CMR1920 -- PROVED

A background is represented exactly by its line loads and retained incidence
labels.

## Theorem CMR1921 -- PROVED

A response is represented exactly by its matching-compatible line occupancies.

## Theorem CMR1922 -- PROVED

For every finite response law, expected complete line energy is the probability
weighted sum of the exact kernels.

## Theorem CMR1923 -- PROVED

For a rational response law with denominator `Z`, the expectation has an exact
integer numerator obtained by summing response multiplicities times kernels.

## Theorem CMR1924 -- CONDITIONAL STRICT CLOSURE

If the complete weighted kernel is below destroyed load or the parent budget,
the selected or averaged response row is strict.

## Corollary CMR1925 -- PROVED

The complete kernel is the finite interface

\[
K(h,k)=\binom{h+k}{3}-\binom h3.
\]

No rank may be discarded unless it is separately routed or paid.

The binomial identity, finite profile sums and integer numerators are checked in
[`scripts/verify_prime_power_complete_line_energy_kernel.py`](../scripts/verify_prime_power_complete_line_energy_kernel.py).
