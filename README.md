<div align="center">
<h1> Rookie V1 </h1>
<p>Hi, I am making a cool Custom Keyboard from scratch, by myself</p>

</div>

<div align="center">

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Project](https://img.shields.io/badge/Project-Hardware-yellow.svg)

</div>


<p align="center">
  <a href="#about-the-project">About</a> •
  <a href="#repository-structure">Structure</a> •
  <a href="#schematic-on-kicad">Schematic</a> •
  <a href="#pcb-on-kicad">PCB</a> •
  <a href="#bill-of-materials">BOM</a> •
  <a href="#license">License</a> •
  <a href="#credits">Credits</a> •
</p>


### About the Project

This is my custom 65% Alice layout keyboard that I’m designing from scratch. I started with watching some YOUTUBE videos and also took some help of AI for boosting up my Knowledge.
then I worked on schematic of the keyboard matrix, diodes, switches,  OLED display, Joystick, and the other components.
After finishing the schematic, I moved on to designing the PCB. I arranged the components, worked on the routing, and checked the connections and DRC errors to make sure everything was correct.
This project is helping me learn more about PCB design, KiCad, and how a keyboard actually works from the schematic to the final PCB.


### Features

- 65% Alice layout — split and angled for a more ergonomic typing position.
- Raspberry Pi Pico (RP2040) 
- 65 keys [Gateron G Pro 3.0 RGB switches](https://meckeys.com/shop/accessories/keyboard-accessories/key-switches/gateron-g-pro-3-0-switch/) arranged in my custom 5 × 15 matrix. MX-compatible mechanical switches.
- Hot-swappable sockets 
- Per-key RGB - 65 [SK6812 MINI-E](https://www.amazon.in/100PCS-Similar-WS2812B-Individually-Addressable/dp/B0DMNBBM9V) 
- [OLED Display](https://amelectronics.in/product/0-91-inch-iic-4-pin-oled-display-module-ssd1306-white/)
- [Analog joystick](https://www.adafruit.com/product/512) 
- PCB-mounted stabilizers — for my larger keys.
- M3 mounting hardware — for mounting the PCB/case.
- Custom Case for the keyboard 
- Custom PCB — designed specifically for my Alice layout.

## Schematic on KiCad
Source : [Rookie V1.kicad_sch](https://github.com/Creepy-yoke/Rookie-V1-/tree/main/Rookie%20V1%20(PCB))
<br>
<br>
<img width="1251" height="477" alt="image" src="https://github.com/user-attachments/assets/f8c74baf-adf7-42fb-8d31-cd2364686303" />


## PCB on KiCad
Source : [Rookie V1.kicad_pcb](https://github.com/Creepy-yoke/Rookie-V1-/tree/main/Rookie%20V1%20(PCB))
<br>
<br>
<img width="1201" height="552" alt="image" src="https://github.com/user-attachments/assets/817ff064-3f32-41cb-8f98-d27ca0399c0c" />

## CASE on Onshape
Source : [Rookie V1 (CASE).step](https://github.com/Creepy-yoke/Rookie-V1-/tree/main/Rookie%20V1%20(CASE))
<br>
<br>

<img width="884" height="506" alt="image" src="https://github.com/user-attachments/assets/d134c56b-84ef-4d43-a8ee-1d3c05b1d169" />

<br>

[Onshape link](https://cad.onshape.com/documents/d718c6f2bf8f1306fd075cc1/w/1f65e877d90938ffe0379d49/e/f8198137f6d496df892af1f1?renderMode=0&uiState=6add21e3e21be264acb29ac8)


## Build of the Board
Coming soon, after I print and assemble it.
STAY TUNED
<br>
<br>


## Bill of Materials
Source: [BOM V1.csv](https://github.com/Creepy-yoke/Rookie-V1-/blob/main/BOM%20V1.csv)
<br>
The following table lists the main components used in the Rookie V1 custom Alice keyboard. Prices are estimates in INR and may vary by supplier.

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
<br>


## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/Creepy-yoke/Rookie-V1-/blob/main/LICENSE.md) file for details 
<br>
So copy it, modify it, sell it, become a billionaire, i expect nothing in return. But if it breaks, explodes, catches fire, or opens a portal to nether, that’s between you and your hardware. I was never here >~<

## Credits
This project uses:
- KiCad - PCB design and schematic capture
- Lion Circuits - PCB manufacturing
- OnShape - CAD case + render
<hr>

  ### WHAT I LEARNED
Not gonna lie I learned many things it was a life time experience and next time I make an PCB for some other project it's  gonna be easy for me I learned shortcuts that will save me time and also made some friend's on SLACK that helped me , 
also #SHOUTOUT to @Flyingfish he saved me some time AND also THX to them who were  part of my journey.
- Here's what I really learned :
I learned how to turn a keyboard schematic into a proper PCB and how important it is to check every connection before moving forward. I also learned how to arrange components properly, route traces, use vias, and fix DRC errors in KiCad. Working on this project helped me understand more about PCB design and how all the different parts of a keyboard connect and work together.
gracias!
<br>

#### NOTE :-
If u want step by step PROCESS to make a simple easy Keyboard which include's Everything, SO just follow the KEEB DOCS, [HERE](https://keeb.hackclub.com/docs/getting-started/) IS THE LINK.
