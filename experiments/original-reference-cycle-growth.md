# Original-reference cycle-growth diagnostic

Run

```text
python scripts/check_original_reference_cycle_growth.py \
  experiments/original-reference-cycle-growth-example.json
```

The stored instance starts from the identity permutation on twelve rows. A
single-cycle seed uses rows `0,1,2,3`. Two later moves use one defect centre and
three untouched original helpers.

The exact output is:

```text
step 1: defect 0 -> 4,  cycle lengths [4]
step 2: defect 4 -> 7,  cycle lengths [7]
step 3: defect 7 -> 10, cycle lengths [10]
final cycle count          1
final defect size         10
untouched original rows    2
outcome target_scale_single_cycle_core
```

Every move has `q=4`. The seed adds four defects; each later generation adds
exactly `q-1=3`. The relative permutation always has one nontrivial cycle, so
the symmetric difference with the original layer is one alternating cycle whose
row-length grows from four to seven to ten.

The checker rejects a move if its centre is not defective after the seed, if a
helper is not an untouched original row, if the selected state is not one directed
cycle, if an original selected edge is reinserted, or if the defect/cycle formulas
fail.
