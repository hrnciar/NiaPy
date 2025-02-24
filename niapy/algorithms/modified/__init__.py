# encoding=utf8
"""Implementation of modified nature-inspired algorithms."""

from niapy.algorithms.modified.hba import HybridBatAlgorithm
from niapy.algorithms.modified.hde import (
    DifferentialEvolutionMTS,
    DifferentialEvolutionMTSv1,
    DynNpDifferentialEvolutionMTS,
    DynNpDifferentialEvolutionMTSv1,
    MultiStrategyDifferentialEvolutionMTS,
    DynNpMultiStrategyDifferentialEvolutionMTS,
    DynNpMultiStrategyDifferentialEvolutionMTSv1,
    MultiStrategyDifferentialEvolutionMTSv1
)
from niapy.algorithms.modified.hsaba import HybridSelfAdaptiveBatAlgorithm
# from niapy.algorithms.modified.jade import (
#     AdaptiveArchiveDifferentialEvolution,
#     cross_curr2p_best
# )
from niapy.algorithms.modified.jde import (
    SelfAdaptiveDifferentialEvolution,
    MultiStrategySelfAdaptiveDifferentialEvolution,
    # DynNpSelfAdaptiveDifferentialEvolutionAlgorithm,
    # DynNpMultiStrategySelfAdaptiveDifferentialEvolution,
    # AgingSelfAdaptiveDifferentialEvolution
)
from niapy.algorithms.modified.plba import ParameterFreeBatAlgorithm
from niapy.algorithms.modified.saba import (
    AdaptiveBatAlgorithm,
    SelfAdaptiveBatAlgorithm
)

# from niapy.algorithms.modified.sade import (
#     StrategyAdaptationDifferentialEvolution,
#     StrategyAdaptationDifferentialEvolutionV1
# )

__all__ = [
    'HybridBatAlgorithm',
    'DifferentialEvolutionMTS',
    'DifferentialEvolutionMTSv1',
    'DynNpDifferentialEvolutionMTS',
    'DynNpDifferentialEvolutionMTSv1',
    'MultiStrategyDifferentialEvolutionMTS',
    'MultiStrategyDifferentialEvolutionMTSv1',
    'DynNpMultiStrategyDifferentialEvolutionMTS',
    'DynNpMultiStrategyDifferentialEvolutionMTSv1',
    'SelfAdaptiveDifferentialEvolution',
    # 'DynNpSelfAdaptiveDifferentialEvolutionAlgorithm',
    'MultiStrategySelfAdaptiveDifferentialEvolution',
    # 'DynNpMultiStrategySelfAdaptiveDifferentialEvolution',
    # 'AgingSelfAdaptiveDifferentialEvolution',
    # 'AdaptiveArchiveDifferentialEvolution',
    # 'cross_curr2p_best',
    # 'StrategyAdaptationDifferentialEvolution',
    # 'StrategyAdaptationDifferentialEvolutionV1',
    'AdaptiveBatAlgorithm',
    'SelfAdaptiveBatAlgorithm',
    'HybridSelfAdaptiveBatAlgorithm',
    'ParameterFreeBatAlgorithm'
]
