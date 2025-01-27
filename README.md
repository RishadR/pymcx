# pymcx

Python package for [MCX](http://mcx.space/) .



## package information

### functions
- `loadmch(fname, format, endian, datadict) :` load .mch file and output the detected photons data as an array or a dictionary.
- `loadmc2(path, dimension) :`
- `create() :` create a configuration variable as a python dictionary that fallow the rules of the json structure configuration file.
- `run(cfg, flags, mcxbin) :` run the mcx simulation with the configuration cfg and mcx flags 

*All the functions can be used separately.*

## How to install
Run the setup.py using pip. Or alternatively, change your directory to the base of this project and run

```
python -m pip install .
```

## How to use it

The way the package work is as follows.

First use the `create()` function to generate a default,python dictionary, configuration parameter `cfg`. Then modify it to take in too account your simulation parameters. The dictionary fallow the same rules as the [Json](http://mcx.space/wiki/index.cgi?Doc/README) configuration file.

If needed you can create a `flags` variable to indicate the desired flags at run time. Example `flags = "--repeat 2 --reflect 0"`

To run the simulation, use the `run()` function as  `data = run(cfg,flags)`. The run function will create a Json file from the cfg dictionary and run the mcx binary as,

	./mcx -f cfg.json *flags*


At the end of the simulation the run function will automatically read the `.mch` and `.mc2` files that was generated by mcx.

Before running the simulation make sure that the mcx binary is at the root of your running python file. If not you can give the path to the mcx binary in to the run function as `run(cfg, flag, mcxpath)`


## Example

```Python

import pymcx as mcx

cfg = mcx.create() #create a default config dictionary

cfg["Session"]["Photons"] = 1e6
cfg["Optode"]["Detector"] = [{"Pos": [29.0,  19.0,  0.0], "R": 1.0}]

data = mcx.run(cfg)

```

To have more information read the Json part of the MCX [readme](http://mcx.space/wiki/index.cgi?Doc/README). The cfg variable is a python dictionary that look like a Json structure.
