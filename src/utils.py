from pathlib import Path
import pandas as pd

DATA_RAW = Path(__file__).resolve().parents[1] / "data" / "raw"
DATA_PROC = Path(__file__).resolve().parents[1] / "data" / "processed"
FIG_DIR = Path(__file__).resolve().parents[1] / "reports" / "figures"

def read_csv_safely(filename: str, **kwargs) -> pd.DataFrame:
    """Lee un CSV desde data/raw con opciones seguras (encoding, separador).
    Ajusta kwargs si los archivos tienen ';' o latin-1.
    """
    path = DATA_RAW / filename
    if not path.exists():
        raise FileNotFoundError(f"No se encontró {path}. Asegúrate de colocar los CSV en data/raw.")
    defaults = dict(encoding='utf-8', sep=',', low_memory=False)
    defaults.update(kwargs)
    return pd.read_csv(path, **defaults)

def save_parquet(df: pd.DataFrame, name: str):
    out = DATA_PROC / f"{name}.parquet"
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(out, index=False)
    return out

def ensure_dirs():
    for p in [DATA_RAW, DATA_PROC, FIG_DIR]:
        p.mkdir(parents=True, exist_ok=True)