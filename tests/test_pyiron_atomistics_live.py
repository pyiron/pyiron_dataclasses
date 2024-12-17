import unittest

from h5io_browser import read_dict_from_hdf
from pint import UnitRegistry

from pyiron_dataclasses.v1.converter import get_dataclass

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
    skip_pyiron_atomistics_test,
    "pyiron_atomistics is not installed, so the pyiron_atomistics tests are skipped.",
)
class TestPyironAtomisticsLive(unittest.TestCase):
    def setUp(self):
        self.project = Project("test")

    def tearDown(self):
        Project("test").remove(enable=True)

    def test_sphinx_calc_minimize(self):
        ureg = UnitRegistry()
        job = self.project.create.job.Sphinx("sx_mini")
        job.structure = self.project.create.structure.ase.bulk("Al", cubic=True)
        job.calc_minimize()
        job.run()
        job_dict = read_dict_from_hdf(
            file_name=job.project_hdf5.file_name,
            h5_path="/",
            recursive=True,
            slash="ignore",
        )
        job_sphinx = get_dataclass(job_dict[job.job_name])
        self.assertEqual(
            job_sphinx.calculation_output.generic.energy_tot[-1],
            -228.7831594386992 * ureg.eV,
        )

    def test_sphinx_calc_static(self):
        ureg = UnitRegistry()
        job = self.project.create.job.Sphinx("sx_static")
        job.structure = self.project.create.structure.ase.bulk("Al", cubic=True)
        job.run()
        job_dict = read_dict_from_hdf(
            file_name=job.project_hdf5.file_name,
            h5_path="/",
            recursive=True,
            slash="ignore",
        )
        job_sphinx = get_dataclass(job_dict[job.job_name])
        self.assertEqual(
            job_sphinx.calculation_output.generic.energy_tot[-1],
            -228.78315945023684 * ureg.eV,
        )

    def test_lammps_calc_static(self):
        ureg = UnitRegistry()
        job = self.project.create.job.Lammps("lmp_static")
        job.structure = self.project.create.structure.ase.bulk("Al", cubic=True)
        job.potential = "2002--Mishin-Y--Ni-Al--LAMMPS--ipr1"
        job.run()
        job_dict = read_dict_from_hdf(
            file_name=job.project_hdf5.file_name,
            h5_path="/",
            recursive=True,
            slash="ignore",
        )
        job_lammps = get_dataclass(job_dict[job.job_name])
        self.assertEqual(
            job_lammps.calculation_output.generic.energy_tot[-1],
            -13.4486826111902 * ureg.eV,
        )

    def test_lammps_calc_md(self):
        job = self.project.create.job.Lammps("lmp_md")
        job.structure = self.project.create.structure.ase.bulk("Al", cubic=True)
        job.potential = "2002--Mishin-Y--Ni-Al--LAMMPS--ipr1"
        job.calc_md(temperature=200.0, n_ionic_steps=1000, n_print=100)
        job.run()
        job_dict = read_dict_from_hdf(
            file_name=job.project_hdf5.file_name,
            h5_path="/",
            recursive=True,
            slash="ignore",
        )
        job_lammps = get_dataclass(job_dict[job.job_name])
        self.assertEqual(len(job_lammps.calculation_output.generic.energy_tot), 11)

    def test_lammps_calc_minimize(self):
        ureg = UnitRegistry()
        job = self.project.create.job.Lammps("lmp_mini")
        job.structure = self.project.create.structure.ase.bulk("Al", cubic=True)
        job.potential = "2002--Mishin-Y--Ni-Al--LAMMPS--ipr1"
        job.run()
        job_dict = read_dict_from_hdf(
            file_name=job.project_hdf5.file_name,
            h5_path="/",
            recursive=True,
            slash="ignore",
        )
        job_lammps = get_dataclass(job_dict[job.job_name])
        self.assertEqual(
            job_lammps.calculation_output.generic.energy_tot[-1],
            -13.4486826111902 * ureg.eV,
        )
