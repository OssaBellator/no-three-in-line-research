# Finite-signature adapter for phase-locked boundary markers

`docs/543--548` isolate the first realization gap: a numerical marker word must
be turned into an actual boundary operation with the advertised controller and
defect outputs.  This chapter gives the finite adapter.  It does not verify the
prime-patching geometry itself; it proves that, once each local marker block and
seam is checked, no additional global boundary identity remains hidden.

A marker block `B_i` has length `ell_i`, phase increment `phi_i in Z/hZ`, and an
exact additive signature

```text
s_i=(boundary defects, controller changes, action counts) in Z^r.
```

A legal concatenation may also contain finitely many seam types with stored
signatures.

## 1. Local verification implies a global signature

### Theorem PP3cnv -- PROVED / BOUNDARY SIGNATURE HOMOMORPHISM

Assume every block realization has the stored signature `s_i`, and every join of
two consecutive blocks is one of finitely many verified seam types.  If internal
interfaces are disjoint and each shared interface contribution is assigned to
exactly one adjacent block or seam, then the signature of a marker word is the
sum of its block and seam signatures.

Consequently, a finite table of local geometric checks is a complete verifier
for every concatenated boundary word.

#### Proof

Every boundary cell, controller change, and defect incidence lies either in one
block interior or in one declared interface.  The disjoint assignment prevents
double counting.  Summing the verified local identities therefore counts every
global incidence exactly once. ∎

## 2. Phase-locked semigroup words lift automatically

### Theorem PP3cnw -- PROVED / PHASE-LOCKED SIGNATURE LIFT

Suppose the length-phase projection of the marker catalogue has a finite
phase-locked conductor: for every demanded phase `t`, every `N>=T_t` has a word
of length `N` and total phase `t`.  Then every such word reconstructs an exact
geometric signature by `PP3cnv`.  No new conductor is introduced by adjoining
additive defect or controller coordinates.

If the word is reconstructed from an Apéry predecessor table, the same
predecessors reconstruct its full signature in linear time in the number of
blocks.

#### Proof

The existence statement concerns only length and phase.  Once the predecessor
table supplies a word, `PP3cnv` supplies all other coordinates by addition.
Adjoining output coordinates cannot invalidate a word already known to be legal;
it only records what that word does. ∎

## 3. Linear boundary rows from block prices

### Theorem PP3cnx -- PROVED / BLOCK-DERIVED BOUNDARY LOSS

Let block `i` have a certified nonnegative loss price `w_i` and let the total seam
price be at most `gamma`.  Every length-`N` word with multiplicities `m_i`
satisfies

```text
boundary loss <= (sum_i m_i w_i + gamma)/N.
```

If `w_i/ell_i<=rho` for every block, then

```text
boundary loss <= rho+gamma/N.
```

Thus a ledger row `rho+epsilon` is valid from every
`N>=ceil(gamma/epsilon)` once the local prices are geometrically verified.

#### Proof

Additivity gives the numerator.  Since
`sum_i m_i ell_i=N`, the block part is at most `rho N`.  Divide by `N`. ∎

## 4. Stored exact fixture

The audit `scripts/check_boundary_signature_adapter.py` uses phase modulus three
and blocks

```text
P: length 4, phase 0, action (4,0), price 4/30;
Q: length 7, phase 1, action (0,7), price 7/20.
```

The exact phase thresholds for `b congruent t mod 3` in `4a+7b=N` are

```text
T_0=60, T_1=67, T_2=74.
```

Every reconstructed action vector sums to `N`.  With one unit of seam price,

```text
boundary loss <= 1/20+1/N <= 7/120
```

for every `N>=120`.  The audit reconstructs all three phase certificates through
length 2000.

## 5. Prime-patching consequence

The boundary realization problem is reduced to a finite local task: exhibit the
actual four- and seven-step geometric blocks, list their exact controller and
defect signatures, and verify the allowed seams.  Once those checks are done,
the phase-locked conductor and the boundary ledger bound follow globally.  The
stored block signatures are still an interface fixture, not a verification of
the actual prime-patching boundary geometry.
