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

| S.no | Product Name | Footprint / Specification | Quantity | Estimated Value (INR) | Link |
|---:|---|---|---:|---:|---|
| 1 | Raspberry Pi Pico | RP2040 | 1 | ₹384 | [Supplier](https://www.thingbits.in/t/brands/raspberry-pi/pico-slash-rp2040) |
| 2 | Gateron G Pro 3.0 Brown Switches | MX-compatible | 65 | ₹1,330 | [Supplier](https://stackskb.com/) |
| 3 | Gateron Hot-swap Sockets | KS-2P02B01-01 family; verify exact part | 65 | ₹650 | [Supplier](https://stackskb.com/) |
| 4 | 1N4148W Diodes | SMD; verify footprint | 65 | ₹86.45 | [Supplier](https://www.ktron.in/product/1n4148w-7-f-fast-switching-diode/) |
| 5 | SK6812 MINI-E RGB LEDs | Addressable RGB | 65 | ≈ ₹2,100* | [Supplier](https://shiroganelab.com/products/keyball-rgb-led-sk6812mini-e) |
| 6 | SSD1306 OLED Display | 0.91-inch, 128×32, I²C | 1 | ₹165.25 | [Supplier](https://www.robogears.in/shop/controllers-systems-displays-display-modules-60/39712-0-91-i2c-oled-display-module-128x32-2605) |
| 7 | Analog Joystick Module | X/Y axes | 1 | ≈ ₹52 | [Supplier](https://directronics.in/product/joystick-module) |
| 8 | Ceramic Capacitors | 100 nF, 0603 | 65 provisionally | ≈ ₹20 | [Supplier](https://robu.in/) |
| 9 | Bulk Capacitor | 470 µF | 1 | ≈ ₹22 | [Supplier](https://robu.in/) |
| 10 | RGB Data Resistor | 330 Ω, 0603 | 1 | ≈ ₹1 | [Supplier](https://robu.in/) |
| 11 | Additional Resistor | Value to be confirmed from schematic | 1 | TBD | TBD |
| 12 | PCB Stabilizer | 2U | 1 | Included in estimate below | TBD |
| 13 | PCB Stabilizer | 2.25U | 3 | Included in estimate below | TBD |
| 14 | PCB Stabilizer | 2.75U | 1 | Included in estimate below | TBD |
| 15 | Mounting Hardware | M3 screws and standoffs | As required | ≈ ₹200 | TBD |
| 16 | Custom PCB | 2-layer FR-4, Rookie V1 Alice | 1 | TBD | [PCB quote](https://www.pcbforyou.in/quote/) |
| 17 | Keyboard Plate | Custom Alice layout | 1 | TBD | TBD |
| 18 | Keyboard Case | Custom Rookie V1 case | 1 | TBD | TBD |
| 19 | Keycaps | MX-compatible, Alice layout | 65-key layout | TBD | TBD |

### Estimated Cost

**Estimated subtotal of priced items: approximately ₹5,510 INR**

This is not the final keyboard cost. PCB fabrication, plate, case, keycaps, shipping and the unconfirmed resistor are excluded or not yet priced.

\* RGB LED pricing is provisional. Capacitor quantity and all component values should be checked against the final schematic and PCB before ordering.

[View the complete BOM CSV](./BOM%20V1.csv)









[HERE](https://github.com/Creepy-yoke/Rookie-V1-/blob/main/BOM%20V1.csv) is my Kicad BOM.csv


## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/Creepy-yoke/Rookie-V1-/blob/main/LICENSE.md) file for details 
<br>
So copy it, modify it, sell it, become a billionaire, i expect nothing in return. But if it breaks, explodes, catches fire, or opens a portal to nether, that’s between you and your hardware. I was never here >~<

## Credits
This project uses:
- KiCad - PCB design and schematic capture
- Lion Circuits - PCB manufacturing
- Amazon - Parts order
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
