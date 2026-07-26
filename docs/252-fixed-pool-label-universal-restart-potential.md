# Fixed pool-label restart potential with zero-mass anchor activation

The fixed-attempt theorem PP3auq--PP3auw leaves one comparability problem: after a
paid source repair, the controller matching inside a slab pool may change.  The
movement/refill **candidate cells** depend only on the fixed pool coordinate sets, but
the active same-slot movement/refill pair depends on the current controller edge.

Counting every inactive latent pair is unnecessarily strong.  The correct restart
rule is:

1. keep the candidate-cell universe fixed;
2. keep only the currently active same-slot anchor entries; and
3. permit a new controller pairing only when every newly activated anchor entry has
   zero mass in the repaired source.

The complete marked-support theorem can enforce this rule because activation of a
positive same-slot anchor entry has ordinary-helper support rank at most two.

## 1. Fixed coordinate and label infrastructure

For each macro `i in [M]`, fix old-coordinate sets

```text
X_i,Y_i subseteq [m],
|X_i|=|Y_i|=R,
```

with the `X_i` pairwise disjoint and the `Y_i` pairwise disjoint.  Fix the complete
movement and refill label sets

```text
Aset,Bset subseteq {m+1,...,m+T}.
```

At every allocation attempt, the distinguished source layer contains a perfect
matching

```text
E_i subseteq X_i x Y_i.
```

The pairing may evolve, but `X_i,Y_i,Aset,Bset` do not.

Let

```text
V_cell
=
union_i ({(x,A):x in X_i,A in Aset}
         union
         {(B,y):B in Bset,y in Y_i}).
```

For a saturated source `S`, let `b_S(z)` be the number of source blocker pairs through
`z`, and define

```text
Xi_cell(S)=sum_(z in V_cell) (b_S(z)-1).
```

### Proposition PP3aux -- PROVED

`V_cell` and `Xi_cell` are independent of the current perfect matching between each
`X_i` and `Y_i`.

#### Proof

Movement cells depend only on `X_i,Aset`; refill cells depend only on `Y_i,Bset`.
Every saturated source has exactly one axis blocker pair through each candidate cell,
so the subtraction by one remains valid after the controller pairing changes.  This
is PP3ku--PP3kw. ∎

## 2. Active same-slot anchor potential

For a current pool edge `e=(x,y) in E_i`, labels `A,B`, and a retained source point
`p=(u,v)`, call `(e,A,B,p)` an active anchor incidence when

```text
(A-v)(B-u)=(x-u)(y-v)>0.
```

This is exactly the same-slot product equation PP3dv.  Put

```text
Lambda_E(S)
=
# {(i,e,A,B,p):
      e in E_i,
      A in Aset,
      B in Bset,
      p in S\{e},
      (e,A,B,p) is an active anchor incidence}.
```

Define the current restart potential

```text
Theta_E(S)=Xi_cell(S)+Lambda_E(S).
```

### Proposition PP3auy -- PROVED

`Theta_E(S)` is a nonnegative integer and exactly dominates the two unary
controller-aware failure tables used by one fixed allocation attempt:

1. nonaxis movement/refill blocker incidences; and
2. active same-slot retained-anchor incidences.

#### Proof

The first table is counted by `Xi_cell`; the second is the definition of
`Lambda_E`.  Both count incidences with full multiplicity. ∎

The anchor universe is allowed to change with `E`.  Comparability will come from
zero-mass activation rather than from counting all inactive pairings.

## 3. Anchor transition under a pairing change

Let a pool-compatible repair change the pool matchings from `E` to `E'`, remove
source cells `D`, and insert source cells `A`.  Write

```text
E_keep=E cap E',
E_del =E\E',
E_new =E'\E.
```

Every anchor incidence after the repair belongs to one of three classes:

1. it uses an unchanged controller edge from `E_keep` and a retained old anchor;
2. it uses an unchanged controller edge and a newly inserted anchor; or
3. it uses a newly activated controller edge from `E_new`.

### Proposition PP3auz -- PROVED

If the repaired state satisfies both conditions

```text
(A) no inserted source point creates an anchor incidence for an edge in E_keep;
(B) every edge in E_new has zero active anchor mass in the repaired source,
```

then

```text
Lambda_(E')(S')
<=
Lambda_E(S)-C_anchor,
```

where `C_anchor` is the number of old active anchor incidences destroyed by deleting
marked source anchors or by deleting their controller edges.

#### Proof

Class 2 is empty by condition (A), and class 3 is empty by condition (B).  Every
surviving class-1 incidence was already present before the repair.  Old incidences
whose anchor or controller is deleted disappear and contribute to `C_anchor`. ∎

Thus newly introduced controller entries need not belong to a permanent universe;
they only need zero initial mass.

## 4. Exact candidate-cell accounting

For source points `p,q`, put

```text
omega(p,q)=# {z in V_cell:p,q,z collinear}.
```

For a repair `S'=(S\D) union A`, define the usual fixed-universe removal and
insertion terms

```text
C_cell(D)
=
sum_(d in D) sum_(p in S\D) omega(d,p)
+
sum_({d,e} subseteq D) omega(d,e),

I_cell(A)
=
sum_(a in A) sum_(p in S\D) omega(a,p)
+
sum_({a,b} subseteq A) omega(a,b).
```

