#!/usr/bin/env python3
"""Deterministic replay audit for AC5fa--AC5fe."""
from collections import Counter
from random import Random

FAULTS = ("source_less", "split", "reuse", "hidden_deposit", "class_mismatch")
SEED = 2601
SYSTEMS = 2600
EXPECTED = {
    "systems": 2600, "initial": 19722, "events": 51343,
    "deposits": 17872, "transitions": 8020, "selected": 25165,
    "class_checks": 259579, "valid": 1163, "invalid": 1437,
}
EXPECTED_FAULTS = {
    "split": 322, "hidden_deposit": 286, "source_less": 258,
    "reuse": 265, "class_mismatch": 306,
}


def make_system(rng, sid):
    classes = rng.randint(3, 7)
    initial, events, live = [], [], {}
    nxt = 0
    for cls in range(classes):
        for _ in range(rng.randint(0, 3)):
            token = f"s{sid}_{nxt}"; nxt += 1
            initial.append((token, cls)); live[token] = cls
    for _ in range(rng.randint(4, 9)):
        for _ in range(rng.randint(0, 2)):
            token = f"s{sid}_{nxt}"; nxt += 1; cls = rng.randrange(classes)
            events.append(("deposit", token, cls, None)); live[token] = cls
        if live and rng.random() < .45:
            old = rng.choice(sorted(live)); cls = live.pop(old)
            new = f"s{sid}_{nxt}"; nxt += 1
            events.append(("transition", old, new, cls)); live[new] = cls
        for token in rng.sample(sorted(live), min(len(live), rng.randint(0, 3))):
            cls = live.pop(token); events.append(("debit", token, cls, 0))
    fault = None
    if rng.random() < .55:
        fault = rng.choice(FAULTS)
        if fault == "source_less":
            events.append(("debit", f"ghost{sid}", rng.randrange(classes), 0))
        elif fault == "split":
            token = f"s{sid}_{nxt}"; nxt += 1; cls = rng.randrange(classes)
            events.append(("deposit", token, cls, None))
            a = f"s{sid}_{nxt}"; nxt += 1; b = f"s{sid}_{nxt}"; nxt += 1
            events.extend((("transition", token, a, cls), ("transition", token, b, cls)))
        elif fault == "reuse":
            token = f"s{sid}_{nxt}"; nxt += 1; cls = rng.randrange(classes)
            events.extend((("deposit", token, cls, None), ("debit", token, cls, 0), ("debit", token, cls, 0)))
        elif fault == "hidden_deposit":
            token = f"s{sid}_{nxt}"; cls = rng.randrange(classes)
            events.extend((("hidden", token, cls, None), ("debit", token, cls, 0)))
        else:
            token = f"s{sid}_{nxt}"; cls = rng.randrange(classes)
            events.extend((("deposit", token, cls, None), ("debit", token, (cls + 1) % classes, 0)))
    return classes, initial, events, fault


def validate(classes, initial, events):
    live = dict(initial); predecessors = set(); debited = set()
    initial_count = Counter(cls for _, cls in initial); deposits = Counter(); issued = Counter()
    for event in events:
        kind = event[0]
        if kind == "deposit":
            _, token, cls, _ = event
            if token in live or token in debited: return "hidden_deposit"
            live[token] = cls; deposits[cls] += 1
        elif kind == "hidden":
            _, token, cls, _ = event; live[token] = cls
        elif kind == "transition":
            _, old, new, cls = event
            if old in predecessors: return "split"
            if old not in live: return "source_less"
            if live[old] != cls: return "class_mismatch"
            predecessors.add(old); del live[old]
            if new in live or new in debited: return "hidden_deposit"
            live[new] = cls
        else:
            _, token, cls, _ = event
            if token in debited: return "reuse"
            if token not in live: return "source_less"
            if live[token] != cls: return "class_mismatch"
            del live[token]; debited.add(token); issued[cls] += 1
        live_count = Counter(live.values())
        for cls in range(classes):
            if live_count[cls] + issued[cls] != initial_count[cls] + deposits[cls]:
                return "hidden_deposit"
    return None


def main():
    rng = Random(SEED); totals = Counter(); faults = Counter()
    for sid in range(SYSTEMS):
        classes, initial, events, injected = make_system(rng, sid)
        observed = validate(classes, initial, events)
        assert observed == injected, (sid, injected, observed)
        totals.update(systems=1, initial=len(initial), events=len(events))
        totals["deposits"] += sum(e[0] == "deposit" for e in events)
        totals["transitions"] += sum(e[0] == "transition" for e in events)
        totals["selected"] += sum(e[0] == "debit" for e in events)
        totals["class_checks"] += len(events) * classes
        totals["valid" if observed is None else "invalid"] += 1
        if observed is not None: faults[observed] += 1
    assert dict(totals) == EXPECTED
    assert dict(faults) == EXPECTED_FAULTS
    print("AC repair-source audit:", dict(totals))
    print("first failures:", dict(faults))


if __name__ == "__main__":
    main()
