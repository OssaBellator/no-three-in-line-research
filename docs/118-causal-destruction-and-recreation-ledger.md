# Causal destruction and recreation ledger

PX225--PX234 bound every rank-at-most-three creation sector and optimize the
allowed-matching cylinder constant.  A strict drift theorem also needs the
negative side of the ledger to be counted without ambiguity.

There are two logically different credits.

1. **Old-certificate destruction.**  Current points are removed and their original
   positions are forbidden, so old certificates meeting the moved block disappear.
2. **Prospective-recreation suppression.**  Clean-star, radial, and packet
   constraints exclude specific certificates that a naive fixed switch or an
   unrestricted rematching could otherwise create.

They may both occur in one decoder step, but they must not be counted twice.
This chapter gives the exact identities.

Let

\[
\Phi(U)=\sum_L\binom{|U\cap L|}{3}
\]

be the collinear-triple certificate potential.

## 1. Full movement deletes the complete old shadow

Let the current state be a disjoint union

\[
S=X\mathbin{\dot\cup}A,
\]

where `A` is a row-column matching block to be rematched.  Every original cell
of `A` is included in the forbidden-position graph.  Let `M` be any allowed
replacement matching on the same row and column sets.

### Theorem PX235 -- PROVED

Every old triple of `S` meeting `A` is absent from `X union M`.  Hence every
allowed replacement destroys exactly the old block shadow

\[
\boxed{
D_A=\Phi(S)-\Phi(X).
}
\]

Here "exactly" refers to old certificates: new triples on the same geometric
lines are creation terms and belong to the replacement-certificate ledger.

### Proof

An old triple meeting `A` contains at least one exact point `a in A`.  The
original position of `a` is forbidden, so `a notin M`.  Therefore the old
three-point set is not contained in `X union M`.

Conversely every old triple not meeting `A` is contained in `X` and survives the
deleting step.  Thus the old certificates deleted are precisely those counted
by `Phi(S)-Phi(X)`. \(\square\)

The same statement holds for several disjoint moved blocks and after compatible
exposure.  It is independent of the replacement distribution.

## 2. Exact cancellation for a fixed switch plus rematching

Use the alternating-star notation of AN3--AN4.  Write

\[
S=X\mathbin{\dot\cup}A\mathbin{\dot\cup}C_0,
\]

where `C_0` is the current pair removed by a fixed rectangle switch, `W` is the
inserted pair, and `A` is the opposite-layer endpoint block that is rematched.
Put

\[
Y=X\cup A.
\]

Define the raw fixed-switch destruction and creation

\[
d=\Phi(S)-\Phi(Y),
\qquad
c=\Phi(Y\cup W)-\Phi(Y),
\]

and its raw potential change

\[
\Delta_{\rm raw}=c-d.
\]

Define the **prospective moved-endpoint load**

\[
\Gamma_A(W)
=
\Phi(X\cup A\cup W)-\Phi(X\cup W).
\]

This is exactly the number of triples in the naive switched state which use at
least one endpoint from `A`.

As in AN4, set

\[
D_\star=\Phi(S)-\Phi(X),
\qquad
F_\star=\Phi(X\cup W)-\Phi(X).
\]

### Theorem PX236 -- PROVED

The fixed part of the alternating ledger satisfies the exact cancellation
identity

\[
\boxed{
F_\star-D_\star
=
\Delta_{\rm raw}-\Gamma_A(W).
}
\]

Consequently, if `M_pi` is any allowed rematching of `A`, then

\[
\Phi(X\cup W\cup M_\pi)-\Phi(S)
=
\Delta_{\rm raw}-\Gamma_A(W)
+
\bigl(\Phi(X\cup W\cup M_\pi)-\Phi(X\cup W)\bigr).
\]

### Proof

Insert and subtract `Phi(X union A)`.  First,

\[
D_\star
=
[\Phi(S)-\Phi(X\cup A)]
+
[\Phi(X\cup A)-\Phi(X)]
=
d+D_A^0,
\]

where `D_A^0=Phi(X union A)-Phi(X)`.  Second,

\[
\begin{aligned}
c-F_\star
&=[\Phi(X\cup A\cup W)-\Phi(X\cup A)]
  -[\Phi(X\cup W)-\Phi(X)]\\
&=\Gamma_A(W)-D_A^0.
\end{aligned}
\]

Thus `F_star=c-Gamma_A(W)+D_A^0`, and subtraction gives

\[
F_\star-D_\star=c-d-\Gamma_A(W).
\]

The second display follows by adding the replacement-matching collateral.
\(\square\)

The identity explains why the endpoint block is valuable even when the raw
rectangle itself is not improving: it cancels naive switch collateral before
the random matching cost is paid.

## 3. Clean-star, loaded-line, and radial credits

### Corollary PX237 -- PROVED

Suppose the naive switched state contains `m` distinct designated triples, each
using at least one point of `A`, and the rematching moves every point of `A`.
Then

\[
\boxed{
\Gamma_A(W)\ge m.
}
\]

In particular:

1. for the AN3 clean star with triples
   `\{z,P_j,Q_j\}`, `Q_j in A`, one has `Gamma_A(W)>=t`;
