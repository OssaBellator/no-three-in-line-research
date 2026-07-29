# Bicliques and matchings inside Hall rectangles

`docs/424` converts a diffuse Hall obstruction into a two-sided incidence
rectangle with many sources, many high-multiplicity targets, and a lower bound
on every selected source degree.  This chapter extracts two standard repair
objects from that rectangle: a common small target core and a large matching.

## 1. Common target cores

Let `G=(S,H,E)` be a finite bipartite graph.  Put

```text
s=|S|,
t=|H|,
```

and assume every source has at least `d` neighbours in `H`.

### Theorem PP3cac -- PROVED / RECTANGLE BICLIQUE EXTRACTION

For every integer `q` with `1<=q<=d`, some `q`-element target set
`C subseteq H` is contained in the neighbourhoods of at least

```text
ceil(s binom(d,q)/binom(t,q))
```

sources.

Equivalently, the rectangle contains a complete bipartite subgraph

```text
K_(r,q)
```

with

```text
r>=ceil(s binom(d,q)/binom(t,q)).
```

#### Proof

Count pairs `(x,C)` where `x in S` and `C` is a `q`-subset of `N(x) intersect H`.
Every source contributes at least `binom(d,q)`, so there are at least
`s binom(d,q)` pairs.  There are `binom(t,q)` possible target cores.  One core
therefore occurs for at least the displayed ceiling number of sources. ∎

This is the two-sided analogue of the rooted biclique extraction in `docs/413`.

## 2. Matching extraction under bounded degrees

Write

```text
E_R=|E|.
```

Assume source degrees are at most `D` and target degrees are at most `Delta`.

### Theorem PP3cad -- PROVED / RECTANGLE MATCHING LOWER BOUND

The rectangle contains a matching of size at least

```text
ceil(E_R/(D+Delta-1)).
```

In particular, since `E_R>=sd`, it contains a matching of size at least

```text
ceil(sd/(D+Delta-1)).
```

#### Proof

Let `M` be a maximal matching of size `m`.  Every edge has at least one endpoint
covered by `M`; otherwise it could be added.  Sum the degrees of the `2m`
covered endpoints.  Each matched pair contributes at most `D+Delta`, but its
matched edge is counted twice.  Hence the number of distinct edges incident to
that pair is at most `D+Delta-1`.  Therefore

```text
E_R<=m(D+Delta-1).
```

Rearrange and take ceilings. ∎

## 3. Simultaneous rectangle output

### Corollary PP3cae -- PROVED / BICLIQUE-AND-MATCHING HALL CORE

Every Hall rectangle with parameters `(s,t,d,D,Delta)` simultaneously contains:

1. for every `q<=d`, a `q`-target common core carried by at least
   `ceil(s binom(d,q)/binom(t,q))` sources; and
2. a matching of size at least `ceil(sd/(D+Delta-1))`.

Thus a diffuse Hall obstruction supplies both a shared-core repair candidate and
an edge-disjoint bank.  A geometric construction may use whichever object has
the better collateral profile.

## 4. Finite diagnostic

The script

```bash
python scripts/check_hall_rectangle_bicliques_matchings.py
```

exhausts all four-source, five-target rectangles in which every source has
exactly two neighbours, and checks the biclique and matching bounds.

The next theorem identifier after this chapter is `PP3caf`.
