# Unary-shadow domain-margin diagnostic

Run

```text
python scripts/check_unary_shadow_domain_margin.py \
  experiments/unary-shadow-domain-margin-example.json
```

The stored complete state has five inserted and seven retained points.  All
coordinates are row/column-disjoint and no three of the twelve points are
collinear.  Eleven movement labels and eleven refill labels are tested against
an identity controller layer split among five macros.

The exact output is:

```text
inserted state size                         5
retained state size                         7
unary incidence weight                    108
simple unary candidate entries            104
maximum witnesses for fixed inserted/candidate 1
maximum unary multiplicity of one candidate    2
binary candidate entries                   14
binary domain bound                        20
crude combined domain bound               128
maximum one-domain loss                     5
base domain size                          600
post-shadow lower bound                   595
allocation threshold                      400
outcome                 direct_unary_binary_shadow_bypass
```

The witness-uniqueness line is the finite form of PP3ahh: after one inserted
cell and one candidate entry are fixed, at most one retained point lies on their
line.  The simple unary support is slightly smaller than the incidence weight
because two different inserted cells can block the same candidate entry, but
the multiplicity is at most the inserted-state size.

The sufficient margin test is

```text
U_Xi+s(s-1)=108+20=128 <= xi R=200.
```

The exact maximum loss from one macro-label-pair domain is only five, leaving
`595>gamma R=400` values in the stored base domain.
