#updating entity

from dataclasses import dataclass
from pathlib import Path
#defining the return type of a function
#this is the entity

#3. Update entity

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path  
