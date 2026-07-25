# Canonical anchor-deficiency cores

PP3vj gives a balanced ownership with only `D_anc` anchor-threshold violations,
but an arbitrary completion may make those violations look scattered.  The
standard alternating-reachability decomposition of a maximum acceptable matching
confines all necessary violations to one exact Hall cut.

After expanding macro capacities into clones, the unmatched labels generate a
Dulmage core `X`.  The acceptable matching is complete on both sides outside the
core, and every missing completion edge goes from `X` to macro slots outside its
acceptable neighbourhood.  Thus the exceptional assignments form a matching
inside one completely unacceptable rectangle.

## 1. Clone-expanded acceptable host

Expand every macro into `W` identical ownership slots.  Let

```text
G_acc = (L,R;E_acc)
```

be the resulting balanced bipartite graph, where `|L|=|R|=T`.  An edge is present
exactly when the corresponding macro--label pair has anchor mass at most the
threshold `u`.

Let `M0` be a maximum matching of `G_acc`, and write

```text
d = T-|M0|.
```

By PP3vi, `d <= D_anc`.

Direct every unmatched acceptable edge from `L` to `R`, and every matched edge
of `M0` from `R` to `L`.  Start alternating reachability from the `d` unmatched
labels of `L`.  Let `X` be the reachable labels and `Y` the reachable slots.

## 2. Exact Dulmage core

### Theorem PP3vn -- PROVED

The alternating-reachability sets satisfy:

1. `Y = N(X)` in the acceptable clone graph;
2. every slot of `Y` is matched by `M0` to a label of `X`;
3. every matched label of `X` is matched to a slot of `Y`;
4. `M0` matches every label outside `X` to a slot outside `Y`;
5. the deficiency is exact:
   
   ```text
   |X|-|Y| = d;
   ```
6. there is no acceptable edge from `X` to `R\Y`.

#### Proof

Every neighbour of a reachable label is reachable by an unmatched forward edge,
unless it is its matched slot, which is also reachable along that same graph
edge.  Hence `N(X) subseteq Y`; the reverse inclusion is immediate from the way
slots are reached, so `Y=N(X)`.

A reachable slot cannot be unmatched, because that would give an augmenting path
from an unmatched label, contradicting maximality of `M0`.  Its matched label is
therefore reachable.  Conversely every reachable matched label is reached from
its matched slot.  This proves statements 2 and 3.

No matched edge crosses from `X` to `R\Y` or from `L\X` to `Y`, so `M0` restricts
to matchings on the two diagonal blocks.  It saturates `Y` and every label outside
`X`.  The only unmatched labels are the original `d` roots, all in `X`, giving
`|X|-|Y|=d`.  The final statement is `Y=N(X)`. ∎

Thus `X` is not merely some deficient Hall set; it is the canonical deficient
set associated with the chosen maximum matching.

## 3. Completion inside one all-bad rectangle

Let `L0` be the unmatched labels of `M0`, and let `R0` be its unmatched macro
slots.  Both have size `d`.

### Corollary PP3vo -- PROVED

One has

```text
L0 subseteq X,
R0 subseteq R\Y.
```

Pairing `L0` bijectively with `R0` completes `M0` to a balanced ownership with
exactly `d` possibly unacceptable assignments.  Every such assignment lies in

```text
X x (R\Y),
```

and every pair in this rectangle is unacceptable.

All other assigned macro--label pairs are anchor-threshold acceptable.

#### Proof

The unmatched labels are the alternating-search roots, so they lie in `X`.
Every slot in `Y` is matched by PP3vn, hence unmatched slots lie outside `Y`.
Since there is no acceptable edge from `X` to `R\Y`, every completion pair is
unacceptable.  The original matching edges are acceptable by construction. ∎

Therefore the threshold violations need not be spread over unrelated Hall
witnesses.

## 4. Collapse back to macro capacities

Because all `W` clones of one macro have the same acceptable label
neighbourhood, a macro contributes either all its clones or none of them to
`Y=N(X)`.

### Proposition PP3vp -- PROVED

There is a macro set `J=N_M(X)` such that

```text
Y = J x [W].
```

The all-bad completion rectangle is therefore

```text
X x (([M]\J) x [W]).
```

Every necessary threshold-violating assignment sends one unmatched label of `X`
to an unused slot of a macro outside `J`.

#### Proof

If one clone of macro `i` is adjacent to a label of `X`, every clone is adjacent
to that label and is reachable.  If no label of `X` is acceptable for the macro,
none of its clones lies in `Y`. ∎

This is the clone-level form of the all-bad score rectangle from PP3mn.

## 5. Localized size profiles

### Corollary PP3vq -- PROVED

At the anchor threshold of PP3of, the canonical deficiency core has one of two
profiles.

1. **Small-label core:**
   
   ```text
   |X| = O(m^(1/2-zeta+o(1))).
   ```
2. **Small excluded-macro side:**
   
   ```text
   T-|X| = O(m^(1/2-zeta+o(1)))
   ```
   
   and the number of macros outside `J` is
   
   ```text
   O(m^(1/40-zeta+o(1))).
   ```

In both cases the exact number of necessary threshold violations is

```text
d = |X|-W|J| <= D_anc
  = O(m^(1/2-zeta+o(1))).
```

#### Proof

Apply PP3vg to `X`.  In the large-label case, apply PP3vh to the excluded macro
set.  The exact deficiency is PP3vn. ∎

## 6. Revised exceptional-assignment endpoint

### Corollary PP3vr -- PROVED

The direct anchor obstruction is reduced to one explicit deficient ownership
core.  Outside that core, every movement or refill ownership assignment may be
chosen anchor-threshold acceptable.

Inside the core, exactly `d=o(T)` labels must cross a completely unacceptable
label-by-macro cut.  The remaining tasks are therefore:

- choose the `d` crossing assignments with low actual anchor weight;
- absorb the core by local label or macro trades;
- or convert its concentrated same-slot anchor geometry.

Scattered threshold violations and multiple unrelated Hall witnesses are no
longer separate open cases.