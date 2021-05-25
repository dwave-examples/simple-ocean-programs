# Copyright 2020 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import subprocess
import sys
import unittest

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class TestBQMFunctionality(unittest.TestCase):
    @unittest.skipIf(os.getenv('SKIP_INT_TESTS'), "Skipping integration test.")
    def test_smoke_bqm_conversion(self):
        """run bqm_conversion.py and check that nothing crashes"""

        demo_file = os.path.join(project_dir, 'BQM_Functionality/bqm_conversion.py')
        subprocess.check_output([sys.executable, demo_file])

    @unittest.skipIf(os.getenv('SKIP_INT_TESTS'), "Skipping integration test.")
    def test_smoke_bqm_offsets(self):
        """run bqm_offsets.py and check that nothing crashes"""

        demo_file = os.path.join(project_dir, 'BQM_Functionality/bqm_offsets.py')
        subprocess.check_output([sys.executable, demo_file])

    @unittest.skipIf(os.getenv('SKIP_INT_TESTS'), "Skipping integration test.")
    def test_smoke_general_program_bqm(self):
        """run general_program_bqm.py and check that nothing crashes"""

        demo_file = os.path.join(project_dir, 'BQM_Functionality/general_program_bqm.py')
        subprocess.check_output([sys.executable, demo_file])

class TestBasicPrograms(unittest.TestCase):
    @unittest.skipIf(os.getenv('SKIP_INT_TESTS'), "Skipping integration test.")
    def test_smoke_general_program_ising(self):
        """run general_program_ising.py and check that nothing crashes"""

        demo_file = os.path.join(project_dir, 'Basic_Programs/general_program_ising.py')
        subprocess.check_output([sys.executable, demo_file])

    @unittest.skipIf(os.getenv('SKIP_INT_TESTS'), "Skipping integration test.")
    def test_smoke_general_program_qubo(self):
        """run general_program_qubo.py and check that nothing crashes"""

        demo_file = os.path.join(project_dir, 'Basic_Programs/general_program_qubo.py')
        subprocess.check_output([sys.executable, demo_file])

class TestExploringPegasus(unittest.TestCase):
    @unittest.skipIf(os.getenv('SKIP_INT_TESTS'), "Skipping integration test.")
    def test_smoke_biclique_embedding(self):
        """run biclique_embedding.py and check that nothing crashes"""

        demo_file = os.path.join(project_dir, 'Exploring_Pegasus/biclique_embedding.py')

        # This test should be made more robust once we have usage information
        subprocess.check_output([sys.executable, demo_file, "5"])

    @unittest.skipIf(os.getenv('SKIP_INT_TESTS'), "Skipping integration test.")
    def test_smoke_clique_embedding(self):
        """run clique_embedding.py and check that nothing crashes"""

        demo_file = os.path.join(project_dir, 'Exploring_Pegasus/clique_embedding.py')

        # This test should be made more robust once we have usage information
        subprocess.check_output([sys.executable, demo_file, "5"])

    @unittest.skipIf(os.getenv('SKIP_INT_TESTS'), "Skipping integration test.")
    def test_smoke_get_available_qubits(self):
        """run get_available_qubits.py and check that nothing crashes"""

        demo_file = os.path.join(project_dir, 'Exploring_Pegasus/get_available_qubits.py')
        subprocess.check_output([sys.executable, demo_file])

    @unittest.skipIf(os.getenv('SKIP_INT_TESTS'), "Skipping integration test.")
    def test_smoke_get_inactive_qubits(self):
        """run get_inactive_qubits.py and check that nothing crashes"""

        demo_file = os.path.join(project_dir, 'Exploring_Pegasus/get_inactive_qubits.py')
        subprocess.check_output([sys.executable, demo_file])

    @unittest.skipIf(os.getenv('SKIP_INT_TESTS'), "Skipping integration test.")
    def test_smoke_get_props(self):
        """run get_props.py and check that nothing crashes"""

        demo_file = os.path.join(project_dir, 'Exploring_Pegasus/get_props.py')
        subprocess.check_output([sys.executable, demo_file])

class TestPegasusEmbeddingVideo(unittest.TestCase):
    @unittest.skipIf(os.getenv('SKIP_INT_TESTS'), "Skipping integration test.")
    def test_smoke_double_plot(self):
        """run double_plot.py and check that nothing crashes"""

        demo_file = os.path.join(project_dir, 'Pegasus_Embedding_Video/double_plot.py')
        subprocess.check_output([sys.executable, demo_file])

    @unittest.skipIf(os.getenv('SKIP_INT_TESTS'), "Skipping integration test.")
    def test_smoke_draw_yield(self):
        """run draw_yield.py and check that nothing crashes"""

        demo_file = os.path.join(project_dir, 'Pegasus_Embedding_Video/draw_yield.py')
        subprocess.check_output([sys.executable, demo_file])

    @unittest.skipIf(os.getenv('SKIP_INT_TESTS'), "Skipping integration test.")
    def test_smoke_embed_draw_clique(self):
        """run embed_draw_clique.py and check that nothing crashes"""

        demo_file = os.path.join(project_dir, 'Pegasus_Embedding_Video/embed_draw_clique.py')
        subprocess.check_output([sys.executable, demo_file])

    @unittest.skipIf(os.getenv('SKIP_INT_TESTS'), "Skipping integration test.")
    def test_smoke_embed_draw_random(self):
        """run embed_draw_random.py and check that nothing crashes"""

        demo_file = os.path.join(project_dir, 'Pegasus_Embedding_Video/embed_draw_random.py')
        subprocess.check_output([sys.executable, demo_file])

    @unittest.skipIf(os.getenv('SKIP_INT_TESTS'), "Skipping integration test.")
    def test_smoke_embed_draw_sparse(self):
        """run embed_draw_sparse.py and check that nothing crashes"""

        demo_file = os.path.join(project_dir, 'Pegasus_Embedding_Video/embed_draw_sparse.py')
        subprocess.check_output([sys.executable, demo_file])

    @unittest.skipIf(os.getenv('SKIP_INT_TESTS'), "Skipping integration test.")
    def test_smoke_pegasus_graph(self):
        """run test_smoke_pegasus_graph.py and check that nothing crashes"""

        demo_file = os.path.join(project_dir, 'Pegasus_Embedding_Video/pegasus_graph.py')
        subprocess.check_output([sys.executable, demo_file])

if __name__ == '__main__':
    unittest.main()
