# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2017.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Module for Circuits."""
from .quantumcircuit import QuantumCircuit
from .classicalregister import ClassicalRegister, Clbit
from .quantumregister import QuantumRegister, Qubit
from .gate import Gate
from .instruction import Instruction
from .instructionset import InstructionSet
from .measure import Measure
from .reset import Reset
from .compositegate import CompositeGate
from .parameter import Parameter
from .parametervector import ParameterVector
