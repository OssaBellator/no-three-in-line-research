# Master exact-width prime-patching lemma

The focused chain now contains the geometry, allocation, restart, activation,
exact-width, designated-credit, old-grid endpoint-shadow, and source-host reduction
components needed for one formal patch statement.  This chapter records that statement
with an explicit finite hypothesis list.

PP3axq--PP3axx correctly distinguished source-host credit from the original current
restart potential.  PP3axy--PP3azj then enlarge the potential by the complete old-grid
endpoint shadow and route every remaining two-inserted-cell source branch through
fixed-template secant descent and alternating rectangles.  The master theorem no
longer assumes a separate cumulative source-certificate closure.

Use

```text
theta=21/40,
M=floor(a m^(1/20)),
R=floor(b m^(19/20)),
W=floor(gamma sqrt(R)/16).
```

The constants `a,b` are chosen by PP3awq after the fixed positive domain margin
`gamma` is known.

## 1. Master input package

Let `S` be a saturated no-three source on `[m]^2`.  The **master patch package** consists
of the following inputs.

### A. Fixed geometry and completion energy

1. **A1 — two-layer source decomposition:** `S=P dot-union Q` with `P,Q` perfect
   matchings.
2. **A2 — slab pools:** one layer contains disjoint permanent matching blocks
   `E_i subseteq X_i x Y_i`, each of size `R`, with `MR<m`.
3. **A3 — internal macro geometry:** every active macro width `w_i<=W` has a
   source-edge assignment satisfying the internal no-three and fixed-rank spread
   conclusions.
4. **A4 — uniform external energy:** patch-only cross-macro mass and ordinary two-slot
   source-anchor mass are within the fixed residual completion budget for every
   saturated source reachable by pool-compatible repairs.

These are PP3asl, PP3gr, PP3dn--PP3ec, PP3he, and PP3hg--PP3hk.

### B. One-attempt controller-aware allocation

5. **B1 — controller-aware domains:** the current macro compatibility graphs are the
   exact domains `J_i^ctrl` of PP3hm--PP3ho.
6. **B2 — heterogeneous ownership:** for prescribed full-scale widths
   `w_1,...,w_L`, PP3aws--PP3awu gives the random two-sided local Ore allocation when
   every complementary score pair has the required slack.
7. **B3 — failure extraction:** denominator collapse or score failure yields one of
   the typed current structures in PP3alc--PP3aut: blocker star, blocker endpoint bank,
   anchor star, anchor endpoint bank, fixed-macro defect bank, or canonical insertion
   structure.

### C. Current local conversion, source-host reduction, and payment

8. **C1 — complete support classification:** every positive source, transition,
   anchor, endpoint, candidate-cell insertion, old-grid endpoint-shadow insertion, and
   same-slot activation event has the bounded or rank-three canonical support form of
   PP3aod--PP3ask, PP3avb, and PP3ayd.
9. **C2 — scale-uniform role host:** every block size `1<=s<=W`, including role domains
   with `O(s)` deletions, is handled by PP3awj--PP3awp.
10. **C3 — terminal current classification:** every dense current-potential support
    branch is one of the source-star, endpoint-bank, anchor-bank, fixed-core petal,
    `A_2/B_3/B_4`, fixed-cell fan, path, partner, Hall, alternating, or rectangle
    classes localized in the current conversion chain through PP3aui.
11. **C4 — direct current payment:** every marked structure carrying current
    candidate-shadow, active-anchor, or old-grid endpoint-shadow credit is spent by the
    direct-payment and permanent-block theorems PP3auc--PP3aui, PP3axa--PP3axh, and
    PP3aye.
12. **C5 — designated-current-credit integrity:** the extracted current-potential
    multiplicity is attached to current source endpoints and survives permanent-block
    refinement as in PP3axa--PP3axh.
