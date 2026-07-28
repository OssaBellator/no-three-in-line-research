# Inverse compatible-source envelope for complete `m=10` Hall transport

The complete exact `m=10` transport audit in `docs/366` assigns every supported
signed flaw `f` an optimal weighted-Hall charge `gamma(f)`.  Let

```text
s(f) = number of compatible clean source cycles of f.
```

This chapter normalizes the exact charge by that source support.

The result is finite.  It does not prove an inverse-support estimate at general
`m`, nor a general lower bound on `s(f)`.

## 1. Complete support-normalized census

### Theorem PP3bsz -- VERIFIED FINITELY / SUPPORT-NORMALIZED MAXIMUM

Across all `47,512` supported signed `m=10` flaws,

```text
sup_f s(f) gamma(f)
 = 3152400/791819
 = 3.981212878196... .
```

The maximum is attained in the exact source-count `600` ledger, whose worst
charge is

```text
gamma = 5254/791819.
```

Consequently the exact margin below four is

```text
4 - sup_f s(f) gamma(f)
 = 14876/791819
 > 0.
```

#### Verification

The aggregate verifier reads every completed ledger row.  For a source-count
band `[l,h]` with band maximum `Gamma`, it checks the conservative endpoint
product `h Gamma`; for an exact-count row this is the exact support-normalized
maximum at that count.  The 183 nonempty rows cover all 47,512 flaws, and every
endpoint product is below four.  The largest endpoint product is the exact
600-source row displayed above. ∎

The support-normalized maximizer differs from the global charge maximizer.  The
latter occurs at source count `550` and has

```text
550 * 2397/349898
 = 659175/174949
 = 3.767812333880... .
```

Thus maximizing `gamma(f)` and maximizing `s(f) gamma(f)` are genuinely
different finite problems.

## 2. Inverse-source charge envelope

### Corollary PP3bta -- PROVED / VERIFIED FINITELY / FOUR-OVER-SUPPORT

Every supported signed `m=10` flaw satisfies

```text
gamma(f) < 4/s(f).
```

#### Proof

If `f` belongs to an audited band `[l,h]`, then `s(f) <= h` and
`gamma(f) <= Gamma`, where `Gamma` is the exact maximum recorded for that band.
The verifier proves `h Gamma < 4`.  Hence

```text
s(f) gamma(f) <= h Gamma < 4.
```

The exact-count rows are the special case `l=h`. ∎

This converts the finite weighted-expansion problem into a source-support
quantity.  In particular, any future general theorem giving both

```text
gamma(f) <= 4/s(f)
and
s(f) >= c m^3
```

would immediately imply

```text
gamma(f) <= (4/c) m^-3.
```

Neither premise is proved asymptotically here.  The new finite ledger instead
identifies inverse compatible-source support as a concrete structural route to
the observed cubic charge scale.

Verify with

```bash
python scripts/verify_m10_hall_inverse_source_support.py .
```

The next theorem identifier after this chapter is `PP3btb`.
