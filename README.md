# mowa-wifi-sensing-labelling

This project enables real-time storage of CSI (channel state information) data in a database and makes it easier for
Wi-Fi Sensing researchers to process CSI data.

<br/>

🌎 [README.md in English](https://github.com/oss-inc/mowa-wifi-sensing-labelling/blob/main/README.md)  
🇰🇷  [README.md in Korean](https://github.com/oss-inc/mowa-wifi-sensing-labelling/blob/main/README_KO.md)

<br/>


## Content

<!-- TOC -->
* [mowa-wifi-sensing-labelling](#mowa-wifi-sensing-labelling)
  * [Content](#content)
  * [Getting Started](#getting-started)
    * [Dependencies](#dependencies)
      * [Hardware](#hardware)
      * [Software](#software)
      * [Python Libraries - Ubuntu](#python-libraries---ubuntu)
      * [Python Libraries - Raspberry Pi 4](#python-libraries---raspberry-pi-4)
    * [Installing](#installing)
  * [Usage](#usage)
    * [Execution Program](#execution-program)
    * [Configuration](#configuration)
  * [Demo](#demo)
  * [License](#license)
<!-- TOC -->

## Getting Started

### Dependencies

#### Hardware

* Raspberry Pi 4 (installed [Nexmon CSI Tool](https://github.com/seemoo-lab/nexmon_csi))

#### Software

* Linux Ubuntu
  > I did it on Linux for the experiment, but it is executable regardless of OS (Windows, macOS).
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

## Usage

### Execution Program

1. Run `app.py` for Flask Server

      ```sh 
      python app.py 
      ```

2. Run `csi_send_server.py` with monitor mode enabled

      ```sh 
      sudo python3 csi_send_server.py 
      ```

### Configuration

1. CSI Data Extraction Mac Address Filtering

      ``` python
      selected_mac = 'Enter your AP MAC Address'
      ```

* If you want to filter the AP MAC address for CSI data extraction, you can modify the 21st line
  in `csi_send_server.py`.

2. Managing Flask and Database

      ```json
      {
         "publish_SERVER": {
           "host": "0.0.0.0",
           "port": "SERVER_PORT"
         },
         "Database": {
           "host": "DATABASE_IP",
           "user": "USER_NAME",
           "password": "USER_PASSWORD!",
           "database": "DATABASE_NAME"
         },
         "private_SERVER": {
           "host": "SERVER_IP",
           "port": "SERVER_PORT"
         }
      }
      ```

* If your database name changes, you should change the query according to that name. <br>Currently, 64 subcarriers are
  being queried. If you want to save more subcarriers, you need to modify `columns_query`. <br><br>
* Example of creating a table

  ```sql
  CREATE TABLE [Your Database Name].{table_name}(
  {
    columns_query
  });
  ```

* Table name is default {label name}\_{Collection start time}\_{Collection end time}

## Demo

<video src="https://github.com/oss-inc/mowa-wifi-sensing-labelling/assets/70201882/b2ab5211-743e-47a0-adb7-20b0a41a3d7c" controls="controls">
</video>

## License

This project is licensed under the BSD-3-Clause license - see
the [LICENSE.md](https://github.com/pjs990301/mowa-wifi-sensing-labelling/blob/main/LICENSE) file for details

The environmental settings are described below.
the [LICENSE_Dependency.md](https://github.com/oss-inc/mowa-wifi-sensing-labelling/blob/main/LICENSE_Dependency.md) file for details


