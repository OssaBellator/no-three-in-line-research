#!/usr/bin/env python3
from pathlib import Path
import subprocess
import tempfile

SOURCE = Path(__file__).with_suffix('.cpp')
with tempfile.TemporaryDirectory() as directory:
    binary = Path(directory) / 'check_boundary_eighth_corrected_transition'
    subprocess.run(['c++', '-O3', '-std=c++17', str(SOURCE), '-o', str(binary)], check=True)
    subprocess.run([str(binary)], check=True)
