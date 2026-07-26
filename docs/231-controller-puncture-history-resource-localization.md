# Controller-puncture histories localize to target-scale resource signatures

PP3akk--PP3akp replace an infinite moving-controller process by finitely many
fixed-universe epochs.  The remaining endpoint is a macro containing
`Theta(R)` distinct punctured star centres, each carrying at least `W` designated
controller-shadow incidences at its puncture time.

The history was previously kept with time labels because candidate entries and
partners may repeat across epochs.  This chapter removes the diffuse possibility.
Encode the history by a bipartite graph between punctured centres and fixed
controller candidate entries.  A maximal-matching argument gives either one
candidate entry repeated through `W` centres or `Omega(R)` records with both
centre and entry distinct.  A second resource split then gives a target-degree
partner, controller, or label stack, or a target-size fully disjoint historical
matching.

Thus reserve exhaustion is not an arbitrary chronological table.  It has one of
five explicit target-scale signatures.  The remaining issue is whether the
corresponding blocker endpoints survive in one current source state, or must be
converted through a telescoping/time-labelled argument.

## 1. Chronological star records

Fix one macro whose puncture reserve contains distinct centres

```text
C={p_1,...,p_H}.
```

At the puncture time of `p_t`, choose exactly `W` incidences from its designated
source-star fibre.  Record each incidence as

```text
(p_t,q,z),
```

where `q` is the other source endpoint at that time and `z` is the controller
candidate entry blocked by `{p_t,q}`.  Write

```text
z=(sigma,e,lambda),
```

where `sigma` is movement or refill type, `e` is the controller edge, and
`lambda` is the final label.

### Proposition PP3apf -- PROVED

For one fixed centre `p_t`, the `W` selected candidate entries are distinct.
Consequently the simple bipartite graph

```text
G_hist subseteq C x Z
```

between puncture centres and candidate entries has left degree exactly `W` and

```text
|E(G_hist)|=HW.
```

#### Proof

If two distinct star partners `q,q'` produced the same candidate entry `z`, then
`p_t,q,z` and `p_t,q',z` would be collinear.  Hence `p_t,q,q'` would lie on one
line in the source present at puncture time, contradicting its no-three property.
The chosen source-star fibre uses distinct partner pairs, so its candidate
entries are distinct. ∎

The right vertices are fixed controller-entry signatures even though their
blocking witnesses are time-dependent.

## 2. Repeated candidate or a large centre--entry matching

Let

```text
Delta_Z=max_z deg_G(z).
```

### Theorem PP3apg -- PROVED

For every integer `D>=1`, at least one of the following holds.

1. One exact candidate entry occurs in at least `D` puncture-star fibres:

   ```text
   Delta_Z>=D.
   ```

2. There is a centre--entry matching of size at least

   ```text
   HW/(W+D).
   ```

#### Proof

Assume `Delta_Z<D` and take a maximal matching of size `s`.  Every history edge
meets a matched centre or a matched candidate entry.  The matched centres are
incident with exactly `sW` edges, while the matched candidate entries are
incident with fewer than `sD` edges.  Therefore

```text
HW < s(W+D),
```

which gives the displayed lower bound, up to the harmless integral rounding. ∎

The first alternative is an exact candidate-recapture stack, not merely repeated
geometric notation.

## 3. Resource localization inside a centre--entry matching

Take a centre--entry matching `M` of size `K` and retain at least `K/2` records of
one common type `sigma`.  In this subfamily both the centres `p` and the complete
candidate entries `z=(sigma,e,lambda)` are distinct.  Attach to every record its
chosen chronological partner `q`.

### Theorem PP3aph -- PROVED

For every integer `D>=1`, the one-type matched family has one of the following
outcomes.

1. One partner point `q` occurs in at least `D` records.
2. One controller edge `e` occurs in at least `D` records.
3. One final label `lambda` occurs in at least `D` records.
4. There is a subfamily of size at least

   ```text
   K/(6D)
   ```

   in which all resources

   ```text
   p, q, e, lambda, z
   ```

   are pairwise distinct within their respective types.

#### Proof

If one of the first three resource degrees reaches `D`, stop.  Otherwise greedily
select a record and delete every remaining record sharing its partner, controller,
or label.  Since every one of those degrees is below `D`, one step deletes fewer
than `3D` records.  The one-type family has size at least `K/2`, so the greedy
selection has size at least `K/(6D)`.  The centre and complete entry coordinates
were already distinct because the family came from the matching `M`. ∎

