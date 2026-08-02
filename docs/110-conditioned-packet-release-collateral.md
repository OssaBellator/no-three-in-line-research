# Conditioned packet release and external collateral transfer

PX210--PX212 extract a common-product packet from large support-four mass and
release it with a constant-density no-two-cycle matching bank.  A recursive
proof also needs sequential exposure: after fixing a bounded partial matching,
the residual packet bank must retain spread without paying one new constant per
exposed edge.

The key observation is exact.  Conditioning on a partial packet matching adds
only the reversed exposed edges to the residual forbidden positions.  Those
reversed edges form one partial matching, regardless of the exposure rank.
Thus conditioning increases the forbidden degree by at most one.

Use the packet normalization from PX212.  Rows and columns are both labelled by
`[h]`; a packet-certified support-four collision is a permutation two-cycle.
Let `F` have maximum row and column degree at most `Delta`, and let

\[
\Omega_F^{\rm rel}
=
\{\pi\in S_h:
 (i,\pi(i))\notin F,
 \ \pi\text{ has no two-cycle}\}.
\]

## 1. Reverse positions after exposure

Let

\[
E_0=\{i_r\mapsto j_r:r\in[a]\}
\]

be an extendable compatible partial matching contained in some member of
`Omega_F^rel`.  Delete its source rows and target columns.

For every exposed edge `i->j`, a future residual edge `j->i` would complete a
two-cycle.  When both its row and column survive, call `j->i` a reverse
position.

### Lemma PX213a -- PROVED

The surviving reverse positions form a partial matching.  Consequently the
residual forbidden graph has maximum row and column degree at most

\[
\boxed{\Delta+1.}
\]

### Proof

The exposed source labels `i_r` are distinct and the exposed target labels
`j_r` are distinct.  Hence the reversed source labels `j_r` are distinct and
the reversed target labels `i_r` are distinct.  Deleting unavailable rows or
columns preserves this property.  Thus the reverse positions have row and
column degree at most one. \(\square\)

The important point is that the cost is one extra partial matching, not `a`
extra matchings.

## 2. Conditioned release cylinders

After deleting `E_0`, the residual row-label and column-label sets need not be
the same.  A packet two-cycle remains possible only for two labels present on
both sides.  The canonical two-cycle event system is therefore a subsystem of
the one used in PX212, with no larger dependency degrees.

### Theorem PX213 -- PROVED

Put

\[
n=h-a.
\]

If

\[
\boxed{
n\ge\max(32,32(\Delta+1)),
}
\]

then `E_0` has at least

\[
\boxed{
e^{-4\Delta-8}n!}
\]

extensions in `Omega_F^rel`.

Consequently, under the uniform measure on `Omega_F^rel`,

\[
\boxed{
\frac{e^{-4\Delta-8}}{(h)_a}
\le
\Pr(E_0\subseteq M)
\le
\frac{e^{4\Delta+4}}{(h)_a}.
}
\]

Condition on `E_0 subseteq M`.  Every further compatible residual partial
matching `E_1` of rank `r` satisfies

\[
\boxed{
\Pr(E_1\subseteq M\mid E_0\subseteq M)
\le
\frac{e^{4\Delta+8}}{(n)_r}.
}
\]

If also

\[
n-r\ge\max(32,32(\Delta+1)),
\]

then

\[
\boxed{
\Pr(E_1\subseteq M\mid E_0\subseteq M)
\ge
\frac{e^{-4\Delta-8}}{(n)_r}.
}
\]

### Proof

By PX213a, the residual forbidden-position graph has maximum degree at most
`Delta+1`.  The residual packet two-cycle events form a subset of all unordered
label-pair transposition events on an order-`n` permutation space.  Repeat the
mixed singleton/two-cycle lopsided-LLL proof of PX212 with `Delta+1` in place of
`Delta`.

The singleton and two-cycle witnesses remain

\[
x_1=\frac2n,
\qquad
x_2=\frac4{n^2}.
\]

The resulting residual density is at least

\[
e^{-4(\Delta+1)-4}
=
e^{-4\Delta-8}.
\]

This proves the extension count.

For the lower bound on `Pr(E_0 subseteq M)`, divide the extension count by the
trivial upper bound `h!` on the full released family.  For the upper bound, use
PX212: at most `(h-a)!` permutations contain `E_0`, while

