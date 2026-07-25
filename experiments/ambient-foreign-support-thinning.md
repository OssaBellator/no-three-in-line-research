# Ambient foreign-support thinning diagnostic

This check accompanies
`docs/195-adaptive-ambient-foreign-support-thinning.md`.

Run:

```bash
python scripts/check_ambient_foreign_support_thinning.py \
  experiments/ambient-foreign-support-thinning-example.json
```

The stored bank has `Q=8`, subbank size `q=4`, one unary support, and one
binary support of each endpoint-index rank two, three, and four.

For every endpoint index and every support rank, the checker averages the
selected degree over all four-subbanks containing that index.  It verifies the
exact factors

```text
(q-1)/(Q-1),
(q-1)_2/(Q-1)_2,
(q-1)_3/(Q-1)_3.
```

It then enumerates all four-subbanks and reports the one minimizing

```text
max unary degree/q
+
max binary degree/(q(q-1)).
```

The stored sparse instance has a support-free subbank and therefore returns
`diffuse_support_subbank`.

Duplicating rank-three supports across a positive fraction of all triples, or
rank-four supports across a positive fraction of all quadruples incident with
one endpoint, exercises the finite support-core branch.
