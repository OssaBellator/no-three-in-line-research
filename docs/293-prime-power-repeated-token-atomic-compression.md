# Repeated full-token histories compress to three atomic recurrent rows

CMR517--CMR540 give separate finite-stock, absence-run, persistent-blocker,
cross-signature and trace-line ledgers.  This chapter combines them with one
fixed persistent central edge.  Fixing that edge removes a factor `t^2` from the
pair and trace signature stocks and gives an explicit threshold which forces a
recurrent atomic row.

The resulting repeated-token quotient has only three unresolved recurrent
currencies:

1. labelled edge reintroduction;
2. one jointly persistent paid-pair selector;
3. one fixed trace-line incidence.

Fresh labelled stock and successful persistent-edge absorption are finite or
terminal branches, not additional recurrent rows.

Fix an inherited envelope of side

\[
t=p^h,
\qquad h\ge2,
\]

and one nonroot full token

\[
\tau=(b,a,c,\theta),
\qquad 1\le b<h.
\]

Its edge universe has exact size

\[
|U_\tau^{(2)}|=\frac{t^2}{p^{2b}}.
\]

Let `J` episodes carry unavailable witness sets

\[
E_j\subseteq U_\tau^{(2)},
\qquad |E_j|\ge H.
\]

## 1. Fixed-central signature stocks

Fix one central edge `e=(u,v)` in an envelope epoch of side `t`.
A pair signature records

\[
(e,(u,y),(x,v)),
\qquad x\ne u,\ y\ne v,
\]

and a trace signature records one noncentral row- or column-arm cell together
with its arm label.

### Theorem CMR1518 -- PROVED

For one fixed central edge, the exact signature stocks are

\[
\boxed{N_{\rm pair}^{e}(t)=(t-1)^2}
\]

and

\[
\boxed{N_{\rm tr}^{e}(t)=2(t-1).}
\]

For `t>=4`,

\[
\boxed{N_{\rm tr}^{e}(t)\le N_{\rm pair}^{e}(t).}
\]

### Proof

Choose independently one noncentral target in row `u` and one noncentral source
in column `v` for a pair signature.  For a trace signature choose one of two
arms and one of its `t-1` noncentral cells.  The final inequality is
`2(t-1)<=(t-1)^2`. ∎

This is sharper than CMR536 because the central edge has already been fixed by
the token recurrence.

## 2. Threshold forcing of one persistent edge

Choose integers

\[
q\ge1,
\qquad R\ge1,
\]

and put

\[
\boxed{\lambda=2Rq(t-1)^2.}
\]

### Theorem CMR1519 -- PROVED

At least one of the following holds.

1. **Finite token-edge stock.**  The episode count satisfies
   \[
   \boxed{
   J\le
   \left\lfloor
   \frac{(\lambda-1)t^2}{Hp^{2b}}
   \right\rfloor.}
   \]
2. **Persistent labelled edge.**  Some edge
   \[
   e\in U_\tau^{(2)}
   \]
   belongs to at least `lambda` witness sets.

### Proof

This is CMR517 with the exact token universe size.  If no edge occurs
`lambda` times, double-counting the incidences `(j,e)` gives

\[
JH\le(\lambda-1)|U_\tau^{(2)}|.
\]

Rearrange. ∎

## 3. Return payment or one long absence run

Suppose the persistent-edge branch of CMR1519 holds.  Let `I(e)` count
absent-to-present reintroductions during the epoch.

### Theorem CMR1520 -- PROVED

At least one of the following holds.

1. **Return payment.**  
   \[
   \boxed{I(e)\ge R.}
   \]
   The exact all-nonroot labelled full-token incidence contributed by those
   returns is at least
   \[
   \boxed{R(p+1)(h-1).}
   \]
2. **Long continuous absence.**  One absence run contains at least
   \[
   \boxed{
   L\ge
   \left\lceil\frac\lambda R\right\rceil
   =2q(t-1)^2}
   \]
   selected token episodes.

### Proof

If `I(e)>=R`, use the first branch and CMR413 for the exact incidence of every
returned edge.  Otherwise `1+I(e)<=R`.  CMR519 gives an absence run of length
at least `ceil(lambda/(1+I(e)))`, which is at least `ceil(lambda/R)`. ∎

## 4. Persistent-aware adaptation inside the run

Apply the CMR524 priority rule in every episode of the long run: absorb `e`
whenever it belongs to a maximum compatible unavailable matching.

### Theorem CMR1521 -- PROVED

