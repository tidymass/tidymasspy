import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from typing import Optional, Tuple

def ms2_plot(
    spectrum1: pd.DataFrame,
    spectrum2: Optional[pd.DataFrame] = None,
    spectrum1_name: str = "spectrum1",
    spectrum2_name: str = "spectrum2",
    range_mz: Optional[Tuple[float, float]] = None,
    ppm_tol: float = 30,
    mz_ppm_thr: float = 400,
    xlab: str = "Mass to charge ratio (m/z)",
    ylab: str = "Relative intensity",
    col1: str = "red",
    col2: str = "black",
    title_size: int = 15,
    lab_size: int = 15,
    axis_text_size: int = 15,
    legend_title_size: int = 15,
    legend_text_size: int = 15,
    interactive_plot: bool = False
):
    """
    Plot MS2 Spectra Comparisons

    Parameters:
    - spectrum1 (pd.DataFrame): First MS2 spectrum.
    - spectrum2 (Optional[pd.DataFrame]): Second MS2 spectrum.
    - spectrum1_name (str): Label for the first spectrum. Default "spectrum1".
    - spectrum2_name (str): Label for the second spectrum. Default "spectrum2".
    - range_mz (Optional[Tuple[float, float]]): Range of m/z values.
    - interactive_plot (bool): Use plotly for an interactive plot.

    Example usage:
    ```python
    spectrum1 = pd.DataFrame({
        "mz": [87.5, 94.8, 97.1, 97.2, 103.3],
        "intensity": [8356.3, 7654.1, 9456.2, 8837.1, 8560.2]
    })
    spectrum2 = pd.DataFrame({
        "mz": [87.5, 94.8, 97.1, 97.2, 103.3],
        "intensity": [7356.3, 6654.1, 8456.2, 7837.1, 7560.2]
    })
    ms2_plot(spectrum1, spectrum2, interactive_plot=False)
    ```
    """
    # Normalize intensities
    spectrum1["intensity"] /= spectrum1["intensity"].max()
    if spectrum2 is not None:
        spectrum2["intensity"] /= spectrum2["intensity"].max()
    
    # Define m/z range if not provided
    if range_mz is None:
        min_mz = min(spectrum1["mz"].min(), spectrum2["mz"].min()) if spectrum2 is not None else spectrum1["mz"].min()
        max_mz = max(spectrum1["mz"].max(), spectrum2["mz"].max()) if spectrum2 is not None else spectrum1["mz"].max()
        range_mz = (min_mz, max_mz)

    # Plotting
    if interactive_plot:
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=spectrum1["mz"], y=spectrum1["intensity"], mode="lines+markers",
            name=spectrum1_name, line=dict(color=col1)
        ))
        if spectrum2 is not None:
            fig.add_trace(go.Scatter(
                x=spectrum2["mz"], y=-spectrum2["intensity"], mode="lines+markers",
                name=spectrum2_name, line=dict(color=col2)
            ))
        fig.update_layout(
            title="MS2 Spectra Comparison",
            xaxis_title=xlab,
            yaxis_title=ylab,
            xaxis_range=range_mz,
        )
        fig.show()
    else:
        plt.figure(figsize=(10, 6))
        plt.stem(spectrum1["mz"], spectrum1["intensity"], linefmt=col1, markerfmt=" ", basefmt=" ", label=spectrum1_name)
        if spectrum2 is not None:
            plt.stem(spectrum2["mz"], -spectrum2["intensity"], linefmt=col2, markerfmt=" ", basefmt=" ", label=spectrum2_name)
        plt.xlabel(xlab, fontsize=lab_size)
        plt.ylabel(ylab, fontsize=lab_size)
        plt.xlim(range_mz)
        plt.legend(fontsize=legend_text_size, title="Spectra")
        plt.title("MS2 Spectra Comparison", fontsize=title_size)
        plt.show()

# Example Data and Function Call for Testing
if __name__ == "__main__":
    spectrum1 = pd.DataFrame({
        "mz": [87.5, 94.8, 97.1, 97.2, 103.3],
        "intensity": [8356.3, 7654.1, 9456.2, 8837.1, 8560.2]
    })
    spectrum2 = pd.DataFrame({
        "mz": [87.5, 94.8, 97.1, 97.2, 103.3],
        "intensity": [7356.3, 6654.1, 8456.2, 7837.1, 7560.2]
    })
    ms2_plot(spectrum1, spectrum2, interactive_plot=False)
