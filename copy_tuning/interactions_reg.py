#
# License: https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2021 https://github.com/Oops19
#
#
from typing import Tuple
from objects.script_object import ScriptObject
from sims4communitylib.services.interactions.interaction_registration_service import CommonInteractionRegistry, CommonInteractionType, CommonScriptObjectInteractionHandler


@CommonInteractionRegistry.register_interaction_handler(CommonInteractionType.ON_SCRIPT_OBJECT_LOAD)
class _RegisterCopyTuningInteractions_CopyTuning_0(CommonScriptObjectInteractionHandler):
    @property
    def interactions_to_add(self) -> Tuple[int]:
        interactions: Tuple = (
            0xC08BA21851057031,  # 'Copy' - fnv('o19_CopyTuning_PMC__Tuning_DC__PMA_DC_Copy')
            0x534195DBB7D3B463,  # 'Paste' - fnv('o19_CopyTuning_PMC__Tuning_DC__PMA_DC_Paste')
            0x231B5CC3BEFCF074,  # 'Restore' - fnv('o19_CopyTuning_PMC__Tuning_DC__PMA_DC_Restore')
        )
        return interactions

    def should_add(self, script_object: ScriptObject, *args, **kwargs) -> bool:
        return True
