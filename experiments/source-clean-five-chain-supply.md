# Source-clean five-chain supply diagnostic

This check accompanies
`docs/188-source-clean-five-chain-supply.md`.

Run:

```bash
python scripts/check_source_clean_five_chain_supply.py \
  experiments/source-clean-five-chain-supply-example.json
```

The stored instance has eight endpoint indices, captive centre `0`, threshold
`q=3`, and no forbidden predecessor, middle, or successor transitions. Hence

```text
|P_q|=|S_q|=7
```

and all

```text
7*6*5*4=840
```

ordered five-chains through the centre are source-clean. The theorem's
conservative finite lower bound is

```text
(7*7-8)(3-1)(3-2)=82.
```

The checker verifies the bound and returns `clean_five_chain_bank`.

To exercise the predecessor-star branch, for every middle `p` retain at most two
safe predecessors and list all remaining `(r,p)` pairs in `forbidden_left`.
The successor branch is transposed. Making every distinct middle pair forbidden
while leaving both outer relations complete exercises `middle_saturation`.

The finite diagnostic verifies exact counting and the theorem branches. It does
not execute the later transition-petal or paid-completion conversions.
