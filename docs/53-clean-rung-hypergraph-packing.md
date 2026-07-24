# Clean-rung hypergraph packing

A matching block may have many locally clean four-edge states, but several
width-two rungs require those states to use disjoint source edges.  This chapter
records the exact hypergraph packing interface and a degree-based sufficient
condition.

## 1. The clean-state hypergraph

Let `E` be an `r`-edge perfect-matching block.  Define the 4-uniform hypergraph

\[
 \mathcal H_E
 =
 \{D\in\tbinom E4:(E\setminus D)\cup Q(D)
   \text{ is no-three-in-line}\}.
\]

Thus the vertices are source matching edges and the hyperedges are the locally
clean canonical width-two states from PP3bz.

A matching of size `K` in `H_E` gives `K` pairwise edge-disjoint reservoirs.
Assigning disjoint two-coordinate new intervals to them produces `K` local
rungs with disjoint variable supports.  Their individual interactions with the
retained block are clean; only patch-patch and external-other-layer geometry
remain.

## 2. Greedy packing from clean-state degree

Let

\[
 h=|\mathcal H_E|,
 \qquad
 \Delta=\max_{e\in E}\deg_{\mathcal H_E}(e).
\]

### Proposition PP3cc -- PROVED

The clean-state hypergraph contains a matching of size at least

\[
 \boxed{
 \left\lceil\frac{h}{4\Delta}\right\rceil
 }
\]

when `h>0`.  In particular, `h>4(K-1)\Delta` guarantees `K` disjoint clean
width-two reservoirs.

#### Proof

Choose a clean hyperedge, delete it and every clean hyperedge meeting it, and
repeat.  One chosen four-edge state meets at most `4 Delta` hyperedges, counting
itself, because each of its four vertices lies in at most `Delta` hyperedges.
Therefore fewer than `4 Delta` clean states are removed per selected state.
Starting from `h` states yields at least `ceil(h/(4 Delta))` selections. ∎

The same ratio controls deletion spread.  If a clean state is sampled uniformly,
then every source edge has deletion probability at most `Delta/h`.

### Corollary PP3cd -- PROVED

If

\[
 \frac{\Delta}{h}\le\rho,
\]

then the uniform clean-state distribution has source-edge deletion marginal at
most `rho`, and `H_E` contains a matching of size at least `1/(4rho)`.

Thus a diffuse clean domain simultaneously supplies local-state spread and a
large disjoint rung packing.

## 3. Concentration alternatives

The degree endpoint can fail even when `h` is moderately large.  A useful exact
diagnostic is the transversal number

\[
 \tau(\mathcal H_E)
 =
 \min\{|Z|:Z\subseteq E,\ D\cap Z\ne\varnothing
 \text{ for every }D\in\mathcal H_E\}.
\]

A small transversal means every clean state is forced to delete one of a few
source edges.  Such a core is precisely where protected trades or cycle choices
should be installed: repairing or making those edges optional can potentially
release many states at once.

### Proposition PP3ce -- PROVED

If the matching number of `H_E` is less than `K`, then the union of a maximum
matching is a transversal of size at most `4(K-1)`.

#### Proof

Let `M` be a maximum matching with fewer than `K` hyperedges.  Any clean
hyperedge disjoint from the union of `M` could be added to `M`, contradicting
maximality.  Hence the union meets every clean hyperedge and has at most
`4(K-1)` vertices. ∎

Failure to pack many clean rungs therefore forces a small source-edge core that
hits every clean canonical state.

## 4. Stored-certificate classification

The script

```bash
python scripts/analyze_clean_rung_hypergraph.py \
  certificates/prime-patching-small.json
```

constructs `H_E` for both perfect matching layers, computes exact maximum
matching and minimum transversal numbers by bitmask dynamic programming, and
reports vertex degrees.

For every stored layer from side four through ten, the maximum matching size is
exactly one.  Up to side nine, the clean-state hypergraph has transversal number
one: one source edge lies in every locally clean state.  At side ten the minimum
transversal size is two for both layers.

This is a stronger finite obstruction than the falling clean fraction alone.
The stored clean domains are not merely small; they are pinned to a tiny edge
core and cannot supply two disjoint canonical rungs.

## 5. Revised asymptotic target

A useful prepared matching block should satisfy at least one of:

1. `h/Delta` grows polynomially, giving many disjoint clean rungs by PP3cc;
2. a small transversal is exposed and neutralized by protected local trades;
3. the state family is enlarged beyond canonical adjacent patches so that the
   clean hypergraph loses its concentrated core;
4. multiple matching layers or incidence-cycle flips produce clean states on
   disjoint endpoint sets.

For a total extension width `T`, the constant-width architecture needs
`K=T/2` clean rungs.  The exact combinatorial target is now

\[
 \nu(\mathcal H_E)\ge T/2,
\]

or a multistate replacement whose bad-box distribution provides the same amount
of effective local entropy.