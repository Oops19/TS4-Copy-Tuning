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
            0x455BBA2948955D9E,  # 'Copy' - fnv('o19_CopyTuning_PMC__Tuning_PMA_Copy_debug')
            0xC729A37324008552,  # 'Paste' - fnv('o19_CopyTuning_PMC__Tuning_PMA_Paste_debug')
            0xED715CD0A1182435,  # 'Restore' - fnv('o19_CopyTuning_PMC__Tuning_PMA_Restore_debug')
        )
        return interactions

    def should_add(self, script_object: ScriptObject, *args, **kwargs) -> bool:
        return True
        # if not CommonTypeUtils.is_sim_instance(script_object):
        #     return False # If the object is not a Sim, return False.
        # return True
