# mowa-wifi-sensing-labelling

이 프로젝트는 CSI(채널 상태 정보) 데이터를 데이터베이스에 실시간으로 저장할 수 있게 해 주고, 이를 보다 용이하게 해 줍니다
CSI 데이터 처리를 위한 와이파이 센싱 연구

## 본문

<!-- TOC -->
* [mowa-wifi-sensing-labelling](#mowa-wifi-sensing-labelling)
  * [본문](#본문)
  * [시작하기](#시작하기)
    * [Dependencies](#dependencies)
      * [하드웨어](#하드웨어)
      * [소프트웨어](#소프트웨어)
      * [Python Libraries - Ubuntu](#python-libraries---ubuntu)
      * [Python Libraries - Raspberry Pi 4](#python-libraries---raspberry-pi-4)
    * [설치](#설치)
  * [사용](#사용)
    * [프로그램 실행](#프로그램-실행)
    * [구성](#구성)
  * [Demo](#demo)
  * [라이선스](#라이선스)
<!-- TOC -->

## 시작하기

### Dependencies

#### 하드웨어

* Raspberry Pi 4 (installed [Nexmon CSI Tool](https://github.com/seemoo-lab/nexmon_csi))

#### 소프트웨어

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

### 설치

1. project repository 복제

      ```sh
      git clone https://github.com/pjs990301/mowa-wifi-sensing-labelling.git
      ```

2. Flask Server 설치

      ```sh
      pip install -r requirements_server.txt
      ```

3. CSI 데이터 전송을 위한 Raspberry Pi 4 구성

      ```sh
      pip install -r requirements_pi.txt
      ```

## 사용

### 프로그램 실행

1. 플라스크 서버용 `app.py` 실행

      ```sh 
      python app.py 
      ```

2. 모니터 모드를 활성화한 상태에서 `csi_send_server.py`를 실행

      ```sh 
      sudo python3 csi_send_server.py 
      ```

### 구성

1. CSI 데이터 추출 Mac 주소 필터링

      ``` python
      selected_mac = 'Enter your AP MAC Address'
      ```

* CSI 데이터 추출을 위해 AP MAC 주소를 필터링하려면 `csi_send_server.py`에서 21번째 줄을 수정해야 합니다.

2. 플라스크 및 데이터베이스 관리

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

* 데이터베이스 이름이 변경되면 해당 이름에 따라 쿼리를 변경해야 합니다. <br>현재 64개의 부반송파가 조회되고 있습니다. 부반송파를 더 저장하려면 `columns_query`를 수정해야 합니다 <br><br>
* Table 생성 예제

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

## 라이선스

이 프로젝트는 MIT 라이선스로 라이선스가 부여됩니다. 자세한 내용은 [LICENSE.md](https://github.com/pjs990301/mowa-wifi-sensing-labelling/blob/main/LICENSE) 파일을 참조하십시오


