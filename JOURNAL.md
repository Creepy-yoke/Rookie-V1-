# Keyboard Build Journal

## Entry 1 — Figuring out hardware and layout
Date: 07/30/2026 <br>
***Time worked: 2 hr*** 

I started planning out the layout for my keyboard. I really didn't want a  keyboard where your hand are kept TOO close and become sweaty, So I found a layout that have some space between, but at the same time, I wanted to maintain most of the function that I would have on a conventional laptop. So, I settled with a 65% layout, I used the reference picture below. its called the ALICE LAYOUT.
I also made my  layout in https://www.keyboard-layout-editor.com/                                                                           
HERE'S THE KEYBORAD [RAW DATA](https://github.com/Creepy-yoke/Rookie-V1-/blob/main/LAYOUT.json)
###### *TOTAL HOURS FOR LAYOUT* :  2 hr

<img width="1080" height="607" alt="image" src="https://github.com/user-attachments/assets/d08eb092-acad-4209-be25-c966cc5bad15" />
<img width="432" height="189" alt="layouut" src="https://github.com/user-attachments/assets/d36e256b-bb1d-48da-ae0b-e1364ab0c700" />
                                                                                                                
## Entry 2 — MAKING my SCHEMATIC
Date: 7/31/2026 <br>
***Time worked: 4 hr*** 

Today I started making my first keyboard schematic in KiCad. First, I added all the symbols from the symbol library, like the switches, diodes, SK6812 RGB LEDs, Raspberry Pi Pico, OLED, and the joystick so it will look cool. I started with the matrix and made a lot of nice progress with tracing and connecting the other components. I also fixed some wiring and checked that everything was connected properly.
<br>  
<img width="1257" height="604" alt="MATRIX SCHEMTIC SWITCHES" src="https://github.com/user-attachments/assets/3d787b9c-45da-429b-a8d7-0bd7fff881c3" />
<img width="616" height="605" alt="KEYPORD PIC SHEMATIC" src="https://github.com/user-attachments/assets/b2e6d629-10a8-40b7-8733-c4f7630ee40b" />



## Entry 3 — Adding the Other Components in Schematic
Date: 8/01/2026 <br>
***Time worked: 3 hr*** 

After the main keyboard matrix was done, I added the extra features I wanted. I added an OLED for displaying information and a joystick that I can use for mouse control. I also added resistors and capacitors for the RGB . I considered adding some other things during the project, but I removed or changed a few ideas to keep the keyboard manageable.                                     
It's easily subject to change after I add the rotary encoder. I'm not exactly sure how I'm supposed to incorporate the encoder right now. All of the other components are pretty simple it just took me some time to connect other componets see
see u later, bye                                                                                    

I have finished my RGB light matrix thingyy , and I was having some  ERRORS while arranging my RGB BACKLIGHT (Matrix) called the   "Input power pin not driven by any Output power pins" and its telling to  Add  PWR_FLAG (its purely a schematic validation tool) ,  near +5v power net line and it  WORKED  (Cleared all the Errors)    
(UPDATE FOR THiS PROBLEM:- It can also be solved after I connected my 5v to VBUS on Raspberry Pi poco so there was no need for PWR_flag )
<br>
<br>
<img width="824" height="565" alt="image" src="https://github.com/user-attachments/assets/d199213e-dd65-445d-975f-5bd75159b55b" />
<img width="623" height="384" alt="image" src="https://github.com/user-attachments/assets/83f04c98-e525-4b72-b055-d60e63be806a" />
<br>
  AND TIME TO GET BACK TO KICAD , SEE U 

## Entry 4 — Wiring UP Everything to each other
Date: 8/02/2026 <br>  
***Time worked: 4 hr*** 

<br>
Wired up the EC11 encoder (A/B/C for rotation, S1/S2 for the click). Also connected the joystick analog it was preety simple to connect then, Spent a while figuring out OLED options — I wanted A looong screen put apparently 4 pin OLEDs don't come in 256x32, so I had to settle for a 128x32 display,  which gave a me a bit more surface area. here's a LOOK!
<br>
<br>
<img width="769" height="582" alt="image" src="https://github.com/user-attachments/assets/cc9e7f90-6eb1-41f3-a087-e7e7c042cb34" />
<br>
<br>
I still need to connect all the components (some parts like :- key matrix, RGB matrix thingyy and etc.) and almost  forgot add  stabilizer and mounting holes and also need to assign the footprints for the components
OKAY! the only things I need to do is assign footprints and solve some ERC ERRORS ( Electric Rules Checker ) , 
<br>
<img width="675" height="437" alt="image" src="https://github.com/user-attachments/assets/939c21b6-cff7-426c-b35e-6d89d0860a57" />

