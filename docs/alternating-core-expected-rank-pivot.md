# Expected collateral profiles to realized pivot banks

**Branch:** `research/alternating-core-chain`

AC3gg--AC3gj orient every created certificate in a fixed realized state to one new pivot cell. Many current frontier outputs are still stated as expected rank weights over a finite legal product bank. Averaging realizes those weights before the pivot orientation, with no arithmetic or geometric loss.

## AC3gk -- expected-rank realization -- PROVED

Let `Omega` be a finite nonempty bank of legal two-layer states, equipped with any probability distribution. For one created-cell rank `r in {1,2,3}`, let

$$
X_r(\omega)\ge0
$$

be the actual total weight of distinct rank-`r` created triples in state `omega`, relative to the fixed parent configuration. Put

$$
T_r=\mathbb E_{\omega\in\Omega}X_r(\omega).
$$

Then one legal state `omega_*` satisfies

$$
\boxed{X_r(\omega_*)\ge T_r.}
$$

After fixing `omega_*`, AC3gg orients its rank-`r` family to pivot buckets of the same total weight. For every `K>=1`, AC3gi then returns either one explicit AC3fr overload or an executable pivot family with private payment at least

$$
\boxed{T_r/K.}
$$

If that pivot product does not improve, AC3gj returns one next-generation created-cell rank of expected weight at least

$$
\boxed{T_r/(3K).}
$$

### Proof

A nonnegative random variable has a value at least its expectation. AC3gg preserves the full realized certificate weight under pivot orientation. Apply AC3gi and AC3gj. QED.

The selected state retains every original line, channel, source-rank, current/new word, blocker path/cycle, closure and arithmetic decoration. Orientation adds only the chosen pivot address.

## AC3gl -- BDA suppressed-bank pivot constants -- PROVED

Let a union-safe BDA heterogeneous product destroy paid weight `D`, have fixed collateral `F`, and put

$$
G=D-F>0.
$$

Assume the BDA5ao suppressed-product criterion fails. Then one of the following three realized pivot outputs occurs.

### Balanced-floor output

If

$$
B_1\ge G/3,
$$

the deterministic cheaper-role product has actual rank-one weight exactly `B_1`. For every `K>=1`, it gives an AC3fr overload or a pivot family with payment at least

$$
\boxed{G/(3K).}
$$

Failure of the pivot product returns one next rank of weight at least

$$
\boxed{G/(9K).}
$$

### Rank-two output

If

$$
T_2\ge G/12,
$$

some legal BDA product state has actual rank-two weight at least `T_2`. It gives an overload or pivot payment at least

$$
\boxed{G/(12K),}
$$

and failed pivot comparison returns one next rank at least

$$
\boxed{G/(36K).}
$$

### Rank-three output

If

$$
T_3\ge G/24,
$$

some legal state has actual rank-three weight at least `T_3`. It gives an overload or pivot payment at least

$$
\boxed{G/(24K),}
$$

and failed pivot comparison returns one next rank at least

$$
\boxed{G/(72K).}
$$

### Proof

BDA5ao supplies the three alternatives. The balanced-floor state is the deterministic cheaper-role product. The rank-two and rank-three cases use AC3gk to realize the corresponding expectation. Apply AC3gi--AC3gj with the displayed lower bounds. QED.

## AC3gm -- scope of the expected-to-pivot adapter -- PROVED

The AC3gk adapter applies verbatim to every finite legal bank whose failed comparison returns an exact expected created-cell rank, including:

1. clean and missing-support BDA products after AC3gc--AC3gf;
2. direct and absent RI companion products after AC3fw--AC3fy;
3. coherent multiscale products after AC3fd;
4. closed-I6 active or blocker rank profiles after their current/new refinement;
5. fixed terms, by choosing any bank state in which the fixed term occurs.

It does not assign payment to a raw candidate profile before realization. Payment begins only after a legal state is fixed and the resulting triples are current certificates in that state.

### Proof

Each listed interface is a finite bank of legal states with exact expected physical certificate weights. AC3gk requires no further structure. The final sentence is the current-certificate requirement in AC3gg--AC3gh. QED.

## Consequence

The previous frontier phrase “terminate rank-two secants and rank-three all-new tuples” is now narrowed. Their local executable transition and private payment are supplied uniformly by realization plus pivot orientation. What remains is:

- termination of repeated pivot returns carrying the same retained labels;
- same-role AC2d overload recursion;
- affine-chain termination;
- global ticket/reuse bounds and the AC4 assembly.

## Finite check

`scripts/verify_ac_expected_rank_pivot.py` exhausts finite weighted banks, verifies expectation realization, the BDA5ao three-way constants and every `1/K`, `1/(3K)` composition identity.
