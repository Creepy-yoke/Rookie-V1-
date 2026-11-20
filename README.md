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
- MX-compatible mechanical switches 65 keys [Gateron G Pro 3.0 RGB switches](https://meckeys.com/shop/accessories/keyboard-accessories/key-switches/gateron-g-pro-3-0-switch/).
- Hot-swappable sockets 
- Per-key RGB - 65 [SK6812 MINI-E](https://www.amazon.in/100PCS-Similar-WS2812B-Individually-Addressable/dp/B0DMNBBM9V) 
- [OLED Display](https://amelectronics.in/product/0-91-inch-iic-4-pin-oled-display-module-ssd1306-white/)
- [Analog joystick](https://www.adafruit.com/product/512)
- KMK Keyboard firmware.
- PCB-mounted stabilizers — for my larger keys.
- M3 mounting hardware — for mounting the PCB/case.
- Custom Case for the keyboard 
- Custom PCB — designed specifically for my Alice layout.

## Repository Structure

- `src/kicad/` - KiCad project sources
- `src/kicad/cad/` - full 3d model
- `production/` - PCB fabrication files (Gerbers, BOM, Pick & Place)
- `images/` - images used in the README and documentation








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
| 2  | Gateron G Pro 3.0 Brown switches | MX-compatible, 5-pin | 70 bought, 66 used | ₹5,250 for 100pcs  | [Supplier](https://www.amazon.in/Pre-lubed-Switches-Mechanical-Keyboard-Pcs-5pin/dp/B0CKTH36NB) |
| 3  | Gateron hot-swap sockets | CPG151101S11 / KS-2P02B01-01-a1; verify footprint | 66 | ₹2,260  | [Supplier](https://www.amazon.in/FABLOFT-Connector-Computers-Tablets-Networking/dp/B0GGZWXYKK) |
| 4  | Matrix diodes | 1N4148W-7-F, SOD-123 | 70 bought, 66 used | ₹86.45 | [Supplier](https://www.ktron.in/product/1n4148w-7-f-fast-switching-diode/) |
| 5  | SK6812 MINI-E | Addressable RGB LEDs | 70 bought, 66 used | ₹2,021 for 100pcs | [Supplier](https://www.etsy.com/in-en/listing/1564895619/sk6812-mini-e-rgb-led-100pcs-for) |
| 6  | OLED display | SSD1306, 0.91-inch, 128x32, I2C | 1 | ₹230 | [Supplier](https://www.flyrobo.in/0.91-inch-128-32-oled-display-module-with-i2c-iic-serial-interface?tracking=ads&tracking=4a9a9a) |
| 7  | Analog joystick module | X/Y axes with push button | 1 | ₹175 + GST & DELIVERY CHARGES | [Supplier](https://www.amazon.in/Prakti-Joystick-Module-Breakout-Sensor/dp/B0BTXGX8R9) |
| 8  | Ceramic capacitor | 100 nF, 0603 | 9 | TBD | Add supplier link |
| 9  | Tantalum capacitor | 470 uF, EIA-7343-31 (D case) | 1 | TBD | Add supplier link |
| 10 | Resistor | 330 ohm, 0603 (RGB data line) | 1 | TBD | Add supplier link |
| 11 | PCB-mount stabilizer | 2U | 1 | ₹90 | [Supplier](https://www.genesispc.in/products/durock-plate-mount-stabilizers-6-25u-4x2u-black?variant=43389442293813) |
| 12 | PCB-mount stabilizer | 2.25U | 3 | TBD | Add supplier link |
| 13 | PCB-mount stabilizer | 2.75U | 2 | TBD | Add supplier link |
| 14 | Pin header | 1x04, 2.54 mm (OLED) | 1 | ₹30 + CHARGES | [Supplier](https://www.digikey.in/en/products/detail/w-rth-elektronik/61300411121/4846827?gclsrc=aw.ds&gad_source=1&gad_campaignid=23291937036&gbraid=0AAAAADrbLliIKDD3judFXeSwHiSCe5YKZ&gclid=Cj0KCQiA2frXBhC_ARIsAPTFcdMQ4Kjc29z9y8HaujkPr1E9KDwt0FmG2u3ggHy4rKL1xhABJRWNmgkaAjFXEALw_wcB) |
| 15 | Pin header | 1x05, 2.54 mm (joystick) | 1 | ₹30 + DELIVERY CHARGES | [Supplier](https://robu.in/product/a2541wr-5p-9t-cjt-1x5-pin-2-54mm-90-single-row-pin-header-rohs/) |
| 16 | Pico header pins | 2x 20-pin, only if the Pico has none | 2 | ₹50 + CHARGES | [Supplier](https://www.electropi.in/20x2-male-berg-strip-straight-header) |
| 17 | M3 screws | 6 mounting holes; length from final CAD | 6 | ₹10 | [Supplier](https://onlyscrews.in/products/m3-x-12mm-phillips-countersunk-csk-mild-steel-black-oxide-screw-dia-3mm-length-12mm?currency=INR&country=IN&variant=67547588133177&stkn=6e84ebfba1b8&utm_adgroup=&utm_assetgroup=6756574039&utm_term=&utm_matchtype=&utm_network=x) |
| 18 | Custom PCB | Two-layer FR-4, Rookie V1 Alice | 1 per keyboard | TBD | [Get quote](https://www.lioncircuits.com/) |
| 19 | Custom keyboard case | Rookie V1 | As per CAD | ₹0 | PRINTED AT HOME |
| 20 | MX-compatible keycap set |  fit the exact Alice layout | 1 compatible set | ₹2,750 | [Supplier](https://neomacro.in/products/soulcat-dragon-pattern-keycaps-pre-order) |
| 21 | USB cable | Type-C | 1 | ₹150 | [Supplier](https://www.amazon.in/dp/B09KH58JZR/ref=sspa_dk_detail_0?aref=5t1nLzLZEZ&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw) |


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