### UPDATE: I have removed the Rotary Encoder due to less GPIO pins
<br>

## Entry 5 — Assigning Footprints
Date: 8/04/2026 <br>
***Time worked: 3 hr*** 

The schematic is mostly finished, I started assigning footprints to the components. This was a little confusing at first because I learned that the symbol in the schematic and the actual footprint on the PCB are different things. I used the KiCad libraries and the ai03 keyboard library (Downloaded from GitHub) to find suitable footprints for the switches, stabilizers and other components.

<img width="360" height="400" alt="image" src="https://github.com/user-attachments/assets/935c620a-a33f-4145-bd1b-302839dcd7b4" />
<img width="360" height="400" alt="image" src="https://github.com/user-attachments/assets/92089a86-d262-4f94-afbc-d482ee58fd79" />
<img width="360" height="400" alt="image" src="https://github.com/user-attachments/assets/0e3d8441-f0d7-4a6b-b70d-c9376467eba7" />
<img width="400" height="150" alt="image" src="https://github.com/user-attachments/assets/ed8846e9-3c24-44a4-84c7-ceeffd28b952" />

## Entry 6 — FINAL LOOK OF SCHEMATIC
Date: 8/05/2026 <br>
***Time worked: 2 hr*** 

### Okay it's me after many  hours later :- 
Wasup people !  I am  glad to announce that I have FINISHED my PCB SCHEMATIC after working Continuously on it  , LETS GO! 
After spending a lot of time checking connections and making sure every component was placed correctly ,  I made tremendous progress with the Schematic and was able to complete it , everything went extremely well this session. 
I implemented resistors and capacitors wherever I needed them I was able to complete the entire schematic. I also assigned footprints to all the components. Along the way I learned a lot about how different parts connect together and fixed several small mistakes that were causing errors.
HERE ARE SOME PIC OF FINAL LOOK :- 
###### *TOTAL HOURS FOR SCHEMATIC* : 16 hr (Entries 2-6)
<img width="1037" height="366" alt="image" src="https://github.com/user-attachments/assets/7caafe6a-a66c-4d30-a9d9-e0d3e020938f" />

Seeing the schematic finally come together feels really satisfying and everything went extremely well this session. 

#### NOW  IT'S READY FOR THE PCB LAYOUT , (BUT FIRS I NEED SOME REST, MY BACK IS PAINING)

 ## Entry 7 — MAKING my PCB
Date: 8/06/2026 <br>
***Time worked: 3 hr*** 

###  Arranging the PCB
After assigning the footprints, I moved everything from the schematic into the PCB Editor. At first there were components everywhere with ratsnest lines connecting each other it was very confusing at first when I started arranging the components neatly on the PCB manually according to my Alice layout. So, first I placed the switches according to my Alice layout  because they were the most important parts. After that I arranged the OLED, Joystick, Micro controller ( Raspberry Pi Pico ) and the smaller components around them (stabilizer, mounting holes).
<br>
<img width="1073" height="465" alt="image" src="https://github.com/user-attachments/assets/7b749477-4d4e-48d5-9fdc-d83849447b36" />

## Entry 8 — Routing the PCB 
Date: 8/07/2026 <br>
***Time worked: 4 hr*** 

After arranging all the components on the PCB, I started working on routing the traces.
The ratsnest lines showed me which components still needed to be electrically connected. My goal was to route these connections while keeping the PCB neat and avoiding unnecessary overlaps.

### Routing Keyboard Matrix
So I first focused on the keyboard matrix connections, routing the traces between the switches and diodes. Since there were many connections it took me some time to get there.
<br>
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/8cb38780-9edd-4067-a04d-c9b416727884" />

<br>
Now for the Oled display, Joystick, RGB LEDs and Raspberry Pi Pico
After routing the matrix, I worked on the connections for the Oled display, Joystick, RGB LEDs and **Raspberry Pi Pico. **
OLED and Joystick were easy but the       RGB Leds took me a lot of time to complete

