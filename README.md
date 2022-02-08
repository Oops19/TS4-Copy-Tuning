# TS4 Copy-Tuning Mod
A simple mod to copy tunings (_super_affordances and _supported_posture_families) from one object to another.

It has no error checks so in case of an exception you will see an orange pop-up.

### Interactions
Within the debug menu (Shift-click on an object) there will be a new '/ Tuning' category.
Interactions which are not available will be hidden.

It offers '🗎 Copy', '📋 Paste' and '⎌ Restore'.
- Copy will save the tuning into a local, non-persistent, cache.
- Paste will copy the current tunings of the object to have a non-persistent backup. Then the tuning will be overridden.
- Restore will copy the tuning form the backup. This works as long as the lot is loaded.

### Saving and Loading the game
The modified tuning will not be saved. After loading all objects work as expected.
Saving and loading the changes will be implemented later.

### Issues
Objects (eg. chairs) may still be usable even though the 'Sit' interaction is missing.

### TODO
Persist the changes and load them with the game.
Allow to specify the list of tunings to be copied.