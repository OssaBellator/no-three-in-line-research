# High-multiplicity trimming for threshold endpoint flow

**Branch:** `research/superregular-resampling`

SRR2ag--SRR2aj bound threshold deficiencies by total source-hole mass and maximum endpoint multiplicity. This note removes a small exceptional endpoint set so that the multiplicity parameter can be chosen rather than assumed.

Fix a threshold set `S subseteq B`. Write

\[
\nu(b)=|\{a:b\in H(a)\}|,
\qquad
M_S=\sum_{b\in S}\nu(b).
\]

For an integer `tau>=0`, define the exceptional set

\[
T_\tau=\{b\in S:\nu(b)>\tau\},
\qquad
S_\tau=S\setminus T_\tau.
\]

## SRR2ak -- exact exceptional-set count -- PROVED

\[
\boxed{
|T_\tau|
\le
\left\lfloor\frac{M_S}{\tau+1}\right\rfloor.
}
\]

Moreover every endpoint of `S_tau` has hole multiplicity at most `tau`, and its residual hole mass satisfies

\[
\boxed{
M_{S_\tau}
=M_S-\sum_{b\in T_\tau}\nu(b)
\le M_S-(\tau+1)|T_\tau|.
}
\]

### Proof

Each exceptional endpoint contributes at least `tau+1` to `M_S`. The residual identity is the partition of the incidence sum. QED.

## SRR2al -- trimmed threshold deficiency bound -- PROVED

Let `r(S_tau)` be the maximum number of sources matchable into the retained threshold set. Then

\[
\boxed{
|A|-r(S_\tau)
\le
\max\left\{
(|A|-|S_\tau|)_+,
\max_{1\le x\le\min\{|A|,\tau\}}
\left(x-|S_\tau|+\left\lfloor\frac{M_{S_\tau}}x\right\rfloor\right)_+
\right\}.
}
\]

Consequently the same right-hand side bounds the number of sources that cannot be assigned a low-cost endpoint after deleting every endpoint of multiplicity greater than `tau`.

### Proof

The retained endpoint set has maximum hole multiplicity at most `tau`. Apply SRR2ah to `S_tau`. QED.

## SRR2am -- computable untrimmed deficiency bound -- PROVED

Because deleting `|T_tau|` endpoints can reduce matching rank by at most `|T_tau|`,

\[
\boxed{
|A|-r(S)
\le
\left(|A|-r(S_\tau)\right)
}
\]

and, more usefully for a flow that is allowed to discard or separately pay exceptional endpoints,

\[
\boxed{
|A|-r(S)+|T_\tau|
\le
E_\tau+|T_\tau|,
}
\]

where `E_tau` is the displayed bound in SRR2al. Thus one may optimize the certified cost

\[
\boxed{
\min_{\tau\ge0}
\left(
E_\tau+\left\lfloor\frac{M_S}{\tau+1}\right\rfloor
\right).
}
\]

### Proof

The first inequality follows from `S_tau subseteq S`, hence `r(S_tau)<=r(S)`. The second simply charges every deleted endpoint once in addition to the retained-set deficiency, and SRR2ak bounds their number. QED.

## SRR2an -- heavy-endpoint overload router -- PROVED

For every proposed `tau`, one exact continuation holds:

1. the trimmed threshold set supports the desired flow with deficiency bounded by `E_tau`;
2. the exceptional set has size at most `M_S/(tau+1)` and is paid or conditioned away separately;
3. one endpoint has multiplicity greater than `tau` and is returned as a concentrated hole-star witness;
4. the total threshold hole mass exceeds its declared bound;
5. or one retained source cut realizes the residual bound.

The low-event frontier therefore no longer requires a uniform endpoint-multiplicity estimate on all low-cost endpoints. It is enough to bound total hole mass and pay a quantitatively small exceptional set.

## Corrected SRR3 frontier

The next geometric task is to prove useful total hole-mass estimates for actual bounded-cycle switching menus and to pay or condition away the high-multiplicity endpoint stars selected by `T_tau`.

## Finite check

`scripts/verify_srr_high_multiplicity_trimming.py` exhausts small hole systems, checks the exceptional-set count, residual mass identity and trimmed deficiency bounds.