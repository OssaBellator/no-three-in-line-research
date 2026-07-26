# Master exact-width prime-patching lemma

The focused chain now contains the geometry, allocation, local conversion, restart,
activation, exact-width, and designated-credit components needed for one formal patch
statement.  This chapter records that statement with an explicit finite hypothesis
list.  It does not replace a conditional conversion by a slogan: every interface is
named, typed, and placed in the acyclic proof order.

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

### C. Current local conversion and payment

8. **C1 — complete support classification:** every positive source, transition,
   anchor, endpoint, candidate-cell insertion, and same-slot activation event has the
   bounded or rank-three canonical support form of PP3aod--PP3ask and PP3avb.
9. **C2 — scale-uniform role host:** every block size `1<=s<=W`, including role domains
   with `O(s)` deletions, is handled by PP3awj--PP3awp.
10. **C3 — terminal conversion:** every dense support branch is one of the source-star,
    endpoint-bank, transition-sunflower, anchor-bank, fixed-core petal, or
    `A_2/B_3/B_4` classes converted in PP3ama--PP3aui and PP3aqo--PP3aqt.
11. **C4 — direct payment:** every current credited marked structure is spent by the
    zero-insertion direct-payment theorem PP3auc--PP3aui.
12. **C5 — designated-credit integrity:** the extracted incidence multiplicity is
    attached to current source endpoints and survives permanent-block refinement as in
    PP3axa--PP3axh.

### D. Restart realization

13. **D1 — fixed infrastructure:** the coordinate sets `X_i,Y_i`, numerical labels,
    and candidate-cell universe remain fixed through all repairs.
14. **D2 — zero-mass activation:** inserted anchors create no positive entry for
    unchanged controllers and every new controller edge starts with zero same-slot
    anchor mass, or PP3avn--PP3awb first clears the activation bank.
15. **D3 — monotone attempt:** every failed allocation is followed by a pool-compatible
    repair with

    ```text
    Theta_(E')(S')<Theta_E(S).
    ```

16. **D4 — acyclicity:** none of A1--D3 invokes repeated-attempt termination.

These are PP3aux--PP3avm, PP3avv--PP3awb, and PP3awc--PP3awi.

## 2. Status of the inputs

### Proposition PP3axi -- PROVED

Inputs A1, A2, A4, B1, B2, C2, C5, D1, D2, and D4 are proved in the cited chapters
without an additional geometric conversion hypothesis.

#### Proof

They are structural decomposition, counting, energy, hypergeometric allocation,
role-domain, exact incidence-accounting, or dependency-order statements.  Their cited
proofs have no terminal geometric alternative. ∎

### Proposition PP3axj -- PROVED / CONDITIONAL NAMED CONVERSION INTERFACES

Inputs A3, B3, C1, C3, C4, and D3 are proved modulo only the explicitly named current
conversion interfaces appearing in PP3ama--PP3aui and PP3aqo--PP3aqt.

No restart, prime-gap, or prime-seed hypothesis occurs inside those local interfaces.

#### Proof

This is the dependency audit PP3awc--PP3awi together with the role-domain and credit
audits PP3awj--PP3axh. ∎

Thus the master theorem below has a finite local hypothesis set; it does not assume its
own conclusion.

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
   with strictly smaller current potential `Theta`.

#### Proof

Use A3--A4 to prepare the internal and external event table.  Apply B1--B2.  Success
gives item 1.  Failure gives a typed credited structure by B3.  Use C1--C3 and the
role-domain theorem C2 to realize or convert it.  C4 and C5 supply strict current
payment.  D1--D2 preserve restart comparability and D3 gives item 2. ∎

All new numerical rows and columns are exactly `{m+1,...,m+t}` because the
heterogeneous classes partition both label sets of size `t`.

## 4. Integer termination

### Theorem PP3axl -- PROVED / CONDITIONAL MASTER INPUT PACKAGE

Repeatedly apply PP3axk after every failed attempt.  After finitely many repairs, an
exact-width `t` patch is installed.

#### Proof

Every current potential `Theta_E(S)` is a nonnegative integer.  Item 2 of PP3axk
strictly decreases it, while D1 keeps the infrastructure fixed and A4 keeps the
completion budgets valid.  Infinite failure is impossible, so a later application
uses item 1. ∎

An upper bound on the number of repairs is the initial current potential, but no
quantitative bound is needed for existence.

## 5. Master exact-width patch lemma

### Theorem PP3axm -- PROVED / CONDITIONAL NAMED LOCAL CONVERSION INTERFACES

Fix `0<c_0<c_1`.  Suppose the named local conversion interfaces in A3, B3, C1, C3, and
C4 hold with the pool, layer, source-validity, and role-domain hypotheses stated in
their chapters.  Then every sufficiently large saturated no-three source on `[m]^2`
can be extended to a saturated no-three source on `[m+t]^2` for every integer

```text
c_0m^(21/40)<=t<=c_1m^(21/40).
```

#### Proof

Choose the amplified slab constants by PP3awq, form the permanent infrastructure, and
apply PP3axl.  Exact saturation and no-three validity are part of item 1 of PP3axk. ∎

This is the consolidated form of PP3avl and PP3aww.

## 6. Prime-gap corollary

### Corollary PP3axn -- PROVED UNDER THE STATED HYPOTHESES

Assume additionally:

1. every sufficiently large prime `p` has a saturated no-three source on `[p-1]^2`;
2. every sufficiently large `y` contains a prime in
   `[y-y^(21/40),y]`; and
3. the named local conversion interfaces in PP3axm hold.

Then `D(n)=2n` for every sufficiently large `n`.

#### Proof

Use the shifted-prime choice PP3awx.  Its required width lies in a fixed band, for
example

```text
(1/2)m^(21/40)<=t<=(5/2)m^(21/40)
```

for all sufficiently large `m`.  Apply PP3axm and then the row upper bound. ∎

The leading constant and exact-width conditions are internal to PP3axm; they are not
extra hypotheses here.

## 7. Honest remaining leaves

### Proposition PP3axo -- PROVED

The master patch lemma does not prove the no-three-in-line conjecture because two
logically separate inputs remain.

1. **Local conversion assembly.**  Every conditional theorem named in A3, B3, C1, C3,
   and C4 must be checked at each call site with its exact pool size, marked size,
   source-validity, and role-domain hypotheses.  PP3awj--PP3axh close the first two
   mismatches found in that audit, but the complete call matrix is not yet certified.
2. **Prime-minus-one seeds.**  The all-`n` branch assumes, rather than proves, a
   saturated no-three construction on `[p-1]^2` for every sufficiently large prime.

The short-interval exponent, patch coefficient, exact-width partition, restart
comparability, and designated-credit bookkeeping are no longer additional leaves.

## 8. Next audit target

### Corollary PP3axp -- PROVED

The next focused task is to construct a theorem-by-theorem call matrix for the local
conversion package.  Each row must record:

```text
caller,
callee,
marked-set size,
helper-pool lower bound,
source layer,
controller punctures,
role-domain losses,
designated credit,
terminal alternatives.
```

A row is closed only when the caller supplies every callee hypothesis or a separate
lemma bridges the mismatch.  After that audit, PP3axm becomes one formally assembled
conditional patch theorem, and the prime-minus-one seed remains the distinct global
frontier.

The no-three-in-line conjecture remains unproved.
