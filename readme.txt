------------------
  IMPORTANT!!!!!
------------------
One new obstacle is the Personal Access Token(PAT) in the github-system.
I made one PAT that lasts for one week(7 days). It will have to be renewed after a week.

See LastPass - GitHub - notes! I need to use this for a while to get used to it.


-----------------------------------------------------------------------

Currently in Progress:
----------------------
- monthly structure, 'january', 'february', etc. on 'Show Recordings'



Thoughts and ideas for change:
------------------------------
- ask for date on 'Show One Recording', use time as a structure for saving data
- Clean Module-structure
- Hash the password
- improve globals['mainMenu']['inputRecs']['keyNum'/'funcToCall']


-----------------------------------------------------------------------
		H I S T O R Y   O F   C H A N G E S / I M P R O V E M E N T S
StartDate	EndDate				Change
-----------------------------------------------------------------------
Not Gited






Gited
2022/01/24-2022/01/??: Logfile for changes - metalogfile, # record new entries (Datetime,New,Item), # record edited entries - prev and new (Datetime,Edited From Old to New), # record deleted entries (Datetime,Removed,Item), # log date of change to each change or set of change
2022/01/23-2022/01/23: Make a numcheck and rangecheck function inside smallFunctions.py, and make the code in showEntries.py,editEntries.py and deleteEntries.py cleaner
2022/01/22-2022/01/22: Edit recordings when with admin authorities
2022/01/21-2022/01/21: Make show range
2022/01/21-2022/01/21: Make username and password into json in a new logindata.py file, removing admin.txt
2022/01/17-2022/01/20: Menu options in a dictionary, so I only change it in one place('inputRec':'1','showRec':'2','deleteRec':'3', etc.)
2022/01/18-2022/01/18:	Clean deleteEntries.py like showEntries.py with deleteMenu() etc.
2022/01/15-2022/01/15: Gather Show Recordings and Show One Recording in one option
2022/01/14-2022/01/14:	When writing password, show no text (or dots/asterix)
2022/01/12-2022/01/14:	Ø is showed as Ã¸ - how to fix - log.txt was Western(Windows 1252)-encoded - The problem is: What is the encoding of PowerShell($OutputEncoding - utf-8), Python(import sys, sys.getdefaultencoding() - utf-8) and Sublime(see bottom line of app - Western(Windows 1252))?
2022/01/12-2022/01/12:	Savebug in Delete Rec and Input Rec (fixed)
2022/01/11-2022/01/11:	Admin cheat menu (with toggles) / Regular user menu (no toggles)
2022/01/09-2022/01/10: Abort 'show one recording' with 'x'
2022/01/09-2022/01/10: Abort 'Input recording' with 'x'
2022/01/09-2022/01/09:	Make a colors.py-file with all the colors, one place to rule them all
2022/01/09-2022/01/09: Red color on: 'Out of range' and 'not a number'
2022/01/09-2022/01/09: Red 'Removed' on Delete Recording
2022/01/09-	2022/01/09:	Add while-loop to delete one entry
2022/01/09-	2022/01/09:	Break out of 'delete one recording' and 'range deletion' with 'x'
2022/01/09-	2022/01/09:	Change menu text on 4 (Delete Recordings)
2022/01/06- 2022/01/09:	Delete range of entries, 4 in menu (in progress)
2022/01/05-	2022/01/06:	Another BackgroundColor for the menu-numbers
2022/01/03-	2022/01/05: Smaller Modules/Files
2022/01/05-	2022/01/05:	Show index on -> Show One Recording
2022/01/02-	2022/01/02:	Delete one entry from breakfastList
2022/01/02-	2022/01/02:	A new line after the menu