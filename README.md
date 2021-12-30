# TS4 Copy-Tuning Mod
A simple mod to copy tunings from one object to another.

It has no error checks so in case of an exception you will see an orange pop-up.

### Interactions
Within the debug menu (Shift-click on an object) there will be a new '/ Tuning' category.
Interactions which are not available will be hidden.

It offers '🗎 Copy', '📋 Paste' and '⎌ Restore'.
- Copy will save the tuning into a local, non-persistent, cache.
- Paste will copy the current tunings of the object to have a non-persistent backup. Then the tuning will be overridden.
- Restore will copy the tuning form the backup. This works as long as the lot is loaded.

### Saving and Loading the game
The modified tuning - but not the backup - will be saved and loaded. After loading there is no 'Restore' option.

One may still copy a tuning from another working object to restore functionality.

### Issues
Objects (eg. chairs) may still be usable even though the 'Sit' interaction is missing.