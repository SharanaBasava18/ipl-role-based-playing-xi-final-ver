import pandas as pd
import numpy as np
from pathlib import Path

# Base directory (project root)
BASE_DIR = Path(__file__).resolve().parent

# Data directories
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
YAML_DIR = RAW_DIR / "yaml"
PROCESSED_DIR = DATA_DIR / "processed"

# Outputs
OUTPUTS_DIR = BASE_DIR / "outputs"

# Ensure required directories exist
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

# Phase boundaries (0-indexed overs)
POWERPLAY_END_OVER = 5
MIDDLE_END_OVER = 14