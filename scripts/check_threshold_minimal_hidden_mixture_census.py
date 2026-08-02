#!/usr/bin/env python3
from pathlib import Path
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "check_threshold_minimal_hidden_mixture_census.cpp"

with tempfile.TemporaryDirectory() as directory:
    binary = Path(directory) / "check_threshold_minimal_hidden_mixture_census"
    subprocess.run(
        ["c++", "-O3", "-std=c++17", str(SOURCE), "-o", str(binary)],
        check=True,
    )
    result = subprocess.run(
        [str(binary)], check=True, capture_output=True, text=True
    )

assert result.stdout.splitlines() == [
    "legal_layers=18 legal_matrices=4475 face=495 pair_sums=12870",
    "minimal_equal_weight_batches=19834 support 2:5 3:210 4:2255 5:17364",
    "partitions 11111:17364 2111:2255 221:175 311:35 41:5",
]
assert result.stderr == ""

print({
    "legal_permutation_layers": 18,
    "legal_four_layer_matrices": 4475,
    "facet_matrices": 495,
    "distinct_pair_sums": 12870,
    "minimal_equal_weight_batches": 19834,
    "support_histogram": {2: 5, 3: 210, 4: 2255, 5: 17364},
    "multiplicity_partition_histogram": {
        "1+1+1+1+1": 17364,
        "2+1+1+1": 2255,
        "2+2+1": 175,
        "3+1+1": 35,
        "4+1": 5,
    },
    "status": "passed",
})
