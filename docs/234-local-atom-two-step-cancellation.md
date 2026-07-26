# Every local insertion atom is cancellable by a second marked move

PP3aor--PP3aox reduce conditioned petal failure to one credit-scale local
`A_2`, `B_3`, or `B_4` atom.  PP3aoy--PP3ape absorb those atoms in the robust
final-allocation branch.  The remaining formulation called them a monotone-only
frontier because the first trade need not decrease `Xi`.

A local atom is, however, made entirely of controller-shadow incidences sharing at
least one newly inserted endpoint cell.  After the first trade that cell belongs
to the source.  A second marked trade moving it destroys every incidence of the
atom.  In the sum of the two exact dynamic identities, the atom's creation and
destruction cancel.

This extends the unary-domain composite theorem PP3aho--PP3aht to all three local
insertion ranks.  Rank-three and rank-four atom multiplicity is not an unpaid cost;
it is temporary removal credit for the second step.

## 1. Local atoms as centred incidence families

Let a source-admissible first trade `T_1` insert endpoint cells

```text
P={a_1,...,a_s}
```

and produce source `S_1`.  Fix one positive local insertion atom `A` selected by
the conditioned path skeleton.

The three possibilities are:

1. `A_2`: incidences whose blocker pair is `{a,p}` for one inserted cell `a` and
   a retained source point `p` that may vary with the candidate entry;
2. `B_3`: incidences whose blocker pair is `{a,b}` for two inserted cells forming
   an adjacent two-arc path;
3. `B_4`: incidences whose blocker pair is `{a,b}` for two inserted cells belonging
   to two disjoint selected arcs.

Let

```text
C=w(A)
```

be the exact dynamic `Xi` weight of the atom, with candidate-entry multiplicity.
Choose one inserted endpoint `a` belonging to its blocker pair support.

### Proposition PP3aqa -- PROVED

Immediately after `T_1`, the point `a` is a source endpoint in `S_1` and belongs
to all `C` selected controller-shadow incidences of `A`.  Any source-admissible
second trade that deletes `a` destroys all `C` incidences.

The statement permits repeated partners, repeated geometric lines, and arbitrary
candidate multiplicity.

#### Proof

For `A_2`, every selected incidence is by definition blocked by `{a,p}` and
contains `a`.  For `B_3` and `B_4`, every selected incidence is blocked by the same
inserted pair `{a,b}` and also contains `a`.  The first trade is source-admissible,
so all blocker endpoints belong to `S_1`.  Deleting `a` removes every selected
pair from the source and therefore removes every associated potential incidence.
The dynamic potential counts incidences with multiplicity, so all `C` units are
removed. ∎

For binary atoms the partner may be the same point `b` in all `C` incidences.  No
distinct-partner hypothesis is needed for accounting.

## 2. Exact two-step cancellation

Write the first insertion cost as

```text
I_1=C+J_1,
```

where `J_1` is every first-step insertion incidence not selected into the atom.
Let the exact first-step removal credit be `R_1`.

Let a second source-admissible marked trade `T_2` move `a`.  Split its insertion
cost as

```text
I_2=I_rec+J_2,
```

where `I_rec` counts recreation of the chosen atom incidences and `J_2` is every
other second-step insertion incidence.

### Theorem PP3aqb -- PROVED

The total two-step potential change satisfies

```text
Xi(S_2)-Xi(S_0)
<=
J_1+I_rec+J_2-R_1.
```

Any additional second-step removal credit only improves the inequality.

#### Proof

The first dynamic identity is

```text
Xi(S_1)-Xi(S_0)=C+J_1-R_1.
```

By PP3aqa, moving `a` removes all `C` selected atom incidences.  Hence

```text
Xi(S_2)-Xi(S_1)
<=
I_rec+J_2-C.
```

Add the two identities. ∎

Thus the possibly enormous atom weight disappears completely from the composite
budget.

## 3. Marked self-recapture of one atom

Place `a` in an ambient tied endpoint layer of size `Q`, choose a marked
source-valid subbank of size `q`, and move `a` using an `MS(K)` law from PP3agk.
For each selected atom incidence, retain its other blocker endpoint and its
candidate entry.

