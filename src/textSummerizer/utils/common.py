import os 
from box.exceptions import BoxValueError
import yaml
from textSummerizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml : Path) -> config_box:
    """ 
    reads yaml files and returns 
    Args:
    path_to_yaml (str)
    Returns:
    ConfigBox: ConfigBox Type
    
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            retun ConfigBox(content)
    except BoxValueError:
        BoxValueError("yamlfile is empty")
    except Exception as e:
        raise e

@ensure_annotations
def mkdirs(path_to_directories : list[Path], verbose=True):
    for path in path_to_directories:
        if verbose:
            logger.info(f"created directory @: {path}")

@ensure_annotations
def get_size(path:Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"