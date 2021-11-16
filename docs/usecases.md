# UPP - Scenarios
## Base functionality
### Loading of locker - by Pharmacist (Super User)
- _Pharmacist_ unlocks the **keypad** with an **RFID chip/card**. This remains unlocked for the whole duration of contact (+5 sec)
- She reads off a **paper-based document** the reference number **(Short form of UUID)** of the _nurse_ that she wants to reserve a _locker_ for. She inputs the **UUID** by using a **keypad** and presses the ENTER BUTTON. A _locker_ opens, she places the items inside and pushes the door, by which it gets locked. 
- If the _pharmacist_ makes a mistake during input, without having pressed ENTER, she can delete single numbers by short-pressing DELETE.
- If the _pharmacist_ makes a mistake AND also presses ENTER. She can delete inputs by holding the DELETE BUTTON and repeating the UUID input, while holding the DELETE BUTTON and then pressing the ENTER BUTTON. 

### Unloading of Locker - by Nurse (User)
- _Nurse_ touches **rfid chip/card** to **reciever**. This opens ALL _lockers_ that are allocated to the nurse. 
### Administration by us
- Easy extension of people (both card creation as well as db) 
- Easy extension of lockers
- Access to System Log files

## Exploratory scenarios
### Loading of locker - by Pharmacist (Super User)
- _Pharmacist_ can access **logfile** on the **LCD-Display** by holding key combination ENTER+1 pressed for 2 seconds. She can then scroll the file up and down with numbers 2 and 8 to see **UUID - ACCES_DATE / ACCESS_TIME** 
- _Pharmacist_ can revoke card privileges for lost cards by holding key combination ENTER+7 pressed for 2 seconds. She receives a text prompt to input, which **Card Nr.** should be deleted. There she inputs the number and presses ENTER. The **LCD-Display** displays "The deletion of <Nr.> was successful".This reverts the keypad back to normal mode. 
- Displaying names of nurses in log file.
- Displaying names of nurses after input. 
- Displaying list of active / inactive cards.
- Printing log files. 
### Unloading of Locker - by Nurse (User)
- 2FA
- Displaying names
### Administration by us
- Adding names to nurses
### Additional
- Displaying which lockers are "filled" (maybe by using a small LED lamp - red/green). 
