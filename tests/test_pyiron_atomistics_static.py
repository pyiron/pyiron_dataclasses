import os
from unittest import TestCase

from h5io_browser import read_dict_from_hdf
from pint import UnitRegistry

from pyiron_dataclasses.v1.converter import (
    get_dataclass,
)


class TestPyironAtomisticsStatic(TestCase):
    def test_all(self):
        ureg = UnitRegistry()
        static_folder = os.path.join(
            os.path.dirname(__file__), "pyiron_atomistics_0_6_13"
        )
        energy_dict = {
            "sx.h5": -228.7831594379917 * ureg.eV,
            "lmp.h5": -9428.45286561574 * ureg.eV,
            "vasp.h5": -14.7459202 * ureg.eV,
        }
        for hdf5_file in os.listdir(static_folder):
            job_dict = read_dict_from_hdf(
                file_name=os.path.join(static_folder, hdf5_file),
                h5_path="/",
                recursive=True,
                slash="ignore",
            )[hdf5_file.split(".")[0]]
            self.assertEqual(
                get_dataclass(job_dict=job_dict).calculation_output.generic.energy_tot[
                    -1
                ],
                energy_dict[hdf5_file],
            )
