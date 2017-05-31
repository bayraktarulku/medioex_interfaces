## ZigBee Interface

### Installing ZigBee interface

No additional installation needed.  Be sure you've installed the [web interface](../web) first.

### Running ZigBee interface

Go to `zigbee` folder inside the repository and run it as root.

```sh
cd medioex_interfaces/zigbee
sudo python3 run.py
```

### How to use

In order to use ZigBee interface, you need to set your ZigBees to `AT` mode. (Not `API`)
And preferably, set your ZigBee Routers' DL and DH adresses to the broadcast adress of the network.

You should send a string with a newline ending `\n`. The string should be in the format below:

`ID|TYPE|PATH|DATA`

Each field has a format, too.

#### `ID` Format

`ID` is a hex value between `0` and `FFF`. Could be any value. This keeps ZigBees from package duplications.

#### `TYPE` Format

`TYPE` field specifies the data is a command or a reply for a command. `C` for command, `R` for reply.
There is no use of `R` while sending a command. You should probably use `C` value.

#### `PATH` Format

`PATH` is the bounce way for the command. Every router should have a unique identifier in `config.py` called `ME`
To form a `PATH`, you should join the nodes' unique identifiers with a comma (`,`). Add a semicolon (`;`) to the start and done!

Before the semicolon is the path that already taken.
After the semicolon is the path that will be taken.

*Responses will use the reverse path of the command!*

#### `DATA` Format

`DATA` is comma separated commands. The command types are below

- `DXY`: Write `Y` to the `X`th digital output. `X` is hex `[0-F]`, `Y` is char `[0-1]`
- `RXY`: Write `Y` to the `X`th relay output. `X` is hex `[0-3]`, `Y` is char `[0-1]`
- `AXY`: Write `Y` to the `X`th analog output. `X` is hex `[0-4]`, `Y` is hex `[0-FFF]`

### Response

For every sent command list -even if it's empty- values of the all inputs will be sent as response.
There is a format for that, too.

`ID|R|5;4,3,2,1|XXXXABCDEFGHIJKL`
XXXX is the hex of the all digital inputs.
You can get the values of digital inputs by following this example:

Let's take `XXXX` as `FF0A`

```
>>> vals = 'FF0A'
>>> bin(int(vals, 16))[2:].zfill(16)
'1111111100001010'
```

Here you can see the the status of every single digital input and relay.
The other `ABCDEFGHIJKL` part is the hex values of the analog inputs, 3 character for each input.


### Examples

Here are the examples for this format:

> `3|C|1;2,3,4,5|R01,DF0,A3FFF`
  I am `1`. Sender of this data.
  This data contains commands.
  The first command is `R01` means "Write 1 to relay output 0".
  The second command is `DF0` means "Write 1 to digital output 15".
  The third command is `A3FFF` means "Write 4095 to analog output 3"


> `ID|R|5;4,3,2,1|FF0AFFEEDDCCBBAA`
  I am `5`. Sender of this data.
  This data contains a reply for your command list that you've sent before.
  All digital inputs and relays are in FF0A. (Switch to binary like the example in response section)
  First Analog Input is FFE (4094)
  Second Analog Input is EDD (3805)
  Third Analog Input is CCB (3275)
  Fourth Analog Input is BAA (2986)