### Theorem PP3ava -- PROVED

One has

```text
Xi_cell(S')-Xi_cell(S)=I_cell(A)-C_cell(D).
```

If, in addition, the two zero-mass anchor conditions of PP3auz hold, then

```text
Theta_(E')(S')-Theta_E(S)
<=
I_cell(A)-C_cell(D)-C_anchor.
```

In particular, if the repair creates no candidate-cell insertion incidence, then

```text
Theta_(E')(S')-Theta_E(S)
<=
-[C_cell(D)+C_anchor].
```

#### Proof

The cell identity is PP3kx because `V_cell` is fixed.  Add the anchor inequality from
PP3auz. ∎

## 5. Complete restart-support rank

Consider a tied endpoint cycle with marked source cells alternating with ordinary
helpers.  Form one support hypergraph containing every positive event that would:

1. violate source validity or cell distinctness;
2. create a new `Xi_cell` incidence;
3. create an anchor incidence using an unchanged controller edge and an inserted
   source anchor; or
4. give positive final anchor mass to a newly inserted controller edge.

### Proposition PP3avb -- PROVED

Every event in this restart-support table has nonempty ordinary-helper support of rank
at most three.

More precisely:

1. a class-3 anchor event has rank one;
2. a class-4 activation event has rank one or two;
3. a candidate-cell blocker insertion has rank at most two; and
4. source-validity and the remaining bounded endpoint conditions have rank at most
   three.

#### Proof

An unchanged-controller anchor event contains one inserted source point.  A new
controller edge is one selected inserted source cell; if its anchor is retained the
event uses one selected cell, and if the anchor is also inserted it uses two.
`Xi_cell` is a pair potential.  The remaining cases are PP3atv--PP3atw.  Strict
alternation gives one ordinary helper in every selected cell. ∎

An independent helper block therefore enforces both zero-mass activation conditions
and zero candidate-cell insertion cost simultaneously.

## 6. Pool-compatible block decomposition

Keep one distinguished source matching layer in the form

```text
P=E_1 dot-union ... dot-union E_M dot-union E_*,
```

and let `Q` be the complementary source matching layer.  For a marked set `D`, put

```text
D_i=D cap E_i,
D_*=D cap E_*,
D_Q=D cap Q.
```

### Proposition PP3avc -- PROVED

Process every nonempty block by a tied cycle using helpers from the same matching
block.  Then:

1. every `E_i` remains a perfect matching between the same `X_i,Y_i`;
2. `E_*` and `Q` remain perfect matchings on their original coordinate sets;
3. the source remains saturated;
4. different blocks may be processed sequentially; and
5. if the block sizes are `s_j`, then

   ```text
   sum_j s_j^2 <= (sum_j s_j)^2.
   ```

#### Proof

A tied permutation within one block preserves its row and column sets and fixes every
other block.  The square inequality is immediate. ∎

At the slab-optimal scale each pool has size `R`, while every target block has size at
most `W=Theta(sqrt(R))`, so the same pool supplies its own critical helper reservoir.

## 7. Pool-compatible paid restart step

Suppose a marked set `D`, `|D|<=W`, carries designated old incidence credit

```text
c(D)=C_cell+C_anchor>0
```

in the current potential `Theta_E`.

### Theorem PP3avd -- PROVED / CONDITIONAL EXISTING CONVERSION INTERFACES

Exactly one of the following occurs.

1. Sequential pool-compatible cycles delete every cell of `D`, preserve all fixed
   coordinate and label infrastructure, activate every new controller edge with zero
   anchor mass, and satisfy

   ```text
   Theta_(E_final)(S_final)-Theta_E(S_initial)<=-c(D).
   ```

2. One restart-support table produces an `Omega(|D|)` canonical source star,
   matching, endpoint bank, transition sunflower, anchor bank, fixed-core petal bank,
   or `A_2/B_3/B_4` structure.

#### Proof

Apply the critical rank-three support theorem in each nonempty block using PP3avb and
PP3avc.  In the independent branch, candidate-cell insertion cost is zero and both
anchor activation classes are absent.  Assign every designated incidence to the
first block cycle deleting one of its marked endpoints or its active controller.
PP3ava gives the displayed decrease.

A dense support branch has one of the already classified canonical source, anchor,
transition, or insertion types and enters PP3aug and PP3aqo--PP3aqt. ∎

## 8. Fixed infrastructure endpoint

### Corollary PP3ave -- PROVED / CONDITIONAL EXISTING CONVERSION INTERFACES

Every controller-aware allocation repair may be performed without changing
`X_i,Y_i,Aset,Bset`.  Controller pairings may change inside the fixed pool rectangles,
but all new same-slot entries start with zero anchor mass.

Actual blocker stars and banks supply `Xi_cell` credit.  Actual same-slot anchor stars
and banks supply `Lambda_E` credit.  Every fixed-attempt failure therefore enters
PP3avd.

### Corollary PP3avf -- PROVED

Restart comparability does not require a universal latent anchor table.  It follows
from:

1. one fixed candidate-cell universe;
2. pool-compatible controller re-pairing; and
3. zero-mass activation of every newly introduced same-slot anchor entry.

The no-three-in-line conjecture remains unproved.
