# Unary-domain composite source-star diagnostic

Run

```text
python scripts/check_unary_domain_composite_star.py \
  experiments/unary-domain-composite-star-example.json
```

The geometric state is the same no-three inserted/retained configuration used
for the unary domain-margin diagnostic.  Unary candidate entries are grouped by

```text
(inserted cell, movement/refill type, final label, macro).
```

The largest fibre is:

```text
inserted index          2
kind                    movement
label                   38
macro                    0
controller edges    10,15,30
retained partners     0,1,3
star degree              3
```

All three retained partners are distinct, verifying the source-star conclusion
of PP3aho.

For the stored finite parameters,

```text
xi R/(2s)=0.5,
```

so the fibre exceeds the pigeonhole threshold.  The marked second-step bound is

```text
E I_self
<=
3(5-2)/(100-2)
=
9/98
=
0.0918367...
```

With first-step credit `4`, first-step other cost `0.5`, and second-step foreign
cost `0.5`, PP3ahq gives

```text
composite change
<=
0.5+9/98+0.5-4
=
-2.9081632...
```

and the checker reports

```text
composite_paid_improvement.
```

The finite `R` and margin are illustrative.  The asymptotic theorem uses the
same exact cancellation with `R_1->infinity` and chooses the marked subbank
slowly enough that self-recapture is `o(R_1)`.