At least one of the following holds.

1. **Persistent-edge absorption.**  The edge `e` is absorbed into the adaptive
   forbidden matching and disappears from the restoration inventory.
2. **Pair/trace majority.**  At least
   \[
   \boxed{q(t-1)^2}
   \]
   episodes of the run are all of one type:
   - two-endpoint absorption-deficiency pair episodes; or
   - paid-line trace-contact episodes.

### Proof

If absorption never occurs, CMR524 assigns every episode to the pair or trace
class.  One class contains at least `ceil(L/2)` episodes.  CMR1520 gives
`L>=2q(t-1)^2`. ∎

## 5. Pair episodes force one paid-pair selector row

### Theorem CMR1522 -- PROVED

In the pair-majority branch, one fixed pair signature

\[
\Sigma=(e,r_y,c_x)
\]

occurs in at least

\[
\boxed{q}
\]

episodes of the same continuous-absence run.  Throughout those occurrences all
three edges `e,r_y,c_x` are unavailable.  The partner pair

\[
Z=\{r_y,c_x\}
\]

is compatible and has deterministic restoration surcharge

\[
\boxed{c_Z=2.}
\]

For every restoration threshold `Q>=1`, CMR531 supplies either a line-clean
completion with

\[
X_L(\delta)=0,
\qquad
T_Z(\delta)<Q,
\]

or the exact obstruction

\[
\boxed{
A_L+\frac2Q+\frac{|B_L|}{Q(n-1)}\ge1.}
\]

### Proof

CMR1518 gives only `(t-1)^2` pair signatures once `e` is fixed.  Pigeonhole the
at least `q(t-1)^2` pair episodes.  Continuous absence makes all three recorded
edges jointly unavailable.  Compatibility and the weighted selector statement
are CMR527 and CMR531. ∎

## 6. Trace episodes force one fixed incidence row

### Theorem CMR1523 -- PROVED

In the trace-majority branch, one fixed trace signature

\[
(e,w,\varepsilon)
\]

occurs in at least

\[
\boxed{q}
\]

episodes of the same continuous-absence run.

When the rooted centre is fixed, `e` and `w` determine one fixed real trace
line.  In the general case the recurrence remains in one fixed row/column
incidence slot of one envelope epoch.

### Proof

There are `2(t-1)` fixed-central trace signatures by CMR1518, and

\[
2(t-1)\le(t-1)^2.
\]

Pigeonhole the at least `q(t-1)^2` trace episodes.  The geometric statement is
CMR540. ∎

## 7. Master repeated-token alternative

### Theorem CMR1524 -- PROVED

For every choice of integers `q,R>=1`, the `J` heavy episodes of one fixed token
reach at least one of:

1. the explicit finite bound
   \[
   J\le
   \left\lfloor
   \frac{(2Rq(t-1)^2-1)t^2}{Hp^{2b}}
   \right\rfloor;
   \]
2. at least `R` reintroductions of one labelled edge, paying at least
   \[
   R(p+1)(h-1)
   \]
   exact full-token incidences;
3. adaptive absorption of the persistent edge;
4. at least `q` repetitions of one jointly persistent paid-pair selector with
   surcharge two;
5. at least `q` repetitions of one fixed trace-line or trace-incidence
   signature.

### Proof

Combine CMR1519--CMR1523. ∎

The thresholds are tunable: increasing `q` or `R` increases the finite episode
allowance but forces proportionally stronger atomic recurrence or return
payment.

## 8. Atomic recurrent quotient endpoint

### Corollary CMR1525 -- PROVED

The repeated-token and reused-support part of the same-owner quotient may be
refined to three atomic recurrent rows:

1. **return row:** one labelled edge reintroduction with exact coefficient
   `(p+1)(h-1)` in the full-token incidence ledger;
2. **selector row:** one fixed jointly persistent triple of unavailable edges
   with the CMR531 paid-pair selector and deterministic surcharge two;
3. **trace row:** one fixed trace-line or row/column incidence signature.

Finite token-edge stock and successful persistent-edge absorption do not require
additional recurrent diagonal classes.  The remaining numerical work is to
bound the selector and trace rows against destroyed parent credit and to combine
them with recurrent root/fixed-interface rows.  No all-`n` theorem is claimed.

Fixed-central stock counts, threshold inversion, absence-run arithmetic and
synthetic episode histories are checked in
[`scripts/verify_prime_power_repeated_token_atomic_compression.py`](../scripts/verify_prime_power_repeated_token_atomic_compression.py).
