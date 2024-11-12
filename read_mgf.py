import re
from typing import List, Dict, Union
import numpy as np
import pandas as pd

def read_mgf(file: List[str]) -> List[Dict[str, Union[Dict[str, float], np.ndarray]]]:
    """
    Read and Process MGF Files
    
    This function reads MGF files and extracts the relevant MS2 spectra information.
    Duplicated peaks and noise can be optionally removed.
    
    Parameters:
    - file (list of str): List of file paths to MGF files.
    
    Returns:
    - list of dict: Processed MS2 spectra information for each MGF file, with each element containing:
        - 'info': A dictionary with 'mz' and 'rt' for the precursor ion.
        - 'spec': A numpy array with each row representing a fragment ion peak (m/z, intensity).
    """
    ms2_data = []

    for mgf_file in file:
        mgf_data = ListMGF(mgf_file)
        
        # Remove empty spectra
        non_empty_mgf_data = [entry for entry in mgf_data if any(re.match(r"^\d", line) for line in entry)]
        
        for entry in non_empty_mgf_data:
            mz = extract_value(entry, pattern="^(PEPMASS|PRECURSORMZ)")
            rt = extract_value(entry, pattern="^(RTINSECONDS|RETENTIONTIME|RTINMINUTES)")

            # Parse spectrum data
            spectrum_lines = [line for line in entry if re.match(r"^\d", line)]
            spectrum = np.array([list(map(float, line.split())) for line in spectrum_lines])
            
            # Construct info and spec dictionary
            info = {'mz': mz, 'rt': rt}
            ms2_data.append({'info': info, 'spec': spectrum})
        
    # Remove spectra with no fragment data
    ms2_data = [spec for spec in ms2_data if spec['spec'].size > 0]
    
    return ms2_data

def ListMGF(file_path: str) -> List[List[str]]:
    """
    Parse an MGF file into a list of spectra entries.
    
    Parameters:
    - file_path (str): Path to an MGF file.
    
    Returns:
    - list of lists: Each sublist represents one spectrum entry in the MGF file.
    """
    with open(file_path, 'r') as file:
        mgf_data = file.readlines()

    spectra = []
    entry = []
    for line in mgf_data:
        line = line.strip()
        if line == "END IONS":
            spectra.append(entry)
            entry = []
        else:
            entry.append(line)
    
    return spectra

def extract_value(lines: List[str], pattern: str) -> float:
    """
    Extracts a numeric value from a list of strings based on a regex pattern.
    
    Parameters:
    - lines (list of str): List of strings to search.
    - pattern (str): Regex pattern to identify the line containing the value.
    
    Returns:
    - float: The extracted numeric value.
    """
    for line in lines:
        match = re.search(pattern, line)
        if match:
            value = re.sub(r"[^\d.]", "", line.split('=')[-1]).strip()
            return float(value)
    return 0.0