## Entry 9 — RGB LED Routing 
Date: 08/08/2026 <br>
***Time worked: 3 hr*** 

The RGB LEDs required additional routing because each LED needed connections for power, ground, data input, and data output.
I connected the LEDs in sequence so that the RGB data signal could travel from one LED to the next.

### Power and Ground :-
I paid extra attention to the power connections because the RGB LEDs can draw significantly more current than the other components.
I also had to think about the different power connections, especially the 5V, 3.3V, and l also kept the size of the power line (5v,3v3) a bit thicker 0.3 or 0.4 cause it prevents the melting of the copper
 If l am right
I tried to keep the power routing clean and make sure the traces had suitable paths 
And for the GND (Ground Plate) l did not connect it manually thanks to an friend l got to know if we add GND plate it will connect all the GND's all by itself, So that saved me some time rather than  doing it manually.
<br>
<img width="1056" height="447" alt="image" src="https://github.com/user-attachments/assets/4c08cdeb-8cc4-4430-9f74-943f243f5e17" />


##  Entry 10 — Routing All Connections To Pico PI + DRC ERRORS
Date: 8/010/2026 <br>
***Time worked: 4 hr***

Well this was preety easy , l just need to route the  connections of Keyboard Matrix (Rows and Columns) , Rgb  to  there GPIO pins on the Pico Pi
( Joystick and OLED was already done) 

