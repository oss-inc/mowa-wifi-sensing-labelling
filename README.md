# mowa-wifi-sensing-labelling
This project enables real-time storage of CSI (channel state information) data in a database and makes it easier for Wi-Fi Sensing researchers to process CSI data.

## Getting Started
### Dependencies
#### Hardware
* Raspberry Pi 4 (installed [Nexmon CSI Tool](https://github.com/seemoo-lab/nexmon_csi))

#### Software
* Linux Ubuntu
* MySQL
* Python == 3.8

#### Python Libraries - Ubuntu
* Flask
* mysql-connector-python

#### Python Libraries - Raspberry Pi 4
* pypcap
* dpkt
* keyboard
* pandas
* numpy
* requests

### Installing
1. Clone the project repository
```sh
git clone https://github.com/pjs990301/mowa-wifi-sensing-labelling.git
```

2. Installing the Flask Server
```sh
pip install -r requirements_server.txt
```

3. Configuring Raspberry Pi 4 for CSI Data Transmission
```sh
pip install -r requirements_pi.txt
```

### Usage
1. Run `app.py` for Flask Server
```
python app.py 
```

2. Run `csi_send_server.py` with monitor mode enabled
```
sudo python3 csi_send_server.py 
```
