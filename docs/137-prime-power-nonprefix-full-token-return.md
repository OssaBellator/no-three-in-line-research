# Arbitrary parent resets have a universal full-token return bound

CMR398--CMR402 compute full-token edge return for recursive prefix resets. The
remaining schedule also uses whole-parent moves: exact harmonic-packet
coverings and joint-parent repairs. Their internal construction is irrelevant
to edge return. When one selected or forbidden matching is replaced, every
newly available cell belongs to the old matching that ceased to be excluded.

Let

\[
t=p^h
\]

and fix a full prefix token

\[
\tau=(b,a,c,\theta),
\qquad
1\le b<h,
\]

with cell universe

\[
U_\tau^{(2)}
=
\{(x,y):x\equiv a\pmod{p^b},
 y\equiv c\pmod{p^b}\}.
\]

## 1. One arbitrary matching reset

Let `K` be a parent matching board, `M` one currently selected or forbidden
perfect matching, and `F` every other fixed forbidden edge, including
persistent deletion masks. Put

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

Consequently,

\[
\boxed{
|(H'\setminus H)\cap U_\tau^{(2)}|
\le
\frac{t}{p^b}.
}
\]

### Proof

A newly available edge was excluded from `H`. Since `F` did not change and the
edge lies in `H'`, it does not belong to `F`. It therefore belongs to `M`, and
because it is now allowed it does not belong to `M'`.

The old perfect matching has one edge in each source column. Exactly `t/p^b`
source columns extend the prescribed column prefix `a`, so at most that many
old matching edges lie in the token universe. ∎

This includes a complete harmonic-packet replacement, a full-parent
derangement, and one layer stage of an ordered joint-parent move.

## 2. Joint-parent and packet schedules

### Corollary CMR404 — PROVED

1. One ordered joint-parent move, replacing both layer matchings once,
   reintroduces at most
   \[
   \boxed{\frac{2t}{p^b}}
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

Apply CMR403 to each changed matching and sum with multiplicity. Overlaps,
opposite-layer occupancy, and persistent deletion masks only reduce the true
returned set. ∎

In particular, every exact harmonic packet supplied by CMR388 costs at most
`t/p^b` in one token ledger when installed by one layer replacement.

## 3. Combined endpoint-visit budget

### Corollary CMR405 — PROVED UNDER THE ONE-PASS PREFIX HYPOTHESIS

Suppose one closure epoch contains

- one descending recursive-prefix pass;
- `R` arbitrary one-layer whole-parent resets;
- `J` ordered joint-parent resets.

Then

\[
\boxed{
D_\tau^{(2)}
\le
\frac{t^2}{p^{2b}}
+
\frac{(2b+R+2J)t}{p^b}.
}
\]

At the deep threshold `p^b\ge t^{2/3}`,

\[
\boxed{
D_\tau^{(2)}
\le
t^{2/3}+(2h+R+2J)t^{1/3}.
}
\]

### Proof

CMR399 pays the prefix-pass return mass and CMR404 pays the non-prefix resets.
Add the exact initial stock from CMR394 and apply the dynamic inventory CMR395.
Use `b\le h` for the specialization. ∎

Exact packet and joint-parent moves are therefore no longer unquantified token
sources. The remaining issue is the number of such moves and whether repeated
use of one ancestor or packet state creates a cycle; each move now has a fixed
linear token-width cost.

No all-`n` theorem is claimed here. Host-churn inclusion, per-reset capacity,
and combined schedule coefficients are checked in
[`scripts/verify_prime_power_nonprefix_token_return.py`](../scripts/verify_prime_power_nonprefix_token_return.py).
