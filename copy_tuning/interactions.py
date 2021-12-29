#
# License: https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2021 https://github.com/Oops19
#
#
from copy_tuning.modinfo import ModInfo

from typing import Any

from event_testing.results import TestResult
from interactions.context import InteractionContext
from sims.sim import Sim
from sims4.tuning.tunable import Tunable

from sims4communitylib.classes.interactions.common_terrain_interaction import CommonTerrainInteraction
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity().name, 'main')
log.enable()


class CopyTuningInteractions(CommonTerrainInteraction):
    INSTANCE_TUNABLES = {
        'action': Tunable(tunable_type=int, default=0),
    }

    __slots__ = {'action', }


    @classmethod
    def on_test(cls, interaction_sim: Sim, interaction_target: Any, interaction_context: InteractionContext, **kwargs) -> TestResult:
        return TestResult.TRUE

    def on_started(self, interaction_sim: Sim, interaction_target: Any) -> bool:
        return self.handle_interaction(interaction_sim, interaction_target)

    def handle_interaction(self, interaction_sim: Sim, interaction_target: Any) -> bool:
        if self.action == 1:
            log.debug("Copy")
            CopyTuningStore.cp_super_affordances = getattr(interaction_target, '_super_affordances')
            CopyTuningStore.cp_supported_posture_families = getattr(interaction_target, '_supported_posture_families')
        elif self.action == 2:
            if not getattr(interaction_target, 'cp_super_affordances'):
                log.debug("Backup")
                setattr(interaction_target, 'cp_super_affordances', getattr(interaction_target, '_super_affordances'))
                setattr(interaction_target, 'cp_supported_posture_families', getattr(interaction_target, '_supported_posture_families'))
            if CopyTuningStore.cp_super_affordances:
                log.debug("Paste")
                setattr(interaction_target, '_super_affordances', CopyTuningStore.cp_super_affordances)
                setattr(interaction_target, '_supported_posture_families', CopyTuningStore.cp_supported_posture_families)
            else:
                log.warn("Nothing to paste")  # My bad, this interaction should have been hidden
        elif self.action == 4:
            if getattr(interaction_target, 'cp_super_affordances'):
                log.debug("Restore")
                setattr(interaction_target, '_super_affordances', getattr(interaction_target, 'cp_super_affordances'))
                setattr(interaction_target, '_supported_posture_families', getattr(interaction_target, 'cp_supported_posture_families'))
            else:
                log.warn("Nothing to restore")  # My bad, this interaction should have been hidden
        return True

class CopyTuningStore:
    cp_super_affordances = None
    cp_supported_posture_families = None