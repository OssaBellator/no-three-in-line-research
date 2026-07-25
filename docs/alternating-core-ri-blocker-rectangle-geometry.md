# Crossed-rectangle geometry of exact RI blocker profiles

**Branch:** `research/alternating-core-chain`

AC3co reduces every heavy blocker-repair term to one exact partial-permutation profile. This note translates that profile into physical geometry. Every prescribed blocker arc inserts one crossed corner of a rectangle whose diagonal anchors are blocker-occupied active cells. When the anchors are I6 cells, the crossed products satisfy exact path and cycle laws.

## Blocked active anchors

Fix one lifted active state. Its blocker-occupied desired cells are

$$
q_i=(x_i,y_i),
\qquad 1\le i\le t.
$$

They have distinct columns and rows. A blocker derangement `pi` removes the diagonal cells `q_i` from the blocker layer and inserts

$$
z_{i,\pi(i)}=(x_i,y_{\pi(i)}).
$$

A rank-`s` blocker prescription is a partial fixed-point-free injection

$$
\phi:C\to[t].
$$

## AC3cp -- crossed-rectangle realization -- PROVED

Every prescribed arc `i->j` inserts the unique cell

$$
\boxed{z_{ij}=(x_i,y_j).}
$$

Together with the two diagonal anchors

$$
q_i=(x_i,y_i),
\qquad
q_j=(x_j,y_j),
$$

it forms three corners of the exact axis-parallel rectangle with fourth corner

$$
\bar z_{ji}=(x_j,y_i).
$$

If both arcs `i->j` and `j->i` are prescribed, the two inserted cells are the opposite crossed diagonal of this rectangle and satisfy

$$
\boxed{
z_{ij}+z_{ji}=q_i+q_j
}
$$

coordinatewise.

### Proof

The derangement replacement keeps blocker column `x_i` and assigns it the freed blocker row `y_j`, giving `z_ij`. The rectangle and coordinate-sum identity are immediate. QED.

## AC3cq -- complete rank-at-most-three arc alphabet -- PROVED

Up to relabelling, a compatible blocker prescription of rank at most three has one of the following directed-graph types.

### Rank one

1. one directed arc.

### Rank two

2. two vertex-disjoint arcs (`q=0`);
3. one directed path of length two (`q=1`);
4. one directed 2-cycle (`q=2`).

### Rank three

5. three vertex-disjoint arcs (`q=0`);
6. one length-two path plus one disjoint arc (`q=1`);
7. one directed path of length three (`q=2`, no cycle);
8. one directed 2-cycle plus one disjoint arc (`q=2`, cycle);
9. one directed 3-cycle (`q=3`).

The overlap/cycle labels are exactly those in AC3ch and AC3cl.

### Proof

The partial map has indegree and outdegree at most one at every vertex and has no loops. Hence each connected component is a directed path or directed cycle of length at least two. Enumerating component-size partitions for one, two, or three arcs gives the list. QED.

## AC3cr -- I6 crossed-product path and cycle laws -- PROVED

Suppose every anchor in one prescribed path or cycle is an I6 moving cell. Write

$$
q_i=(x_i,y_i),
\qquad
x_i y_i=\lambda_i.
$$

For one crossed blocker cell define its product parameter

$$
\mu_{ij}=x_i y_j.
$$

Then

$$
\boxed{
\mu_{ij}=\lambda_j\frac{x_i}{x_j}.
}
$$

For a directed path

$$
i_0\to i_1\to\cdots\to i_k,
$$

we have the telescoping identity

$$
\boxed{
\prod_{r=0}^{k-1}\mu_{i_r i_{r+1}}
=
\left(\prod_{r=1}^{k}\lambda_{i_r}\right)
\frac{x_{i_0}}{x_{i_k}}.
}
$$

For a directed cycle

$$
i_1\to i_2\to\cdots\to i_k\to i_1,
$$

we have the exact norm law

$$
\boxed{
\prod_{r=1}^{k}\mu_{i_r i_{r+1}}
=
\prod_{r=1}^{k}\lambda_{i_r},
}
$$

where `i_{k+1}=i_1`.

In particular:

- a 2-cycle satisfies
  $$
  \boxed{\mu_{ij}\mu_{ji}=\lambda_i\lambda_j};
  $$
- a 3-cycle satisfies
  $$
  \boxed{\mu_{ij}\mu_{jk}\mu_{ki}=\lambda_i\lambda_j\lambda_k}.
  $$

### Proof

Since `y_j=lambda_j/x_j`, the one-arc identity follows. Multiply along a path; all intermediate column ratios cancel. A cycle also cancels the final endpoint ratio. QED.

## AC3cs -- anchor-kind router -- PROVED

Every blocked active anchor is of one of two physical kinds:

1. an I6 block cell in `X` with a source-target-shift channel and product parameter `lambda_i`;
2. an RI5f closure cell in `Q` with boundary-path provenance.

A rank-`s` partial prescription involves at most `2s` anchor vertices in `C union phi(C)`. Therefore there are at most

$$
\boxed{2^{2s}}
$$

anchor-kind words.

Let one exact `(t,s,q)` blocker profile have raw weight `S`. One anchor-kind word carries at least

$$
\boxed{S/2^{2s}}.
$$

- If the selected word is all-I6, every path and cycle component receives the AC3cr product law.
- Otherwise the output names a closure anchor and a crossed rectangle incident to its boundary path, entering the AC3cc--AC3cg closure-star/secant interface.

### Proof

Label each involved anchor by its two possible kinds and apply weighted pigeonhole. The two outputs follow from AC3cr and the definition of a closure anchor. QED.

## AC3ct -- exact blocker affine/profile router -- PROVED

Every blocker collateral triple using the selected prescription has:

- one of the nine arc-graph types from AC3cq;
- one anchor-kind word;
- one to three crossed cells `z_ij` determined by its anchor identities and arcs;
- zero to two unchanged blocker context cells;
- one primitive affine line direction and signed offset;
- for every all-I6 path or cycle, the exact AC3cr product identity.

For every direction threshold `gamma` and offset threshold `beta`, the raw profile returns many directions, many parallel offsets, or one heavy exact affine line. On a fixed exact anchor complex, all crossed cells are uniquely determined; thus a heavy exact line is a heavy exact crossed-cell tuple together with its fixed-context incidence.

Under the large-blocker output of AC3cn, one exact anchor-kind class has raw weight at least

$$
\boxed{
\frac{(t)_sG}{108\,2^{2s}L}.
}
$$

The exact sharp probability replaces the numerator bound by

$$
\boxed{
\frac{G}{36\,p_{t,s}^{\rm sharp}\,2^{2s}L}.
}
$$

### Proof

All structural fields are determined by the partial permutation and physical anchors. Direction/offset concentration is weighted pigeonhole. Apply AC3cs to the AC3cn raw profile bound. QED.

## Frontier after AC3cp--AC3ct

The blocker output is now an exact crossed-rectangle complex. Its probability, partial-permutation type, physical anchors, affine line, and I6 path/cycle product laws are all explicit. The remaining blocker task is to terminate one selected complex through:

- closure-star/secant payment when a closure anchor occurs;
- rational/carry classification of the all-I6 product law;
- or AC resource/no-recycling treatment of a heavy exact crossed-cell tuple.

## Finite check

`scripts/verify_ac_ri_blocker_rectangle_geometry.py` exhausts compatible rank-at-most-three partial permutations, verifies the nine graph types, rectangle identities, anchor-kind counts, and all path/cycle product laws over small finite fields.