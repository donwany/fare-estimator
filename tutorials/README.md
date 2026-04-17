## CLI (Command Line Interface)
```bash
uv --help
gemini --help
claude --help
ollama --help
git --help
gh --help
docker --help
terraform --help
minikube --help

```


## CLI Libraries
 - ArgParse
 - Click
 - Typer
 - Fire
 - Docopt
 - Cement

### Weather Usage
```python
python weather.py --city Houston
python weather.py --city Austin --units imperial
uv run weather.py --city Houston
```

### Grocery
```python
python grocery.py add --item Eggs --quantity 12
python grocery.py view
```

### Install it locally
```bash
pip install -e .
uv pip install -e .
```

### Fare V1
```python
python fare_v1.py --help
python fare_v1.py --distance 5
python fare_v2.py --distance 10 --rate 3
```

### Fare V2
```python
# help
python fare_v2.py --help
# basic
python fare_v2.py --distance 5
# with custom rate
python fare_v2.py --distance 10 --rate 3
# with currency choice
python fare_v2.py --distance 8 --currency EUR
# with multiple discounts(nargs)
python fare_2.py --distance 10 --discounts 2 1 0.5
# full example
python fare_v2.py --distance 12 --rate 2.5 --passengers 3 --currency GHS --discounts 1 0.5
```

### Fare
```python
# example
uv run fare_v1.py estimate --distance 10 --rate 3
python fare_v1.py estimate --distance 10 --rate 3
# estimate fee
fare estimate --distance 10 --rate 3
# estimate with discounts
fare estimate --distance 10 --discounts 2 1
# json output
fare estimate --distance 10 --json
# book a ride
fare book --distance 8 --pickup "Airport" --dropoff "Hotel"
# view history
fare history
# verbose mode
fare estimate --distance 5 --verbose
# username/password
fare login --username testuser
fare login --username testuser --password secret123
```

## ArgParse
```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name")
args = parser.parse_args()

print(f"Hello {args.name}")
```

### Click
```python
import click

@click.command()
@click.option('--name', default="Student")
def greet(name):
    print(f"Hello {name}")

if __name__ == "__main__":
    greet()

# python app.py --name John
```

## Typer
```python
import typer

def main(name: str = "Student"):
    print(f"Hello {name}")

typer.run(main)
```
## Docopt
```python
from docopt import docopt

doc = """
Usage:
  app.py --name=<name>
"""

args = docopt(doc)
print(args["--name"])
```

## Fire
```python
import fire

def greet(name="Student"):
    return f"Hello {name}"

if __name__ == "__main__":
    fire.Fire(greet)
    
# python app.py greet --name=John
```

## Publish: Ollama
```bash
uv init \
--package ollama-lite \
--python=3.14 \
--description "Lightweight CLI inspired by Ollama"

# project structure
ollama-lite/
│
├── pyproject.toml
├── README.md
├── LICENSE
│
└── src/
    └── ollama_lite/
        ├── __init__.py
        └── cli.py

# .toml file
[project.scripts]
ollama-lite = "ollama_lite.cli:main"

# uv build
# twine upload --username __token__ --password "pypi-xxxx" dist/*
# uv publish --username __token__ --password "pypi-xxxx"
```

### Usage
```bash
pip install ollama-lite

ollama-lite run llama3
ollama-lite pull mistral
ollama-lite --help
```