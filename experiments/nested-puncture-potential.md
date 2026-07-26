# Nested puncture potential diagnostic

Run

```text
python scripts/check_nested_puncture_potential.py \
  experiments/nested-puncture-potential-example.json
```

The example starts with five candidate entries and three active controller points.
The first stage punctures `c0`, removes the entry controlled by `c0`, and then
moves `c0` in a trade that decreases the potential of the four-entry punctured
universe by three.  The second stage punctures and moves `c1`, leaving only the
two entries controlled by `c2` and decreasing that fixed-universe potential by
one.

The exact output is

```text
initial candidate entries 5
nested candidate entries [5, 4, 2]
nested potentials [9, 5, 2]
strict drops [4, 3]
outcome nested_puncture_paid_termination
```

The paid drops measured after puncturing are respectively

```text
8 -> 5,
3 -> 2.
```

The larger chronological drops arise because deleting candidate entries at a
puncture can only decrease the potential.  This is the finite form of
PP3apm--PP3apo: although the candidate universe changes, the nested potentials
remain directly ordered and every successful paid puncture stage makes strict
global progress.