- PCB Layers :-
- F.cu  (Red)
- B.cu (Blue)
- Vias (Dots kinda thing that lets u use both layers)
This made routing much easier,and thees are the layers l used  
Keyboard Matrix , Rgb , Joystick  , Display -} u can check out my file [HERE](https://github.com/Creepy-yoke/Rookie-V1-/blob/main/Rookie%20V1%20(PCB)/Rookie%20V1.kicad_pcb) downloadit and clear ur doubts.

<br>

##### DRC Errors for PCB :-

After completing most of the routing, I ran the Design Rules Checker (DRC) in KiCad to look for problems such as:
Unconnected connections
Clearance violations
Overlapping or conflicting tracks

I then went back and fixed the errors that appeared It was no sweat just some text were intersecting with dome part and some layer like dots that l mistakenly added just delete those 
At this point, the PCB was starting to look GREAT 👍🏻 
<br>
<img width="662" height="524" alt="image" src="https://github.com/user-attachments/assets/9213d0af-47b2-4bdf-aa21-928f8f199b56" />
##### Next step: To add its shape

##  Entry 11 — SHAPE OF THE PCB 
Date: 8/11/2026 <br>
***Time worked: 2 hr*** 

Like this was preety much easy to just selected the layer Edge Cut and put lines accordingly to my reference pic at top , I can also just make it an rectangular box but i just chose that cause while l design my case it will give me an idea for the perimeter ig. The hard part here was keeping the angles the same.
And after that it was good to go 
3D (keycaps , hotswapp , display , Joystick )
I added there 3d models from GrabCAD so l can get a preety good look how my Keyboard going to look and it also helps me to know  how much height should be the walls (boarders) of the case. 
<br>
<img width="1061" height="474" alt="image" src="https://github.com/user-attachments/assets/87549082-058a-4c85-8c9d-9cad6780b664" />
<br>

## Entry 12 — Last look of the PCB
Date: 8/12/2026 <br>
***Time worked: 2 hr***

<br>
<img width="1050" height="480" alt="image" src="https://github.com/user-attachments/assets/faf2e541-6268-4f27-9ddd-df7d07e9a735" />

<br> 


### Okay it's me after many  hours later (AGAIN) :- 
HOWDY FELAS!, I am here to proudly state that I have have FINISHED my PCB  after working Continuously on it well, HURRAY!
I am not gonna lie it took a lot lot lot of time bruh (MOST WITH THE GD ERROR) , I was about to quit but I am glad that I Didn't. Overall, everything went extremely well this session, and I’m really happy with how much progress I made. Completing the PCB feels like a big step forward for my keyboard project
Well , l am relieved and the last step is just to make an CASE for it 
Cant wait to finish it  and look how it turns out, supper dupper excited.      
SO LETS GET GOING ,BYE    
<br>

###### *TOTAL HOURS FOR PCB* :  18hr (Entries 7-12)

## Entry 13 — THE CASE
Date: 8/13/2026 <br>
***Time worked: 1 hr 30 min***

### Choosing the mount
Well I got to pick a MOUNT first cause there's a lot,
                                                                                                                                       
<img width="1080" height="896" alt="image" src="https://github.com/user-attachments/assets/38117efe-1d2c-481f-8601-7db5a8cde2fd" />
                                                                                                                                      
I will go with The PLATELESS MOUNT cause I want to see my PCB, I'll add a plate in future. What's the points of having an Mechanical Keyboard if u don't have the fell while typing , ANYWAYS, TO THE DESIGNIG PART.
 
 For making the case I am using software called Onshape u may be familiar with it cause it's only one I know and also I am following the guide (DOCS) of HACKPAD just the CASE part

 I wanted the light's to shine in front of the keyboard and joystick border must be in hexagon 
  Here's some reference pic from AI pic I created.
  <br>
<img width="1774" height="887" alt="image" src="https://github.com/user-attachments/assets/d2b1ccdd-2159-4422-a214-0280c4b94a30" />

<img width="478" height="703" alt="image" src="https://github.com/user-attachments/assets/f6d5fd0b-18cb-4199-878b-1d4eedd73dc6" />

 <br>
 
 ## Entry 14 - DESIGNIG THE CASE
 Date: 10/18/2026 <br>
 ***Time worked: 1 hr 17 min***
 
 So, I designed the body and I cant add my PCB .step file cause its make my the software too slow and laggy so I fixed this by importing the PCB into Onshape as one composite part, which made the file much faster. I also added the screw holes and the light bar in front wall of the case and a cutout shape where the Pico pi micro-usb goes.

 
 HERES THE LOOK , still need to do a lot of work tho.
 <br>
 <br>
<img width="884" height="506" alt="image" src="https://github.com/user-attachments/assets/eda7594b-164d-456b-860e-aad9e4cb618b" />

 ## Entry 15 - FINAL LOOK of the CASE
  Date: 10/24/2026 <br>
 ***Time worked: 1 hr 30 min***
 
I have finished the case and ready to submit i have added the PCB to the case and the screw holes position was not correct (where the screw goes M3). Also the case looks simple i have the plan to stick stickers that I have, you can customize it by yourself if you like . Also the light bar was out of the positoin too so relocated it and i do not need the cutout for micro-usb so I have removed it.

<br>

[HERE](https://cad.onshape.com/documents/d718c6f2bf8f1306fd075cc1/w/1f65e877d90938ffe0379d49/e/f8198137f6d496df892af1f1?renderMode=0&uiState=6add21e3e21be264acb29ac8) is my Onshape link, you can check it out
###### *TOTAL HOURS ON CASE* :  4 hr 17 min (Entries 13-15)

<img width="1320" height="754" alt="image" src="https://github.com/user-attachments/assets/98f4cb56-550c-4ac0-98d6-55091da3737f" />



 ## Entry 16 - Planning the FIRMWARE
 Date: 10/26/2026 <br>
 ***Time worked: 40 min***

<br>

<img width="550" height="700" alt="image" src="https://github.com/user-attachments/assets/d7c10dde-fdc1-4735-bf20-65308e544450" />

<br>


 So, I have watched many videos and did some research on the firmware, so I decided I was going with the KMK firmware, which is the simplest. I know the steps as soon as I get my components (parts). Really quickly I am going to touch on what is KMK and why am I using it.
 <br>

“KMK is a feature-rich and beginner-friendly firmware for computer keyboards written and configured in [Circuit Python](https://github.com/adafruit/circuitpython).”
Here is a link to their [GitHub](https://github.com/KMKfw/kmk_firmware) with more information.
I am using it because I find it much easier to use that QMK, the standard for most keyboards. It can all be done in plain text on any computer and is in Python.
I’m making this instructable and the because I want more eyes on this project because I think its great, and I’m not good enough at python to help build software so I hope someone who does this can help with this project.



 ## Entry 17 - FIRMWARE STEPS (After I get my parts) :
 Date: 10/27/2026 <br>
 ***Time worked: 50 min***

These are the steps that I will be following in the future after I get my components (parts). There are only 2 steps that I need to do before writing the firmware code. So I will be writing the code before getting my parts so that when my parts are delivered to me, I will just copy the file that contains the code for my keyboard into the Pico.

- STEP 1 - So first I need to install Circuit Python on the Pico; for this, I just need to download the CircuitPython UF2 from [Adafruit's Website](https://circuitpython.org/board/raspberry_pi_pico/). Now I need to plug my Pico into my computer/laptop, and it will show as an external storage device; then we just need to drag the UF2 file that we just downloaded into the Pico. It should eject itself and install CircuitPython and show backup. AND just like that, bada bing bada boom Circui tPython is installed on my Pico. 

<br>

- STEP 2 - OK, now I need to run the firmware on this bad boy (Pico). So I need to head over to [GITHUB](https://github.com/KMKfw/kmk_firmware) and download the latest version of KMK firmware as a zip file. After downloading the file, Ectract it/Unzip it. From that unzipped KMK file, we only need 2 things, which is KMK folder and the boot.pi . I will be copying those two from the folder and pasting them into the Pico (After I get my parts).

<br>

<img width="496" height="397" alt="Screenshot 2026-10-30 033558" src="https://github.com/user-attachments/assets/7fa784a6-0bf0-4b4f-bb51-6d65a4f8b68d" />


<br>
 
SO, that was the step I need to take before writing or pasting the firmware code into the Pico. The only thing left is to write the code.



 ## Entry 18 - Writing the FIRMWARE (CODE)
 Date: 10/28/2026 <br>
 ***Time worked: 1 hr***

SO, wassup people in this brand new day. I have written the code for my firmware for my keyboard. I have created a file named called " main.py " (can also use the file name "code.py "). This is mainly done using a code.py file. There should be one on the Pico; if not, we just need to create a new file called code.py. I can just ignore that and make my own file. I will be using VS Code to write my code; I can also use Notepad++ or just Notepad, I can edit this file using Notepad++, but this can also be done in Notepad in the future.
<br>
I just need to copy the example format from the GitHub page and paste it into the main.py file; I still need to edit this according to my rows, columns, and keymaps, etc.


<p align="center">
  <img src="https://github.com/user-attachments/assets/87250d14-595b-46fd-af98-8574130e2679" width="48%" />
  <img src="https://github.com/user-attachments/assets/1567aea3-72e4-4da3-a00a-12529deba50c" width="50%" />
</p>







<br>


I need to give this file all the specifics of my num pad.
To do this, I first need to give the code the pin numbers for the rows and columns in lines. Next, I need to change the diode orientation, as the code needs to know how everything is set up. I changed it from COL2ROW to ROW2COL.
Most of the way done now; I just need to add the key map, or what keys should be where. I referenced this web page to find all the key codes I can use. I won’t go over this in detail but take a look and what I used and make any changes you want. <br>
OK, I WILL BE SEEING U AFTER SOME FINAL TOUCHES TO THE FIRMWARE. PROBABLY I WILL DO IT TOMORROW


## Entry 19 - LOOK AT THE FIRMWARE 
 Date: 10/29/2026 <br>
 ***Time worked: 34 min***


OK, I just want to make an entry that I have now finished assigning all the keys in the keymap, including their positions and functions. It took some time to organise the key positions and double-check the assignments, especially because of the angled Alice layout. I am happy that I have finally completed this part because it brings my keyboard one step closer to becoming a working product rather than just a PCB design.
I also completed the GPIO pin assignments for the keyboard matrix, connecting the appropriate pins for the rows and columns. I made sure that the firmware layout matches the physical key placement on my PCB so that each key will correspond to its correct position when pressed.
This is an important step towards getting my keyboard fully functional, as the firmware will allow the microcontroller to recognise key presses and send the correct inputs to the computer.

<br> 

<img width="1089" height="651" alt="image" src="https://github.com/user-attachments/assets/79c49df7-da81-4646-8b34-143dfe3ab4df" />

<br>

## Entry 20 - FINAL LOOK at the FIRMWARE 
 Date: 10/30/2026 <br>
 ***Time worked: 28 min***

So I am here to give you the wonderful news that I have competed our firmware for my Alice Layout Keyboard. So heres what i did i this 28 mins, first i have imported the RGB extension thing the made a another layer mostly to control my RGB lghts. And alsoi got few bugs in my keymap and


## Entry 21 - CALCULATION 
 Date: 10/30/2026 <br>
 ***Time worked: 2 hr***

So, I first made a table and then listed out what components I need for my keyboard and added them to the Excel sheet. I still need to confirm a few things like prices and check before I submit it.

<br>

 <img width="1233" height="671" alt="image" src="https://github.com/user-attachments/assets/4befad0b-5cef-4099-a1f8-91f02f32d168" />

<br>


Ok, just finished calculating how much this would cost, with the BOM and everything. Everything is good to go; finally completed the whole thing. Here are the results: 

<br>

### Bill of Materials


| S.no | Product Name | Specification / Footprint | Quantity | Estimated Cost (INR) | Link |
|---:|---|---|---:|---:|---|
| 1  | Raspberry Pi Pico (USB-C) | RP2040 development board | 1 | ₹383.50 | [Supplier](https://www.thingbits.in/products/raspberry-pi-pico) |
| 2  | Gateron G Pro 3.0 Brown switches | MX-compatible, 5-pin | 70 bought, 66 used | ₹1,330 for 7 packs of 10 | [Supplier](https://meckeys.com/shop/accessories/keyboard-accessories/key-switches/gateron-g-pro-3-0-switch/) |
| 3  | Gateron hot-swap sockets | CPG151101S11 / KS-2P02B01-01-a1; verify footprint | 66 | ₹650 (check this covers 66) | [Supplier](https://stackskb.com/store/gateron-hotswap-sockets/) |
| 4  | Matrix diodes | 1N4148W-7-F, SOD-123 | 70 bought, 66 used | ₹86.45 | [Supplier](https://www.ktron.in/product/1n4148w-7-f-fast-switching-diode/) |
| 5  | SK6812 MINI-E | Addressable RGB LEDs | 70 bought, 66 used | TBD (earlier estimate ₹559) | [Supplier](https://www.amazon.in/100PCS-Similar-WS2812B-Individually-Addressable/dp/B0DMNBBM9V) |
| 6  | OLED display | SSD1306, 0.91-inch, 128x32, I2C | 1 | ₹165.25 | [Supplier](https://amelectronics.in/product/0-91-inch-iic-4-pin-oled-display-module-ssd1306-white/) |
| 7  | Analog joystick module | X/Y axes with push button | 1 | ₹100 + GST | [Supplier](https://robboquad.com/analog-joystick-module/) |
| 8  | Ceramic capacitor | 100 nF, 0603 | 9 | TBD | Add supplier link |
| 9  | Tantalum capacitor | 470 uF, EIA-7343-31 (D case) | 1 | TBD | Add supplier link |
| 10 | Resistor | 330 ohm, 0603 (RGB data line) | 1 | TBD | Add supplier link |
| 11 | PCB-mount stabilizer | 2U | 1 | TBD | Add supplier link |
| 12 | PCB-mount stabilizer | 2.25U | 3 | TBD | Add supplier link |
| 13 | PCB-mount stabilizer | 2.75U | 2 | TBD | Add supplier link |
| 14 | Pin header | 1x04, 2.54 mm (OLED) | 1 | TBD | Add supplier link |
| 15 | Pin header | 1x05, 2.54 mm (joystick) | 1 | TBD | Add supplier link |
| 16 | Pico header pins | 2x 20-pin, only if the Pico has none | 2 | TBD | Add supplier link |
| 17 | M3 screws | 6 mounting holes; length from final CAD | 6 | TBD | Add supplier link |
| 18 | Custom PCB | Two-layer FR-4, Rookie V1 Alice | 1 per keyboard | TBD | [Get quote](https://www.lioncircuits.com/) |
| 19 | Custom keyboard case | Rookie V1 | As per CAD | ₹0 | printed at home |
| 20 | MX-compatible keycap set | Must fit the exact Alice layout | 1 compatible set | TBD | Add supplier link |
| 21 | USB cable | Type-C | 1 | ₹0 if already owned | n/a |



### Partial Cost Summary

The currently priced items total approximately **₹2,715.20 before joystick GST**.
This is not the full keyboard cost. RGB LEDs, remaining electronic parts,
stabilizers, mounting hardware, PCB fabrication, plate, case, keycaps
and shipping still need confirmed prices.
The rotary encoder is not included because it was removed from the design.



[HERE](https://github.com/Creepy-yoke/Rookie-V1-/blob/main/BOM%20V1.csv) is my Kicad BOM.csv













 
