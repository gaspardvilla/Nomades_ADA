# Applied Data Science Course - Two Weeks Session

This repository contains all the exercises and materials required for the two-week Applied Data Science course session.

## Repository Structure

- `exercices/` - Jupyter notebooks with course exercises organized by date
- `Corrections/` - Exercise solutions and corrections
- `generators/` - Data generation modules for creating synthetic datasets
- `generator.py` - Main script to generate all required data files
- `slides_builders/` - Materials for building course slides

## Setup Instructions

### 1. Create Virtual Environment

Create a conda environment named `ada` and install the required packages:

```bash
conda create -n ada python=3.11 pip -y
conda activate ada
pip install -r requirements.txt
```

### 2. Generate Data

Before starting the exercises, you need to generate the synthetic datasets:

```bash
python generator.py
```

This will create a `data/` folder containing all the CSV files needed for the exercises.

All datasets are generated with fixed random seeds for reproducible results across the course.
