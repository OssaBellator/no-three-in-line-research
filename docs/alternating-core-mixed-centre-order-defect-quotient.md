# Order-defect quotients for mixed-centre affine phase semigroups

**Branch:** `research/alternating-core-chain`

AC3rp--AC3ry close common-centre affine families and reduce mixed-sign translations to primitive
zero-sum relations.  The remaining affine obstruction is a finite family of integer-affine cycle
maps with no common fixed centre.  Their multipliers commute, but their intercepts depend on the
chronological order.

This note isolates that order dependence exactly.  Every adjacent transposition has one integer
swap defect.  The gcd of those defects gives a finite commutative residue quotient, and inside a
bounded physical memory interval each fixed count vector has only finitely many exact lifts.

## Finite affine alphabet

Let `Lambda={1,...,s}` be the live affine cycle-address alphabet in one fixed epoch.  Write

`f_i(h)=A_i*h+B_i`,

with `A_i,B_i in Z`.  A word `w=i_1...i_m` acts chronologically by applying `f_(i_1)` first and
`f_(i_m)` last.  Its exact affine map is

`F_w(h)=A(w)*h+B(w)`,

where

`A(w)=prod_(r=1)^m A_(i_r)`.

For two addresses define the signed pair-swap defect

`kappa_(i,j)=(A_j-1)B_i-(A_i-1)B_j`.

Thus `kappa_(j,i)=-kappa_(i,j)`.

## AC3rz -- exact adjacent-swap defect law -- PROVED

Suppose a word contains adjacent addresses `i,j`, followed by a suffix whose multiplier product is

`M_suf`.

Let `w_ij` be the word with order `i,j` at that location and `w_ji` the word with those two
addresses swapped.  Then

`A(w_ij)=A(w_ji)`

and

`B(w_ij)-B(w_ji)=M_suf*kappa_(i,j)`.

### Proof

Before the suffix, applying `i` then `j` gives intercept `A_j B_i+B_j`, while applying `j` then
`i` gives `A_i B_j+B_i`.  Their difference is

`(A_j-1)B_i-(A_i-1)B_j=kappa_(i,j)`.

Every later affine map multiplies an existing input difference by its multiplier.  Multiplying over
the suffix gives the displayed formula.  The total multiplier is the same because integer
multiplication is commutative. QED.

The defect is context-sensitive only through the suffix multiplier; its primitive physical address
is the ordered pair `(i,j)`.

## AC3sa -- zero pair defects classify the commuting families -- PROVED

All pair defects vanish if and only if the affine maps commute pairwise.

Moreover, if all `kappa_(i,j)=0`, then exactly one of the following holds:

1. every `A_i=1`, so the family consists entirely of translations; or
2. some `A_i!=1`, every nontranslation map has one common rational fixed centre
   
   `q=B_i/(1-A_i)`,
   
   and every translation in the family is the identity.

### Proof

The first statement follows by comparing `f_j o f_i` and `f_i o f_j`; their multipliers agree and
their intercept difference is `kappa_(i,j)`.

Assume all defects vanish and choose `i` with `A_i!=1`.  For every `j` with `A_j!=1`, the equation
`kappa_(i,j)=0` rearranges to

`B_i/(1-A_i)=B_j/(1-A_j)`.

If `A_j=1`, the same equation becomes `(A_i-1)B_j=0`, hence `B_j=0`.  The converse is immediate.
QED.

Thus a genuinely mixed-centre family has at least one nonzero pair defect.

## AC3sb -- commutative residue quotient -- PROVED

Assume some pair defect is nonzero and put

`g=gcd{|kappa_(i,j)|:1<=i<j<=s}`.

Then `g>=1`.  Reducing affine maps modulo `g` makes the whole family commute.  Equivalently, if two
words have the same count vector

`m=(m_1,...,m_s)`,

then

`A(w)=A(w')`

exactly and

`B(w)=B(w') mod g`.

The affine residue-map stock has at most `g^2` parameter pairs `(A mod g,B mod g)`.

### Proof

Every pair defect is divisible by `g`, so AC3rz says every adjacent transposition leaves the affine
map unchanged modulo `g`.  Any two words with the same count vector are connected by adjacent
transpositions.  Their exact multipliers are the common product `prod_i A_i^(m_i)`, and their
intercepts are congruent modulo `g`.  There are at most `g` multiplier residues and `g` intercept
residues. QED.

For `g=1` the order-sensitive residue quotient is trivial, even though exact order defects may be
nonzero.

## AC3sc -- bounded exact lift multiplicity -- PROVED

Suppose physical memory is confined to an integer interval

`L<=h<=U`,

of width `R=U-L`.  Fix one input value `h_0` and one count vector `m`.  Among all chronological
orderings with count vector `m`, the number of distinct feasible exact output values is at most

`floor(R/g)+1`.

More generally, every one residue class modulo `g` has at most `floor(R/g)+1` representatives in the
physical interval.

### Proof

AC3sb makes all outputs for the fixed input and count vector congruent modulo `g`.  Distinct such
integers differ by at least `g`.  An interval of width `R` contains at most `floor(R/g)+1` integers
from one residue class. QED.

This bound is independent of the word length and of the number of permutations of the count
vector.

## AC3sd -- mixed-centre order router -- PROVED UNDER THE ORDER-LIFT CONTRACT

Inside one fixed bounded affine epoch, the mixed-centre branch decomposes into:

1. a **commutative count ledger**, namely the count vector together with the residue affine map
   modulo `g`;
2. an **exact order lift**, chosen from at most `floor(R/g)+1` feasible values for each fixed input
   and count vector;
3. a finite primitive pair-defect dictionary `(i,j,kappa_(i,j))`.

Suppose every recurrent count-ledger relation is quotient-erased, descending, impossible, ticketed
or resetting, and every nontrivial return among exact order lifts is likewise descending, ticketed
or resetting.  Then the mixed-centre affine epoch contains no infinite nonterminal history.

### Proof

AC3sb removes chronological order from the residue ledger.  AC3sc bounds the exact lift multiplicity
above each fixed count ledger.  An infinite history would therefore force either infinitely many
unpaid count-ledger relations or infinitely many unpaid returns among a finite lift fibre.  Both are
excluded by the stated contracts. QED.

The theorem does not claim that the count ledger is automatically finite: unbounded multiplier or
count growth remains an explicit affine gate.  Its gain is that mixed-centre order sensitivity is no
longer an opaque semigroup phenomenon.

## Corrected AC4 phase-memory frontier

The scalar-affine branch is now separated into exact finite interfaces:

- common-centre multiplication ranks;
- same-sign translation ranks;
- primitive mixed-sign translation relations;
- and mixed-centre commutative residue ledgers with bounded exact order lifts.

The remaining affine work is unranked growth or recurrence in the commutative count ledger and
unticketed returns between exact `g`-spaced lifts.  Genuinely nonlinear path memory, changing laws,
fresh weighted capacity, nonadditive outputs, unpaid loss and the other AC4 interfaces remain
unchanged.

## Finite check

`scripts/verify_ac_mixed_centre_order_defect.py` exhausts and samples small integer-affine families.
It checks the adjacent-swap formula, pairwise-zero classification, same-count congruence modulo the
defect gcd, residue-map commutativity and the bounded exact-lift count.