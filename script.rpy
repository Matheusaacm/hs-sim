init -20 python:
    import discord_rpc
    import time

    def readyCallback(current_user):
        print('Our user: {}'.format(current_user))

    def disconnectedCallback(codeno, codemsg):
        print('Disconnected from Discord rich presence RPC. Code {}: {}'.format(
            codeno, codemsg
        ))

    def errorCallback(errno, errmsg):
        print('An error occurred! Error {}: {}'.format(
            errno, errmsg
        ))

label before_main_menu:
    python:
        # Note: 'event_name': callback
        callbacks = {
            'ready': readyCallback,
            'disconnected': disconnectedCallback,
            'error': errorCallback,
        }
        discord_rpc.initialize('746209972899283025', callbacks=callbacks, log=False)
        start = time.time()
        print(start)
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Main Menu',
                'start_timestamp': start,
                'large_image_key': 'homestuck_sim_icon'
            }
        )
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()

    return
# Declare characters used by this game. The color argument colorizes the
# name of the character.
define left2 = Position(xpos=0.2, xanchor='left')
define flash = Fade(.25, 0.0, .75, color="#fff")
define e = Character('Narrator', color="#000000")
define john = Character('John Egbert', color="#0715cd")
define sams = Character('Sams Undertail', color="#008000")
define bro = Character('Bro Stirder', color="#ffa500")
define rob = Character('Rob Krazowski', color="#C0C0C0")
define karkat = Character('Karkat Vantas', color="626262")
define nepeta = Character('The Weed Woman.', color="#416600")
define doc = Character('Doc Scratch', color="#000000")
define jaed = Character('Jaed Hardly', color="#4ac925")
# The game starts here.
label start:
    python:
        callbacks = {
            'ready': readyCallback,
            'disconnected': disconnectedCallback,
            'error': errorCallback,
        }
        discord_rpc.initialize('746209972899283025', callbacks=callbacks, log=False)
        start = time.time()
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Volume 1: John and the silent protagonist',
                'state': 'Arrived on Earth',
                'large_image_key': 'johnroom',
                'start_timestamp': start
            }
        )

        discord_rpc.update_connection()
        discord_rpc.run_callbacks()

stop music fadeout 1.0
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
scene bg sky
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

e "You wake up in a cold sweat at the middle of the street, you look at the sky and feel a hint of peace."

e "After staring at the sky some more, you try to remember how you got here, but you can't."

e "You have a panic attack for some minutes before recomposing yourself."

e "You get up, dust off your clothes and walk around."

e "Suddenly, you hear someone approaching behind you."

play music "C:/Users/aline/OneDrive/Pictures/HOMEDATING SIM/game music/johntheme.mp3"
scene bg john backyard2
show john blue happy2 at left
with dissolve

john "Hello!"

e"The boy seems friendly, you come closer to him and wave your hand."

john "So, are you new in this neighborhood?"

john "..."

e "..."

john "You're not much of a talker, aren't you?"
show john blue rollingeyes at left

john"I'm not that much of a visitors guy but you seem alright, also the fact that all my friends are asleep right now. I hate timezones."

show john happy2 at left

john"Come in!"

e"You hesitantly enter the boy's house."

scene bg john room1
with fade
show john blue happy2

python:
   start = time.time()
   discord_rpc.update_connection()
   discord_rpc.run_callbacks()
   discord_rpc.update_presence(
       **{
           'details': 'Volume 1: John and the silent protagonist',
           'state': 'Johns House',
           'large_image_key': 'johnroom',
           'start_timestamp': start
       }
   )

   discord_rpc.update_connection()
   discord_rpc.run_callbacks()

john"This is my room! It's not very tidy but I like it here- -"

show john blue ceptic

john"...Wait a minute, I think there's something...different...in here..."

scene bg john room2
show john blue excited

john"Nevermind, everything's fine!"

john"So, hello new friend..? My name is John Egbert, what's yours?"

e"..."

show john blue happy2

john"(let's try something else) So, where did you come from?"

e"..."

show john blue rollingeyes
john"You really going to give me the silent treatment?"

menu:
     "Try to talk to John.":
         jump talk
     "Continue being silent.":
         jump silent

