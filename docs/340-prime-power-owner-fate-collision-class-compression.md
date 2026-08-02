# Owner/fate/collision class compression is lossless only with the complete key

A recurrent child is represented by a nonnegative coefficient together with its
structural owner, fate, collision class, local-line class, interface label and
all remaining provenance needed by later rows. Write

\[
\kappa(c)=(o,f,\chi,\ell,\iota,\lambda).
\]

## Theorem CMR1894 -- PROVED

The tuple `kappa(c)` is the exact compression key for the declared recurrent
row. Credits with different keys remain distinct.

## Theorem CMR1895 -- PROVED

For each key `k`, the compressed coefficient is the exact sum

\[
a_k=\sum_{\kappa(c)=k}a_c.
\]

## Theorem CMR1896 -- PROVED

If `w_k>0` is the child Lyapunov weight, the compressed weighted row is
`sum_k a_k w_k`.

## Theorem CMR1897 -- PROVED

Compression by the complete key is lossless:

\[
\sum_c a_c w_{\kappa(c)}=\sum_k a_k w_k.
\]

## Theorem CMR1898 -- PROVED

Dropping fate, collision, line or interface coordinates is not an exact
quotient in general. Two credits can then collapse into one projected class
even when one is recurrent and the other is routed to a strict descendant,
creating an artificial self-loop or cycle.

## Theorem CMR1899 -- PROVED

For an incomplete geometric or provenance fibre, the honest coarse row is the
componentwise maximum of all exact rows in that fibre. An arbitrary
representative is not valid.

## Theorem CMR1900 -- PROVED

For rational coefficients and weights, multiplication by a common positive
denominator gives an equivalent exact integer row inequality.

## Corollary CMR1901 -- PROVED

Every recurrent-row implementation must store the complete key, exact
class-coefficient sums, positive child weights and either exact fibre rows or a
componentwise upper quotient. This chapter does not assert that every
recurrent state has already been populated.

The finite grouping identities, projection warning, upper-fibre domination and
integer clearing are checked in
[`scripts/verify_prime_power_owner_fate_class_compression.py`](../scripts/verify_prime_power_owner_fate_class_compression.py).