13. **C6 — source-host reduction:** unary source support is current `Xi_old` credit,
    while anchored-pair, transition, and inserted-triple branches enter fixed-template
    secant descent and the two-switch rectangle reduction PP3ayg--PP3azj.  Their
    chromatically normalized source mass vanishes at the adaptive secondary scale, so
    every terminal branch is current payment, source-valid joint completion, robust
    final completion, or an explicit current endpoint-host failure.

The current restart potential is

```text
Theta_E^+(S)
=
Xi_cell(S)+Lambda_E(S)+Xi_old(S).
```

### D. Restart realization

14. **D1 — fixed infrastructure:** the coordinate sets `X_i,Y_i`, numerical labels,
    movement/refill candidate-cell universe, and old-grid universe remain fixed through
    all repairs.
15. **D2 — zero-mass activation:** inserted anchors create no positive entry for
    unchanged controllers and every new controller edge starts with zero same-slot
    anchor mass, or PP3avn--PP3awb first clears the activation bank.
16. **D3 — monotone attempt:** after C1--C6 realize the extracted failure, every
    noncompletion branch produces a pool-compatible state with

    ```text
    Theta_(E')^+(S')<Theta_E^+(S).
    ```

17. **D4 — acyclicity:** none of A1--D3 invokes repeated-attempt termination.

These are PP3aux--PP3avm, PP3avv--PP3awb, PP3awc--PP3awi,
PP3axy--PP3ayf, and PP3azg--PP3azi.

## 2. Status of the inputs

### Proposition PP3axi -- PROVED

Inputs A1, A2, A4, B1, B2, C2, C5, D1, D2, and D4 are proved in the cited chapters
without an additional terminal geometric conversion hypothesis.

#### Proof

They are structural decomposition, counting, energy, hypergeometric allocation,
role-domain, exact incidence-accounting, activation-clearing, fixed-universe potential,
or dependency-order statements. ∎

### Proposition PP3axj -- PROVED / CONDITIONAL NAMED CURRENT CONVERSION INTERFACES

Inputs A3, B3, C1, C3, C4, C6, and D3 are conditional only on the explicitly named
current candidate-shadow, active-anchor, endpoint-shadow, Hall, alternating,
non-superregular, endpoint, and rectangle conversion interfaces.

There is no additional cumulative source-certificate host hypothesis.  No restart,
prime-gap, or prime-seed hypothesis occurs inside the local interfaces.

#### Proof

Use the dependency audit PP3awc--PP3awi, the role-domain and current-credit audits
PP3awj--PP3axh, and the source-host closure PP3axy--PP3azj. ∎

Thus the master theorem below has a finite current-conversion hypothesis set and does
not assume its own conclusion.

## 3. One exact-width attempt

Fix constants `0<c_0<c_1`.  Choose `a,b` by PP3awq so that the maximal slab width is
larger than `c_1m^theta`.  Let

```text
c_0m^theta<=t<=c_1m^theta.
```

Partition `t` into widths `w_i` by PP3awr.

### Theorem PP3axk -- PROVED / CONDITIONAL MASTER INPUT PACKAGE

From every current permanent-infrastructure state, exactly one of the following occurs.

1. The heterogeneous controller-aware allocation installs an exact-width `t` patch.
2. A finite pool-compatible package produces another permanent-infrastructure state
   with strictly smaller current potential `Theta_E^+`.
3. A robust final-state branch installs the patch after a finite source-valid composite
   path without requiring monotone intermediate potential.

#### Proof

Use A3--A4 to prepare the internal and external event table.  Apply B1--B2.  Success
gives item 1.  Failure gives a typed structure by B3.  Current-potential structures are
realized and paid by C1--C5.  Source-host structures are routed by C6 into current
payment, a source-valid joint state preserving the original credit, or robust final
completion.  D1--D2 preserve restart comparability and D3 gives item 2 whenever the
patch has not already been installed. ∎

All new numerical rows and columns are exactly `{m+1,...,m+t}` because the
heterogeneous classes partition both label sets of size `t`.

