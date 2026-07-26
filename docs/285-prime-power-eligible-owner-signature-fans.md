# Eligible owner pairs form finite prime-power signature fans

Retain old matching `M`, the absolute edge order, and an allowed entering owner
`a notin M`.  Let the owner have matching side `d` inside an inherited
prime-power envelope of side

\[
t=p^k,
\]

with ambient coordinate span `W_omega<=t-1`.
For another allowed response edge `b`, define

\[
\chi_a^M(b)=\mathbf1_{\{b\in M\text{ or }a\prec b\}}.
\]

### Theorem CMR1454 -- PROVED

Conditioned on `a in R`, the response-layer partners eligible to accompany
owner `a` are exactly

\[
\boxed{\{b\in R\setminus\{a\}:\chi_a^M(b)=1\}.}
\]

### Proof

An edge in `M` is old and never precedes `a` among entering edges.  An edge
outside `M` is entering and is eligible exactly when it follows `a`. ∎

Define

\[
\mathscr C_e^{\rm elig}(a)=
\sum_{\substack{b\in O\\a,b\text{ nonaxis}}}c_\omega(h(a,b))
+
\frac1{p_e(a)}
\sum_{\substack{b\in E(H_e)\setminus\{a\}\\
\{a,b\}\text{ compatible}\\a,b\text{ nonaxis}}}
\chi_a^M(b)p_e(a,b)c_\omega(h(a,b)).
\]

### Theorem CMR1455 -- PROVED

\[
\boxed{
g_e(a)\le\Gamma_e^{\rm elig}(a)
:=\frac12\mathscr C_e^{\rm elig}(a)
\le\Gamma_e^{\rm cap}(a).}
\]

### Proof

Use CMR1454 in the realized capacity bound CMR1447 and exact conditional pair
probabilities.  Dropping `chi_a^M` gives CMR1449. ∎

For an old edge `a in M`, set the owner weight to zero.

## Prime-power signatures

For a nonaxis pair, write

\[
b-a=G(u,v)
\]

with `G>0` and canonically oriented primitive `(u,v)`.  Put

\[
s(a,b)=v_p(G),
\qquad
\delta(a,b)=[u:v]\in\mathbb P^1(\mathbb F_p),
\]

and let `H(a,b)` be the dyadic band containing the primitive height.  Record
also whether the partner is fixed in `O` or belongs to the response layer.

### Theorem CMR1456 -- PROVED

Every eligible pair has one signature

\[
\boxed{\sigma(a,b)=(t_{\rm pair},s,\delta,H).}
\]

Here `0<=s<=k-1`.  At depth `s`, both cells lie in the same prefix carry cell
and separate at the next digit in projective direction `delta`.

### Proof

The gcd scale and primitive direction are unique.  Since all coordinates lie
in one side-`p^k` envelope, a nonzero difference has valuation at most `k-1`.
Division by the exact `p`-adic scale leaves a nonzero projective direction.
The common prefix residue is determined by the owner and `s`. ∎

Let `m_{e,sigma}(a)` be the conditional expected number of eligible selected
partners in signature class `sigma`.  Put

\[
B_\omega=1+\left\lfloor\log_2\max\{1,W_\omega\}\right\rfloor.
\]

### Theorem CMR1457 -- PROVED

\[
\boxed{
\mathscr C_e^{\rm elig}(a)
\le\sum_{\sigma=(t_{\rm pair},s,\delta,H)}
 c_{\omega,H}m_{e,\sigma}(a).}
\]

For fixed owner `a`, at most

\[
\boxed{C_\omega=2k(p+1)B_\omega}
\]

signature positions occur.

### Proof

Use the band coefficient CMR1453.  There are two partner types, `k` separation
depths, `p+1` projective directions and `B_omega` height bands.  The prefix
cell is determined by `a` and `s`. ∎

### Theorem CMR1458 -- PROVED

If `Gamma_e^{elig}(a)>=G_0`, some nonzero class satisfies

\[
\boxed{
\frac12c_{\omega,H}m_{e,\sigma}(a)
\ge\frac{G_0}{C_\omega}.}
\]

Hence

\[
\boxed{m_{e,\sigma}(a)\ge
\frac{2G_0}{C_\omega c_{\omega,H}}.}
\]

### Proof

The nonnegative class contributions number at most `C_omega` and sum to at
least `2G_0`. ∎

### Theorem CMR1459 -- PROVED

For every signature class, some response containing `a` realizes at least

\[
\boxed{\lceil m_{e,\sigma}(a)\rceil}
\]

eligible selected partners of that class.

### Proof

The class population is a nonnegative integer random variable with that
conditional expectation. ∎

Put

\[
D_p(H)=(p-1)\left\lceil\frac{4H}{p}\right\rceil^2.
\]

### Theorem CMR1460 -- PROVED

A fixed projective class contains at most `D_p(H)` canonically oriented
primitive integer directions with

\[
H\le\max(|u|,|v|)<2H.
\]

Consequently, `K` simultaneously selected partners in one signature class put
at least

\[
\boxed{\left\lceil\frac K{D_p(H)}\right\rceil}
\]

partners on one real line through `a`.

### Proof

For each nonzero projective scalar, each coordinate lies in one residue class
modulo `p` inside an interval of length below `4H`, giving at most
`ceil(4H/p)^2` vectors.  Sum over `p-1` scalars. ∎

### Corollary CMR1461 -- PROVED

Failure of the eligible-edge assignment certificate produces, in one actual
response, a simultaneous owner-labelled family with one separation depth, one
prefix carry cell, one projective direction and one primitive-height band.  It
concentrates quantitatively on one real line through the owner.  The theorem
applies to scattered residual factors because matching side `d`, envelope
height `k` and ambient coordinate span `W_omega` are kept separate.  The open
step is the weighted execution gain of that loaded signature.  No all-`n`
theorem is claimed.

Checked in full-grid and synthetic prime-power specializations by
[`scripts/verify_prime_power_eligible_owner_signature_fans.py`](../scripts/verify_prime_power_eligible_owner_signature_fans.py).
