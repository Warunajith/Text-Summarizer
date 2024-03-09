from dataclasses import dataclass
from pathlib import Path

# This is Entity 
# Entity is used as a return type of functions

@dataclass(frozen=True)
class DataIngestionConfig():
    root_dir:Path
    source_URL: str
    local_data_file:Path
    unzip_dir:Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list