import yaml
from pathlib import Path

def load_config(path=None):
    """
    Load YAML configuration file.
    If no path is provided, defaults to 'config/config.yaml' relative to this file.
    """
    if path is None:
        path = Path(__file__).parent / "config" / "config.yaml"
    else:
        path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    with open(path, "r") as f:
        config = yaml.safe_load(f)

    if config is None:
        raise ValueError(f"Config file is empty or invalid: {path}")

    return config
