import unittest

from h5io_browser.base import read_dict_from_hdf
from pint import UnitRegistry

from convert import (
    convert_sphinx_job_dict,
    convert_lammps_job_dict,
)

try:
    from pyiron_atomistics import Project
    skip_pyiron_atomistics_test = False
except ImportError:
    skip_pyiron_atomistics_test = True


def get_node_from_job_dict(job_dict, node):
    node_name_lst = node.split("/")
    tmp_dict = job_dict
    for group in node_name_lst:
        tmp_dict = tmp_dict[group]
    return tmp_dict


@unittest.skipIf(
    skip_pyiron_atomistics_test, "pyiron_atomistics is not installed, so the pyiron_atomistics tests are skipped."
)
class TestPyironAtomisticsLive(unittest.TestCase):
    def setUp(self):
        self.project = Project("test")

    def tearDown(self):
        Project("test").remove()

    def test_sphinx(self):
        ureg = UnitRegistry()
        job = self.project.create.job.Sphinx("sx")
        job.structure = self.project.create.structure.ase.bulk("Al", cubic=True)
        job.calc_minimize()
        job.run()
        job_dict = read_dict_from_hdf(
            file_name=job.project_hdf5.file_name,
            h5_path="/",
            recursive=True,
            slash='ignore',
        )
        job_sphinx = convert_sphinx_job_dict(job_dict[job.job_name])
        self.assertEqual(job_sphinx.calculation_output.generic.energy_tot[-1], -228.78315944 * ureg.eV)

    def test_lammps(self):
        ureg = UnitRegistry()
        job = self.project.create.job.Lammps("lmp")
        job.structure = self.project.create.structure.ase.bulk("Al", cubic=True)
        job.potential = '2002--Mishin-Y--Ni-Al--LAMMPS--ipr1'
        job.run()
        job_dict = read_dict_from_hdf(
            file_name=job.project_hdf5.file_name,
            h5_path="/",
            recursive=True,
            slash='ignore',
        )
        job_lammps = convert_lammps_job_dict(job_dict[job.job_name])
        self.assertEqual(job_lammps.calculation_output.generic.energy_tot[-1], -9428.45286562 * ureg.eV)
