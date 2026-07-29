# Common cores plus private markers inside Hall rectangles

`docs/430` extracts a common target core and a matching from a dense Hall
rectangle, but treats the two objects separately.  This chapter combines them:
a common core may be conditioned on while a residual matching supplies one
private marker target per selected source.

## 1. Residual edges after fixing a common core

Let `F` be a family of sources in a bipartite graph, each of degree at least
`d`.  Suppose every source in `F` is adjacent to a fixed target set `C` of size
`q`.

### Proposition PP3cau -- PROVED / COMMON-CORE RESIDUAL EDGE COUNT

After deleting the targets in `C`, the induced graph on `F` has at least

```text
|F|(d-q)
```

edges.

#### Proof

Each source loses at most the `q` core edges and therefore retains at least
`d-q` edges.  Sum over `F`. ∎

## 2. Private-marker matching

Assume source degrees are at most `D` and target degrees are at most `Delta`.

### Theorem PP3cav -- PROVED / CORE-PLUS-MATCHING EXTRACTION

The residual graph contains a matching of size at least

```text
ceil(|F|(d-q)/(D+Delta-1)).
```

#### Proof

Greedily choose a residual edge.  Removing its two endpoints deletes at most
`D+Delta-1` residual edges.  Starting from at least `|F|(d-q)` edges therefore
produces the displayed number of pairwise endpoint-disjoint edges. ∎

The matched residual target attached to a source is a private marker outside
the shared core.

## 3. Quantified hybrid extraction from a rectangle

Let a Hall rectangle have `s` sources and `t` targets, minimum source degree
`d`, maximum source degree `D`, and maximum target degree `Delta`.

### Theorem PP3caw -- PROVED / BICLIQUE WITH PRIVATE PETALS

For every `1<=q<d`, there is a `q`-target set `C` common to at least

```text
f_q=ceil(s binom(d,q)/binom(t,q))
```

sources and, among those sources after deleting `C`, a matching of size at least

```text
ceil(f_q(d-q)/(D+Delta-1)).
```

Thus the rectangle contains a family of sources sharing the same core `C` and
carrying pairwise distinct residual marker targets.

#### Proof

Double-count source--`q`-subset incidences as in `PP3cac` to obtain `C` and a
source family of size at least `f_q`.  Apply `PP3cau` and `PP3cav` to that
family. ∎

This is exactly the local form needed by marker-based recleaning: common data
may be repaired uniformly, while one residual target identifies each selected
source.

## 4. Revised Hall frontier

A diffuse Hall obstruction now contains a common conditioned core with an
edge-disjoint private-marker bank.  The remaining geometric question is whether
those residual matched targets can be converted into clean local moves without
destroying the shared core.

## 5. Exact diagnostic

Run

```bash
python scripts/check_hall_core_private_markers.py
```

The script generates ten thousand deterministic Hall rectangles, checks every
admissible core order, and verifies the residual edge and matching bounds.
