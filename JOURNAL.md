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
Date: 8/03-04/2026 <br>
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
Date: 8/09-10/2026 <br>
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


### DRC Errors for PCB :-
After completing most of the routing, I ran the Design Rules Checker (DRC) in KiCad to look for problems such as:
Unconnected connections
Clearance violations
Overlapping or conflicting tracks

I then went back and fixed the errors that appeared It was no sweat just some text were intersecting with dome part and some layer like dots that l mistakenly added just delete those 
At this point, the PCB was starting to look GREAT 👍🏻 
<br>
<img width="662" height="524" alt="image" src="https://github.com/user-attachments/assets/9213d0af-47b2-4bdf-aa21-928f8f199b56" />
### Next step: To add its shape

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

[HERE](https://cad.onshape.com/documents/d718c6f2bf8f1306fd075cc1/w/1f65e877d90938ffe0379d49/e/f8198137f6d496df892af1f1?renderMode=0&uiState=6add21e3e21be264acb29ac8) is my Onshape link, you can check it out.
<br>

###### *TOTAL HOURS ON CASE* :  2 hr 47 in

<img width="1320" height="754" alt="image" src="https://github.com/user-attachments/assets/98f4cb56-550c-4ac0-98d6-55091da3737f" />



# Entry 16 - CALCULATION 
 Date: 10/25/2026 <br>
 ***Time worked: 2 hr***

Just finished calculating how much this would cost, with the BOM and everything. Here are the results:
<br>

### Bill of Materials


| S.no | Product Name | Specification / Footprint | Quantity | Estimated Cost (INR) | Link |
|---:|---|---|---:|---:|---|
| 1  | Raspberry Pi Pico (USB-C) | RP2040 development board | 1 | ₹383.50 | [Supplier](https://www.thingbits.in/products/raspberry-pi-pico) |
| 2  | Gateron G Pro 3.0 Brown switches | MX-compatible, 5-pin | 65 | ₹1,330 for 7 packs of 10 | [Supplier](https://stackskb.com/store/gateron-g-pro-3-0-brown-ks-9-tactile-switch-pack-of-10/) |
| 3  | Gateron hot-swap sockets | KS-2P02B01-01-a1; verify footprint | 65 | ₹650 | [Supplier](https://stackskb.com/store/gateron-hotswap-sockets/) |
| 4  | Matrix diodes | 1N4148W-7-F, SOD-123 | 70 bought, 65 used | ₹86.45 | [Supplier](https://www.ktron.in/product/1n4148w-7-f-fast-switching-diode/) |
| 5  | SK6812 MINI-E | Addressable RGB LEDs | 70 bought, 65 used | TBD | [Supplier](https://shiroganelab.com/products/keyball-rgb-led-sk6812mini-e) |
| 6  | OLED display | SSD1306, 0.91-inch, 128x32, I2C | 1 | ₹165.25 | [Supplier](https://www.robogears.in/shop/controllers-systems-displays-display-modules-60/39712-0-91-i2c-oled-display-module-128x32-2605) |
| 7  | Analog joystick module | X/Y axes with push button | 1 | ₹100 + GST | [Supplier](https://robboquad.com/analog-joystick-module/) |
| 8  | Ceramic capacitors | 100 nF; package must match PCB | Confirm from KiCad | TBD | Confirm schematic |
| 9  | Bulk capacitor | 470 uF; voltage/package must match PCB | 1  | TBD | Confirm schematic |
| 10 | RGB data resistor | 330 ohm; package must match PCB | 1  | TBD | Confirm schematic |
| 11 | Additional resistor | Value/package to be confirmed | 1  | TBD | Check schematic |
| 12 | PCB-mount stabilizer | 2U | 1 provisional | TBD | Confirm layout |
| 13 | PCB-mount stabilizer | 2.25U | 3 provisional | TBD | Confirm layout |
| 14 | PCB-mount stabilizer | 2.75U | 1 provisional | TBD | Confirm layout |
| 15 | Pico header pins or sockets | Only if required by mounting method | As required | TBD | Confirm assembly |
| 16 | OLED connector/header | 4-pin, only if used | As required | TBD | Confirm assembly |
| 17 | Joystick connector/header | Matching the selected module, only if used | As required | TBD | Confirm assembly |
| 18 | M3 screws and standoffs | Length/quantity from final CAD | As required | TBD | Confirm assembly |
| 19 | Custom PCB | Two-layer FR-4, Rookie V1 Alice | 1 per keyboard | TBD | [Get quote](https://www.lioncircuits.com/) |
| 20 | Custom keyboard case | Rookie V1; include all separate case pieces | As per CAD | ₹0 | printed at home |
| 21 | MX-compatible keycap set | Must fit the exact Alice layout | 1 compatible set | TBD | Add supplier link |
| 22 | USB cable | Type - C     | 1 if supplied | TBD | Confirm connector |


### Partial Cost Summary

The currently priced items total approximately **₹2,717.20 before joystick GST**.
This is not the full keyboard cost. RGB LEDs, remaining electronic parts,
stabilizers, mounting hardware, PCB fabrication, plate, case, keycaps
and shipping still need confirmed prices.
The rotary encoder is not included because it was removed from the design.



[HERE](https://github.com/Creepy-yoke/Rookie-V1-/blob/main/BOM%20V1.csv) is my Kicad BOM.csv

 
