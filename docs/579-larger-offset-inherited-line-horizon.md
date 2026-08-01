# Larger-offset inherited-line horizon for boundary words

`docs/573` showed that the explicit side-four/side-seven catalogue has no
five-block word when successive vertical offsets are restricted to absolute
value at most twenty-four.  This chapter enlarges the exact search radius and
uses inherited pair-line state to determine every extension.

Let a placed word carry its complete point set `X` and the normalized line set

```text
L(X)={line(p,q): p,q in X, p != q}.
```

The candidate blocks remain the four dihedral variants of the explicit blocks
`P` and `Q` from `docs/561`.

## 1. Exact inherited-line extension test

### Theorem PP3crh -- PROVED / COMPLETE PAIR-LINE STATE

Assume `X` and a translated candidate block `B` each contain no collinear
triple.  Then `X union B` contains no collinear triple if and only if both hold:

1. no point of `B` lies on a line in `L(X)`;
2. no point of `X` lies on a line determined by two points of `B`.

After a legal extension, the exact next state is obtained by adjoining the
internal lines of `B` and every cross-line through one point of `X` and one point
of `B`.

#### Proof

Any new collinear triple must contain points from both sets.  It therefore has
either two old points and one new point, covered by condition 1, or one old point
and two new points, covered by condition 2.  The update lists every pair in the
new union, so it is exact. ∎

## 2. Radius-thirty-two census

### Theorem PP3cri -- PROVED / LARGER-OFFSET PATH CENSUS

Allow every successive vertical offset in `[-32,32]`.  Starting from all eight
block/variant states, the exact counts of globally legal placed words of lengths
one through six are

```text
8, 688, 886, 376, 8, 0.
```

The eight length-five survivors use only side-four blocks.  Their two variant
words are

```text
1,1,3,1,1
3,3,1,3,3
```

and their four offset patterns are

```text
(-32,-26,12,-28), (-28,12,-26,-32),
(28,-12,26,32),   (32,26,-12,28).
```

Every survivor has twenty-eight points and exactly `780=binom(40,2)` distinct
pair lines after accounting for its five eight-point blocks.

#### Proof

The checker applies `PP3crh` to every candidate extension.  The exact extension
attempt totals at new lengths two through six are

```text
4160, 357760, 460720, 195520, 4160.
```

The stored counts and survivor descriptions are direct exhaustive outputs. ∎

## 3. Six-block obstruction at radius thirty-two

### Theorem PP3crj -- PROVED / BOUNDED LARGE-OFFSET OBSTRUCTION

None of the eight five-block survivors admits a sixth block with offset in
`[-32,32]`.  Thus enlarging the previous radius from twenty-four to thirty-two
postpones the obstruction by one block but does not produce a repeatable boundary
word.

#### Proof

For each survivor, all eight target block/variant states and all sixty-five
offsets are tested by the exact inherited-line criterion.  All `4160` attempts
fail. ∎

## 4. Exact audit

Run

```bash
python scripts/check_boundary_large_offset_horizon.py
```

The result is a bounded coordinate obstruction, not a theorem for arbitrary
offsets.  The remaining boundary alternatives are a proof controlling all large
offsets, a seam replacement/deletion catalogue, or different local blocks.
