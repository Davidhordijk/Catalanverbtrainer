# Catalan Verb Trainer
A tool to train conjugating Catalan verbs.
I started to create this tool as I noticed that studying conjugations of verbs from a textbook doesn't make sure you are ready to use them in conversation.
The main problem is that you learn them in a certain order: 1st, 2nd, 3rd person singular and then 1st, 2nd, 3rd person plural.
In conversation you need to know a specific conjugation on the spot, without mentally going through: "parlo parles parla parlem parleu parlen" before knowing the 3rd person plural of "parlar".


**MVP**
- [x] all checkboxes in
	tenses
	moods
	persons
	quantity
	
 - [x] checkboxes in columns
	 temps, persones, modes, quantitats
 - [x] make dice

 - [x]  Make the dice roll

 - [x] Teksten kloppend: 

** V2 **
- [x] Interface
	- [x] 	Make window stable
	- [x] 	Keyword i.o. sentence output
 	- [x] 	User input: click to show if answer is correct
        - [ ] User flow
        	- [ ] make enter key displace where user can give input
        	- [ ] add text to make app self-explanatory
         	- [ ] display error if verb is not in database 

- [ ] Verb sheet integration
	- [x] browse for database options
 	- [x] add test verb sheet of three verbs with csv
        - [x] put test verbs in csv file
        - [x] think of database structure and headers
        - [x] make sure all tenses work, with if-then statements for composite tenses
        - [x] fix plusquamperfet
        - [x] fix perfet
        - [x] fix passat perifrastic
        - [ ] add irregular verbs
        - [ ] think of way to recognise and classify regular verbs so that all of the can be used without having a database with all of them in there


** V3 **
- [ ] User progress
	- [ ] think of first way to track user progress: profile that can store info?

 - [ ] Better looks (drop the windows XP vibe)



Later / Maybe:
- [ ] Think of logical place for gerundi's, past/present/future(e.g. estic parlant, estava parlant, estaré parlant )
- [x] test and delete gramatically impossible times
- [ ] fix imperatiu (if only imperatiu and all tenses are selected, sometimes it still becomes indicatiu)
- [ ] duocards like flow: User input: wrong answer: "<- arrow" right answer: "-> arrow"