2. if the inserted pair `W={u,v}` has `r` moved current anchors on its line,
   then the radial triples `\{u,v,a\}` give `Gamma_A(W)>=r`;
3. any loaded-line neutralization receives one unit of cancellation credit for
   every distinct naive switched triple hit by the moved endpoint set.

### Proof

Every designated triple is counted in
`Phi(X union A union W)-Phi(X union W)` because it is present before `A` is
rematched and uses a point of `A`.  Distinct designated triples contribute
distinct certificates. \(\square\)

Thus AN4 can be rewritten using the optimized spread factor from PX232.  If the
moved block has order `t`, forbidden degree `Delta`, and weighted certificate
counts `T_1,T_2,T_3`, then

\[
\boxed{
\mathbb E[\Phi(S_\pi)-\Phi(S)]
\le
\Delta_{\rm raw}-\Gamma_A(W)
+
\mathcal C(t,\Delta)
\left(
 \frac{T_1}{t}
 +\frac{T_2}{(t)_2}
 +\frac{T_3}{(t)_3}
\right).
}
\]

For a clean star of order `t`, it is sufficient that

\[
\boxed{
\Delta_{\rm raw}
+
\mathcal C(t,\Delta)
\left(
 \frac{T_1}{t}
 +\frac{T_2}{(t)_2}
 +\frac{T_3}{(t)_3}
\right)
<t.
}
\]

This is the exact linear-sign interface for alternating neutralization.

## 4. Packet constraints suppress recreation, not base deletion

Let `M_0` be the current perfect matching on a packet rematching block, and
assume, as in PX196--PX218, that every cell of `M_0` belongs to the inherited
forbidden-position graph `F`.  Let `P` be the family of packet-certified
rank-two cross events excluded by the no-two-cycle release condition.

### Theorem PX238 -- PROVED

The two packet credits are separate.

1. Every old certificate meeting `M_0` is destroyed already by the base allowed
   bank `Omega_F`, by PX235.
2. Adding the packet no-two-cycle constraints contributes no additional old-
   certificate destruction beyond that base deletion.
3. Its exact additional benefit is prospective: every `E in P` has probability
   zero and is removed from the rank-two creation weight.

Therefore an old selected packet defect may be used once in the destruction
term of a drift ledger, while the complete packet cross family may be removed
once from the creation term.  They are different credits and may not be merged
or counted twice.

### Proof

Every edge of `M_0` is forbidden, so no member of the base allowed family
contains any old matching edge.  Hence every old certificate meeting the block
is absent before packet constraints are imposed.

The release family is the subset of `Omega_F` avoiding all events in `P`.
Consequently every such prospective rank-two cylinder has probability zero.
This changes the creation family but cannot delete an old certificate a second
time. \(\square\)

PX223--PX224 remain valid as decompositions for selecting defect-rich packet
blocks.  PX238 clarifies their causal role: the selected defects certify the old
shadow of the block, while packet constraints prevent the corresponding
candidate family from reappearing.

## 5. Unified strict-sign criterion

### Corollary PX239 -- PROVED

Consider any decoder step consisting of:

- deletion of a current moved block `A`;
- a deterministic fixed insertion `W`;
- an allowed replacement matching of order `s` and forbidden degree `Delta`;
- an optional prospective exclusion family, such as packet crosses.

Let

\[
D_A=\Phi(S)-\Phi(S\setminus A)
\]

be the old block shadow, let

\[
F_W=\Phi((S\setminus A)\cup W)-\Phi(S\setminus A),
\]

and let `W_r^ext` be the remaining rank-`r` creation weight after deleting
forbidden cylinders and all prospectively excluded packet events.  If
`s>=8Delta`, then

\[
\boxed{
\mathbb E[\Phi(S')-\Phi(S)]
\le
-D_A+F_W
+
\mathcal C(s,\Delta)
\sum_{r=1}^3\frac{W_r^{\rm ext}}{(s)_r}.
}
\]

Hence strict improvement follows whenever the right-hand side is negative.
For a fixed switch plus moved endpoint block, PX236 replaces `-D_A+F_W` exactly
by `Delta_raw-Gamma_A(W)`.

### Proof

PX235 gives the old destruction term.  The deterministic insertion contributes
`F_W`.  Every remaining new certificate is represented by a compatible
rank-at-most-three cylinder; PX232 bounds its probability by
`mathcal C(s,Delta)/(s)_r`.  Prospectively excluded packet cylinders contribute
zero.  Sum by linearity of expectation. \(\square\)

## 6. Updated frontier

The destruction side is now exact, but the sign is not yet universally
negative.

- clean stars and radial cores have explicit cancellation credit;
- packet-rich blocks have exact old-shadow credit and exact recurrence
  suppression;
- all remaining creation sectors have the optimized cylinder factor.

The next theorem must lower-bound `Gamma_A(W)` or `D_A` relative to the external
linear creation terms produced by the decoder extraction.  This is a narrower
problem than assigning an informal unit of "destruction" to every star ray or
packet cross.

## 7. Verification

Run

```bash
python scripts/verify_product_causal_destruction_ledger.py
```

The verifier checks the cancellation identity on random finite triple systems,
checks the clean-star and radial lower credits, verifies full-move deletion, and
confirms that packet exclusions remove prospective rank-two cylinders without
creating a second old-destruction credit.
