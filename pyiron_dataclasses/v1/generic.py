from dataclasses import dataclass
import numpy as np
from typing import Optional, List


@dataclass
class DensityOfStates:
    energies: str
    int_densities: str
    tot_densities: str


@dataclass
class ElectronicStructure:
    efermi: float
    eig_matrix: np.ndarray
    k_points: np.ndarray
    k_weights: np.ndarray
    occ_matrix: np.ndarray
    dos: DensityOfStates


@dataclass
class OutputGenericDFT:
    energy_free: np.ndarray
    energy_int: np.ndarray
    energy_zero: np.ndarray
    scf_energy_free: np.ndarray
    scf_energy_int: np.ndarray
    scf_energy_zero: np.ndarray
    cbm_list: Optional[np.ndarray]
    e_fermi_list: Optional[np.ndarray]
    final_magmoms: Optional[np.ndarray]
    magnetization: Optional[np.ndarray]
    n_elect: Optional[float]
    n_valence: Optional[dict]
    potentiostat_output: Optional[np.ndarray]
    bands_k_weights: Optional[np.ndarray]
    kpoints_cartesian: Optional[np.ndarray]
    bands_e_fermi: Optional[np.ndarray]
    bands_occ: Optional[np.ndarray]
    bands_eigen_values: Optional[np.ndarray]
    scf_convergence: Optional[List[bool]]
    scf_dipole_mom: Optional[np.ndarray]
    scf_computation_time: Optional[np.ndarray]
    valence_charges: Optional[np.ndarray]
    vbm_list: Optional[np.ndarray]
    bands: Optional[ElectronicStructure]
    scf_energy_band: Optional[np.ndarray]
    scf_electronic_entropy: Optional[np.ndarray]
    scf_residue: Optional[np.ndarray]
    computation_time: Optional[np.ndarray]
    energy_band: Optional[np.ndarray]
    electronic_entropy: Optional[np.ndarray]
    residue: Optional[np.ndarray]


@dataclass
class GenericOutput:
    cells: np.ndarray  # N_steps * 3 *3  [Angstrom]
    energy_pot: np.ndarray  # N_steps  [eV]
    energy_tot: np.ndarray  # N_steps  [eV]
    forces: np.ndarray  # N_steps * N_atoms * 3  [eV/Angstrom]
    positions: np.ndarray  # N_steps * N_atoms * 3  [Angstrom]
    volume: np.ndarray  # N_steps
    indices: Optional[np.ndarray]  # N_steps * N_atoms
    natoms: Optional[np.ndarray]  # N_steps
    pressures: Optional[np.ndarray]  # N_steps * 3 * 3
    steps: Optional[np.ndarray]  # N_steps
    stresses: Optional[np.ndarray]  # N_steps
    temperature: Optional[np.ndarray]  # N_steps
    unwrapped_positions: Optional[np.ndarray]  # N_steps * N_atoms * 3  [Angstrom]
    velocities: Optional[np.ndarray]  # N_steps * N_atoms * 3  [Angstrom/fs]
    dft: Optional[OutputGenericDFT]
    elastic_constants: Optional[np.ndarray]


@dataclass
class ChargeDensity:
    total: np.ndarray


@dataclass
class Server:
    user: str
    host: str
    run_mode: str
    cores: int
    threads: int
    new_h5: bool
    accept_crash: bool
    run_time: int  # [seconds]
    structure_id: Optional[int]
    memory_limit: Optional[str]
    queue: Optional[str]
    qid: Optional[int]


@dataclass
class Executable:
    version: str
    name: str
    operation_system_nt: bool
    executable: Optional[str]
    mpi: bool
    accepted_return_codes: List[int]


@dataclass
class GenericDict:
    restart_file_list: list
    restart_file_dict: dict
    exclude_nodes_hdf: list
    exclude_groups_hdf: list


@dataclass
class Interactive:
    interactive_flush_frequency: int
    interactive_write_frequency: int


@dataclass
class GenericInput:
    calc_mode: str
    structure: str
    fix_symmetry: Optional[bool]
    k_mesh_spacing: Optional[float]
    k_mesh_center_shift: Optional[np.ndarray]
    reduce_kpoint_symmetry: Optional[bool]
    restart_for_band_structure: Optional[bool]
    path_name: Optional[str]
    n_path: Optional[str]
    fix_spin_constraint: Optional[bool]
    max_iter: Optional[int]
    temperature: Optional[float]
    n_ionic_steps: Optional[int]
    n_print: Optional[int]
    temperature_damping_timescale: Optional[float]
    pressure_damping_timescale: Optional[float]
    time_step: Optional[int]


@dataclass
class Units:
    length: str
    mass: str


@dataclass
class Cell:
    cell: np.ndarray  # 3 * 3   [Angstrom]
    pbc: np.ndarray  # 3


@dataclass
class Structure:
    dimension: int
    indices: np.array
    info: dict
    positions: np.ndarray  # N_atoms * 3  [Angstrom]
    species: List[str]
    cell: Cell
    units: Units
