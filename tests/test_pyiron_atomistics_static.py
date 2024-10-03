import os
from unittest import TestCase

from h5io_browser.base import read_dict_from_hdf
from pint import UnitRegistry

from convert import (
    convert,
    convert_sphinx_job_dict,
    convert_lammps_job_dict,
    convert_vasp_job_dict,
)


class TestPyironAtomisticsStatic(TestCase):
    def test_sphinx(self):
        ureg = UnitRegistry()
        job_dict = read_dict_from_hdf(
            file_name=os.path.join(os.path.dirname(__file__), "static", "sx.h5"),
            h5_path="/sx",
            recursive=True,
            slash='ignore',
        )
        job_sphinx = convert_sphinx_job_dict(job_dict=job_dict)
        self.assertEqual(job_sphinx.calculation_output.generic.energy_tot[-1], -228.7831594379917 * ureg.eV)

    def test_lammps(self):
        ureg = UnitRegistry()
        job_dict = read_dict_from_hdf(
            file_name=os.path.join(os.path.dirname(__file__), "static", "lmp.h5"),
            h5_path="/lmp",
            recursive=True,
            slash='ignore',
        )
        job_lammps = convert_lammps_job_dict(job_dict=job_dict)
        self.assertEqual(job_lammps.calculation_output.generic.energy_tot[-1], -9428.45286561574 * ureg.eV)

    def test_vasp(self):
        ureg = UnitRegistry()
        job_dict = read_dict_from_hdf(
            file_name=os.path.join(os.path.dirname(__file__), "static", "vasp.h5"),
            h5_path="/vasp",
            recursive=True,
            slash='ignore',
        )
        job_vasp = convert_vasp_job_dict(job_dict=job_dict)
        self.assertEqual(job_vasp.calculation_output.generic.energy_tot[-1], -14.7459202 * ureg.eV)

    def test_all(self):
        ureg = UnitRegistry()
        static_folder = os.path.join(os.path.dirname(__file__), "static")
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
                slash='ignore',
            )[hdf5_file.split(".")[0]]
            self.assertEqual(
                convert(job_dict=job_dict).calculation_output.generic.energy_tot[-1],
                energy_dict[hdf5_file]
            )
