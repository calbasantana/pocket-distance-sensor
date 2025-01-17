![Image_1](https://github.com/user-attachments/assets/b0f54053-2228-4e61-9200-109c2e711bf4)

# Introduction
When I had my old car, a 2018 Mazda CX-3, I was always getting frustrated with how hard it was to tell if I was close to another car or not when parking. My car didn't have a built-in proximity sensor, so I decided to take on this project to build one for it.

The idea being that if I had a distance sensor (light-based or sound-based) at the front of the car and hooked up the circuitry inside the car with the small screen, I could make it all work. However, I was in the middle of buying a new car and this project took on a different form, one of being a pocket distance sensor. It certainly isn't perfect, but it is a cool little thing. In the future, I would love to make it more compact.

# Materials
This pocket distance sensor makes use of the following:

- 3D-printed case
- Custom PCB
- Hardware parts

In the following sections, I will get into more details about each.

## 3D-Printed Case

I decided to go with something simple; something that could hold the battery and the screen with everything else in between.

![Image_2](https://github.com/user-attachments/assets/2eff39e0-9316-43b9-9401-2fc38c603700)

There are a total of 4 files attached here for this case:

- Case Top
- Case Bottom
- Battery Cover
- 4X Magnet Cover

I personally did not end up using the Battery Cover I designed and I found the Magnet Covers to be unnecessary if you're using strong glue to keep the magnets in their place.

### Specifications & Material(s)
Below you can find the printer and material used.
#### 3D Printer
 Original Prusa Mini+
#### Material(s)
 INLAND PLA 3D Printer Filament - 3D Printing PLA Filament 1.75mm, Dimensional Accuracy +/- 0.03mm - 1kg Cardboard Spool (2.2 lbs), True Red PLA
 – this can be purchased for $25.99 at the following link: https://www.amazon.com/Inland-PLA-Printer-Filament-1-75mm/dp/B09P22PTGG/ref=sr_1_3?crid=9I7URGV2CGNU&dib=eyJ2IjoiMSJ9.xA_ymmXS4KUf2pO0k7MrQ40wAD8QcoFPu66tyBLa0rAXMOOZ8eD5gzGllaZmuiB8s6qwVfE7zJcNTG3H4iRI_F7okGdJQJ20vcZtprVsYLaBNxv7f9V7q-swGcHHMoE65dmwDMOC2fjsmbC14OVYyRXYfUriPzMs4l9Lug0Ifr2HXkNDIrOigZ5kj7CsqpaxHKvqEl_mYF5wBtR2LA4TVmJPTF--dMvzaqkv2Auhsn4.nsIeLQ8120PdCT5mJwT0nGTlIryazu9uhkhaN868RsE&dib_tag=se&keywords=true%2Bred%2Bfilament%2Binland&qid=1737073478&sprefix=true%2Bred%2Bfilament%2Binlan%2Caps%2C105&sr=8-3&th=1

#### Software
 PrusaSlicer
![Image_3](https://github.com/user-attachments/assets/6ec19aa6-54d0-4b70-953f-ffbe2785eb5d)
##### Settings
  Layer Height: .2mm \
  Infill: 30% \
  Supports: Everywhere \
  Estimated Printing Time: 8 hours and 1 minutes

## Custom PCB

I decided to create a custom PCB for the pico, screen connections, and other hardware pieces to be more compact. I did this using EasyEDA (https://easyeda.com/).

Below you can see the schematics on EasyEDA:

![Image_4](https://github.com/user-attachments/assets/9733ae1c-5c18-4559-8de0-73418a19801d)


And here you can see the PCB layout:

![Image_5](https://github.com/user-attachments/assets/25529ad7-e7d0-4480-bde3-a1f5ee49c3ab)


For convenience, I've attached the Gerber .zip file, which can be uploaded at this website for purchase: https://jlcpcb.com/?href=easyeda-home

Overall, it is very cheap to make a PCB, so I find myself doing large batches - the biggest pain is the shipping.

Once you do have your PCB, make sure to solder it appropriately and attach the active buzzer. See photos below:

![Image_6](https://github.com/user-attachments/assets/bbc7e2a7-9639-4614-9fd4-d297831c6c79)

![Image_7](https://github.com/user-attachments/assets/ee7c8b0d-a570-452a-b3c6-fb045727595a)

## Hardware Parts
The following materials were purchased for this project, but it's cheaper if you already have some available:

![Image_8](https://github.com/user-attachments/assets/ea677c11-c87d-479b-b6b8-df4ed9fbe452)


Pimoroni Pico LiPo - this can be purchased for $11 at the following link: https://shop.pimoroni.com/products/pimoroni-pico-lipo?variant=39386149093459

YDL 3.7V 2500mAh 724957 Lipo battery Rechargeable Lithium Polymer ion Battery Pack with PH2.0mm JST Connector - this can be purchased for $12 at the following link: https://www.amazon.com/YDL-2500mAh-battery-Rechargeable-Connector/dp/B07BTY599F/ref=sr_1_6?crid=2MP6R0GVM0Z1X&dib=eyJ2IjoiMSJ9.eagHhmMYsNsXb4xTJqQhajqqiTY8HyAxv5sBif7eHYR2EXrTL7SSFRvd5PNjWNaVyJmzNTuUod0JPd8w8yLVc3SrJcPi9TvKd11-3c_j4ZHBNvwrVySVHUJhoOR6gThnBm6gPWH2s33cIlO8abkns-sfcGShELU1rvegu8zIXrD-oXPiJ-a5aofMkRNFRP8fWL2IBkuwWXMFQsAKAZEiPghzKmeeS4mdYYeuzcunIM_zilsTYNt5C0Ke8qeG2tHVUzxn1a9HcCkeruu2aHBPqwEJJTIHTxfqtFQY1vKHB1dxHg7vFyX9RkcPvLooAkJ0-MQb5dKP482scF1XVmp2vizqcmlWD_l3TDE_qZxIJ-7eRo3wO0UP8lrIrSwq58syla-Xo3LYmAt50cWyqg15L3lddG9_aFlywSQp3wLT2_wXo5IJSEeX2IBsz9LBuZFH.VV-Ia3l9Aglag64ZcM0YLwoB4Tzmzdk60nEi1n5GLzg&dib_tag=se&keywords=3.7v+2500mah&qid=1737074753&sprefix=3.7v+2500mah%2Caps%2C111&sr=8-6

10Pcs 5V Active Buzzer Electronic Alarm Magnetic Long Continuous Beep for Arduino (Pack of 10) CYT1036 - this can be purchased for $7 at the following link: https://www.amazon.com/Cylewet-Electronic-Magnetic-Continuous-Arduino/dp/B01N7NHSY6/ref=sr_1_6?crid=1R6DSXS7VQSM2&dib=eyJ2IjoiMSJ9.4eKCBCAGNlPGhQZejCBwuYC_3NPWP3DQUe6BJ-X7F03qNiVpZcbccZZnByW1-kdI7qxQSwQspplr6Qze3rGo2aJUPqcwDiNhv1WAfSb76flztbXMJY0ACzPeN-TbfEKkc-gxS0dxQoxQhn351QctHwmxdEIivliK7qwigTFidWa4zcz0DJiH_AErx1iFZzI3MPl7x4XRgMxDVhifEyShKe_6MKTb7bo_xbSlrACCAxEB4RY6b1SeFDTMXClj3YXEQ_rFAvEM_a4qtiNhNguOiukQ-E-SOrKLXcuJ2LzHX_z_ujcAi0seRKdhQrRNN7o1UJoiAOtsOCQZVu4YATDJnKB2pmx1Fr5VsWSIN4U0c-xnOBqDXePR3xD9GXfj8lDQ.okybXhf3Vt1BBol6gUeA4k9Dts7u4MoVkTxUgurwb14&dib_tag=se&keywords=15pcs+Super+Loud+Active+Passive+Piezo+Buzzer+Alarm+12mm+Dia+DC+5V+2+Terminals+Electronic+Continuous+Sound+Buzzer+for+Arduino&qid=1737075106&s=hi&sprefix=15pcs+super+loud+active+passive+piezo+buzzer+alarm+12mm+dia+dc+5v+2+terminals+electronic+continuous+sound+buzzer+for+arduino+%2Ctools%2C98&sr=1-6-catcorr

2pcs HC-SR04 Ultrasonic Sensor for Arduino, ESP32, ESP8266, Raspberry Pi - this can be purchased for $7 at the following link: https://www.amazon.com/DIYables-HC-SR04-Ultrasonic-Arduino-Raspberry/dp/B0BDFLPZ2R/ref=sr_1_15?dib=eyJ2IjoiMSJ9.kC1FOvq7HuTguusTr5_MOc6CKuuDsragARW5dzzMZyurbwYEEudsjDjYINU0ufxqysiGeX8N8GMkBYlUJKbgHzdd2xXgFdY7qNxXRqaHDcA5Jtp6fKpjF9iyl52R6fiUIrwsnKnhiZ68wmG0L7bQUQX4EjRoiAe2qo_DJNi9i-Uy3DRzbIkOSBywAF5HXuwJ4KlZ59RQewQqhx46oi2QFNgEv1YisWN4SGphCYb9P8Sz7vjKvYjil7K-GSGFfX7T-vmmDpP30XpjfiYSKIWXnLLRDrOcPrEFFFDqEBTZfm7Zk95-RjcZC138Y-bDQxE8XVMbKyFkhfmGYqHtgkd81XRZcgO6I7P-uFgJKSbcrnZvnYQv8yBTdOZ3Gqt6OIi2y3InVvmo9APHmG95sCXnDHaAfn518qKI8wFb4-o-OGdpth27ifgVHliqH9bFWqYM.Fr2hWC3sWRAPz2gmo8LBWkv2nZP2tULgr12U4twHgGI&dib_tag=se&keywords=hc%2Bsr04&qid=1737075198&sr=8-15&th=1

Teyleten Robot 0.96 inch LCD OLED Display Board Module 12864 128X64 IIC I2C SSD1306 Driver 4 Pins for Raspberry Pi Arduino(5pcs, White Light) - this can be purchased for $13 at the following link: https://www.amazon.com/Teyleten-Robot-Display-SSD1306-Raspberry/dp/B0CN373JF4/ref=sr_1_3?crid=361XZM49GGPR5&dib=eyJ2IjoiMSJ9.8GhymqwidwtFXaOkkBgoxQlUjpMRQbXjpogMPXYpXgx6QkWFzutNfWqWSYygVtJKwN9fN-CBPD9V3OLDMxZMLbClGec5Z97FShn4g5OU32uo8NTog24mWkz8_QyK4lez193pZTXMBkGq2aXj0XGbB_3rjggQrLrheLH3bptoQS8gll-E_2ACKM9Q9VM5JBg_a7VzGdSj3qJffmQVtJYjKtAWVFtpcttYWBLJ4aMeA-18Yec68-YUsoqKz_IGmIp_g9nsE1PBJFkP7nZeq0nfwfOc2tCADS1pZKo1FhWvvXKSJBhjpSvFSE34vyUn9ew1v78GIz3NaWYYe74sxLk7yeLYBLi2kraO_TZdkwZ2XOQ.8AQL7ul9nRMH659-BqF4DZRPfkUNtKWy56OVeahCJ-g&dib_tag=se&keywords=Songhe+0.96+inch+12864+128X64+OLED+LCD&qid=1737075310&s=electronics&sprefix=songhe+0.96+inch+12864+128x64+oled+lcd%2Celectronics%2C103&sr=1-3

If you don't have any of these materials already available, this project might be expensive at $50 - not including taxes and shipping. If you already have most common items, this might only cost $11 - $24.

# Assembly

This part is pretty straightforward. Put everything where it belongs so it is assembled like in the picture from the top.

# Coding

I've attached the main.py file used for this. Simply download it to your computer and upload it to the Pico. My preferred way of doing this is through Thonny (https://thonny.org/).

## Running the Code


# Tips
 It can be hard to align the card precisely. For this reason, I recommend using some scotch tape on either both or one of the sides of the metal card. I didn’t have scotch tape readily available, so I carefully added some electrical tape.
 ![Image_4](https://github.com/user-attachments/assets/9e7eda4a-26a8-4de4-a63d-540204487ea2)
