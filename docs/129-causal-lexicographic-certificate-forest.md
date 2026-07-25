# Causal lexicographic descent for nested certificate forests

PX235--PX239 separate old-certificate deletion from prospective recreation.
PX263--PX266 give nested recursive blocks of logarithmic-logarithmic depth.
The remaining bookkeeping question is whether a defect already paid at one
level can return during a later neutralization and create a recursion cycle.

For the designated star, line, radial, coordinate-field, and packet
certificates, the answer is no. Historical-position and packet-complement
constraints make every paid certificate permanently absent. This yields a
lexicographic descent theorem independent of the numerical creation constants.

The theorem does not pay diffuse, unassigned collateral. It proves that the
only missing sign is the conversion of that collateral into either immediate
descent or a deeper designated child.

## 1. Abstract designated-certificate forest

Fix a maximum depth `d`. At level `j`, let `D_j` be a finite set of selected
**designated certificates** which the level-`j` bank is required to neutralize.
Write

\[
d_j=|D_j|.
\]

A level-`j` transition is **causal** when:

1. it leaves `D_0,...,D_(j-1)` empty;
2. it strictly decreases `d_j`;
3. every newly designated obligation is assigned only to a level greater than
   `j`.

### Theorem PX277 -- PROVED

Every sequence of causal transitions strictly decreases

\[
\boxed{(d_0,d_1,\ldots,d_d)}
\]

in lexicographic order. In particular, no designated certificate can recur
and no causal transition sequence can cycle.

If `M` bounds the total number of designated certificates which can occur at
one time, the same order is represented by the integer potential

\[
\boxed{
\Psi_{\rm des}
=
\sum_{j=0}^d d_j(M+1)^{d-j}.
}
\]

Every causal transition strictly lowers `Psi_des`.

### Proof

For a level-`j` transition, all coordinates before `j` are unchanged and equal
to zero, while coordinate `j` strictly decreases. Changes at deeper
coordinates are irrelevant to lexicographic comparison. The positional-base
formula has the same property because the total possible contribution of all
deeper coordinates is less than one unit in coordinate `j`. \(\square\)

## 2. Geometric ancestor safety

### Theorem PX278 -- PROVED

The designated certificates used by the product decoder admit causal ancestor
safety as follows.

1. **Clean-star certificate.** For a designated triple `{z,P,Q}`, with `Q` the
   moved endpoint, the fixed row of `Q` meets the line `zP` in the unique cell
   `Q`. Recreating the triple requires returning to the historical position of
   `Q`.
2. **Loaded-line certificate.** For every old line triple charged to a moved
   endpoint `Q`, the fixed row of `Q` meets the old line in the unique historical
   cell `Q`.
3. **Radial certificate.** The same unique-row intersection holds for the old
   radial line assigned to `Q`.
4. **Coordinate-field and mixed-shadow certificates.** Once the fixed centre
   and fixed partner are chosen, their line again has one cell in the moved
   endpoint row.
5. **Packet certificate.** Recreating a designated packet cross is exactly the
   complementary packet two-cycle forbidden by PX212 or PX217.

Therefore historical position constraints form at most one additional partial
matching per ancestor level, while packet recreation is handled by one packet
event family per released packet.

### Proof

A nonvertical real line has at most one point in a fixed grid row. Each
row-preserving rematching can therefore recreate a designated line certificate
through a moved endpoint only at its unique historical cell. Historical cells
from one generation form a partial matching because the moved endpoints have
distinct rows and columns.

The packet statement is the exact two-cycle identity of PX212. \(\square\)

Thus the accumulated ordinary forbidden degree along a nested branch satisfies

\[
\boxed{\Delta_j\le\Delta_0+j,}
\]

apart from separately counted packet families, exactly as used in PX265.

## 3. Designated recursion closes at subpower cost

### Corollary PX279 -- PROVED

Along the nested chain of PX265, all paid designated certificates can be kept
permanently absent through depth

\[
d=O(\log\log N).
\]

The causal vector cannot cycle, and the product of all required optimized
cylinder losses remains

\[
\boxed{N^{o(1)}}
\]

by PX266. Packet constraints retain the same conclusion for every fixed
number of packet families per generation by PX218.

### Proof

Apply PX278 to obtain the ancestor-safety constraints, PX277 for monotonicity,
and PX266 for the cumulative spread loss. \(\square\)

## 4. Exact strict-sign-or-child interface

Let `U_j` denote unresolved, unassigned collateral at level `j`. A decoder
satisfies the **strict-sign-or-child interface** if, at the shallowest level
with `U_j>0`, it performs one of the following without increasing any shallower
coordinate:

1. strictly lowers `U_j`; or
2. removes at least one unit from `U_j` and assigns it to a designated child at
   a deeper level.

### Theorem PX280 -- PROVED

If the strict-sign-or-child interface holds through depth `d`, and every depth-
`d` terminal core is either absorbed or certified impossible, then the full
recursive process terminates. The proof uses the lexicographic vector

\[
\boxed{(U_0,d_0,U_1,d_1,\ldots,U_d,d_d).}
\]

### Proof

An immediate improvement lowers the first affected `U_j`. A child conversion
also lowers `U_j`; the new designated obligation appears later in the vector.
A designated neutralization lowers `d_j` by PX277. Hence every operation
strictly lowers the displayed finite vector. Terminal handling closes the
last coordinate. \(\square\)

PX280 identifies the precise remaining theorem. Recurrence of paid defects,
probability loss, and recursion depth are no longer obstacles. What remains is
to prove the strict-sign-or-child interface for the diffuse clean-star/radial
and small-block packet collateral, and to classify or absorb the terminal
obstruction certificates of PX276.

## 5. Verification

Run

```bash
python scripts/verify_product_causal_lexicographic_descent.py
```

The verifier generates random causal transition systems, checks lexicographic
and scalar-potential descent, validates the depth-dependent forbidden-degree
count, and tests the strict-sign-or-child vector assembly.
