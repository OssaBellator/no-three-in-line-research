# Side-six minimax repair choice profile

The canonical side-six repair graph has 546 states, two solutions, and a previously verified minimax path profile. This chapter measures how many next moves preserve each state's optimal defect barrier and reduce the remaining optimal path length by one.

## PX1114 — exact optimal-choice histogram

Across all 546 states, the number of minimax-optimal next moves has distribution

`{0:2, 1:102, 2:19, 3:14, 4:18, 5:17, 6:32, 7:25, 8:43, 9:22, 10:24, 11:34, 12:33, 13:32, 14:16, 15:11, 16:23, 17:20, 18:13, 19:12, 20:8, 21:11, 22:5, 23:4, 24:1, 25:2, 34:1, 35:2}`.

The two zero-choice states are exactly the two solutions.

## PX1115 — forced and high-choice states

Among the 544 nonsolutions:

- 102 states have a unique minimax-optimal first move;
- every nonsolution has at least one such move;
- the maximum number of optimal first moves is 35;
- the total number of optimal first-move choices is 5,004.

Thus the finite graph has substantial aggregate choice reserve, but it also contains many locally forced states.

## PX1116 — uphill states are not forced

The ten states whose minimum solution barrier exceeds their current defect have optimal-choice distribution

`{3:2, 6:2, 7:4, 8:2}`.

Therefore every bounded-uphill trap has at least three minimax-optimal exits. The need to increase defect does not coincide with first-move rigidity in this graph.

## PX1117 — strengthened global repair target

A global bounded-barrier theorem should exploit a reserve of locally optimal choices while controlling collisions between fibres. The finite model shows that one cannot assume a uniform branching lower bound over all nonsolutions, because 102 states are forced, but the exceptional uphill states themselves retain multiple valid exits.

## Verification

```bash
python scripts/verify_product_side_six_repair_choice_profile.py
```