label talk:

     e"You try to talk, but you feel like something is holding you back."

     show john blue ayuwoki

     john"Uhhh, are you okay?"

     e"You manage to make some noises, but when it comes to actual words, all that comes out is a garbled mess of noises."

     e"Eventually, you manage to say hello, but nearly faint from pure fatigue."

     scene bg you tried too hard
     with dissolve

     e"YOU TRIED TOO HARD"

     jump goodendingroute

label silent:
     e"You continue being silent for the rest of the day, as John gets more and more weirded out."
     scene bg john backyard
     e"At the first opportunity he gets, John locks the door to his house in pure fear, leaving you alone in the streets."
     e"KICKED OUT ENDING."
     return
label goodendingroute:
     scene bg john room2

     show john blue concerned
     with fade

     john"Hey, buddy, are you okay, man?"

     e"You wake up, extremely confused about what happened."

     john"I'm sorry I stressed you out, you didn't have to do that for me."

     e"You make several gestures with your hands, trying to point out that you're okay."

     show john blue happy2

     john"I don't understand what you're saying right now, but I still hope we can be friends I guess."

     e"You nod and step away, waving goodbye at John."

     scene bg sky
     with dissolve

     play music "C:/Users/aline/OneDrive/Pictures/HOMEDATING SIM/game music/homestuckintro.mp3"

     e"You look at the sky again."

     e"You hear the birds singing, the sound of the wind blowing and the leaves flying out of the trees."

     e"You hear the rustling of the bushes around you, a faint noise of cars passing by."

     e"You have a feeling you're going to have a long day."

     e"..."

     e"......"

     stop music fadeout 1.0

     scene bg dungeon
     with flash

     python:
        start = time.time()
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Volume 2: Segs Dungeon with Sams Undertail',
                'state': 'Segs Dungeon',
                'large_image_key': 'dungeon',
                'start_timestamp': start
            }
        )

        discord_rpc.update_connection()
        discord_rpc.run_callbacks()

     e"...After getting existencial for a bit, you return to your senses when you're suddenly teleported to a random underground dungeon."

     e"You feel like there's someone behind you."

     play music "C:/Users/aline/OneDrive/Pictures/HOMEDATING SIM/game music/samstheme.mp3"

     sams"hey kid"

     e"OH GOD OH FU"

     show sams skele normal
     with fade

     sams"whatcha doing here boi"

     e"The skeleton appears to be extremely tall and skinny, he seems to be floating in the air."

     e"You try to talk to him and manage to spit some words out about teleporting and stuff."

     show sams skele happy

     sams"oh intersting"

     show sams skele jkbish

     sams"jk you are a lil fucking bitch i saw u wit john over there im watchin u bro lol"

     show sams skele angry

     e"You feel uncomfortable nearby him."

     sams"what are you doing here anyway"

     sams"this is my fucking segs dungeon you dont deserve to be here"

     sams"if u came to bust a nut then go to the nut corner"

     sams"bitch"

     e"You continue to spit some words out about teleporting and how you can't control your weird powers."

     sams"whatfuckin ever"

     sams"i only trust my friends"

     sams"like jhon jaed kk and shit"

     sams"i do not know you and if you get in my way ill fucking obliterate you"

     sams"now get out of my way before i step on you"

     e"You get extremely annoyed, but your efforts will not go in vain."

     e"You continue talking to Sams and blocking his path to the other side."

     sams"listen, kid"

     sams"we dont want this"

     sams"i just wanna do my fucking ultra prank on jhon"

     sams"please stop talking to me dude"

     e"You notice this is the perfect opportunity to make a new friend."

     e"You tell Sams that in exchange of his friendship, you will do the biggest prank the world has ever seen on this Jhon guy."

     stop music fadeout 1.0

     show sams skele happy

     sams"you got my attention"

     show sams skele normal

     play music "C:/Users/aline/OneDrive/Pictures/HOMEDATING SIM/game music/samstheme2.mp3"

     sams"what type of prank ur gonna do tho is it gonna actually be funny or is it gonna be scary are you gonna use any objects is it gonna be in public i have so many questions"

     e"You stand there speechless, you did not think this over, stupid."

     show sams skele happy

     sams"dude?"

     e"You can't think of any excuses so you just nod agreeingly."

     show sams skele normal

     sams"ohhhh okay i get it i get it"

     sams"ok ok so new friend lets do friend stuff"

     e"You nod again."

     show sams skele normal at left

     sams"so uhhhh if u havent noticed yet i have a lil friend captured right behind me"

     hide sams skele normal
     with dissolve

     e"Sams moves behind you so you can see the creature with more clarity."

     sams"i call him jerry"

     sams"he was doing segs rp and got permanently stuck in the fluffy handcuffs"

     sams"now hes stuck there"

     sams"forever"

     sams"funny isnt it"

     e"You get a bit disturbed by the story, but manage to fake a positive reaction."

     show sams skele normal
     with dissolve

     sams"youre a good listener dude"

     sams"i guess i can count on you with that prank"

     sams"make it kinky bro"

     sams"thats the sams trademark"

     hide sams skele normal
     with dissolve

     e"Sams slowly goes away as you reflect on what to do next."

     e"You stare at the cake that suddenly appeared and pick it up as you stare into the horizon."

     e"'Who even is this Jhon guy?' You reflect a bit about it."

     scene bg goodend2
     with fade
     pause

     stop music fadeout 1.0

     scene bg black
     with fade

     e"After some time, you finally manage to get out of the sex dungeon."

     scene bg alternia1
     with dissolve
     pause

     e"..."

     e"..."

     e"...Where the fuck are you?"

     python:
        start = time.time()
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Intermission 1: Bro Stirder Dich Irder',
                'state': 'Middle of Nowhere',
                'large_image_key': 'desert',
                'start_timestamp': start
            }
        )

        discord_rpc.update_connection()
        discord_rpc.run_callbacks()

     scene bg black
     with fade

     play music "C:/Users/aline/OneDrive/Pictures/HOMEDATING SIM/game music/intermissiontheme.mp3"

     "INTERMISSION 1"
     pause

     stop music fadeout 1.0

     scene bg coolkid scene1
     with fade

     e"You are a McRonalds worker in the middle of a desert."

     e"As you can see, you work in the middle of nowhere."

     e"Most of the employees are dead, or working at another company."

     e"You receive an extremely minimal wage, so tiny you can't even pay for coned ice cream."

     e"You live a boring life, your wife cheated on you, your friends betrayed you, all your brothers, sisters and cousins are all happily married while you are the odd one out of the bunch."

     play music "C:/Users/aline/OneDrive/Pictures/HOMEDATING SIM/game music/coolguymcgee1.mp3"

     e"At this point, you're just a sad, lonely and grumpy sack of shi- - FOR FUCK'S SAKE WHO IS IT NOW"

     label vertical_scroll_test:
        scene bg coolkid scene2 with dissolve:
            subpixel True
            yalign 1.0
            pause 2.0
            linear 10.0 yalign 0.0
        pause 12.0

     bro"hey coolkid."

     scene bg desert
     with dissolve

     show rob bla angry at right
     show coolkid bro angry at left2
     with dissolve

     rob"What are you doing here, punk?"

     bro"fucking yo mom"

     rob"Shut the fuck up about my mom."

     bro"no lol"

     rob"Don't you have like, a brother or something?"

     bro"he died"

     rob"Did you kill him?"

     bro"maybe"

     bro"i cant confirm my good buddy buddy"

     rob"You're even worse than most of the punks I meet here."

     bro"ur welcome buddy"

     rob"Fuck off."

     bro"you fuck off lol"

     rob"Go fuck your weird blind troll friend or something, I have better stuff to do."

     bro"no haha she is lesbian you idiot"

     bro"hehe"

     bro"im gay buddy."

     rob"For fuck's sake go away already."

     bro"no"

     rob"Why are you even here?"

     bro"i came to ask question"

     rob"Make it fucking quick."

     bro"so theres this dood named jhon and i wanna kill him cuz he kiled one of my fellows wit a dog pressurizer"

     rob"I'm not going to help you with that, dumbass. Get the hell out of here before I call the fucking cops."

     bro"well too bad"

     bro"cuz ill have to kill you."

     rob"..."

     rob"..Fine."

     rob"He came to the store like 3 months ago and had an argument with his weird sister, then they headed opposite ways."

     bro"ok lol bye get rekt"

     hide coolkid bro angry
     with dissolve

     stop music fadeout 1.0

     e"Bro walks away as you get increasily more annoyed at wannabe coolkids like him."

     show rob bla angry

     rob"Fucking punks."

     rob"Think they can do anything."

     rob"And that stupid hat."

     rob"Keeps just fumbling around his head like the thing's alive."

     hide rob bla angry
     show bg black
     with fade

     "BACK TO THE STORY"

     python:
        start = time.time()
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Volume 3: Happy Birthday, Karkat',
                'state': 'Alternia',
                'large_image_key': 'karkat_house',
                'start_timestamp': start
            }
        )

        discord_rpc.update_connection()
        discord_rpc.run_callbacks()

     scene bg alternia2
     with fade

     e"You are in Alternia, and you don't even know how did that happen."

     e"Just some time ago you were on Earth, inside Sams Undertail's sex dungeon, and after rummaging through the whole thing you just randomly end up in another planet?"

     e"You look around the place and rethink your decisions."

     e"You decide to teleport somewhere nearby."

     python:
        start = time.time()
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Volume 3: Happy Birthday, Karkat',
                'state': 'Karkats House',
                'large_image_key': 'karkat_house',
                'start_timestamp': start
            }
        )

        discord_rpc.update_connection()
        discord_rpc.run_callbacks()

     scene bg karkat chair
     with flash

     karkat"AH!"

     scene bg karkat chair2
     with hpunch
     pause

     scene bg karkat house
     with fade

     show karkat six angry
     with dissolve

     karkat"WHAT DO YOU THINK YOU'RE DOING HERE YOU LITTLE BIT- -"

     show karkat six thinkative

     karkat"HUH..."

     karkat"YOU'RE....DIFFERENT FROM US"

     show karkat six angry

     karkat"WHERE THE FUCK ARE YOU FROM?"

     e"You shrug."

     karkat"UGH, WHATEVER"

     e"Karkat rolls his eyes at you."

     e"You try to talk with him, end up spitting out a few words, then manage to form entire sentences, you can actually talk?"

     "COUGH COUGH, who are you?"

     e"Karkat turns around in shock."

     karkat"DID YOU JUST LIKE, TALK??"

     "ACK WHEEZE"

     "yeah"

     karkat"EWWW EWWW WHAT THE FUCK"

     show karkat six sad

     karkat"BRO, ARE YOU OKAY?"

     "no"

     show karkat six angry

     karkat"EWWWWW EWWWWW NOOOO WHY DO YOU TALK DIE"

     show karkat six sad

     karkat"*AHEM* I MEAN UH, SORRY"

     "fuck you"

     "...i mean uh, it's okay"

     karkat"SO, WHAT EVEN ARE YOU DOING HERE? I DIDN'T ASK FOR VISITORS"

     "idk man i was walking around the COUGH"

     "sewers and then i ended up here"

     show karkat six angry

     karkat"WHAT THE FUCK THE SEWER SYSTEM LEADS DIRECTLY TO MY HOUSE??? FUCK"

     "uhhhhh"

     karkat"AAAGGHHN I HATE IT HERE"

     karkat"WHY IS IT ALWAYS ON MY BIRTHDAY THAT THIS SHIT HAPPENS"

     show karkat six thinkative

     karkat"WAIT A MINUTE"

     show karkat six angry

     karkat"I JUST REVEALED PERSONAL INFORMATION TO A STRANGER THAT BROKE INTO MY HOUSE SHIT"

     "it's okay man"

     "i won't do shit"

     "yet"

     karkat"FUCK YOU, GET OUT OF MY HOUSE"

     "i'll come back"

     karkat"I'LL BUY A GUN IF YOU FUCKING COME BACK"

     "okay...yeah.. HEY LOOK LOOK IT'S A BIRD"

     scene bg black
     with fade

     e"You manage to sneak into Karkat's closet while he's distracted. You really fucked this up didn't you?"

     karkat"OH THANK GOD HE'S FUCKING GONE"

     karkat"AGH FUCK JERKING OFF I'M GONNA CALL HER ALREADY"

     e"Karkat picks up his weird troll phone and dials a number."

     nepeta"You got it wit you foo?"

     karkat"FUCK YOU YEAH I DO"

     nepeta"Meet me at the back or I'll send them again, and I won't spare you."

     karkat"YES MA'AM."

     e"After this interesting breakthrough you decide to follow Karkat to wherever he's going."

     e"You hide in the trunk of his car and wait until he drives over to the place."

     scene bg darkalley
     with dissolve

     show karkat six sad at left

     karkat"M- MA'AM..? WHERE ARE YOU?"

     python:
        start = time.time()
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Volume 3: Happy Birthday, Karkat',
                'state': 'Dark Alley',
                'large_image_key': 'darkalley',
                'start_timestamp': start
            }
        )

        discord_rpc.update_connection()
        discord_rpc.run_callbacks()

     e"You hop out of the trunk."

     "pffft bro are you fucking scared of some rando drug dealer?"

     show karkat six angry

     karkat"WHAT THE FUCK HOW DID YOU FUCKING GET IN HERE GET THE FUCK OUT"

     "nah bro i wanna be your friend imma get you rid of this fuckin wannabe gangster sucking out your money"

     show karkat six sad at right

     karkat"DO YOU EVEN KNOW WHAT SHE DOES TO PEOPLE WHO CROSS HER PATH???? GET THE HELL OUT OF HERE BEFORE SHE- ....Shit. Too late."

     play music "C:/Users/aline/OneDrive/Pictures/HOMEDATING SIM/game music/nepetatheme.mp3"

     show nepeta mad talk
     with dissolve

     nepeta"Who's the lil shit you brought wit you?"

     nepeta"Is he gonna suicide bomb on me or some shit?"

     karkat"N-NO MA'AM. I GUARANTEE THAT. NOW PLEASE, LET'S JUST DO THE TRADE."

     nepeta"I see through your lies brotha. You gonna make him snitch on me for you. I'm going to pull the fucking trigger on you."

     karkat"NO NO I SWEAR TO GOD HE GOT IN MY TRUNK SOMEHOW"

     nepeta"Why should I trust you? You shouldn't even be alive after that night."

     nepeta"Homies, get these verms out of here."

     hide karkat six sad
     with dissolve

     e"Several heavily armed men come out of hiding and start dragging Karkat to the execution room."

     karkat"NO PLEASE I DON'T WANNA DIE"

     e"You should really say something right now."

     "WAIT, STOP"

     e"The men suddenly stop."

     nepeta"What the fuck is it?"

     "I CAME INTO THE TRUNK. HE'S RIGHT, LEAVE HIM ALONE PLEASE."

     nepeta"...I'm gonna have to kill you then. You're useless to me."

     "FUCK FUCK SHIT NO PLEASE FOR THE LOVE OF GOD"

     nepeta"Dju think you could just waltz around in here as a first timer and not expect instant termination? Fuck you."

     stop music

     scene bg black
     with fade

     play music "C:/Users/aline/OneDrive/Pictures/HOMEDATING SIM/game music/gunshot.mp3"

     e"A sharp pain can be felt in your chest. God fucking damnit."

     stop music

     e"You drop dead in the ground and start being dragged to their trash compactor."

     e"You hear nothing else but silence for the past few minutes, until..."

     scene bg scratch room
     with fade

     show ds annoyed
     with dissolve

     doc"God fucking damnit."

     doc"Listen. You should be dead right now, but i'm giving you another chance. You still have a lot to do in this story, just keep going."

     doc"...I hope you live a little bit longer than that next time."

     scene bg darkalley
     with fade

     e"You wake up in the alley at the same place you died. You are covered with blood but you feel no pain and the bullet in your chest was surgically removed from your corpse. You feel fine."

     e"Karkat is probably still alive, but not only he'll never talk to you again, he's also getting considerably more screwed with the weed woman due to your entrance."

     e"You really fuck up things man. Keep going though I guess."

     e"Now you gotta plan how you'll get back to Karkat's house, how you'll win his trust back and how you will end his lifetime sentence with the Weed Woman."

     e"Let's get to planning then."

     play music "C:/Users/aline/OneDrive/Pictures/HOMEDATING SIM/game music/the definitive plan..mp3"

     "First of all, he said his birthday was today, I could make him a birthday party at some local party place, he would definitely appreciate that."

     "Second of all, i'm probably only going to get here on foot if I don't train those teleporting powers, so I better do that I guess."

     "Third of all, i'm gonna recruit the best gang I possibly can to beat that freakish lady."

     "I gotta do all of this before the sun rises or else the party places will close. Let's do this."

     e"You begin running through the Alternia streets, feeling like you can finally solve this."

     e"As you run more, you begin to feel lighter and lighter."

     scene bg karkat house
     with flash

     show karkat six angry
     with dissolve

     "I DID IT!! HOLY SHIT I DID IT! FUCK YES- oh. uhhhhh..."

     "...hey."

     karkat"WHAT THE FUCK????? WHY ARE YOU STILL HERE YOU ALMOST GOT ME FUCKING KILLED, WHAT THE FUCK IS WRONG WITH YOU"

     karkat"YOU WHITE ASS FUCKING IDIOTIC MANIAC-"

     "I'm not important right now. You need to go to Papparelio's Party Station. It's your birthday. I'm sorry for what I did."

     karkat"WHAT THE FUCK DO YOU MEAN MY BIRTHDAY"

     e"You teleport away."

     karkat"FUCK YOU"

     hide karkat six angry

     show bg darkalley
     with flash

     e"You turn to the big building they were dragging Karkat to."

     "KARKAT WANTS TO TALK WITH YOU GUYS URGENTLY."

     "I KNOW YOU'RE ALL STILL IN THERE."

     "MEET HIM AT PAPPARELIO'S. HE'LL BE WAITING."

     scene bg hideout
     with flash

     show jaed green surprised

     jaed"whjat the fuck??? who are you?????"

     "I don't know who you are either but you guys probably know who the Weed Woman is."

     jaed"oh yeah weve been trynna hunt her down for liek a month now ig"

     "I found her and her gang. In Papparelio's. Be there. When I say now, you guys'll attack."

     jaed"sure idk :/"

     scene bg party room
     with flash
     stop music fadeout 1.0

     e"You are finally going to end all of this. Good luck."

     play music "C:/Users/aline/OneDrive/Pictures/HOMEDATING SIM/game music/happybirthdaykarkat.mp3"
     show karkat six thinkative at right
     with dissolve

     python:
        start = time.time()
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Volume 3: Happy Birthday, Karkat',
                'state': 'Papparelios Party Station',
                'large_image_key': 'party',
                'start_timestamp': start
            }
        )

        discord_rpc.update_connection()
        discord_rpc.run_callbacks()

     karkat"THIS PLACE LOOKS FUCKING WEIRD. WHY IS IT SO OVERREALISTIC? WHAT ARE THOSE FUCKING MEAT STATUES THAT LOOK LIKE... BIG... WEIRD.. PINK BABIES... EUGH WHAT THE FUCK IS THIS PLAACE"

     "I invited you here because I care man"
     "I'm sorry for almost making you get executed."

     karkat"UMMM... OKAY... YEAH SURE..... THIS BIRTHDAY IS FUCKING AWFUL THOUGH"

     "uhhh okay"

     e"You start to hear the rustling of heavy equipment and machinery under the tables. They are here. Now we just need her to start the party."

     karkat"WHY DIDN'T YOU INVITE ANY OF MY FRIENDS THIS IS FUCKING AWKWARD AND PLAIN TERRIFYING"

     "sorry bro idk who your friends are"

     karkat"AGH FUCK WHY DOES IT ALL SMELL SHITTY THERE'S NOT EVEN FOOD IN HERE YET"

     "..."

     e"You start to hear heavy footsteps coming from the door. She's here."

     show nepeta sad at right
     with dissolve

     nepeta"Wow, what a nice place. I heard they like to play fancy music at 7 PM."

     nepeta"Hey little guy, you're still alive from what I see."

     nepeta"I just wanted to apologize for what happened earlier today. I've been trying to get into rehab recently, it's been really hard since Karkat killed my husband 5 months ago."

     "YOU DID WHAT?????"

     show karkat six angry

     karkat"SHUT. THE FUCK UP."

     nepeta"Oh, you didn't know that?"

     karkat"THIS HAS BEEN THE WORST BIRTHDAY EVER BUT AT LEAST I'M STILL FUCKING ALIVE"

     nepeta"I really need to restart my life. God, it's all a fucking mess. I miss when everything was simple."

     e"You look at the clock and see that it's 6:59 PM. It's almost time."

     stop music fadeout 1.0

     karkat"WHY DID THE FUCKING MUSIC STOP THAT WAS THE BEST PAAAART"

     karkat"THANKS FOR THE EFFORT I FUCKING GUESS DUDE"

     nepeta"Oooo, it's the time."

     e"3.... 2.... 1..... And....."

     "....NOW!"

     hide nepeta sad
     hide karkat six angry
     scene bg complete party room shootout
     with flash
     play music "C:/Users/aline/OneDrive/Pictures/HOMEDATING SIM/game music/the battle..mp3"
     play sound "C:/Users/aline/OneDrive/Pictures/HOMEDATING SIM/game music/shoot.mp3"

     show nepeta scared at right
     show karkat six angry at right

     nepeta"WAIT??? IS THIS AN AMBUSH???"

     karkat"YEAH WHAT THE FUCK DUDE IS THIS AN AMBUSH"

     "i... i...."

     hide nepeta scared
     with dissolve

     e"Nepeta gets shot and falls to the ground."

     karkat"OH JESUS WHAT THE FUCK"

     karkat"WE GOTTA GET THE HELL OUT OF HERE"

     "SHIT SHIT SHIT"

     "I'M SORRY I'M SORRY OH MY GOD WE'RE ALL GOING TO DIE"

     karkat"SHUT THE FUCK UP STOP BEING A CRYBABY WE CAN STILL SURVIVE THIS SHIT"

     e"You and Karkat hide under a desk."

     "FUCK FUCK FUCK SHIT SHIT WHY DID I NOT THINK THIS OVER NOW WE'RE BOTH GOING TO DIE"

     karkat"AT LEAST SHE'S FINALLY GONE"

     "Was it WORTH IT THOUGH??"

     "We just ENDED THE LIFE OF A BROKEN YOUNG WOMAN WHO COULD'VE DONE SO MUCH WITH HER LIFE"

     karkat"FUCK YOU"

     karkat"NEVER SAY THAT SHIT TO ME EVER AGAIN"

     karkat"LET'S HEAD TO THE FUCKING EXIT NOW"

     e"You and Karkat walk in the middle of the battlefield, every bullet that passes by is just one centimeter away from certain death. Your luck will not allow it though. Karkat's luck will."

     hide karkat six angry
     with dissolve

     e"Karkat falls in the ground after getting shot in the leg."

     "HOLY SHIT ARE YOU OKAY"

     karkat"AUGH... FUCK... YEAH I CAN'T DO IT....FUCK...."

     "OH MY GOD OH MY GOD I'M SO SORRY I'M SO SORRY"

     scene bg complete party room shootoutfire
     with flash

     e"Karkat takes his last breath as you run away crying from the party place."

     scene bg black
     with flash
     stop music fadeout 1.0
     stop sound fadeout 1.0

     play sound "C:/Users/aline/OneDrive/Pictures/HOMEDATING SIM/game music/explos.mp3"

     e"A huge explosion occurs in the restaurant, knocking you down."

     stop sound fadeout 1.0

     play music "C:/Users/aline/OneDrive/Pictures/HOMEDATING SIM/game music/act3end.mp3"

     e"You try to get up, but decide against it as you are too tired to do so. You faintly see the sun rising from the horizon as your eyes slowly close."

     e"You lay down and sleep in the big, comfortable concrete floor outside the restaurant. Today was a long day."

     e"END OF ACT 3"

     stop music fadeout 1.0
