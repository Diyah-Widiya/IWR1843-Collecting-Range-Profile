
# IWR1843-Collecting-Range-Profile-
The provided code is for recording range profiles without using the DCA1000 EVM, utilizing the Vital Sign Labs driver from xWR1642 implemented on the IWR8143 board.

# Overview IWR1843
This documentation will outline the process of collecting range profile data from IWR1843 without using DCA1000EVM. It's important to note that the xWR1642 radar is similar to IWR1843, operating at a frequency of 76-81 GHz. The main difference lies in the number of transmit antennas, with xWR1642 having 2-Tx and IWR1843 having 3-Tx. Further details, such as maximum sampling rate, can be found in the [documentation](https://www.ti.com/lit/an/swra656c/swra656c.pdf?ts=1704782078011&ref_url=https%253A%252F%252Fwww.google.com%252F).

This document will involve data acquisition for range detection on a specific subject. In addition to recording data, we also provide code for processing range profiles. It's worth noting that the idea for recording range profiles was inspired by [this source](https://run.unl.pt/handle/10362/118695). Feel free to explore it for more information.

# Required Steps
1. **Required Hardware**
   - IWR1843 EVM
   - Micro USB cable (included in the EVM package)
   - 5V/2.5A Power Supply
2. **Download Lab Project: TI mmWave Lab Driver Vital Signs**
   - [mmwave_automotive_toolbox_3_6_0](mmwave_automotive_toolbox_3_6_0)
   - Once downloaded, open:
     - The pre-built binaries are located in the folder: \labs\lab0001-driver-vital-signs\vitalSigns_pjt\pre-built-Binaries\xwr16xx_vitalSigns_lab.bin
   - Ensure that you have Uniflash installed from TI. [Download link here](https://www.ti.com/tool/download/UNIFLASH/8.5.0)
3. **Flash Lab Binaries**
   - Refer to the comprehensive TI documentation at [this link](https://dev.ti.com/tirex/explore/node?a=AocYeEd__3.3.0&node=A__AIgKjYqi9iMXG2F0NZ41ow__com.ti.mmwave_automotive_toolbox__AocYeEd__3.3.0)
4. Ensure that pins are in flash mode during the hardware flash process, where SOP0 and SOP2 should be 'ON.'
5. Once the flashing process is complete, return the hardware to functional mode, i.e., SOP0 'ON,' SOP1, and SOP2 'OFF.'
6. Run the code `collect-data-iwr1843.py`.
7. Read the data using `read.ipynb`.

# Reference 
1. [RADAR-WORLD GitHub Repository](https://github.com/alexandrasdl/RADAR-WORLD/tree/main)
2. [Texas Instrument Documentation](https://www.ti.com/)

