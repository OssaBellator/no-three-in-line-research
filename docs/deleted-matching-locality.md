# Remote-cylinder locality with a deleted host matching

SRR1d supplies a stationary four-cycle oracle in sufficiently dense
missing-edge hosts. The remaining issue is correlation between
vertex-disjoint matching cylinders. That correlation is exactly
computable when the missing cells themselves form a partial matching.

Let

\[
G_Q=K_{N,N}\setminus Q,
\]

where \(Q\) is a partial matching of rank \(t\), and let \(\mu_Q\) be
the uniform measure on perfect matchings of \(G_Q\). For a host-valid
partial matching \(E\) of rank \(s\), write \(Z_Q(E)\) for the number of
perfect matchings of \(G_Q\) containing \(E\). Let \(q(E)\) be the number
of missing cells in \(Q\) whose row and column are both unused by \(E\).

## SRR2a -- deleted-matching cylinder locality

### Theorem SRR2a -- PROVED

The extension count is

\[
\boxed{
Z_Q(E)
=
\sum_{j=0}^{q(E)}
(-1)^j\binom{q(E)}j(N-s-j)!.
}
\]

Equivalently,

\[
Z_Q(E)=(N-s)!\,\alpha_Q(E),
\]

where, whenever \(N-s>t\),

\[
\boxed{
1-\frac{t}{N-s}
\le
\alpha_Q(E)
\le1.
}
\]

Let \(F,B\) be compatible host-valid partial matchings of ranks \(f,b\)
whose row sets and column sets are disjoint. If
\(N-f>t\) and \(N-b>t\), then

\[
\boxed{
\frac{\mu_Q(B\mid F)}{\mu_Q(B)}
\le
\frac{(N)_b}{(N-f)_b}
\cdot
\frac1{
\left(1-\frac{t}{N-f}\right)
\left(1-\frac{t}{N-b}\right)
}.
}
\]

Here \((a)_b=a(a-1)\cdots(a-b+1)\). For fixed \(f,b\) and
\(t=o(N)\), the right side is \(1+o(1)\).

### Proof

After fixing \(E\), there are \(N-s\) unused rows and columns. A missing
cell of \(Q\) is still relevant exactly when both of its endpoints are
unused, and those \(q(E)\) surviving cells remain a matching.
Inclusion--exclusion over the surviving forbidden cells gives the first
box.

After division by \((N-s)!\), \(\alpha_Q(E)\) is the probability that a
uniform permutation of the unused vertices avoids those \(q(E)\)
cells. The upper bound is immediate. Each forbidden cell occurs with
probability \(1/(N-s)\), so the union bound gives

\[
\alpha_Q(E)\ge1-\frac{q(E)}{N-s}
\ge1-\frac{t}{N-s}.
\]

For disjoint compatible \(F,B\),

\[
\frac{\mu_Q(B\mid F)}{\mu_Q(B)}
=
\frac{Z_Q(F\cup B)Z_Q(\varnothing)}
{Z_Q(F)Z_Q(B)}.
\]

Substitution of the factorial and \(\alpha\) factors gives

\[
\frac{(N)_b}{(N-f)_b}
\cdot
\frac{
\alpha_Q(F\cup B)\alpha_Q(\varnothing)
}{
\alpha_Q(F)\alpha_Q(B)
}.
\]

Bound both numerator factors by one and use the two lower bounds in the
denominator. This proves the last box. \(\square\)

## Resampling consequence

Every vertex of \(G_Q\) has degree at least \(N-1\). Hence SRR1d gives
at least \(N-3\) four-cycle partners for every distinguished host edge
when \(N\ge4\), together with a reversible uniform-stationary
flaw-removal kernel.

If a forbidden partial matching \(F\) contains the distinguished edge
and \(B\) is vertex-disjoint from \(F\), the switch cannot create \(B\)
pathwise. Starting from \(\mu_Q\) conditioned on \(F\), SRR2a therefore
gives

\[
\frac{\Pr(B\text{ after resampling}\mid F)}{\mu_Q(B)}
\le
\frac{(N)_b}{(N-f)_b}
\cdot
\frac1{
\left(1-\frac{t}{N-f}\right)
\left(1-\frac{t}{N-b}\right)
}.
\]

Thus all five one-layer SRR1 properties hold for complete hosts with a
deleted matching of rank \(t=o(N)\), for fixed-rank flaws and remote
events. This does not yet handle arbitrary missing-edge patterns or the
correlation created by conditioning on an edge-disjoint second layer.

`scripts/verify_deleted_matching_locality.py` enumerates the exact
extension counts and all disjoint rank-at-most-two cylinder pairs for
small deleted-matching hosts.
