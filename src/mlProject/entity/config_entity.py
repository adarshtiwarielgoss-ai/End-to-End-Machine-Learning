from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True) #entity it is a return type of function 
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path