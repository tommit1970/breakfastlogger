------------------
  IMPORTANT!!!!!
------------------
One new obstacle is the Personal Access Token(PAT) in the github-system.
I made one PAT that lasts for one week(7 days). It will have to be renewed after a week.

See LastPass - GitHub - notes! I need to use this for a while to get used to it.


-----------------------------------------------------------------------

Currently in Progress:
----------------------
2022/04/01-2022/05/15: Making a the start of a windows-version of BreakfastLogger, incl. training on tkinter



Thoughts and ideas for change:
------------------------------
- read log option
- on register breakfast update breakfastList (bug in app already running from 30.april - 1.mai)
	- check if current date is in the set month
- scan months to check if there are any irregularities (like may in april)
- scan if there are any missing entries
- adminaccess: True/False in heading, a = Login/Logout
- gap in register checking, from date to date
- a total remake of datesystem in breakfastDataFile and breakfastList
- show entries on delete recordings
2022/03/??-2022/03/??:- make a visual representation of users - show avatar
2022/03/??-2022/03/??:- log usercreations, changes and deletions in log.txt
2022/03/??-2022/03/??:- if the file log.txt becomes too big save first about 100 lines to another archive
2022/03/??-2022/03/??:- aborted in deleteEntry - not red
2022/03/??-2022/03/??:- all options in (b)rackets in red - do a walk through
2022/03/??-2022/03/??:- Clean Module-structure
2022/03/??-2022/03/??:- logged in as one user, can only change username and password for this user
2022/03/??-2022/03/??: Make a master password to access all

Errors:
-------


-----------------------------------------------------------------------
		H I S T O R Y   O F   C H A N G E S / I M P R O V E M E N T S
StartDate	EndDate				Change
-----------------------------------------------------------------------
Not Gited



Gited
2022/04/10-2022/04/20: Making Insert possible in Admin mode (Insert and Edit)
2022/03/19-2022/03/19:- Check if the file lastEntryDate.txt does exist
2022/03/17-2022/03/17: UserName must be minimum 3 characters long
2022/03/17-2022/03/17: Make it not possible to change UserName
2022/03/16-2022/03/16: Use getpass on modified passwords in User Actions and make it impossible to make the same password
2022/03/16-2022/03/16: Make all key-options in menu to 'key' and 'func'
2022/03/16-2022/03/16: Fixed, when old password is made new, username and password has to be correct, 2022/03/15-2022/03/15: Correct colors on modify user
2022/03/15-2022/03/15: Abort feedback on abort - delete recordings
2022/03/15-2022/03/15: When modifying password update created
2022/03/??-2022/03/13: Made syncing the two DBs (local and cloud) possible
2022/03/??-2022/03/13: Fixed the menu options for admins -> move menu option Set MongoDB inside DB Actions
2022/03/02-2022/03/02: Set MongoDB to local or cloud
2022/02/27-2022/02/27: Colors in new password - module
2022/02/27-2022/02/27: Make sure that new password is different from old after password expire
2022/02/23-2022/02/26: Flush output after keyboard-press (keyboard-module) to avoid (space) in menu - Found it: keyboard.wait('space', suppress = True)
2022/02/21-2022/02/24: Manage users from admin, create, view, modify or delete userdata
2022/02/17-2022/02/17: Save passwords in binary format, it worked
2022/02/17-2022/02/17: Make "Aborted"(x to abort) red on edit
2022/02/12-2022/02/12: Check the freshness of the password, check expire date, must create new password, compare today with creation day of password, if password has expired demand new password, if user does nothing give no access to admin priviliges
2022/02/11-2022/02/11: Make new password(include in globals,include in break.py - if else - list,include in menu,password-handling in admin.py)
2022/02/05-2022/02/08: When you are in another year and month than the current year and month, registering is still possible, but it will register in current year and month
2022/02/09-2022/02/10: Hash the password - trained with hashboy.py and I learned that hashed passwords can be compared within the bcrypt-module
2022/02/09-2022/02/10: Mongodb and python
2022/02/08-2022/02/08: If breakfastList > 15 make a pause with <enter> to continue
2022/02/05-2022/02/07: Clean writeFile, subFunctions created
2022/02/05-2022/02/07: Fix ./DataFolder-issue with 2 and 02, simplify file-structure(filename = 2022-02_breakfastDataFile.txt), walked through all files involved, step-by-step really slowly checking and testing on the way
2022/02/04-2022/02/04: Layout: Set Time Focus (Current year: 2022 Current month: 2), remove from top
2022/02/02-2022/02/02: Exit out of setTimeFocus (x to abort)
2022/02/02-2022/02/02: Chech input in setTimeFocus, Year must be a number between 2000 and 2100, and Month 1-12
2022/02/02-2022/02/02: Fixed mkdir(year) before mkdir(month) if no year is created, mkdir() can not create two directories at once
2022/01/31-2022/02/01: It seems like python is saving .txt-files in western 1252 encoding as default so I did something like: # changed all the .txt-files to utf-8 encoding, # changed all the fileHandling.py to open(file, 'rxw', encoding="utf-8") both reading and saving because this worked with ft.py and test.txt
2022/01/30-2022/01/30: Input recording is possible when focus is in old month (error)
2022/01/27-2022/01/29: Yearly and Monthly file structure(Automatic, Done), '2022' 'january'=> 01, 'february', etc. on 'Show Recordings', # fileHandling.py => check if ./DataFolder/<year>/<month>/breakfastDataFile.txt exists or create it in folder system (Done), # Inform user in menu what month is focused on (done)
2022/01/26-2022/01/26: Note in README.md that break.py is the main-file
2022/01/24-2022/01/26: Logfile for changes - metalogfile, # record new entries (Datetime,New,Item), # record edited entries - prev and new (Datetime,Edited From Old to New), # record deleted entries (Datetime,Removed,Item), # log date of change to each change or set of change
2022/01/23-2022/01/23: Make a numcheck and rangecheck function inside smallFunctions.py, and make the code in showEntries.py,editEntries.py and deleteEntries.py cleaner
2022/01/22-2022/01/22: Edit recordings when with admin authorities
2022/01/21-2022/01/21: Make show range
2022/01/21-2022/01/21: Make username and password into json in a new logindata.py file, removing admin.txt
2022/01/17-2022/01/20: Menu options in a dictionary, so I only change it in one place('inputRec':'1','showRec':'2','deleteRec':'3', etc.)
2022/01/18-2022/01/18:	Clean deleteEntries.py like showEntries.py with deleteMenu() etc.
2022/01/15-2022/01/15: Gather Show Recordings and Show One Recording in one option
2022/01/14-2022/01/14:	When writing password, show no text (or dots/asterix)
2022/01/12-2022/01/14:	?? is showed as ???? - how to fix - log.txt was Western(Windows 1252)-encoded - The problem is: What is the encoding of PowerShell($OutputEncoding - utf-8), Python(import sys, sys.getdefaultencoding() - utf-8) and Sublime(see bottom line of app - Western(Windows 1252))?
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