# Two-valued transition pseudoforest regression

This experiment accompanies:

- [`docs/169-two-valued-transition-pseudoforest-states.md`](../docs/169-two-valued-transition-pseudoforest-states.md);
- [`scripts/check_two_valued_transition_pseudoforest.py`](../scripts/check_two_valued_transition_pseudoforest.py);
- [`two-valued-transition-pseudoforest-example.json`](two-valued-transition-pseudoforest-example.json).

Run

```bash
python scripts/check_two_valued_transition_pseudoforest.py \
  experiments/two-valued-transition-pseudoforest-example.json
```

## Feasible pseudoforest fixture

The first case consists of:

- one triangle component with three labelled two-choice sets;
- one three-vertex tree component with two labelled two-choice sets.

The triangle is unicyclic and has exactly two cyclic orientations. The tree has
exactly three states, indexed by its unused root. Therefore the predicted number
of injective assignments is

```text
2 * 3 = 6.
```

Exact enumeration returns six assignments.

## Minimal theta failure

The second case has four predecessor vertices and five labelled choice edges:

```text
0--1,
0--2--1,
0--3--1.
```

This is a theta graph with

```text
|E|=5,
|V|=4,
|E|-|V|=1.
```

The full five-label family is an inclusion-minimal Hall witness, and exact
enumeration returns no injective assignment.

The checker algorithm was independently reproduced and executed against the
fixture on 25 July 2026. This finite regression verifies the state counts and
Hall/pseudoforest equivalence on the examples; it does not establish the
asymptotic source or paid hypotheses of the transition conversion.