Call alternative 4 a **chronological full resource matching**.

## 4. Slab-scale consequence

Use

```text
H>=beta R,
W=sqrt(R),
```

for one fixed `beta>0`, and truncate every puncture star to exactly `W`
designated incidences.

### Corollary PP3api -- PROVED

For all sufficiently large `R`, reserve exhaustion gives at least one of:

1. one exact candidate entry repeated through at least `W` distinct punctured
   centres;
2. one chronological partner point occurring with at least `W` distinct centres;
3. one controller edge supporting at least `W` distinct same-type candidate
   entries;
4. one final movement or refill label supporting at least `W` distinct controller
   entries;
5. a chronological full resource matching of size at least

   ```text
   (beta/12+o(1))W.
   ```

#### Proof

Apply PP3apg with `D=W`.  The repeated-entry branch gives item 1.  Otherwise the
centre--entry matching has size at least

```text
HW/(W+W)>=beta R/2.
```

Apply PP3aph to that matching with `D=W`.  Its three high-degree alternatives are
items 2--4.  The full resource matching has size at least

```text
(beta R/2)/(6W)=(beta/12)W.
```

∎

All five outcomes are already at the target patch width.

## 5. Interpretation of the five signatures

### Proposition PP3apj -- PROVED

The outcomes in PP3api have the following exact meanings.

1. **Candidate-recapture stack:** the same controller edge, side, and final label
   is blocked at `W` different puncture times by blocker pairs having distinct
   punctured centres.
2. **Chronological source star:** one geometric partner point is paired with `W`
   distinct punctured centres.
3. **Controller-label star:** one controller edge carries `W` distinct labels on
   one movement/refill side.
4. **Fixed-label controller fibre:** one label carries `W` distinct controller
   edges on one side.
5. **Full chronological matching:** there are `Omega(W)` records with distinct
   punctured centres, partners, controllers, labels, and candidate entries.

#### Proof

Candidate entries in the matched family are distinct.  Therefore fixing the
controller edge forces distinct labels, and fixing the label forces distinct
controllers.  The other statements are the definitions of the corresponding
resource degrees and matching. ∎

The result keeps geometric/time identity explicit: a chronological partner star
need not yet be a star in the final source state.

## 6. Stable-history conversion interface

Call a chronological record **stable** when both blocker endpoints belong to one
common retained source state in which its candidate entry is still relevant.

### Corollary PP3apk -- PROVED / CONDITIONAL STABLE-HISTORY INTERFACE

If an `Omega(W)` subfamily in any PP3api outcome is stable, then it enters the
existing conversion machinery.

1. A stable partner stack is a target-size source star.
2. A stable fixed-label fibre with endpoint-disjoint blocker pairs enters
   PP3ald--PP3alf.
3. A stable full chronological resource matching is already a target-size
   controller-disjoint blocker bank after the usual two-layer refinement and
   `o(R)` batch puncturing.
4. A stable candidate stack or controller-label star is an explicit fixed-entry
   or fixed-controller ownership core for the local Ore and controller-defect
   conversions.

If no target-size stable subfamily exists, reserve exhaustion has been reduced to
an intrinsically temporal problem: most designated blocker endpoints disappear
or change before a common retained state is reached.

#### Proof

Apply the cited source-star, fixed-label resource-matching, layer-refinement, and
controller-defect interfaces to a stable subfamily.  The resource distinctness in
PP3api supplies their disjointness hypotheses.  Negating stability leaves exactly
the stated transient-history alternative. ∎

## 7. Revised puncture-history frontier

### Corollary PP3apl -- PROVED

A macro-local `Theta(R)` puncture history is no longer an unstructured terminal
core.  It contains a target-scale:

1. repeated exact candidate stack;
2. chronological source-partner star;
3. controller-label star;
4. fixed-label controller fibre; or
5. full chronological resource matching.

The remaining genuinely new puncture issue is **temporal stability**: converting
one of these signatures when most of its blocker partners or candidate witnesses
are transient across the puncture epochs.  Static resource localization is now
complete.

The no-three-in-line conjecture remains unproved.