## 4. Integer termination

### Theorem PP3axl -- PROVED / CONDITIONAL MASTER INPUT PACKAGE

Repeatedly apply PP3axk after every failed attempt.  After finitely many repairs, an
exact-width `t` patch is installed.

#### Proof

Every current potential `Theta_E^+(S)` is a nonnegative integer.  Item 2 of PP3axk
strictly decreases it, while D1 keeps the infrastructure fixed and A4 keeps the
completion budgets valid.  Items 1 and 3 install the patch.  Infinite failure is
impossible. ∎

An upper bound on the number of monotone repairs is the initial value of
`Theta_E^+`, but no quantitative bound is needed for existence.

## 5. Master exact-width patch lemma

### Theorem PP3axm -- PROVED / CONDITIONAL NAMED CURRENT CONVERSION INTERFACES

Fix `0<c_0<c_1`.  Suppose the named current conversion interfaces in A3, B3, C1, C3,
C4, and C6 hold with the pool, layer, source-validity, role-domain, conditional-host,
and rectangle hypotheses stated in their chapters.  Then every sufficiently large
saturated no-three source on `[m]^2` can be extended to a saturated no-three source on
`[m+t]^2` for every integer

```text
c_0m^(21/40)<=t<=c_1m^(21/40).
```

#### Proof

Choose the amplified slab constants by PP3awq, form the permanent infrastructure, and
apply PP3axl.  Exact saturation and no-three validity are part of the installing
outcomes of PP3axk. ∎

This is the corrected consolidated form of PP3avl and PP3aww.

## 6. Prime-gap corollary

### Corollary PP3axn -- PROVED UNDER THE STATED HYPOTHESES

Assume additionally:

1. every sufficiently large prime `p` has a saturated no-three source on `[p-1]^2`;
2. every sufficiently large `y` contains a prime in
   `[y-y^(21/40),y]`; and
3. the named current conversion interfaces in PP3axm hold.

Then `D(n)=2n` for every sufficiently large `n`.

#### Proof

Use the shifted-prime choice PP3awx.  Its required width lies in a fixed band, for
example

```text
(1/2)m^(21/40)<=t<=(5/2)m^(21/40)
```

for all sufficiently large `m`.  Apply PP3axm and then the row upper bound. ∎

The leading constant, exact-width partition, and small-width avoidance are internal to
PP3axm; they are not extra hypotheses here.

## 7. Honest remaining leaves

### Proposition PP3axo -- PROVED

The master patch lemma does not prove the no-three-in-line conjecture because two
logically separate inputs remain.

1. **Current local conversion call matrix.**  Every conditional current theorem named
   in A3, B3, C1, C3, C4, and C6 must be checked at each call site with its exact pool
   size, marked size, layer, controller punctures, role-domain losses, source-validity,
   and conditional-host hypotheses.
2. **Prime-minus-one seeds.**  The all-`n` branch assumes, rather than proves, a
   saturated no-three construction on `[p-1]^2` for every sufficiently large prime.

The cumulative source-certificate rich-line branch, short-interval exponent, patch
coefficient, exact-width partition, restart comparability, activation clearing,
role-domain Hall, and designated-current-credit bookkeeping are no longer additional
leaves.

## 8. Next audit target

### Corollary PP3axp -- PROVED

The next focused task is a theorem-by-theorem current call matrix for the endpoints
used after PP3azg.  Each row must record

```text
caller,
callee,
current potential type,
marked-set size,
helper-pool lower bound,
source layer,
controller punctures,
role-domain losses,
conditional arcs or rectangles,
designated credit,
and terminal alternatives.
```

A row closes only when its caller supplies every callee hypothesis or a separate bridge
lemma repairs the mismatch.  Once the call matrix is certified, PP3axm is one formally
assembled conditional exact-width patch theorem, and the prime-minus-one seed remains
the distinct global frontier.

The no-three-in-line conjecture remains unproved.
