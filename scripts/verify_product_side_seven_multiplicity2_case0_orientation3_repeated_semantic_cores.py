#!/usr/bin/env python3
"""Verify repeated semantic cores for syntactic support mask 6975."""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

EXPECTED = {
    0:  (6936, 6936, 6936, 6, 4, 128, 40320, 7882978161453882300),
    1:  (6936, 6936, 6936, 6, 4, 128, 40320, 10389227261746506059),
    6:  (6936, 6936, 6936, 6, 4, 128, 40320, 2053789240634635346),
    7:  (6936, 6936, 6936, 6, 4, 128, 40320, 3283643103880941133),
    9:  (6920, 6920, 6920, 5, 2, 314, 20160, 16429959761875911231),
    50: (6936, 6936, 6936, 6, 4, 128, 40320, 17808303332386298926),
    51: (6936, 6936, 6936, 6, 4, 128, 40320, 4561182836759228041),
    56: (6936, 6936, 6936, 6, 2, 100, 20160, 15825782073327293270),
    57: (6936, 6936, 6936, 6, 2, 100, 20160, 5483712444602972791),
    60: (6936, 6936, 6936, 6, 4, 128, 40320, 929907610810491328),
    61: (6936, 6936, 6936, 6, 4, 128, 40320, 14471345860482743135),
    63: (6936, 6936, 6936, 6, 2, 100, 20160, 17996084423278382969),
}

FINAL = re.compile(
    r"^FINAL case=0 orientation=3 top_index=(\d+) "
    r"selector0_mask=(\d+) selector1_mask=(\d+) pair_mask=(\d+) "
    r"pair_size=(\d+) clean_extensions=(\d+) top_nodes=(\d+) "
    r"tested_bottoms=(\d+) digest=(\d+) PASS$"
)


def main() -> None:
    root = Path(__file__).resolve().parent
    source = root / (
        "measure_product_side_seven_multiplicity2_case0_orientation3_"
        "semantic_cover_core_index.cpp"
    )
    assert source.exists(), source

    observed_masks: dict[int, int] = {}
    total_extensions = 0
    total_bottoms = 0
    with tempfile.TemporaryDirectory() as temporary_directory:
        executable = Path(temporary_directory) / "semantic-core-index"
        subprocess.run(
            ["g++", "-O3", "-std=c++17", str(source), "-o", str(executable)],
            check=True,
        )
        for top_index, expected in EXPECTED.items():
            completed = subprocess.run(
                [str(executable), str(top_index)],
                check=True,
                capture_output=True,
                text=True,
            )
            final = completed.stdout.strip().splitlines()[-1]
            match = FINAL.fullmatch(final)
            assert match is not None, final
            values = tuple(int(match.group(index)) for index in range(2, 10))
            assert int(match.group(1)) == top_index
            assert values == expected, (top_index, values, expected)
            observed_masks[top_index] = values[2]
            total_extensions += values[4]
            total_bottoms += values[6]
            print(final)

    assert list(observed_masks.values()).count(6936) == 11
    assert list(observed_masks.values()).count(6920) == 1
    assert total_extensions == 40
    assert total_bottoms == 403200
    print("PX1019--PX1021 repeated semantic cover cores: PASS")


if __name__ == "__main__":
    main()
