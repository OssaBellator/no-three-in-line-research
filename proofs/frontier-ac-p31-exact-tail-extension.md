# Frontier pass: exact p=31 switch-tail extension

## Active branch

`agent/ac-p31-exact-tail-extension`

Parent: `agent/ac-p31-explicit-switch-frontier` at `c00e4673c28b0cfd8c5e1508f3f671bfa1b5336e`.

Only AC remains active. Historical branches are used only as immutable source libraries.

## New theorem block

- **AC5nx:** exact barrier ten from six triples to five.
- **AC5ny:** exact barrier ten from five triples to four.
- **AC5nz:** 212-switch cumulative trajectory from the strongest p=31 AN successor to four triples.
- **AC5oa:** complete exclusion of a lower state through barrier nine at the four-triple checkpoint.
- **AC5ob:** fail-closed resumable barrier-ten traversal.

## Exact physical gains

The six-to-five segment has 26 legal switches and maximum potential ten. Its exact search processed 65,864 accepted states and discovered 75,944 states.

The five-to-four segment has 32 legal switches and maximum potential ten. Its exact search processed 182,765 accepted states and discovered 223,691 states.

Thus the physical p=31 trajectory now contains 212 switches from the 75-triple AN successor to a state with four exact remaining triple occurrences.

The complete lower components above the five-triple state have sizes `2,18,68,501` at barriers `6,7,8,9`. The complete lower components above the four-triple state have sizes `2,10,29,286,2033` at barriers `5,6,7,8,9`.

## Deterministic audit

Run:

```text
g++ -O3 -std=c++20 scripts/verify_ac_p31_exact_tail_extension.cpp -o verify_p31_tail
./verify_p31_tail
```

Expected output records:

- six-to-five switches: `26`;
- five-to-four switches: `32`;
- both exact barriers: `10`;
- total extension switches: `58`;
- cumulative switches: `212`;
- final potential: `4`.

All assertions pass in the equivalent local execution.

## Open physical frontier

The barrier-ten component above the four-triple endpoint is not yet exhausted. The committed checkpoint records 293,150 processed states, 338,944 accepted states and 45,794 queued states without a lower endpoint. This is explicitly an incomplete search and supplies no lower bound beyond barrier nine.

The next task is to finish that component or extract its first three-triple path, then continue through two, one and zero.

No pull request, merge, issue or default-branch modification was created.
