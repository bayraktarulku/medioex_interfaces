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
