# The side-four rank-three zero-response problem has a finite blocker atlas

Let

\[
H_4=K_{4,4}\setminus(I_4\cup\{(0,1)\}).
\]

A raw host is `H4\X`, where `X` is a partial matching in `H4`; it is retained
when it has a perfect matching. A response is zero when its four grid cells
contain no collinear triple.

## Theorem CMR1958 -- PROVED

Zero-response feasibility is decided exactly by enumerating perfect matchings
and applying the determinant collinearity test to every response triple.

## Theorem CMR1959 -- PROVED

There are exactly 86 executable raw side-four hosts. Exactly 75 admit at least
one zero-triple response and 11 admit none.

## Theorem CMR1960 -- PROVED

The inclusion-minimal partial-matching deletion blockers for all zero responses
are exactly

```text
{(0,2),(2,0)}
{(0,2),(3,1)}
{(1,3),(3,1)}
```

## Theorem CMR1961 -- PROVED

Every zero-response-free raw host contains at least one of these three canonical
blockers.

## Theorem CMR1962 -- PROVED

Among the 11 zero-response-free hosts, nine have minimum response-triple count
one and two have minimum response-triple count four.

## Theorem CMR1963 -- PROVED

The exact dispatch is: select a zero-triple response when one exists; otherwise
retain the canonical blocker class and its exact positive-response minimum.

## Theorem CMR1964 -- PROVED

The atlas audit rejects altered host counts, missing blockers, nonminimal
blockers and incorrect survivor minima.

## Corollary CMR1965 -- PROVED

The normalized side-four zero-response problem is completely finite. This atlas
does not prove that every larger or provenance-refined host has a zero response
or a globally strict alternative.

The full 86-host enumeration and blocker atlas are checked in
[`scripts/verify_prime_power_rank_three_zero_response_blockers.py`](../scripts/verify_prime_power_rank_three_zero_response_blockers.py).
