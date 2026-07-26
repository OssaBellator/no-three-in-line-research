# Paired secant block-preservation diagnostic

Run

```text
python scripts/check_paired_secant_block_preservation.py \
  experiments/paired-secant-block-preservation-example.json
```

The finite model has two permanent matching blocks.  The tentative block uses

```text
{(1,1),(2,2)}
```

and the witness block uses

```text
{(5,5),(6,6)}.
```

Each block is crossed internally.  The four product states preserve the row and column
margins of both blocks separately.  The all-cross state is

```text
{(1,2),(2,1),(5,6),(6,5)},
```

so it omits all four designated diagonal pivots and therefore clears both assigned
secant certificates.

The expected output is

```text
tentative block margins [[1, 2], [1, 2]]
witness block margins [[5, 6], [5, 6]]
four product states 4
all-cross state [[1, 2], [2, 1], [5, 6], [6, 5]]
designated pivots omitted 4
permanent blocks preserved True
outcome paired_secant_block_preservation
```

This verifies the finite block-preservation identity in PP3azk and the preferred
all-cross state used by PP3azm--PP3azr.
