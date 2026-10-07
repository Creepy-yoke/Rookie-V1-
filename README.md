# Rookie-V1 
Hi, I am making a cool Custom Keyboard from scratch, by myself

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
- KMK Keyboard firmware.
- PCB-mounted stabilizers — for your larger keys.
- M3 mounting hardware — for mounting the PCB/case.
- Custom Case for the keyboard 
- Custom PCB — designed specifically for your Alice layout.

## Schematic on KiCad
Source : src/kicad/schem/
<br>
<img width="1251" height="477" alt="image" src="https://github.com/user-attachments/assets/f8c74baf-adf7-42fb-8d31-cd2364686303" />


## PCB on KiCad
Source : src/KiCad/pcb/
<br>
<img width="1201" height="552" alt="image" src="https://github.com/user-attachments/assets/817ff064-3f32-41cb-8f98-d27ca0399c0c" />


## Build of the Board
UPCOMIMG........................
STAY TUNED
<br>
<br>


## Bill of Materials
Source: `production/pcb/bom.csv`



| S.no | Product Name | Footprint | Quantity | Value | Link |
|-----|-----|-----|-----|-----|-----|
| 1   | Gateron G Pro 3.0     | MX            | 65 | ₹1225 | [Link](https://example.com) |
| 2   | Kailh Hot-swap Socket | KS-2P02B01-01 | 65 | ₹650  | [Link](https://example.com) |
| 3   | SK6812 MINI-E         | SMD           | 65 | ₹559  | [Link](https://example.com) |
| 4   | Gateron G Pro 3.0     | MX            | 65 | ₹1225 | [Link](https://example.com) |
| 5   | Kailh Hot-swap Socket | KS-2P02B01-01 | 65 | ₹650  | [Link](https://example.com) |
| 6   | SK6812 MINI-E         | SMD           | 65 | ₹559  | [Link](https://example.com) |
<br>
[Here](https://github.com/Creepy-yoke/Rookie-V1-/blob/main/BOM%20V1.csv) is my Kicad BOM.csv


## Amazon order
### amzzon parts
UPCOMIMG........................



## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/Creepy-yoke/Rookie-V1-/blob/main/LICENSE.md) file for details [(MIT LICENSE-2)](https://mit-license.org/).
<br>
If you have remixed, adapted or build upon this work and wish to remove the non-commercial clause for your own project please contact me on Slack this is [@MD](https://hackclub.enterprise.slack.com/team/U0BDB5F8FQE).Your request is more than likely to be granted. The non-commercial part of the license is intended to avoid direct copies of the work to be sold for commercial gain by third parties.


## Credits
This project uses:
- KiCad - PCB design and schematic capture
- Lion Circuits - PCB manufacturing
- Amazon - Parts order
- OnShape - CAD case + render
  
<br>
<br>
<br>

  ### WHAT I LEARNED
Not gonna lie I learned many things it was a life time experience and next time I make an PCB for some other project it's  gonna be easy for me I learned shortcuts that will save me time and also made some friend's on SLACK that helped me , 
also #SHOUTOUT to @Flyingfish he saved me some time AND also THX to them who were  part of my journey.
- Here's what I really learned :
I learned how to turn a keyboard schematic into a proper PCB and how important it is to check every connection before moving forward. I also learned how to arrange components properly, route traces, use vias, and fix DRC errors in KiCad. Working on this project helped me understand more about PCB design and how all the different parts of a keyboard connect and work together.
gracias!

#### NOTE :-
If u want step by step PROCESS to make a simple easy Keyboard which include's Everything, SO just follow the  #### KEEB DOCS
[HERE]( https://keeb.hackclub.com/docs/getting-started/ ) IS THE LINK.