### Proposition PP3aqc -- PROVED / CONDITIONAL ON `MS(K)`

The expected recreation of the chosen local atom satisfies

```text
E I_rec
<=
K C (q-2)/(Q-2).
```

This holds for all three ranks and remains valid when all binary incidences use
one repeated partner and one repeated geometric blocker line.

#### Proof

Each selected incidence is one centre-credit incidence through the distinguished
point `a`.  Proposition PP3agh associates to its nonaxis credit line a partial
matching of ambient trace cells, and PP3agk bounds its recreation probability.
The proof of PP3agj explicitly permits repeated lines and repeated trace cells,
because multiplicity is retained on both sides of the potential identity.  Sum
over the `C` atom incidences. ∎

At `q=o(Q)` and `K=1+o(1)`, this is `o(C)`.  More importantly for PP3aqb, one can
choose `q` sufficiently slowly so that it is `o(R_1)` whenever

```text
Q R_1/C -> infinity,
```

exactly as in PP3ahr.

## 4. Composite paid criterion

### Theorem PP3aqd -- PROVED / CONDITIONAL COMPOSITE MARKED-HOST INTERFACE

Assume a marked source-valid second-step law moving `a` exists.  If

```text
J_1+E[I_rec+J_2] < R_1,
```

then some supported two-step outcome strictly decreases `Xi`.

In particular, it is sufficient that

```text
J_1=o(R_1),
E J_2=o(R_1),
E I_rec=o(R_1).
```

#### Proof

Take expectations in PP3aqb.  The expected composite change is negative, so one
supported pair of source-admissible trades has negative change. ∎

The first trade is allowed to have positive potential change and the selected
atom may have weight much larger than `R_1`; neither quantity appears in the final
criterion.

## 5. Application to the three explicit petal endpoints

### Corollary PP3aqe -- PROVED / CONDITIONAL EXISTING PETAL AND MARKED INTERFACES

After an independent helper completion from PP3aok--PP3aoo, a credit-scale local
atom has one of the following forms.

1. **Unary arc atom `A_2`.**  Move its inserted arc cell in a second marked trade.
   The unary incidences become centre credit and cancel by PP3aqb.
2. **Rank-three path atom `B_3`.**  Choose either inserted cell of the blocked pair
   as the marked centre.  All path-atom multiplicity cancels.
3. **Rank-four partner atom `B_4`.**  Choose either endpoint of the disjoint-arc
   blocker pair.  All partner/fan multiplicity cancels.

The remaining alternatives are:

1. strict composite paid improvement;
2. second-step foreign unary/rank-three/rank-four support concentration;
3. marked source, transition, controller-pool, Hall, alternating, or
   distinguished-endpoint host failure;
4. first-step nonatom collateral already at the original removal-credit scale;
5. failure of the required marked self-recapture scale.

No local atom weight remains as an uncancelled term.

## 6. Relation to robust final allocation

The two completion architectures now agree on the local atoms.

### Corollary PP3aqf -- PROVED

A conditioned local `A_2/B_3/B_4` atom has the exact endpoint:

1. robust final allocation absorbs its simple support by PP3aoy--PP3ape; or
2. a second marked move cancels its full dynamic multiplicity by PP3aqa--PP3aqe;
   or
3. explicit first-step collateral, second-step foreign support, or host failure
   occurs.

Thus neither weighted local multiplicity nor the insistence on a one-step
potential decrease is necessary for the prime-patching route.

## 7. Revised atom frontier

### Corollary PP3aqg -- PROVED

The single credit-scale local atom is no longer an independent frontier, even
outside robust final allocation.  Its weight is either:

1. ignored at the domain-support scale; or
2. created and then cancelled as exact second-step removal credit.

The live paid problem is now entirely the **uncancelled collateral**:

```text
first-step nonatom cost
+
second-step self-recapture
+
second-step foreign insertion cost,
```

along with the marked/external host conditions required to realize the composite
trade.

The no-three-in-line conjecture remains unproved.
