# One-helper bridges and finite local-cost atomization

PP3aok--PP3aoq reduce a conditioned petal to an independent helper completion and
a finite local-core table.  The unary arc and rank-three path petals are already
spanning directed paths.  A rank-four partner petal consists of two disjoint arcs;
one additional helper index joins them into a spanning five-vertex path.

On a fixed directed path, every selected canonical insertion pattern supported on
the path vertices is one of three explicit atoms:

1. one path arc (`A_2`);
2. one adjacent two-arc path (`B_3`);
3. one pair of nonadjacent path arcs (`B_4`).

There are at most ten atoms for the path lengths used in the marked filler.  Hence
local-core cost at the removal-credit scale cannot be diffuse.  It is one
credit-scale unary arc, rank-three path, or rank-four disjoint-arc atom.  When the
bridge helper varies, failure produces an existing heavy insertion pencil rather
than a new four-vertex local table.

## 1. Insertion atoms on a fixed path

Let

```text
P=v_0->v_1->...->v_r
```

be a directed path of `r` arcs, with `1<=r<=4`.  Assume the path is source-clean.

### Proposition PP3aor -- PROVED

The positive canonical insertion patterns whose endpoint support is contained in
`V(P)` and whose arcs are selected by the path consist exactly of:

```text
r                         rank-two unary A_2 atoms,
r-1                       rank-three binary B_3 atoms,
binom(r,2)-(r-1)          rank-four binary B_4 atoms.
```

Their total number is

```text
C_r = 2r-1 + (r-1)(r-2)/2.
```

In particular,

```text
C_1=1,
C_2=3,
C_3=6,
C_4=10.
```

#### Proof

Every selected unary atom is one path arc.  A pair of selected path arcs has
support rank three exactly when the arcs are adjacent, giving `r-1` pairs.  Every
other unordered pair is vertex-disjoint and has support rank four.  Diagonal and
transposition atoms are absent from a path and from every single-cycle
completion. ∎

No higher-rank insertion class exists in the dynamic `Xi` normal form.

## 2. Local-cost atomization

Give the selected `A_2`, `B_3`, and `B_4` atoms their exact nonnegative insertion
weights.  Let

```text
J_P^loc
```

be their sum and let `R_P>0` be the path's removal credit.

### Corollary PP3aos -- PROVED

Exactly one of the following holds.

1. `J_P^loc<R_P`.
2. One local insertion atom has weight at least

   ```text
   R_P/C_r.
   ```

For `r<=4`, the second threshold is at least `R_P/10`.

#### Proof

If every one of the `C_r` atoms had weight below `R_P/C_r`, their sum would be
below `R_P`. ∎

Combined with an independent residual helper completion, alternative one gives a
strict paid improvement by PP3aom.

## 3. Bridging two disjoint arcs

Fix two compatible disjoint arcs

```text
a->b,
c->d
```

on four endpoint indices.  For a helper index `x` outside those indices, define
the two bridge orientations

```text
P_x^+ : a->b->x->c->d,
P_x^- : c->d->x->a->b.
```

Call an orientation **source-clean** when all four of its arcs and every canonical
source condition supported on the path hold.

### Proposition PP3aot -- PROVED

Conditioned on either source-clean bridge path inside a `q`-index marked block,
the number of single-cycle completions is

```text
(q-5)!,
```

and every residual compatible `u`-arc forest has probability

```text
1/(q-5)_u,
```

unless it creates a proper directed cycle.

#### Proof

The bridge path has four fixed arcs on five vertices.  Apply PP3aok. ∎

The complete local insertion table of a bridge path has exactly `C_4=10` atoms.

## 4. Bridge-helper endpoint

Let `X` be a helper reservoir.  For each `x in X`, test both bridge orientations.
Let `X_clean` be the set of helpers admitting at least one source-clean
orientation, and for each such helper choose one clean orientation `P_x` of
minimum local insertion cost.

### Theorem PP3aou -- PROVED / CONDITIONAL INDEPENDENT-COMPLETION INTERFACE

Suppose some `x in X_clean` has:

1. a residual helper-support-independent completion after fixing `P_x`; and
2. local insertion cost `J_(P_x)^loc<R_(P_x)`.

Then a source-valid strict paid improvement exists.

If no such helper exists, at least one of the following holds.

1. Every independently completable clean bridge has one `A_2`, `B_3`, or `B_4`
   local atom of weight at least one tenth of its removal credit.
2. Every clean bridge has a second-generation terminal residual pencil from
   PP3aoo.
3. The clean-helper set is small because unary source, anchored-transition, or
   another fixed-path source condition fails on most bridge helpers.
4. The conditional single-cycle, controller-pool, distinguished-endpoint, Hall,
   or alternating host fails explicitly.

#### Proof

The paid branch is PP3aom and PP3aot.  Otherwise apply PP3aos to every
independently completable clean bridge, PP3aoo to every noncompletable one, and
record source or external host failure for the remaining helpers. ∎

Thus the disconnected rank-four local-core table is replaced by one bridge choice
and the already named source/insertion structures.

## 5. Heavy bridge families are existing pencils

Assume a set `Y subseteq X_clean` of helpers has source-clean bridge paths and
removal credits at least `R_*>0`.  Suppose every `x in Y` has local cost at least
`R_*`.

### Theorem PP3aov -- PROVED

After passing to a subfamily of size at least `|Y|/20`, one fixed orientation and
one fixed local atom role has weight at least `R_*/10` for every retained helper.
The resulting variable-helper family is exactly one of:

1. a fixed-axis `A_2` arc pencil;
2. a fixed-centre `B_3` path pencil;
3. a fixed-centre-arc `B_4` partner pencil.

#### Proof

Choose one of two bridge orientations and one of at most ten local atom positions
witnessing PP3aos.  Pigeonhole the at most twenty possibilities.  In every fixed
position all nonvariable path vertices and arcs are fixed, while only the bridge
helper changes.  This is precisely the listed terminal insertion geometry. ∎

Consequently a near-linear heavy bridge family rejoins PP3aoi with no loss beyond
an absolute constant.

## 6. Revised explicit-petal frontier

### Corollary PP3aow -- PROVED

After PP3aok--PP3aov, the local paid endpoints have the following exact form.

1. An `A_2` arc petal is paid after an independent completion unless its one local
   arc already costs at least its credit.
2. A `B_3` path petal is paid unless one of its at most three local `A_2/B_3`
   atoms costs at least one third of its credit.
3. A `B_4` partner petal either admits a source-clean bridge and paid independent
   completion, or produces a credit-scale `A_2`, `B_3`, or `B_4` variable-helper
   pencil, a second-generation residual pencil, or a source/external host failure.

The finite local-core table and diffuse residual collateral are no longer
independent frontiers.

### Corollary PP3aox -- PROVED

The remaining paid insertion problem is narrowed to **credit-scale local atoms**
in the three existing geometries, together with external endpoint-host failure.
It is no longer a problem of controlling a large mixed local/ambient table.

The no-three-in-line conjecture remains unproved.
