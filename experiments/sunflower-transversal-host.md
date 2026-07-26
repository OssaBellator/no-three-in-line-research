# Sunflower-transversal single-cycle host diagnostic

Run

```text
python scripts/check_sunflower_transversal_host.py \
  experiments/sunflower-transversal-host-example.json
```

The stored transversal system uses

```text
H=6,
b=4,
empty-core petal size=2,
nested fixed-core size=2,
nested petal size=1.
```

There are exactly

```text
binom(6,3) 2^3 = 160
```

transversal helper blocks.  The exact output is

```text
H 6
b 4
empty-core petal size 2
transversal blocks 160
one-helper probability 0.250000000000
one-helper formula 1/4
two-distinct-petal probability 0.050000000000
same-petal pair probability 0.000000000000
prescribed-arc probability 0.016666666667
maximum selected vertices from one petal 1
nested core size 2
nested petal size 1
nested fixed core selected 0
target signatures selected 0
outcome sunflower_transversal_single_cycle_host
```

The one-helper and two-helper probabilities agree with

```text
(b-1)/(H|P|)=1/4
```

and

```text
(b-1)_2/((H)_2 |P|^2)=1/20.
```

Conditional on selecting two helpers in distinct petals, the prescribed directed
arc occurs with single-cycle probability `1/(b-1)=1/3`, giving the joint value
`1/60`.

The empty-core block meets every two-point petal in at most one helper, so no
empty-core signature is selected.  In the nested-pencil example the entire fixed
core is omitted, so singleton petals also cause no target signature.
