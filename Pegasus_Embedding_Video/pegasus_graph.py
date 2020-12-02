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

import dwave_networkx as dnx
from random import seed, sample

seed(5640)

P16_perfect = dnx.pegasus_graph(16)

mask_nodes = sample(list(P16_perfect), int(.96*len(P16_perfect)))

P16 = P16_perfect.subgraph(mask_nodes).copy()


P6_perfect = dnx.pegasus_graph(6)

mask_nodes = sample(list(P6_perfect), int(.96*len(P6_perfect)))

P6 = P6_perfect.subgraph(mask_nodes).copy()
