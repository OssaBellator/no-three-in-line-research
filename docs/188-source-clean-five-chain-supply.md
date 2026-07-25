# Dense source-clean five-chain supply or transition-petal failure

The fixed-centre local-credit theorem PP3aeb--PP3aeg uses a dense family of
source-clean five-index chains through the captive centre. The transition
localization PP3zj--PP3zv already contains the ingredients needed to guarantee
such a family quantitatively.

At an intermediate safe-choice threshold `q`, either both outer roles have at
least `q` choices on at least `q` middle indices, in which case the sparse
middle relation leaves a large Cartesian family of clean chains, or one outer
role is almost completely forbidden outside fewer than `q` exceptional
middles. Choosing `q=N/log N` gives `N^(4-o(1))` clean chains in the first
case. The second case is precisely the near-complete transition role-star
feeding the disjoint-petal and credited-bank chain PP3zw--PP3aaj.

Thus failure of dense source-clean chain supply is not an additional marked-Xi
frontier.

## 1. Thresholded outer-choice sets

Let `V` be a controller pool of size `N`, fix `c in V`, and retain the
transition relations

```text
L_c={(r,p): r->p->c is source-invalid},
M_c={(p,s): p->c->s is source-invalid},
F_c={(s,t): c->s->t is source-invalid}.
```

For `p,s!=c`, put

```text
A_L(p)={r notin {p,c}: (r,p) notin L_c},
A_F(s)={t notin {s,c}: (s,t) notin F_c}.
```

For an integer `q>=3`, define

```text
P_q={p!=c: |A_L(p)|>=q},
S_q={s!=c: |A_F(s)|>=q}.
```

Let `C_c` be the family of ordered four-tuples `(r,p,s,t)` for which all five
indices in

```text
r -> p -> c -> s -> t
```

are distinct and all three adjacent two-arc paths are source-valid.

### Proposition PP3aeh -- PROVED

For every `q>=3`,

```text
|C_c|
>=
(|P_q||S_q|-|M_c|-N)_+ (q-1)(q-2).
```

#### Proof

There are at least `|P_q||S_q|-|M_c|-N` ordered pairs `(p,s)` with `p!=s`
and `(p,s) notin M_c`. Fix one such pair. Choose
`r in A_L(p)` avoiding `s`; at least `q-1` choices remain. For each chosen
`r`, choose `t in A_F(s)` avoiding `p` and `r`; at least `q-2` choices
remain. Every resulting chain is source-clean. Different ordered choices give
different chains. ∎

## 2. Exact clean-bank or role-star dichotomy

### Theorem PP3aei -- PROVED

For every integer `q>=3`, at least one of the following holds.

1. **Clean five-chain bank:**

   ```text
   |C_c|
   >=
   (q^2-|M_c|-N)_+ (q-1)(q-2).
   ```

2. **Predecessor role-star:**

   ```text
   |P_q|<q,
   ```

   and for every `p outside P_q`,

   ```text
   |{r:(r,p) in L_c}| >= N-q-1.
   ```

   Thus all but fewer than `q` middle indices have a forbidden predecessor
   degree at least `N-q-1`.

3. **Successor role-star:** the transposed statement holds:

   ```text
   |S_q|<q
   ```

   and every `s outside S_q` has at least `N-q-1` forbidden successors.

4. **Middle saturation:**

   ```text
   |M_c|+N >= q^2.
   ```

#### Proof

If either `|P_q|<q` or `|S_q|<q`, use the definition of the corresponding
threshold set. Outside `P_q`, at most `q-1` of the `N-2` possible predecessors
are safe, so at least `N-q-1` are forbidden; the successor case is identical.

Otherwise both threshold sets have size at least `q`. Proposition PP3aeh gives
alternative 1 unless its positive factor vanishes, in which case
`|M_c|+N>=q^2`. ∎

The fourth alternative is displayed because it is the only possible reason
that two large outer-choice sets fail to yield a clean Cartesian core.

## 3. Slab-optimal dense supply

Use the slab-optimal pool scale

```text
N=m^(19/20+o(1))
```

and the middle divisor bound

```text
|M_c|<=2mD_m+2N=m^(1+o(1)).
```

Choose

```text
q=ceil(N/log N).
```

### Corollary PP3aej -- PROVED

For all sufficiently large `m`, middle saturation in PP3aei is impossible.
Consequently at least one of the following holds.

1. There are

   ```text
   |C_c| >= N^4/(3 log^4 N)=N^(4-o(1))
   ```

   source-clean ordered five-index chains through `c`.

2. All but `o(N)` middle indices belong to a predecessor-role forbidden star
   of degree `(1-o(1))N`.

3. All but `o(N)` middle indices belong to the transposed successor-role
   forbidden star.

#### Proof

One has

```text
q^2=N^2/log^2 N,
```

whereas `|M_c|+N=m^(1+o(1))=o(N^2/log^2 N)`. Hence the middle-saturation
alternative is impossible. In the clean-bank branch, PP3aeh gives

```text
(q^2-|M_c|-N)(q-1)(q-2)
=
(1-o(1))q^4
>= N^4/(3log^4 N).
```

In either star branch, `q=o(N)` and the degree lower bound `N-q-1` is
`(1-o(1))N`. ∎

## 4. Handoff to the existing transition conversion

### Corollary PP3aek -- PROVED

Each role-star alternative in PP3aej feeds the existing transition chain:

```text
near-complete role star
-> disjoint witness-petal bank        (PP3zw--PP3zz)
-> free or one-pool credited bank     (PP3aaa--PP3aae)
-> diffuse-collateral averaging       (PP3aaf--PP3aaj).
```

In particular, each star alternative supplies a target-size `W` endpoint or
petal bank unless one of the already-listed source, endpoint-host, or
bank-credit cores occurs.

#### Proof

The star degrees and number of affected middles in PP3aej are at least the
near-complete hypotheses used by PP3zw--PP3aaj. Apply those theorem chains. ∎

## 5. Consequence for local-credit splitting

### Corollary PP3ael -- PROVED

At a source-light captive centre, the deterministic local-credit theorem
PP3aeb--PP3aeg may be invoked without separately assuming dense source-clean
five-chain supply. Either:

1. `C_c` has size `N^(4-o(1))`, so PP3aee splits expensive local cost into
   `Omega(N)`, `Omega(N^2)`, or `Omega(N^3)` heavy fixed-centre objects; or
2. a predecessor/successor transition role-star returns to the credited
   transition-petal conversion PP3zw--PP3aaj.

Therefore failure of dense source-clean chain supply is no longer an
independent marked-centre frontier.

## 6. Revised marked-centre endpoint

### Corollary PP3aem -- PROVED

The marked-centre branch now reduces to:

1. an exact paid five-chain completion through PP3ady;
2. a heavy unary arc-petal, rank-three path/grid, or rank-four partner family;
3. a credited transition-petal/resource bank;
4. residual source or off-centre insertion concentration;
5. one of the already-listed weighted-grid, conditional-Hall,
   alternating-host, or endpoint-host failures.

Neither an opaque centre-core term, deterministic local-credit table, nor
failure of dense clean-chain supply remains a separate case.

## 7. Finite diagnostic

The script

```text
scripts/check_source_clean_five_chain_supply.py
```

enumerates thresholded outer-choice sets and all source-clean ordered
five-chains. It verifies the lower bound in PP3aeh and reports the clean-bank,
predecessor-star, successor-star, or middle-saturation branch.
