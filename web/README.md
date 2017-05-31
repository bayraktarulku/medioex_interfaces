## Web Interface

The web interface contains no HTML templates. Just a simple API.

All endpoints implemented as a `GET` request. So you can use `curl` to test it quickly.

### Installing web interface
Clone the repository
```sh
git clone git@github.com:nejdetckenobi/medioex_interfaces.git
```

Go to `web` folder inside the repository.
```sh
cd medioex_interfaces/web
```

Run the installation script as root. That will download the required libs and install them.
```sh
sudo ./install.sh
```

### Running web interface

Go to `web` folder inside the repository and run it as root.

```sh
cd medioex_interfaces/web
sudo python3 run.py
```

### How to use

The interface contains 6 endpoints

- `/api/ai`: This endpoint reads values from Analog Inputs.
- `/api/ao`: This endpoint writes to Analog Outputs.
- `/api/di`: This endpoint reads values from Digital Inputs.
- `/api/do`: This endpoint writes to Digital Outputs.
- `/api/ro`: This endpoint writes to Relay Outputs.
- `/api/temperature`: This endpoint reads from the default temperature sensor on MedIOEx. Gives floating value. (Celsius)

These endpoints accepts the parameters below:

- `pin`: `[1-4]` for Analog Outputs and Analog Inputs, `[1-12]` for Digital Outputs, `[13-16]` for Relay  Outputs, `[1-16]` for Digital Inputs.

- `val`: `[0-1]` for Digitals, `[0-4095]` for Analogs.

**Note**: `val` parameter is only for writing purposes. All endpoints return JSON.
