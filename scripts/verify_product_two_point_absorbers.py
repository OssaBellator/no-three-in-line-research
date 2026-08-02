#!/usr/bin/env python3
"""Compile and run the exact PX146--PX147 absorber census."""
from pathlib import Path
import subprocess
import tempfile

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'scripts'/'verify_product_two_point_absorbers.cpp'

def main():
    with tempfile.TemporaryDirectory() as directory:
        binary=Path(directory)/'verify_two_point_absorbers'
        subprocess.run(['g++','-O3','-std=c++17',str(SOURCE),'-o',str(binary)],check=True)
        subprocess.run([str(binary)],check=True)

if __name__=='__main__':
    main()
