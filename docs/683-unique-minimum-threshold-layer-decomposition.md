# Unique minimum threshold layer decomposition

`docs/677` gives an algebraically sharp eight-state threshold mixture. This chapter
resolves the corresponding permutation-layer decomposition exactly.

An eight-state batch contains 32 permutation layers. Its aggregate target is
`8S`, where `S` is the threshold source matrix.

## PP3ddh — Twelve illegal layers are necessary

The separating functional on one permutation layer has the following score
ranges:

```text
legal layers:   0, 1, or 2,
illegal layers: -2, -1, 1, 2, or 3.
```

The target aggregate `8S` has score `-24`. Every legal layer contributes
nonnegative score and every illegal layer contributes at least `-2`. Therefore any
32-layer decomposition of `8S` contains at least

```text
12
```

illegal layers.

The identity permutation `(0,1,2,3)` is the unique layer with score `-2`.
Consequently equality at twelve illegal layers forces all twelve illegal layers to
be identity layers and every remaining layer to be a legal score-zero layer.

## PP3ddi — The optimum decomposition is unique

After subtracting twelve identity layers from `8S`, enumerate nonnegative counts
of the nine legal score-zero permutation types. There is exactly one solution.

It uses four copies of each permutation

```text
(2,3,0,1),
(2,1,3,0),
(1,3,2,0),
(1,2,0,3),
(0,2,3,1),
```

and zero copies of the other four score-zero legal types.

Thus the minimum-illegal 32-layer decomposition is uniquely

```text
12 identity layers
+ 4 copies of each of the five exposed legal permutations.
```

This is exactly the layer refinement of the three-hidden/five-legal state mixture
in `docs/677`.

## PP3ddj — Exact geometric obstruction

Each exposed matrix in the minimal mixture has a unique four-layer decomposition:
four repeated copies of its listed legal permutation. Likewise, the hidden state
`4I_4` has the unique decomposition into four repeated identity layers.

The four identity points are collinear. Hence no regrouping or alternative
permutation-layer decomposition can remove the hidden illegality while preserving
the same 32-layer aggregate and the minimum count of twelve illegal layers.

Any geometric threshold mechanism must therefore do at least one of the following:

1. hide the twelve identity layers from exposed-state legality;
2. leave the permutation-layer model;
3. use more than 32 layers and a non-minimal hidden mass;
4. change the source aggregate.

## Verification

`scripts/check_threshold_minimal_layer_decomposition.py` enumerates all 24
permutation layers, classifies their legality and scores, proves the score lower
bound, and exhausts the integer count vectors of the nine legal score-zero layers.
It finds exactly one minimum-illegal decomposition.

## Evidence boundary

The result is a sharp algebraic and layer-level obstruction. It does not construct
a geometric hidden phase, an exposed-state-safe schedule, or an all-length
threshold recurrence.
