# Complementary-degree global allocation regression

This experiment accompanies
[`docs/78-ore-balanced-global-allocation.md`](../docs/78-ore-balanced-global-allocation.md).

Run

```bash
python scripts/check_global_label_ore.py \
  experiments/global-label-ore-example.json
```

The fixture has `T=4`, `M=2`, and balanced ownership

```text
0,0,1,1.
```

The resulting global compatibility graph is

\[
 K_{1,1}\mathbin{\dot\cup}K_{3,3}.
\]

Its left and right degree sequences are both

```text
1,3,3,3.
```

Therefore the old PP3fx minimum-degree requirement fails:

\[
 \delta(G)=1<T/2=2.
\]

However, every nonedge joins a degree-one vertex to a degree-three vertex, so

\[
 d(a)+d(b)=4=T.
\]

PP3gj--PP3gk certify a perfect matching, and the exact augmenting-path checker
returns matching size four.

The fixture demonstrates the intended gain of complementary degrees.  A small
exceptional movement-label shadow may be paired with a refill label that is
compatible with almost every other movement label, and vice versa.  Separate
`T/2` lower bounds would charge both exceptions even though they do not form a
Hall obstruction together.

The random balanced theorem PP3gl is asymptotic and is not expected to certify
this four-label fixture with `h=0`: its union-bound term equals four.  The fixed
ownership theorem PP3gk is the exact finite endpoint.
