# Owner-intersecting parity-clean macro deletion

`docs/315` gives a parity-clean macro repair when the successor rotation on the
three owners of a flaw remains parity satisfiable.  That direct condition is
stronger than necessary.  To delete the old atomic flaw, it is enough to replace
one of its three owner blocks.

This chapter enlarges the macro action accordingly.  It proves a simple clean-
degree criterion, verifies it through `m=8`, and records the first pair-local
parity obstructions at `m=8`.

No asymptotic owner-intersection or seed theorem is claimed.

## 1. Any owner-intersecting rotation deletes the old flaw

### Proposition PP3blo -- PROVED

Let `(rho,e)` be a parity-clean signed Hamilton state and let `A` be a present
three-owner atomic flaw with owner set `S`.  Apply a successor rotation on any
source triple `T` satisfying

```text
T intersect S != empty.
```

Then the old atomic flaw `A` is absent after the rotation, independently of the
new orientation vector.

#### Proof

Every source in `T` receives a different successor, because the three old
successors are distinct and are cyclically permuted.  Choose `s in T intersect
S`.  The old signed orbit block owned by `s` therefore disappears.  The atomic
flaw `A` records three selected cells together with their old signed owner
assignments, including the cell supplied by the old block of `s`.  Since that
block is no longer selected, the identical atomic flaw cannot remain. ∎

The rotation need not use exactly the three owners of `A`; touching one owner is
sufficient.

## 2. A clean-degree criterion

For a parity-satisfiable Hamilton cycle `rho`, let `d_clean(rho)` be the number of
three-source successor rotations whose output cycle also has a satisfiable
parity system.

### Proposition PP3blp -- PROVED

If

```text
d_clean(rho) > C(m-3,3),
```

then for every three-element owner set `S` there is a parity-satisfiable
successor rotation whose source triple intersects `S`.

#### Proof

Exactly `C(m-3,3)` source triples are disjoint from a fixed three-set `S`.  If
more than that many rotations are parity satisfiable, they cannot all be indexed
by triples disjoint from `S`.  Hence at least one clean rotation intersects
`S`. ∎

This criterion is sufficient rather than necessary.  The exact audit also counts
owner-intersecting clean rotations directly.

## 3. Exact extension through `m=8`

### Theorem PP3blq -- VERIFIED FINITELY

For every Hamilton cycle with `4<=m<=8`, every parity system and every successor
rotation were reconstructed from exact orbit geometry.  The parity-satisfiable
induced rotation graph is connected in every case, and every inconsistent cycle
is at distance at most one from it.

| `m` | all cycles | satisfiable | minimum clean degree | `C(m-3,3)` | degree margin | minimum clean rotations intersecting any owner triple |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 6 | 6 | 4 | 0 | 4 | 4 |
| 5 | 24 | 22 | 9 | 0 | 9 | 9 |
| 6 | 120 | 112 | 16 | 1 | 15 | 15 |
| 7 | 720 | 664 | 26 | 4 | 22 | 22 |
| 8 | 5,040 | 3,542 | 27 | 10 | 17 | 19 |

Thus PP3blp applies throughout the audited range.  The exact direct transition
counts at `m=8` are

```text
satisfiable -> satisfiable     154,496,
satisfiable -> inconsistent     43,856,
inconsistent -> satisfiable     43,856,
inconsistent -> inconsistent    40,032.
```

Parity inconsistency first splits into two mechanisms at `m=8`:

```text
one owner pair forbids both XOR values      480 cycles,
nonzero-XOR signed constraint cycle       1,018 cycles.
```

The latter have shortest witness cycles

```text
length 3: 910,
length 4: 108.
```

Every pair-local obstruction occurs exactly once in its Hamilton cycle.

#### Verification

Run

```bash
python scripts/check_hamilton_owner_intersecting_parity_macro.py \
  experiments/hamilton-owner-intersecting-parity-macro-audit.json
```

The checker tests both orientation parities on every owner pair, distinguishes
pair-local impossibility from signed-cycle frustration, constructs all
`282,240` directed rotations at `m=8`, checks constraint-update locality, and
counts clean rotations intersecting every possible owner triple. ∎

## 4. Universal finite macro targetability on the parity-clean manifold

### Corollary PP3blr -- VERIFIED FINITELY / MACRO GAP CLOSED THROUGH `m=8`

For every `4<=m<=8`, every parity-clean signed Hamilton state and every present
three-owner flaw admit the following macro deletion:

1. choose a parity-satisfiable successor rotation whose source triple intersects
   the flaw's owner set;
2. apply that rotation;
3. choose a nearest satisfying orientation for the new parity system.

The output is Hamilton, pair-2-cycle-free, duplicate-orbit valid, and free of all
two-owner flaws.  The selected old three-owner flaw is deleted, and the signed
assignment support is at most

```text
3 + floor(m/2).
```

#### Proof

PP3blq supplies an owner-intersecting clean rotation.  PP3blo deletes the old
flaw.  PP3bjg preserves Hamiltonicity, while PP3bli constructs a nearest clean
orientation at Hamming distance at most `floor(m/2)`.  The three rotated sources
and the changed orientation sources give the displayed support bound. ∎

Other three-owner flaws may be created.  The result closes finite macro
**targetability**, not monotone descent or termination.

## 5. Revised parity frontier

The direct prescribed-rotation gap is no longer the right finite obstruction.
The asymptotic targets are now:

1. prove that parity-satisfiable Hamilton cycles exist for the required large
   values of `m`;
2. prove that every owner triple has at least one, preferably many, clean
   intersecting rotations;
3. classify and avoid pair-local owner pairs that forbid both XOR values;
4. control collateral three-owner flaws after owner-intersecting rotation and
   nearest parity recleaning;
5. combine the enlarged macro with a weighted causal or witness theorem.

The degree criterion `d_clean>C(m-3,3)` is useful finitely but asymptotically
strong.  A direct local theorem for rotations meeting a prescribed owner triple
would be the sharper endpoint.
