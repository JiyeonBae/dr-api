# Dimensionality Reduction API

This project provides various dimensionality reduction techniques using a Python-based API. The Conda environment file (`dr_api.yml`) ensures consistent and reproducible dependencies.


## Features
- **Supports 40 DR techniques**: Includes popular methods like PCA, t-SNE, UMAP, and techniques using Tapkee and drtoolbox.
- **Seamless integration**: Combines Python-based, WSL-based, and Octave-based DR methods.

## Requirements
- **Conda Environment**: The project runs in a Conda virtual environment named `dr_api`.
- **Dependencies**:
  - Octave 4.4.1
  - Python libraries (e.g., `umap-learn`, `scikit-learn`, `tensorflow`)
  - WSL (for Tapkee execution)

## Development and Testing Environment
This project was developed and tested in the following environment:
- **Operating System:** Windows 10
- **Python Version:** 3.10.13
- **Conda Version:** conda 24.11.0
- **WSL Version:** WSL2
- **Octave Version:** 4.4.1
  
## Setting up the Conda Environment

### Step 1: Clone the Repository
1. Clone the repository:
   ```bash
   git clone https://github.com/JiyeonBae/dr-api.git
   ```

### Step 2: Create and Activate the Environment
- Create the Conda environment using the provided YAML file and activate the newly created environment:
   ```bash
   conda env create -f dr_api.yml
   conda activate dr_api
   ```
- This will create a Conda environment and automatically install all the required libraries and dependencies specified in the `dr_api.yml` file. The YAML file contains a list of necessary packages, their versions, and the channels to install from. Once the environment is activated, you'll have access to all the required libraries for the project.

### Step 3: Install WSL for Using Tapkee Prebuilt Files
Run the following command to install Windows Subsystem for Linux (WSL)
   ```bash
  wsl --install
   ```
### Step 4: Install Octave 4.4.1
- Download and install from: https://ftp.gnu.org/gnu/octave/windows/

### Step 5: Configure Octave Path
1. Open the file `_drtoolbox.py`.
2. Locate the following line in the file and replace the path with the location of your Octave installation directory.:
   ```python
   octave_path = "C:/Octave/Octave-4.4.1/bin/octave.bat"
3. Configure the CFLAGS Environment Variable
  Ensure that the CFLAGS environment variable points to the Octave include directory. This is required to compile and execute code that uses Octave header files.  
  For example:
    ```bash
    CFLAGS=-I/C:/Octave/Octave-4.4.1/include/octave-4.4.1/octave
    ```
## Hyperparameters and Configuration

The hyperparameters required for each Dimensionality Reduction technique are stored in the `_metadata.json` file. This file includes:

- **Recommended Ranges**: Suggested ranges for each hyperparameter that can be adjusted during hyperparameter tuning to optimize model performance, depending on the dataset.
- **Default Values**: Predefined settings that are typically used for optimal performance.

For example, the `n_neighbors` hyperparameter for UMAP has a default value of 15, with a recommended range of 2 to 100. Users can adjust these values based on the dataset and specific needs.


## Usage Example
After setting up the environment, you can use the core functions from the `dr.py` file as follows:
```python
from dr import *

# Generate a random dataset with 100 samples and 5 features
X = np.random.rand(100, 5)

# Testing the UMAP function
umap_result = run_umap(X, n_neighbors=5, min_dist=0.1, init="random")
print("UMAP Result:", umap_result)

# Testing the PaCMAP function
pacmap_result = run_pacmap(X, n_neighbors=5, MN_ratio=0.5, FP_ratio=0.5, init="random")
print("\nPaCMAP Result:", pacmap_result)

# The results will be the data with shape (100, 2).
```


## Acknowledgments

This project was inspired by and incorporates code and ideas from the following repositories:

**1. Dimensionality Reduction techniques:** https://github.com/hj-n/umato_exp/blob/master/_final_exp/_dr_provider.py  
**2. Dimensionality Reduction techniques, including Tapkee build files and drtoolbox:** https://github.com/mespadoto/proj-quant-eval/blob/master/code/01_data_collection/projections.py

These repositories provided foundational code for various Dimensionality Reduction techniques, which were adapted and integrated into this project for ease of use and efficiency.

