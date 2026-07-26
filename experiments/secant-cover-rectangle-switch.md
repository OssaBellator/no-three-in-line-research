# Secant-cover rectangle-switch diagnostic

Run

```text
python scripts/check_secant_cover_rectangle_switch.py \
  experiments/secant-cover-rectangle-switch-example.json
```

The stored tentative template has five internally no-three cells with distinct row and
column resources.  Its secants cover every cell of the disjoint `3 x 3` endpoint
rectangle.

Assigning one witnessing template pair to every covered cell gives template-resource
degrees

```text
[5, 5, 3, 3, 2].
```

Thus the finite cover enters the fixed-centre branch of PP3ayq.  The centre `(4,4)`
and partner `(-1,-1)` witness the covered endpoint cell `(0,0)`.

The diagonal state

```text
{(4,4),(0,0)}
```

is replaced by the cross state

```text
{(4,0),(0,4)}.
```

Both states use columns `{0,4}` and rows `{0,4}` exactly once.  The cross state omits
both points belonging to the designated triple.

The expected output is

```text
endpoint side 3
template size 5
covered endpoint cells 9
template resource degrees [5, 5, 3, 3, 2]
fixed centre [4, 4]
fixed-centre degree 5
pivot covered cell [0, 0]
pivot partner [-1, -1]
state-zero diagonal [[4, 4], [0, 0]]
state-one cross diagonal [[4, 0], [0, 4]]
same column resources True
same row resources True
target triple omitted True
outcome secant_cover_rectangle_switch
```

This verifies the witnessed-cover extraction and the exact degree-preserving
cross-orientation identity in PP3ayp--PP3azb.
