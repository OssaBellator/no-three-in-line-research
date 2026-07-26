# Terminal high-support source-pencil diagnostic

Run

```text
python scripts/check_terminal_source_pencil.py \
  experiments/terminal-source-pencil-example.json
```

The stored anchored-pair pencil has 12 variable extensions.  The fixed inserted
cell is `(0,0)`, the variable cells lie on the row `y=10`, and extension `x` uses
the retained anchor

```text
p_x=((x+1)x,10(x+1)).
```

The line through `(0,0)` and `p_x` meets `y=10` at exactly `(x,10)`.  Hence one
fixed anchor determines one variable extension.

The exact output is

```text
anchored variable extensions 12
distinct retained anchors 12
same-layer anchors 6
controller classes including free 3
exact uniform-class bank 2
theorem bank lower bound 2
first recovered extension 1
last recovered extension 12
triple variable candidates 12
triple completions [6]
outcome anchored_bank_and_unique_triple_completion
```

After alternating the anchors between the two source permutation layers, six
remain in one layer.  Splitting those six among the free class and two controller
pools leaves a uniform two-anchor endpoint bank, attaining the finite lower bound

```text
ceil(ceil(12/2)/3)=2.
```

For the inserted-triple test, the two fixed cells `(0,0)` and `(3,3)` determine the
line `y=x`.  Among 12 candidate variable columns on the fixed row `y=6`, exactly
the column `x=6` completes the collinear triple.  This is the finite
line--coordinate uniqueness used in PP3anz.
