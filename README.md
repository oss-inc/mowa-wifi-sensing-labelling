# mowa-wifi-sensing-labelling
This project enables real-time storage of CSI (channel state information) data in a database and makes it easier for Wi-Fi Sensing researchers to process CSI data.

## Getting Started
### Dependencies
#### Hardware
* Raspberry Pi 4 (installed [Nexmon CSI Tool](https://github.com/seemoo-lab/nexmon_csi))

#### Software
* Linux Ubuntu
    > I did it on Linux for the experiment, but it is executable regardless of OS(Windows, macOS).
* MySQL Server == 8.0.33
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


### Config
1. CSI Data Extraction Mac Address Filtering
```
selected_mac = 'Enter your AP MAC Address'
```
* If you want to filter the AP Mac address for CSI data extraction, you can modify the 21st line in `csi_send_server.py`.

2. Managing Flask and Database
```
{
  "publish_SERVER": {
    "host" : "0.0.0.0",
    "port" : "SERVER_PORT"
  },
  "Database" : {
    "host": "DATABASE_IP",
    "user": "USER_NAME",
    "password": "USER_PASSWORD!",
    "database": "DATABASE_NAME"
  },
  "private_SERVER": {
    "host" : "SERVER_IP",
    "port" : "SERVER_PORT"
  }
}
```
* If your database name changes, you should change the query according to that name. <br>Currently, 64 subcarriers are being queried. If you want to save more subcarriers, you need to modify `columns_query`.
```
Example of creating a table

CREATE TABLE Your Database Name .{table_name} (
        {columns_query}
    );
    """
```
