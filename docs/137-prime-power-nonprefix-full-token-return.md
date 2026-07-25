# Arbitrary parent resets have a universal full-token return bound

CMR398--CMR402 compute full-token edge return for recursive prefix resets.  The
remaining scheduling problem also uses whole-parent moves: exact harmonic-band
coverings and joint-parent repairs.  Their internal construction is irrelevant
to edge return.  When one selected matching is replaced, every newly available
cell belongs to the old matching that ceased to be selected or forbidden.
Therefore one full prefix token receives at most one returned edge per source
column in its fixed column prefix.

Let

\[
t=p^h
\]

and fix a full prefix token

\[
\tau=(b,a,c,\theta),
\qquad
1\le b<h.
\]

Its cell universe is

\[
U_\tau^{(2)}
=
\{(x,y):x\equiv a\pmod{p^b},
 y\equiv c\pmod{p^b}\}.
\]

## 1. One arbitrary matching reset

Let `K` be a parent matching board, let `M` be one currently selected or
forbidden perfect matching, and let `F` collect every other fixed forbidden
edge, including persistent deletion masks.  Put

\[
H=K\setminus(M\cup F).
\]

Replace `M` by an arbitrary perfect matching `M'` and put

\[
H'=K\setminus(M'\cup F).
\]

No disjointness between `M` and `M'` is required.

### Theorem CMR403 — PROVED

The newly available edges satisfy

\[
\boxed{H'\setminus H\subseteq M\setminus M'.}
\]

Consequently

\[
\boxed{
|(H'\setminus H)\cap U_\tau^{(2)}|
\le
\frac{t}{p^b}.
}
\]

### Proof

An edge newly available in `H'` was excluded from `H`.  Since the fixed
forbidden set `F` did not change and the edge lies in `H'`, it cannot belong to
`F`.  It must therefore belong to `M`, and because it is now allowed it cannot
belong to `M'`.  This proves the set inclusion.

The old perfect matching `M` has one edge in each source column.  Exactly
`t/p^b` source columns have residue `a modulo p^b`, so at most that many edges
of `M` can lie in the full-token universe. ∎

This includes a complete exact-band replacement, a full-parent derangement,
and a one-layer stage of an ordered joint-parent move.

## 2. Joint-parent and packet schedules

### Corollary CMR404 — PROVED

1. One ordered joint-parent move, with both layer matchings replaced once,
   reintroduces at most
   \[
   \boxed{
   \frac{2t}{p^b}
   }
   \]
   edges into one direction-labelled full-token inventory.
2. A schedule containing `R` arbitrary one-layer whole-parent resets and `J`
   ordered joint-parent resets contributes at most
   \[
   \boxed{
   \frac{(R+2J)t}{p^b}
   }
   \]
   full-token edge reintroductions.

### Proof

Apply CMR403 to each changed matching and sum with multiplicity.  Suppression
by overlaps, opposite-layer occupancy, or persistent deletion masks only
reduces the true returned set. ∎

In particular, every exact harmonic packet supplied by CMR388 costs at most
`t/p^b` in the token ledger when installed by one layer replacement.

## 3. Combined endpoint-visit budget

### Corollary CMR405 — PROVED UNDER THE ONE-PASS PREFIX HYPOTHESIS

Suppose a closure epoch contains:

- one descending recursive-prefix pass;
- `R` arbitrary one-layer whole-parent resets;
- `J` ordered joint-parent resets.

Then one exact full token satisfies

\[
\boxed{
D_\tau^{(2)}
\le
\frac{t^2}{p^{2b}}
+
\frac{(2b+R+2J)t}{p^b}.
}
\]

At the tunable deep threshold

\[
p^b\ge t^{2/3},
\]

this becomes

\[
\boxed{
D_\tau^{(2)}
\le
 t^{2/3}+
 (2h+R+2J)t^{1/3}.
}
\]

### Proof

CMR399 pays the prefix-pass return mass.  CMR404 pays all listed non-prefix
resets.  Add the exact initial stock from CMR394 and apply the dynamic inventory
CMR395.  The deep specialization uses `b<=h`. ∎

Thus exact-band and joint-parent moves no longer form an unquantified token
source.  The remaining scheduling issue is the **number** of such moves and the
possibility that repeated use of the same ancestor or packet state creates a
cycle; their per-move token cost is fixed and linear in the token width.

No all-`n` theorem is claimed here.  Host-churn inclusion, per-reset capacity,
and combined schedule coefficients are checked in
[`scripts/verify_prime_power_nonprefix_token_return.py`](../scripts/verify_prime_power_nonprefix_token_return.py).