\[
|\Omega_F^{\rm rel}|
\ge
e^{-4\Delta-4}h!.
\]

After conditioning, at most `(n-r)!` extensions contain `E_1`; divide by the
lower bound `e^(-4Delta-8)n!` on all extensions of `E_0`.  For the conditional
lower bound, apply the same residual extension theorem to `E_0 union E_1` and
divide by the trivial upper bound `n!`. \(\square\)

Thus arbitrary bounded-rank sequential exposure costs one absolute `e^4`
factor relative to PX212, independently of how many edges were exposed.

## 3. External certificate-load transfer

Let `C_r` be a finite weighted family of rank-`r` partial matchings in the packet
subgrid, with `1<=r<=3`.  Delete every member which uses a forbidden cell or
contains a packet two-cycle; its probability under the release measure is zero.
Let

\[
W_r^{\rm ext}
=
\sum_{E\in\mathcal C_r^{\rm ext}}w(E)
\]

be the remaining external weight.

For `M` uniform on `Omega_F^rel`, put

\[
\Phi_{\rm ext}(M)
=
\sum_{r=1}^3
\sum_{E\in\mathcal C_r^{\rm ext}}
w(E)\mathbf1_{E\subseteq M}.
\]

### Theorem PX214 -- PROVED

If `h>=max(32,32Delta)`, then

\[
\boxed{
\mathbb E\Phi_{\rm ext}(M)
\le
 e^{4\Delta+4}
 \sum_{r=1}^3
 \frac{W_r^{\rm ext}}{(h)_r}.
}
\]

Every packet-certified rank-two transposition event has expectation exactly
zero.

More generally, after conditioning on an extendable rank-`a` partial matching
`E_0`, if `n=h-a>=max(32,32(Delta+1))`, then

\[
\boxed{
\mathbb E\bigl(
 \Phi_{\rm ext}(M)
 \mid E_0\subseteq M
\bigr)
\le
 e^{4\Delta+8}
 \sum_{r=1}^3
 \frac{W_r^{\rm ext}(E_0)}{(n)_r}.
}
\]

Here `W_r^ext(E_0)` includes only residual certificates compatible with the
exposure.

### Proof

Every released-compatible rank-`r` cylinder has probability at most

\[
\frac{e^{4\Delta+4}}{(h)_r}
\]

by PX212.  Multiply by weights and sum.  A partial matching containing a packet
two-cycle has probability zero by definition of the release family.

Under conditioning, apply the upper cylinder estimate from PX213 in residual
order `n`. \(\square\)

### Corollary PX214a -- PROVED

Suppose every packet-release state destroys at least `D_rel` units of old
certificate weight.  If

\[
\boxed{
D_{\rm rel}
>
 e^{4\Delta+4}
 \sum_{r=1}^3
 \frac{W_r^{\rm ext}}{(h)_r},
}
\]

then some packet release strictly lowers the total certificate potential.

The same statement holds after exposure with the conditioned PX214 constant.

### Proof

PX214 bounds the expected newly created external weight.  Packet-certified
transposition weight contributes zero.  If the expected creation is smaller
than the weight destroyed in every state, some state has negative net change.
\(\square\)

## 4. Updated packet frontier

PX212--PX214 now provide the full probabilistic interface for packet release.

1. the release family has constant density;
2. packet-certified support-four collisions have probability zero;
3. all other rank-at-most-three cylinders retain fixed-rank spread;
4. bounded-rank exposure costs only one extra forbidden partial matching;
5. the exact remaining input is geometric external weight, not probability
   theory.

The next theorem must therefore bound

\[
W_1^{\rm ext},
\qquad
W_2^{\rm ext},
\qquad
W_3^{\rm ext}
\]

for a packet extracted by PX211, or decode excessive external weight into a
second packet, loaded line, clean star, or bounded composite batch.

## 5. Verification

Run

```bash
python scripts/verify_product_conditioned_packet_release.py
```

The verifier checks that reverse positions form one partial matching, enumerates
conditioned released families at small orders, verifies the residual
`Delta+1` LLL inequalities, confirms zero probability for packet two-cycles,
and checks weighted external-load transfer.