# funplot
Python CLI to plot functions graphs

# Installation

1. Download the latest version
2. Extract files
3. Inside the directory run
  ```sh
  pip3 install .
  ```

# Examples

```sh
funplot draw -if examples/cos.json --figure cos.png
```

![Cosine](https://raw.githubusercontent.com/mastro-elfo/funplot/main/screenshots/cos.png)

```sh
funplot draw -if examples/hyperbole2.json --figure hyperbole2.png
```
![hyperbole2](https://raw.githubusercontent.com/mastro-elfo/funplot/main/screenshots/hyperbole2.png)

```sh
funplot draw -if examples/hyperbole2.json --figure tan_cot.png
```

![Tangent and Cotangent](https://raw.githubusercontent.com/mastro-elfo/funplot/main/screenshots/tan_cot.png)

# Commands

## `draw`

```sh
funplot draw <options>
```

### Options

#### `-f`, `--function` (str, multiple)
The function or list of functions to plot.

```sh
funplot draw -f "cos(x)" -f "sin(x)"
```

#### `-ld` `--left-domain` (float)
Domain left limit.

#### `-rd` `--right-domain` (float)
Domain right limit.

#### `--points` (int)
Number of points to plot the function.

#### `-ll` `--lower-limit` (float)
Function lower limit.

#### `-ul` `--upper-limit` (float)
Function upper limit.

#### `-t` `--title` (str)
Title of the graph.

#### `-va` `--vertical-asymptote` (float, multiple)
X coordinate of a vertial asymptote.

#### `-ha` `--horizontal-asymptote` (float, multiple)
Y coordinate of an horizontal asymptote.

#### `-oa` `--oblique-asymptote` ((float, float), multiple)
A pair of values which represent the slope and intercept of an oblique asymptote.

```sh
funplot draw <options> -oa 1 -1
```

#### `-p` `--point` ((float, float), multiple)
X and Y coordinate of a point.

```sh
funplot draw <options> -p -1 -2
```

#### `-if` `--input-file` (str)
Loads config from a JSON file.

#### `-of` `--output-file` (str)
Dumps config to a JSON file.

#### `--figure` (str)
File name of the output image. The format is inferred from the extension.

```sh
funplot draw <options> --figure "filename.pdf"
```
