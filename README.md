# NET-VIZ
<a href="https://twitter.com/Evilsturn">
<img alt="Twitter Handle" src="https://brandvisibility.com.ng/wp-content/uploads/2022/02/Twitter-Logo-2010-2012.png" width="165"/>

![Contributors](https://img.shields.io/github/contributors/Evilsturn/NetViz?style=plastic)
![Forks](https://img.shields.io/github/forks/Evilsturn/NetViz)
![Stars](https://img.shields.io/github/stars/Evilsturn/NetViz)
![Issues](https://img.shields.io/github/issues/Evilsturn/NetViz)


## Description
### Net-Viz is a network traffic visualization tool that parses through PCAP files and generates a KML file which can be imported over to Google Maps to Visalize the Data. 

## Prerequisite
### [Wireshark](https://www.wireshark.org/)(Or any Alternatives):
Wireshark is a network traffic analyzer or 'sniffer' which allows to capture packets in the network and can be saved as PCAP file.
#### *Note - You can use any network traffic analyzer BUT make sure to save the packets in PCAP format*
### [Python 3+](https://www.python.org/downloads/):
This script is entirely written in Python 3 so make sure you have it installed.

## HOW TO SETUP
- #### Clone the repository on to your local machine using `git clone git@github.com:Evilsturn/NetViz.git` then change your working directory to the path of the repository.
- #### Install all the Python dependencies using `pip install -r requirements.txt`
- #### Open Wireshark and select the interface you want to capture.
  ![image](https://user-images.githubusercontent.com/62092586/188264126-160c6b62-46bf-43be-a7c8-ca0b0e39419e.png)
- #### Click on the blue shark-fin Icon at the top left to start capturing the packets.
  ![image](https://user-images.githubusercontent.com/62092586/188264181-16ebce26-ddd8-4215-a79d-502669aae918.png)
- #### Click on the Red stop button when you want to stop capturing the packets.
  ![image](https://user-images.githubusercontent.com/62092586/188264318-7ddd7c97-1484-44c2-8566-197a2cea3e7c.png)
- #### To save the packets Go to File>Export Specified Packets
  ![image](https://user-images.githubusercontent.com/62092586/188264367-a27ec608-2158-43f3-add5-0302a305813c.png)
- #### Browse to the local repository then select the Packets folder also make sure to select the Save as type to pcap
  ![image](https://user-images.githubusercontent.com/62092586/188264506-9fb39d40-d468-4fa0-a2d9-138b5e2d7ac3.png)
- #### Now run the net-viz.py script using `python net-viz.py`
