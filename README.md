<div align="center">
<h1> Rookie V1 </h1>
<p>Hi, I am making a cool Custom Keyboard from scratch, by myself</p>
</div>

<div align="center">

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Project](https://img.shields.io/badge/Project-Hardware-yellow.svg)
![Hackatime Badge](https://img.shields.io/badge/Hacktime-10hr-purple)

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
- 65 keys [Gateron G Pro 3.0 RGB switches](https://meckeys.com/shop/accessories/keyboard-accessories/key-switches/gateron-g-pro-3-0-switch/) arranged in your custom 5 × 15 matrix. MX-compatible mechanical switches.
- Hot-swappable sockets 
- Per-key RGB - 65 [SK6812 MINI-E](https://www.amazon.in/100PCS-Similar-WS2812B-Individually-Addressable/dp/B0DMNBBM9V) 
- [OLED Display](https://amelectronics.in/product/0-91-inch-iic-4-pin-oled-display-module-ssd1306-white/)
- [Analog joystick](https://www.adafruit.com/product/512) 
- PCB-mounted stabilizers — for your larger keys.
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
UPCOMIMG........................
<br>
<br>
<br>

## Build of the Board
UPCOMIMG........................
STAY TUNED
<br>
<br>


## Bill of Materials
Source: ???


## Bill of Materials

The following table lists the main components used in the Rookie V1 custom Alice keyboard. Prices are estimates in INR and may vary by supplier.

## Bill of Materials

The following BOM describes the Rookie V1 custom Alice keyboard.
Prices are estimates in INR. TBD means the exact part or price
must be confirmed before ordering.

| S.no | Product Name | Specification / Footprint | Quantity | Estimated Cost (INR) | Link |
|---:|---|---|---:|---:|---|
| 1  | Raspberry Pi Pico (USB-C) | RP2040 development board | 1 | ₹383.50 | [Supplier](https://www.thingbits.in/products/raspberry-pi-pico) |
| 2  | Gateron G Pro 3.0 Brown switches | MX-compatible, 5-pin | 65 | ₹1,330 for 7 packs of 10 | [Supplier](https://stackskb.com/store/gateron-g-pro-3-0-brown-ks-9-tactile-switch-pack-of-10/) |
| 3  | Gateron hot-swap sockets | KS-2P02B01-01-a1; verify footprint | 65 | ₹650 | [Supplier](https://stackskb.com/store/gateron-hotswap-sockets/) |
| 4  | Matrix diodes | 1N4148W-7-F, SOD-123 | 65 | ₹86.45 | [Supplier](https://www.ktron.in/product/1n4148w-7-f-fast-switching-diode/) |
| 5  | SK6812 MINI-E | Addressable RGB LEDs | 65 | TBD | [Supplier](https://shiroganelab.com/products/keyball-rgb-led-sk6812mini-e) |
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
| 19 | Custom PCB | Two-layer FR-4, Rookie V1 Alice | 1 per keyboard | TBD | [Get quote](https://www.pcbforyou.in/quote/) |
| 20 | Custom switch plate | Matches Alice layout and stabilizer cut-outs | 1 | TBD | Add fabrication link |
| 21 | Custom keyboard case | Rookie V1; include all separate case pieces | As per CAD | TBD | Add Onshape/fabrication link |
| 22 | MX-compatible keycap set | Must fit the exact Alice layout | 1 compatible set | TBD | Add supplier link |
| 23 | USB cable | Type - C     | 1 if supplied | TBD | Confirm connector |


### Partial Cost Summary

The currently priced items total approximately **₹2,717.20 before joystick GST**.
This is not the full keyboard cost. RGB LEDs, remaining electronic parts,
stabilizers, mounting hardware, PCB fabrication, plate, case, keycaps
and shipping still need confirmed prices.
The rotary encoder is not included because it was removed from the design.









[HERE](https://github.com/Creepy-yoke/Rookie-V1-/blob/main/BOM%20V1.csv) is my Kicad BOM.csv


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
