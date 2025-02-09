# Dataclasses for pyiron
[![Pipeline](https://github.com/pyiron/pyiron_dataclasses/actions/workflows/pipeline.yml/badge.svg)](https://github.com/pyiron/pyiron_dataclasses/actions/workflows/pipeline.yml)

The `pyiron_dataclasses` module provides a series of [dataclasses](https://docs.python.org/3/library/dataclasses.html) 
for the `pyiron` workflow framework. It can load HDF5 files created by `pyiron_atomistics` and read the content stored 
in those files, without depending on `pyiron_atomistics`. Furthermore, it is not fixed to a single version of 
`pyiron_atomistics` but rather matches multiple versions of `pyiron_atomistics` to the same API version of 
`pyiron_dataclasses`. 

## Usage 
Using the `get_dataclass()` function of the built-in converter:
```python
from h5io_browser import read_dict_from_hdf
from pyiron_dataclasses.v1.converter import get_dataclass

job_classes = get_dataclass(
    job_dict=read_dict_from_hdf(
        file_name=job.project_hdf5.file_name,
        h5_path="/",
        recursive=True,
        slash='ignore',
    )[job.job_name]
)
job_classes
```

## Supported Versions 
### Version 1 - `v1`
Supported versions of `pyiron_atomistics`:
* `0.6.20`
* `0.6.21`
