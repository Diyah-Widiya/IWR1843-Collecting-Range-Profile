# Import Libraries
import serial
import time
import numpy as np
import os

''' Parameters configuration'''
# Change the configuration file name
configFileName = "profile_VitalSigns_20fps.txt"
# Change Port: please take care with each respective baud rate defined at serialConfig()
CLIport_ = "COM4"
Dataport_ = "COM3"
interval = 10  # Set the desired interval in seconds

# other global variables
CLIport = {}
Dataport = {}
byteBuffer = []
dir =r'D:\DATA PENELITIAN AGUSTUS 2023\Data Collection Series\TI\record' # change with your directory 
# ------------------------------------------------------------------
# ------------------------------------------------------------------
timestr = time.strftime("%Y-%m-%d_%H-%M-%S")
        # Replace colons with underscores in the timestamp
timestr = timestr.replace(":", "_")
def start_fmcw():
    """ Set serial ports, send configuration file to radar, and initialize IWR chip """
    global CLIport, Dataport
    # Open the serial ports for the configuration and the data ports
    
    # Windows
    CLIport = serial.Serial(CLIport_, 115200)
    Dataport = serial.Serial(Dataport_, 921600)

    # Read the configuration file and send it to the board
    config = [line.rstrip('\r\n') for line in open(configFileName)]
    for i in config:
        CLIport.write((i + '\n').encode())
        time.sleep(0.01)
        
    fmcw_process()

# ------------------------------------------------------------------

def fmcw_process():
    """ Read and save complex values coming from IWR """
    
    def readAndParseData18xx(Dataport):
        """Gets frame data from module"""
        global byteBuffer
    
        readBuffer = Dataport.read(Dataport.in_waiting)
        byteVec = np.frombuffer(readBuffer, dtype='int8')
        byteBuffer.append(np.array(time.time()))
        byteBuffer.append(np.array(byteVec))
        print("---")
    
    start = time.time()
    while time.time() - start < interval:
        # Update the data and check if the data is okay
        readAndParseData18xx(Dataport)
        time.sleep(0.01)  
    stop_fmcw()


def stop_fmcw():
    """ Finish and save IWR files inside a previously defined directory """
    global CLIport, Dataport, byteBuffer
    
    # Stop acquisition and close open doors
    CLIport.write(('sensorStop\n').encode())
    CLIport.close()
    Dataport.close()

    # Find the number of files in the path and increase the value for the recorded file
   
    number_of_files_in_path = len([1 for x in list(os.scandir(dir)) if x.is_file()])
    filename = timestr + ".txt"

    # Open directory and start writing inside .txt. file
    with open(dir + filename, "w+") as f:
        for i in range(len(byteBuffer) - 1):
            if byteBuffer[i + 1].size == 0 or byteBuffer[i].size == 0:
                print("is empty")
            else:
                for x in np.nditer(byteBuffer[i]):
                    if byteBuffer[i].size > 1:
                        f.write(str(x) + " ")
                    else:
                        f.write("\n" + str(x) + "\n")
        f.write("\n")

    print("File saved: {}".format(filename))

# -------------------------    MAIN   -----------------------------------------

start_fmcw()
print("finish")
