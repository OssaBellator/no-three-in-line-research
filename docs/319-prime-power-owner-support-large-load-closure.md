# Small owner supports close a recurrent large-load regime

CMR1718--CMR1725 bound the probability mass of owned prescriptions by the
matching number of the possible owner-edge support. Adding explicit geometric
multiplicity caps turns that capacity into a strict-improvement theorem for
small-support recurrent states.

This is especially useful for reused-support and prime-field terminal states,
where the exact support has one or two edges. It applies only when every
recurrent child credit under consideration has its canonical owner in the
specified support and all other child classes have already been routed or
included.

Fix a response host of side `d` with a nonempty response law. Let `A` be the
possible owner-edge support and let `mu=mu(A)` be its matching number. For each
rank `r in {1,2,3}`, let `m_r` bound the number of genuinely new credits sharing
one rank-`r` response prescription and owner label.

Put

\[
L_d(m_1,m_2,m_3)
=
\sum_{r=1}^3m_r C(d-1,r-1).
\]

## 1. Support-local expected collateral bound

### Theorem CMR1726 -- PROVED

The expected number of genuinely new rank-at-most-three credits whose canonical
owners lie in `A` is at most

\[
\boxed{
\mu(A)L_d(m_1,m_2,m_3).
}
\]

### Proof

For each rank, CMR1719 bounds the distinct owned-prescription mass by
`mu(A) C(d-1,r-1)`. Multiply by the maximum credit multiplicity `m_r` and add the
three ranks. ∎

When the owned candidate map is injective, the parenthesized factor becomes

\[
1+(d-1)+C(d-1,2)
=
1+d(d-1)/2.
\]

## 2. Strict-improvement closure

Suppose the selected execution destroys `D` current credits and creates no
unaccounted recurrent credit outside the owner-supported family.

### Theorem CMR1727 -- PROVED

If

\[
\boxed{
D
>
\mu(A)L_d(m_1,m_2,m_3),
}
\]

then at least one executable response has strictly smaller potential.

### Proof

CMR1726 bounds the expected new recurrent collateral below the destroyed load.
Every already routed structural or finite-resource child lies outside the
recurrent diagonal comparison by hypothesis. A finite response average below
the current potential contains one strict-improvement response. ∎

The theorem is a diagonal-row criterion, not a claim that every response host is
nonempty.

## 3. Vertex-cover specialization

Suppose `A` is covered by `k` source/target vertices.

### Theorem CMR1728 -- PROVED

The sufficient condition

\[
\boxed{
D>kL_d(m_1,m_2,m_3)
}
\]

implies strict improvement.

### Proof

CMR1720 gives `mu(A)<=k`; apply CMR1727. ∎

The cover vertices may be owner rows, target columns, token supports, prefix
supports, carry supports or fixed-interface endpoints. Shared vertices are
counted once.

## 4. Fixed finite support

Suppose the possible owner set itself has at most `s` edges.

### Theorem CMR1729 -- PROVED

Since `mu(A)<=s`, strict improvement follows from

\[
\boxed{
D>sL_d(m_1,m_2,m_3).
}
\]

For an injective candidate map this becomes

\[
\boxed{
D>s\left(1+d(d-1)/2\right).
}
\]

### Proof

Every matching in an `s`-edge graph has size at most `s`. Apply CMR1727. ∎

This bound can be sharpened whenever the support edges share a source or target,
because then `mu(A)<s`.

## 5. Prime-field reused-support specialization

CMR1608 proves that a prime-field root terminal support `J(a,b)` has size one or
two.

### Theorem CMR1730 -- PROVED

Assume every recurrent child retained in the reused-support row has canonical
owner in the fixed terminal support `J(a,b)`.

1. For a one-edge support, strict improvement follows from
   \[
   D>L_d(m_1,m_2,m_3).
   \]
2. For a two-edge support, strict improvement follows from
   \[
   D>2L_d(m_1,m_2,m_3).
   \]
3. If the two support edges share a source or target, the matching number is one,
   so the first threshold applies.

### Proof

Use CMR1608 and apply CMR1729. In branch three, the two-edge support has matching
number one. ∎

Response-layer reintroductions already routed through the returned-edge kernel
are not counted a second time in this reused-support row.

## 6. Weighted potential version

Give rank-`r` credits nonnegative potential weight at most `lambda_r` in addition
to multiplicity cap `m_r`. Put

\[
L_d^{\lambda}
=
\sum_{r=1}^3m_r\lambda_r C(d-1,r-1).
\]

### Theorem CMR1731 -- PROVED

The expected new weighted potential owned in `A` is at most

\[
\boxed{
\mu(A)L_d^{\lambda}.
}
\]

Hence destruction of weighted load `D_w` is strict whenever

\[
\boxed{D_w>\mu(A)L_d^{\lambda}.}
\]

### Proof

Apply the weighted owner-support theorem CMR1722 with multiplicity caps and
compare the resulting expectation with the destroyed weighted load. ∎

This includes selector restoration weights and class-dependent Lyapunov weights.

## 7. Integer slack and overflow localization

Assume the response law has common denominator `Z>0`. Define the integer support
slack

\[
S_A
=
ZD-Z\mu(A)L_d(m_1,m_2,m_3).
\]

### Theorem CMR1732 -- PROVED

1. `S_A>0` is an exact sufficient integer certificate for strict improvement.
2. If the certificate fails and `mu(A)>0`, then some rank satisfies
   \[
   \boxed{
   m_r C(d-1,r-1)
   \ge
   \left\lceil\frac{D}{3\mu(A)}\right\rceil.
   }
   \]

### Proof

The first statement clears the response denominator in CMR1727. If all three
rank contributions were smaller than `D/(3mu)`, their sum would be smaller than
`D/mu`, contradicting failure of the strict support bound. Use integrality for
the ceiling. ∎

Thus every failed support closure identifies one quantitatively large rankwise
multiplicity class for sharper geometric analysis.

## 8. Small-support endpoint

### Corollary CMR1733 -- PROVED

Small owner supports now have a complete recurrent-row compiler.

1. Determine the exact owner support and its matching number or a vertex cover.
2. Prove rankwise prescription multiplicity caps.
3. Compare destroyed load with the support-local expectation bound.
4. If the integer slack is positive, place the row in strict improvement.
5. If it fails, retain only a rank class meeting the explicit multiplicity
overflow threshold.
6. Apply the one- or two-edge specialization to prime-field reused-support states.

The unresolved reused-support frontier is therefore confined to states with
large prescription multiplicity, insufficient destroyed load, or child owners
outside the claimed fixed support. No all-`n` theorem is claimed.

Support-local expectations, strict thresholds, one/two-edge specializations,
weighted forms and multiplicity overflow are checked in
[`scripts/verify_prime_power_owner_support_large_load_closure.py`](../scripts/verify_prime_power_owner_support_large_load_closure.py).
