
## Install
```bash
uv add argparse
# or 
uv sync
```

## Usage
```bash
python main.py --distance 8.7 --rate 5.5 --currency EUR
uv run main.py --distance 8.7 --rate 5.5 --currency USD
```

## Install
```bash
uv pip install -e .
```

## Run
```bash
aboboyaa --distance 8.7 --rate 5.5 --currency USD
```

## Commands
 - [uv] - `appName`
 - `publish` | `add` | `remove` - commands (verb)
 - `[options]` - `--username` | `--password`
 - [uv] publish --username ... --password ...
 - [uv] add requests [options]
 - `aboboyaa` estimate --distance 10 --rate 2.5
```bash
publish
  --username
  --password
  
estimate
  --distance
  --rate
  
book
  --distance
  --pickup
  --dropoff

# current
aboboyaa --distance 10 --rate 2.5
uv run cli.py --distance 10 --rate -2.5
# upgrade
uv run cli.py estimate --distance 10 --rate 2.5
# finally
aboboyaa estimate --distance 10 --rate 2.5
 
# USAGE
uv run cli.py estimate --distance 10 --rate 2.5
uv run cli.py book --distance 559 --rate 2.7 --pickup "Dallas" --dropoff "Houston"
uv run cli.py login --username "admin" --password "Dallas"
uv run cli.py doctor --question "I am sick of hypertension"

aboboyaa book --distance 559 --pickup "Dallas" --dropoff "Houston"
```
