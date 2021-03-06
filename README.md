<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Tags][tags-shield]][tags-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />


<div align="center">
  <a href="https://github.com/matbmoser/SOTA">
    <img src="media/img/logo.jpg" alt="Logo" width="300" height="300">
  </a>
  <h1 align="center">Sistema de Optimización de Tiempo de Aparcamiento (SOTA)</h1>
    <a href="https://github.com/matbmoser/SOTA"><strong>Explore the docs »</strong></a>
    <br >
    <br >
    <a href="https://github.com/matbmoser/SOTA">View Demo</a>
    ·
    <a href="https://github.com/matbmoser/SOTA/issues">Report Bug</a>
    ·
    <a href="https://github.com/matbmoser/SOTA/issues">Request Feature</a>

</div>
<br>


<div align="justify">

  # Description
  > **_NOTE:_** The system default lenguage is Spanish, because the project is for a University in Spain (Interfaces are in ```Spanish```, system intern communication messages are in ```English```. The docs are in ```English``` for easing the universal undertanding of the PTOS System, all over the world)

  <h2 align="Left">Parking Time Optimization System (PTOS)</h2>

  <p>
    PTOS or SOTA (in Spanish) is a Smart Parking integrated system that offers a safe live view to managers and users of a Smart Campus Parking Lot. The system is capable of handling the detection of a licence plate by a IP Camera at the entrance of a parking lot and asign to registered users a parking place with a unique ticket.
    <br><br>
    Users are able to interact with the system in a Web Aplication called UFV MyParking. There can to add vehicles that will be detected by the cameras in the parking lot entrance and exits. They are also able to visualize the parking lot capacity and status
    <br><br>
    Once a user enterers a ticket will be generated indicating the asigned parking place. This asigned place is the one that best suits the type of vehicle configured in the WebApp.
    <br >
    </p>
</div>

<!-- TABLE OF CONTENTS -->
  <summary>Table of Contents</summary>
    
  - [Description](#description)
    - [Integrated Systems:](#integrated-systems)
  - [Important](#important)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [For Windows](#for-windows)
      - [Install Git with Gitbash](#install-git-with-gitbash)
      - [Install Docker:](#install-docker)
      - [Use a Web Browser](#use-a-web-browser)
  - [Deploying the App](#deploying-the-app)
    - [1 - Start Docker Daemon](#1---start-docker-daemon)
    - [2 - Clone this Repository](#2---clone-this-repository)
    - [3 - Configure Credentials (Optional):](#3---configure-credentials-optional)
      - [Digital Twin Global Configurations:](#digital-twin-global-configurations)
      - [Device Manager Global Configurations](#device-manager-global-configurations)
    - [Docker Compose File](#docker-compose-file)
    - [4- Build the App](#4--build-the-app)
    - [Execute Build Docker Script](#execute-build-docker-script)
  - [User Manual](#user-manual)
    - [Access To Digital Twin](#access-to-digital-twin)
      - [**Access Digital Twin Default Credentials**](#access-digital-twin-default-credentials)
    - [Digital Twin Interface](#digital-twin-interface)
      - [Dark Mode](#dark-mode)
      - [Light Mode](#light-mode)
    - [Header](#header)
    - [Map](#map)
    - [Action Buttons](#action-buttons)
    - [Device Manager Server Admin](#device-manager-server-admin)
      - [Before Opened](#before-opened)
      - [After Opened](#after-opened)
    - [Connect Camera](#connect-camera)
      - [Before Connected](#before-connected)
      - [After Opened](#after-opened-1)
    - [Add Vehicle Button](#add-vehicle-button)
    - [Delete Vehicle Button](#delete-vehicle-button)
    - [See Places Button](#see-places-button)
    - [Barrers Button](#barrers-button)
      - [Open Entrace Barrer](#open-entrace-barrer)
      - [Close Entrace Barrer](#close-entrace-barrer)
      - [Change to Exit Barrer](#change-to-exit-barrer)
    - [Refresh and AutoRefresh Button](#refresh-and-autorefresh-button)
      - [Enabled Refresh](#enabled-refresh)
      - [Disabled Refresh](#disabled-refresh)
    - [Access To WebApp UFV MyParking](#access-to-webapp-ufv-myparking)
      - [**Access WebApp Default Credentials**](#access-webapp-default-credentials)
    - [Register](#register)
      - [Data Policy](#data-policy)
    - [Dashboard](#dashboard)
      - [Menu User](#menu-user)
      - [Menu Manager](#menu-manager)
      - [Menu Admin](#menu-admin)
      - [Header](#header-1)
    - [Profile](#profile)
      - [Edit profile data](#edit-profile-data)
    - [Vehicles](#vehicles)
      - [Add Vehicle](#add-vehicle)
      - [Delete Vehicle](#delete-vehicle)
    - [Tickets](#tickets)
      - [Open Valid Virtual Ticket](#open-valid-virtual-ticket)
      - [Invalid Virtual Ticket](#invalid-virtual-ticket)
    - [Responsive Views](#responsive-views)
      - [Responsive Login](#responsive-login)
      - [Responsive Dashboard Parking Zones](#responsive-dashboard-parking-zones)
      - [Responsive Header](#responsive-header)
      - [Responsive Map](#responsive-map)
      - [Responsive Ticket](#responsive-ticket)
    - [Open TCP/IP Camera Simulator](#open-tcpip-camera-simulator)
      - [Start Camera](#start-camera)
  - [License](#license)
  - [Contact](#contact)

<br>
<hr>

## Integrated Systems:
<br>

<div style="font-size:1.5em">


  1. <strong>Digital Twin</strong> (Parking Administration Platform and Simulator)

  2. <strong>DeviceManager</strong> (Simulated IP Cameras Manager Server)

  3. <strong>UFV MyParking WebApp</strong> (Vehicle and User Platform)
  
  
</div>

<hr>
<br>

> ## Digital Twin ScreenShot
<br>
<img align="center" src="media/img/screenshotDigitalTwin.jpg" alt="Logo" width="100%" height="100%">
<br>

<br>

> ## UFV MyParking WebApp ScreenShot
<br>
<img align="center" src="media/img/parking webapp.jpg" alt="Logo" width="100%" height="100%">
<br>
<br>

> ## Virtual Tickets 

<br>
<img align="center" src="media/img/Tickets Virtuales.jpg" alt="Logo" width="100%" height="100%">
<br>


<br>
<br>

# Important

If you want to deploy the system in your local machine, you must have a linux (unix) enviroment, we recommend the use of  ```Git Bash``` to be able to execute the ```buildDocker.sh``` script and deploy the system into container using ```docker-compose```


> ## Built With

* [PHP 8.1](https://www.php.net/distributions/php-8.1.6.tar.gz)
* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/install/)
* [Laravel 9](https://laravel.com/docs/9.x/releases)
* [Vue.js 3](https://vuejs.org/)
* [Prime Vue](https://www.primefaces.org/primevue/)
* [Python 3.10](https://www.python.org/downloads/)
* [Composer](https://getcomposer.org/)
* [npm](https://www.npmjs.com/)


> ## Technology arquitecture

<br>
<img align="center" src="media/img/tecnology arquitecture.jpg" alt="Logo" width="100%" height="100%">
<br>

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
# Getting Started

You need to install ```Git``` or ``` GitBash``` to be able to handle the scripts used by the system. Despite of that you will need to install ```Docker``` in your local machine. The system has the docker files configured and waiting for being mounted.

## Prerequisites

## For Windows 

For the installation of the system you will need:

### Install Git with Gitbash

```
https://gitforwindows.org/
```
> **_NOTE:_** If you already have a virtualizated linux bash shell, like cygwin, please make sure you can execute .sh scripts.

### Install Docker:
> **_NOTE:_**  Please check the system requirements to successfullu install docker

- Link for Windows 
https://docs.docker.com/desktop/windows/install/

- Link for Mac:
https://docs.docker.com/desktop/mac/install/

- Link for Linux:
https://docs.docker.com/desktop/linux/install/


### Use a Web Browser

Both ```Digital Twin``` and ```UFV MyParking``` systems make use of the browser to interact with the users. So make sure that you have a updated browser like Google Chrome, Firefox, Edge or Any Chromium Browser.

<p align="right">(<a href="#top">back to top</a>)</p>

# Deploying the App

## 1 - Start Docker Daemon

Here you will find more information about it:

  ```sh
  https://docs.docker.com/desktop/windows/
  ```
>  **_NOTE:_**: In windows you just need to open the Docker Desktop App

## 2 - Clone this Repository

  ```sh
  git clone https://github.com/matbmoser/SOTA.git
  ```

## 3 - Configure Credentials (Optional): 
Configure the database credentials, default settings and default of the enviroment.

>  **_NOTE:_** The system is already configurated with default values, so is optional the configuration of credentials. If you are willing to modify parameters like the connection to the Database, here there is a description. 

### Digital Twin Global Configurations:
Go to:
```sh
 cd digital-twin/src/assets/mod/configs
```
>  **_NOTE:_** If you are unsafe about editing the configurations you can let them in their default values.

The directory contains two configuration files.
```sh

├───configs
    ├───config.php ## Global configurations
    └───db.config.php ## Database configurations

```

### Device Manager Global Configurations

Go to:
```sh
 cd digital-twin/deviceManager/assets/mod/configs
```

**Device Manager Scructure:**
```sh
├───camera ## Camera Connection Files
│   └───socket ## Socket Camera Client Files
├───db ## Database files
│   ├───controllers ## Data Access Controllers
│   └───dbConfig.py #<HERE you can edit the DB Connection Settings>
├───docs ## Useful docs like SJMP protocol description
├───operators ## Encription Tools and Operators
├───protocols ## Comunication Protocols Handlers
├───server ## Server Files
└───globalConfig.py ##<HERE you can edit the global configurations> 
```

**UFV MyParking Laravel Configurations**

Go to:
```sh
 cd /webapp/src
```

Open the following file:
```
.env
```

Laravel unificates all the global configurations in only one enviroment file.
To configurate the database parameters you can access the file and modify the following parameters:
```sh
DB_CONNECTION=mysql
DB_HOST=mysql # Indicate DB Server ip or hostname.
DB_PORT=3306 # DEFAULT: MySQL 3306
DB_DATABASE=sotadb ## The default database created is sotadb.
DB_USERNAME=<username> # DEFAULT: root
DB_PASSWORD=<password>
```
## Docker Compose File
You can modify the docker compose file before building the app.

```yml
## --------------------------------------------------------------
# Parking Time Optimization System Configuration
# Author: Mathias Brunkow Moser 
# ©2022 - ALL RIGHTS RESERVED
## --------------------------------------------------------------

version: "3.9"

services:
  ## MySQL Database Configuration
  mysql:
    image: mysql
    container_name: mysql-bbdd
    environment:
      ## Database configuration
      MYSQL_DATABASE: "sotadb"
      
      MYSQL_USER: "dbadmin"
   
      MYSQL_PASSWORD: "GT9zEN(FdxSAmWiy"

      MYSQL_ROOT_PASSWORD: "s0t42022"
    ports:
      ## Port Configuration
      - "3306:3306"

    volumes:
      - ./data:/var/lib/mysql

  ## phpMyAdmin administrator configuration
  php-my-admin:
    image: phpmyadmin
    container_name: php-my-admin
    ports:
      - 7777:80
    environment:
      - PMA_HOST=mysql
    depends_on:
      - mysql

  ## UFV MyParking WebApp Configuration
  php-apache:
    container_name: php-webapp
    build:
      context: ./webapp
    environment:
      WEBAPP: "/var/www/webapp"
    ports:
      # Range of ports in production
      - "8080:80"
      ## Port range in Development
      - "3001:8001"
      - "3000:8000"
      - "3002:8002"
    volumes:
      ## Create volumes to save the configurations
      - ./webapp/src:/var/www/webapp
      - ./webapp/apache/default.conf:/etc/apache2/sites-enabled/000-default.conf
    depends_on:
      - mysql
    networks:
      ## Belongs to the internal network created
      - default
      - appNet

  ## Digital twin configuration
  digital-twin:
    container_name: digital-twin
    build:
      context: ./digital-twin
    environment:
      ## Configuration of default path variables
      DEVICE_MANAGER: "/usr/src/app"

      DIGITAL_TWIN: "/var/www/digital-twin"

    ports:
      ## Range of ports used.
      - "3333:80" # Access port to the digital twin.
      - "8888:8888" # Default device manager port.
      - "4050-4100:4050-4100" # Device manager port range.
    volumes:
      ## Volumes created to configure the environment
      - ./digital-twin/src:/var/www/digital-twin
      - ./digital-twin/php/php.ini-development:/usr/local/etc/php/php.ini-development
      - ./digital-twin/php/php.ini-production:/usr/local/etc/php/php.ini-production
      - ./digital-twin/deviceManager:/usr/src/app
      - ./digital-twin/apache/default.conf:/etc/apache2/sites-enabled/000-default.conf
    depends_on:
      - mysql
    networks:
      - default
      - appNet

## We create networks so that containers can communicate with each other.
networks:
  default: 
    driver: bridge
  appNet: 
    external: true

## The volumes used by the database will be stored in data.
volumes:
  data:

```

<p align="right">(<a href="#top">back to top</a>)</p>

## 4- Build the App

>  **_NOTE:_** When you build the docker compose container enviroment, a new directory will be created, it will contain the persistent data from the system database.
```
  ./data
```

## Execute Build Docker Script

The deployement from all the SOTA system is centralized in only one Bash Script.

For building the docker compose container enviroment run the following script.
 ```sh
  ./buildDocker.sh
 ```
>  **_ALERT:_** If you execute for the first time the script it will take some minutes.


 The script will perform a series of actions to build the containers.
 

```sh
########## < buildDocker.sh >

## Set up internal network
docker network create appNet 

## Build Docker Compose <docker-compose.yml> file required
docker-compose up -d --build

## Give permits for Laravel to access the storage.
docker exec -it php-webapp chmod -R 777 storage 

## Install all the PHP Laravel packets
docker exec -it php-webapp composer install
## Install all JS Packets 
docker exec -it php-webapp npm install

## Wait 15 seconds for MySQL Server Container to startup 
sleep 15

## Execute the preconfigured database migration. 
docker exec -it php-webapp npm run migrate 
```
>  **_NOTE:_** This is a simplified version of ```buildDocker.sh```, to show the main commands.
<p align="right">(<a href="#top">back to top</a>)</p>

# User Manual

Once the migrations are completed, the system is ready to go.

## Access To Digital Twin

You can enter in the Digital Twin accessing the following url:

```sh
 http://localhost:3333
```

For safety reasons you will be redirected to a login page in ```/login```:
<br>
<img align="center" src="media/img/digitalTwin/loginDigitalTwin.jpg" alt="Logo" width="100%" height="100%">
<br>

### **Access Digital Twin Default Credentials**
Introduce the following credentials to have access to the digital twin.

<br>
> Default <strong> Admin Credentials</strong>:

> Email: <strong> admin@myparking.com </strong><br>
> Password: <strong> 789456123 </strong> # Default Password

<br>
> Default <strong>Manager Credentials</strong>:

> Email: <strong> manager@myparking.com </strong><br>
> Password: <strong> 789456123 </strong> # Default Password

<br>
<p align="right">(<a href="#top">back to top</a>)</p>
** You can configure more default users in "```./webapp/src/database/seeders/UserSeeder.php```" and after you need to run again "```./buildDocker.sh```" to execute the migrations.

_In case you want to execute a manual migration you can use:_

```sh
docker exec -it php-webapp php artisan migrate --seed
```
<hr>

## Digital Twin Interface

The the digital twin will have some test data included so you can visualize how the data is shown:

You have two interface color modes: ```Dark Mode``` (DEFAULT) and ```Light Mode```:

### Dark Mode
<br>
<img align="center" src="media/img/digitalTwin/digitalTwinInterface.jpg" alt="Logo" width="100%" height="100%">
<br>
<br>

### Light Mode
<br>
<img align="center" src="media/img/digitalTwin/lightMode.jpg" alt="Logo" width="100%" height="100%">
<br>
<br>

>  **_NOTE:_** Here you can visualize the parking place in real time, by zones.
<p align="right">(<a href="#top">back to top</a>)</p>
<hr>

## Header

<br>
<img align="center" src="media/img/digitalTwin/digitalTwinHeader.jpg" alt="Logo" width="100%" height="100%">
<br>

<br>
In the header are able to:

* Logout
* Visualize your current information
* Change to light/dark modes
<p align="right">(<a href="#top">back to top</a>)</p>
<hr>

## Map
The map will show you the parking lot capacity status, in zones.

>  **_NOTE:_** In smartphones you will be not able to see the zones capacity just with ```Ver Plazas``` Action Button.

<br>
<img align="center" src="media/img/digitalTwin/map.jpg" alt="Logo" width="100%" height="100%">
<br>
<p align="right">(<a href="#top">back to top</a>)</p>
<hr>

## Action Buttons

<br>
<img align="center" src="media/img/digitalTwin/digitalTwinButtons.jpg" alt="Logo" width="100%" height="100%">
<br>

<br>
In the action buttons you are able to:

* Open a Camera Manager Server
* Add a new vehicle to the parking place
* Delete vehicle from parking place
* See all the vehicles inside the parking place
* Simulate the control of the barrers
* Visualize the parking place free space capacity
* Visualize the parking place filled space capacity

<p align="right">(<a href="#top">back to top</a>)</p>
<hr>

## Device Manager Server Admin
This server manages all the cameras, and recieves WebSocket and TCP connections if the structures uses the **SJMP Protocol** [```digital-twin/deviceManager/docs/SJMPProtocolDescription.pdf```](./digital-twin/deviceManager/docs/SJMPProtocolDescription.pdf) packet structure.


<img align="center" src="media/img/digitalTwin/openServerButton.jpg" alt="Logo" width="20%" height="50%">

### Before Opened
<br>
<img align="center" src="media/img/digitalTwin/openServer.jpg" alt="Logo" width="75%" height="100%">
<br><br>

When Started up a random UUID will be generated as ```serverid```.

Here you can see the server status, inside the ```digital-twin``` docker container.

### After Opened
<br>
<img align="center" src="media/img/digitalTwin/openedServer.jpg" alt="Logo" width="75%" height="100%">
<br>

<br>
In server admin you can:

* Choose a random port to open the server.
* Choose the default port.
* Open the server when is closed
* Close the server when is opened (will close all the cameras)
* If open you can see the server log inside the ```digital-twin``` container

<p align="right">(<a href="#top">back to top</a>)</p>

<hr>

## Connect Camera

<br>
<img align="center" src="media/img/digitalTwin/connectCamara.jpg" alt="Logo" width="45%" height="45%">
<br>

### Before Connected
<br>
<img align="center" src="media/img/digitalTwin/connectCamaraModal.jpg" alt="Logo" width="70%" height="50%">
<br><br>

The camera will connect to the current running server using **SJMP Protocol** [```digital-twin/deviceManager/docs/SJMPProtocolDescription.pdf```](./digital-twin/deviceManager/docs/SJMPProtocolDescription.pdf)

Here you can see the logs for the camera connected to the server in ```digital-twin``` docker container.

You will recieve a sessionid which can identify your session in the server.

### After Opened
<br>
<img align="center" src="media/img/digitalTwin/connectedCamaraModal.jpg" alt="Logo" width="70%" height="50%">
<br>

<br>
In camera admin you can:

* See camera status
* Disconnect the camera

<br>
After you connected the button will change to disconnect: 

<br>
<img align="center" src="media/img/digitalTwin/disconnectCamara.jpg" alt="Logo" width="45%" height="45%">
<br>
<br>

>  **_NOTE:_** If you reload the digital twin page, the camera will reconnect to the server and recieve a new sessionid.

<hr>


<p align="right">(<a href="#top">back to top</a>)</p>

<div id="addVehicle"></div>

## Add Vehicle Button

<br>
<img align="center" src="media/img/digitalTwin/addVehicle.jpg" alt="Logo" width="45%" height="45%">
<br>

>  **_NOTE:_** Make sure the camera is connected, before adding!

Here you can simulate to add a new vehicle like a camera.

The camera will send a **SJMP Protocol** [```digital-twin/deviceManager/docs/SJMPProtocolDescription.pdf```](./digital-twin/deviceManager/docs/SJMPProtocolDescription.pdf) IN Flag with the plate


<br>
<img align="center" src="media/img/digitalTwin/cameraEntrance.jpg" alt="Logo" width="70%" height="50%">
<br>

<hr>

<div id="deleteVehicle"></div>

## Delete Vehicle Button

<br>
<img align="center" src="media/img/digitalTwin/deleteVehicle.jpg" alt="Logo" width="45%" height="45%">
<br>

>  **_NOTE:_** Make sure the camera is connected, before adding!

Here you can simulate to delete a new vehicle like a camera.

The camera will send a **SJMP Protocol** [```digital-twin/deviceManager/docs/SJMPProtocolDescription.pdf```](./digital-twin/deviceManager/docs/SJMPProtocolDescription.pdf) IN Flag with the plate


<br>
<img align="center" src="media/img/digitalTwin/cameraExit.jpg" alt="Logo" width="70%" height="50%">
<br>

<hr>

## See Places Button

<br>
<img align="center" src="media/img/digitalTwin/plazasButton.jpg" alt="Logo" width="45%" height="45%">
<br>

Here you can see all the vehicles in the parking.

<br>
<img align="center" src="media/img/digitalTwin/filledSpaces.jpg" alt="Logo" width="70%" height="50%">
<br>

<hr>

<p align="right">(<a href="#top">back to top</a>)</p>



## Barrers Button

<br>
<img align="center" src="media/img/digitalTwin/barreraButton.jpg" alt="Logo" width="45%" height="45%">
<br>

Here you can simulate to open and close the barrers.

### Open Entrace Barrer
<br>
<img align="center" src="media/img/digitalTwin/openBarrera.jpg" alt="Logo" width="70%" height="50%">
<br><br>

### Close Entrace Barrer
<br>
<img align="center" src="media/img/digitalTwin/closeBarrera.jpg" alt="Logo" width="70%" height="50%">
<br><br>

### Change to Exit Barrer
<br>
<img align="center" src="media/img/digitalTwin/barreraExit.jpg" alt="Logo" width="70%" height="50%">
<br><br>

<br>
All the information from status will appear in the monitor.

<br>
<hr>

## Refresh and AutoRefresh Button

<br>

**_Autorefesh:_**
Every 10 seconds it will update the parking map and info if is on. 

You can click in refresh to refresh the information in the map.

### Enabled Refresh
<br>
<img align="center" src="media/img/digitalTwin/autoRefresh.jpg" alt="Logo" width="45%" height="45%">
<br>
<br><br>

### Disabled Refresh
<br>
<img align="center" src="media/img/digitalTwin/autoRefreshOff.jpg" alt="Logo" width="45%" height="45%">
<br>
<br><br>

<br>
The parking information will update then.

<br>

<p align="right">(<a href="#top">back to top</a>)</p>

<hr>

## Access To WebApp UFV MyParking

You can enter in the WebApp UFV MyParking accessing the following url
if available:

>  **_NOTE:_** If is not available you can change in the ```docker-compose.yaml``` the default port in ```php-webapp``` container, then rerun the ```./buildDocker.sh``` command.

```sh
 http://localhost:8080
```

For safety reasons you will be redirected to a login page in ```/login```:
<br>
<img align="center" src="media/img/webapp/login.jpg" alt="Logo" width="100%" height="100%">
<br>

### **Access WebApp Default Credentials**
Introduce the following credentials to have access to the webapp:

<br>
> Default <strong> Admin Credentials</strong>:

> Email: <strong> admin@myparking.com </strong><br>
> Password: <strong> 789456123 </strong> # Default Password

<br>
> Default <strong>Manager Credentials</strong>:

> Email: <strong> manager@myparking.com </strong><br>
> Password: <strong> 789456123 </strong> # Default Password

<br>
> Default <strong>User Credentials</strong>:

> Email: <strong> conductor@email.com </strong><br>
> Password: <strong> 123456789 </strong> # Default Password

## Register
You can also create your own user: 

>  **_NOTE:_** To register click in ```Registrate``` in the bottom of the login.

<br>
<img align="center" src="media/img/webapp/register.jpg" alt="Logo" width="100%" height="100%">
<br>
<br>

### Data Policy

Read the data policy if is necesary, there we specify why the data is stored.
<br>
<img align="center" src="media/img/webapp/dataPolicy.jpg" alt="Logo" width="70%" height="50%">
<br><br>

<br>


## Dashboard
The dashboard shows you all the parking places.

<br>
<img align="center" src="media/img/webapp/dashboard.jpg" alt="Logo" width="100%" height="100%">
<br>
<br>


The menu is variable by the permits of the user rol.
### Menu User

<br>
<img align="center" src="media/img/webapp/menuUser.jpg" alt="Logo" width="40%" height="50%">
<br><br>

<br>

### Menu Manager

<br>
<img align="center" src="media/img/webapp/managerMenu.jpg" alt="Logo" width="40%" height="50%">
<br><br>

<br>

### Menu Admin

<br>
<img align="center" src="media/img/webapp/menuAdmin.jpg" alt="Logo" width="40%" height="50%">
<br><br>

<br>


### Header

<br>
<img align="center" src="media/img/webapp/header.jpg" alt="Logo" width="100%" height="100%">
<br><br>

<br>

<p align="right">(<a href="#top">back to top</a>)</p>

<hr>


## Profile
Click over the icon of profile in the ```header```

Here you can see your data and permits:

>  **_NOTE:_** As a normal user you have no permits, change to admin to have more permits.

<br>
<img align="center" src="media/img/webapp/profile.jpg" alt="Logo" width="50%" height="50%">
<br>
<br>

### Edit profile data

Here you can modify your data, and password.
<br>
<img align="center" src="media/img/webapp/editPassword.jpg" alt="Logo" width="50%" height="50%">
<br>

<br>

<p align="right">(<a href="#top">back to top</a>)</p>

## Vehicles
Add vehicles so you can simulate them in the ```digital twin```

Here you can see and manage all your vehicles

<br>
<img align="center" src="media/img/webapp/vehiculos.jpg" alt="Logo" width="100%" height="100%">
<br>
<br>

### Add Vehicle

Click over the add button in the ```bottom right``` of the screen
<br>
<img align="center" src="media/img/webapp/addButton.jpg" alt="Logo" width="15%" height="20%">
<br>

Introduce your ```plate``` and ```vehicle type``` :

<br>
<img align="center" src="media/img/webapp/matricula.jpg" alt="Logo" width="40%" height="50%">
<br><br>

<br>

### Delete Vehicle

Click over the delete button in the ```right``` of the register and click on ```delete```:

<br>
<img align="center" src="media/img/webapp/deleteVehiculo.jpg" alt="Logo" width="50%" height="50%">
<br><br>

<br>

<p align="right">(<a href="#top">back to top</a>)</p>

## Tickets

>  **_NOTE:_** Go to digital twin and click over the <a href="#addVehicle">```Add Vehicle Button```</a> and add the plate you just added


You will recieve a ticket if you ```refresh the page```.

<br>
<img align="center" src="media/img/webapp/tickets.jpg" alt="Logo" width="100%" height="100%">
<br>
<br>

Click over ```Ver Ticket```:

### Open Valid Virtual Ticket

You can see your parking place in the top left:
<br>
<img align="center" src="media/img/webapp/ticket.jpg" alt="Logo" width="100%" height="100%">
<br>

>  **_NOTE:_** Go to digital twin and click over the <a href="#deleteVehicle">```Delete Vehicle Button```</a> and add the plate in your ticket and _refresh_ the page.

<br>

### Invalid Virtual Ticket

Your ticket is now invalid, because you went from the parking lot.

<br>
<img align="center" src="media/img/webapp/invalidTicket.jpg" alt="Logo" width="100%" height="100%">
<br><br>

<br>

<p align="right">(<a href="#top">back to top</a>)</p>

## Responsive Views

All the WebApp UFV MyParking is responsive so you can see how the views are in mobile:

###  Responsive Login

<br>
<img align="center" src="media/img/webapp/loginResponsive.jpg" alt="Logo" width="40%" height="50%">
<br><br>

<br>

###  Responsive Dashboard Parking Zones

<br>
<img align="center" src="media/img/webapp/responsiveDashboard.jpg" alt="Logo" width="50%" height="50%">
<br><br>

<br>


###  Responsive Header

<br>
<img align="center" src="media/img/webapp/responsiveHeader.jpg" alt="Logo" width="50%" height="50%">
<br><br>

<br>

###  Responsive Map

<br>
<img align="center" src="media/img/webapp/map.jpg" alt="Logo" width="50%" height="50%">
<br><br>

<br>

###  Responsive Ticket

<br>
<img align="center" src="media/img/webapp/responsiveTicket.jpg" alt="Logo" width="50%" height="50%">
<br><br>

<br>

<p align="right">(<a href="#top">back to top</a>)</p>

## Open TCP/IP Camera Simulator

You can open a new camera and simulate using the ```CameraManager``` simulator

>  **_NOTE:_** You need to have an ```open server```, in the ```digital twin```!

Execute the script:

```sh
 ./openCamera.sh
```

A menu will open for you to configure a ```new camera```:
<br>
<img align="center" src="media/img/camera/openCamera.jpg" alt="Logo" width="100%" height="100%">
<br>

Select the diferent options to:
* Start new Camera
* Start Default Camera, if the default server is open.
* Disconnect a camera
* Add a vehicle to parking (needs to exist)
* Delete vehicle from parking (needs to be inside)
* List all the cameras in the manager


>  **_NOTE:_** If you exit ```all the cameras``` will be closed!

###  Start Camera

Introduce the data from the open server to connect!

>  **_NOTE:_**  If you introduce empty, the default settings will be used.

<br>
<img align="center" src="media/img/camera/startCamera.jpg" alt="Logo" width="100%" height="100%">
<br><br>

<br>

>  **_NOTE:_** After this you are ready to ```add/delete vehicles```, select the ```camera``` in the list that will be deployed.
> Then you can add the ```vehicle plate```, and it is done!

<!-- LICENSE -->
# License

Distributed under the Creative Commons License. See `LICENSE.md` for more information.

Commercial use is not authorized, please contact with: Mathias Moser  - matbmoser@gmail.com

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
# Contact

Mathias Moser  - matbmoser@gmail.com

Project Link: [https://github.com/matbmoser/SOTA](https://github.com/matbmoser/SOTA)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/matbmoser/SOTA.svg?style=for-the-badge
[contributors-url]: https://github.com/matbmoser/SOTA/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/matbmoser/SOTA.svg?style=for-the-badge
[forks-url]: https://github.com/matbmoser/SOTA/network/members
[tags-shield]: https://img.shields.io/github/v/tag/matbmoser/SOTA.svg?sort=semver&style=for-the-badge
[tags-url]: https://github.com/matbmoser/SOTA/tags
[issues-shield]: https://img.shields.io/github/issues/matbmoser/SOTA.svg?style=for-the-badge
[issues-url]: https://github.com/matbmoser/SOTA/issues
[license-shield]: https://img.shields.io/github/license/matbmoser/SOTA.svg?style=for-the-badge
[license-url]: https://github.com/matbmoser/SOTA/blob/master/LICENSE.md
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/mathias-brunkow-moser
