# mowa-wifi-sensing-labelling
This project enables real-time storage of CSI (channel state information) data in a database and makes it easier for Wi-Fi Sensing researchers to process CSI data.

## Getting Started
### Dependencies
#### Hardware
* Raspberry Pi 4 (installed [Nexmon CSI Tool](https://github.com/seemoo-lab/nexmon_csi))

#### Software
* Linux Ubuntu
    > I did it on Linux for the experiment, but it is executable regardless of OS(Windows, macOS).
* MySQL
* Python == 3.8

#### Python Libraries - Ubuntu

<details>
<summary>Open </summary>
<div markdown="1">

* Flask
* mysql-connector-python

</div>
</details>

#### Python Libraries - Raspberry Pi 4

<details>
<summary>Open </summary>
<div markdown="1">
  
* pypcap
* dpkt
* keyboard
* pandas
* numpy
* requests

</div>
</details>

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
