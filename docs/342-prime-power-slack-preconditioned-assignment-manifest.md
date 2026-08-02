# Rank-three slack preconditions the executable assignment manifest

Let a response host have denominator `Z`, pure rank-three numerator `A3` and
integer slack `S3=Z-A3`. Pure rank three is paid once. Every remaining
rank-one, rank-two, return and selector contribution must fit in the residual
strict budget `S3-1`.

## Theorem CMR1910 -- PROVED

Replacing the pure rank-three term by the exact host slack `S3` is an exact
preconditioning identity.

## Theorem CMR1911 -- PROVED

The weighted rank-one and rank-two residual score is certified against the
remaining budget after rank-three payment.

## Theorem CMR1912 -- PROVED

Return and selector residual terms use the same remaining budget and are not
optimized against a second copy of rank-three slack.

## Theorem CMR1913 -- PROVED

Every preconditioned rank-two and rank-three inner dual covers the exact residual
coefficient it claims.

## Theorem CMR1914 -- PROVED

One outer dual covers the complete preconditioned score on every allowed edge.

## Theorem CMR1915 -- PROVED

After clearing denominators, strictness is the exact integer inequality

\[
A_3+A_{\rm residual}\le Z-1.
\]

## Theorem CMR1916 -- PROVED

Negative slack, duplicate allocation, unallocated claimed slack, incomplete
inner coverage and nonstrict total rows are rejected.

## Corollary CMR1917 -- PROVED

A slack-preconditioned manifest stores `Z`, `A3`, one exact allocation of
`S3-1`, the residual labelled coefficients and complete inner/outer duals. It
does not assert that every host has positive slack.

The integer allocation and corruption checks are implemented in
[`scripts/verify_prime_power_slack_preconditioned_manifest.py`](../scripts/verify_prime_power_slack_preconditioned_manifest.py).
