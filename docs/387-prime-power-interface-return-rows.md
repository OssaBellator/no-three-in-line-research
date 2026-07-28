# Global return and interface rows with lexicographic descent

Disconnected synchronized block components still require one common global scale, while
return, interface and off-diagonal rows must be checked against that scale. This chapter
combines exact integer weight inequalities with a well-founded rank for critical rows.

## Theorem CMR2270 — PROVED AS AN INTERFACE

Every synchronized block-ratio component receives one positive integer component multiplier.
The multiplier family covers every component exactly and is normalized by

\[
\boxed{\gcd\{k_C\}=1.}
\]

For global state `g` in component `C`, the final global weight is

\[
\boxed{\widehat W_g=k_C W_g.}
\]

## Theorem CMR2271 — PROVED

Every global state receives one nonnegative integer interface rank `rho(g)`. The rank records
cover the complete global state registry exactly.

The rank is a separate well-founded coordinate; it does not replace the integer weight.

## Theorem CMR2272 — PROVED

A return, interface or off-diagonal row is the exact record

\[
(r,\text{kind},p,b,\{a_t\},\text{evidence}),
\]

where `p` is a known nonauxiliary nonsink parent, `b` is a signed integer fixed offset and
all target multiplicities `a_t` are positive integers on known nonauxiliary states.

## Theorem CMR2273 — PROVED

For each interface row, the checker reconstructs

\[
L_r=b+\sum_t a_t\widehat W_t,
\qquad
\mu_r=\widehat W_p-L_r.
\]

Negative margin is rejected.

## Theorem CMR2274 — PROVED

A positive-margin interface row is classified as strict. A zero-margin row is accepted only
when it has at least one target and every positive target strictly descends in rank:

\[
\boxed{\mu_r=0\Longrightarrow \rho(t)<\rho(p)\quad\text{for every }a_t>0.}
\]

Thus a critical row is certified by a secondary well-founded descent rather than silently
treated as strict.

## Theorem CMR2275 — PROVED

The certificate publishes the final global state weights, component multipliers, complete
rank registry, exact row loads, margins, strict/critical-descending partition and all
component, rank, weight and row digests.

## Theorem CMR2276 — HONEST INTERFACE BOUNDARY

The arithmetic proves strict weight decrease or zero-weight rank descent relative to the
supplied rows, component multipliers and ranks. It does not prove that the supplied rows are
the genuine complete return/interface family or that the declared rank has its intended
external meaning.

## Corollary CMR2277 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_interface_return_rows.py` validates component scaling, constructs
the final global integer weight registry and accepts exactly strict or critical-descending
return/interface/off-diagonal rows.

The checker was syntax-compiled in the publication environment. No genuine interface-row
population or global rank table is yet supplied.
