# Python Exercises

Just some generic programming exercises using Python.

## Exercises

- [Project Euler](https://projecteuler.net/archives)

  ![Image of the project euler progress badge](https://projecteuler.net/profile/WaterGenie35.png)

- [LeetCode](https://leetcode.com/problemset/)
  - [NeetCode](https://neetcode.io/practice) subset

## Environment

- [Miniconda](https://docs.anaconda.com/miniconda/index.html#latest-miniconda-installer-links)

```shell
conda env create -f environment.yml
conda activate python-exercises
```

## Run

```shell
python src/main.py EXERCISE PROBLEM_NUMBER

# Example
python src/main.py project_euler 1
```

## Development

### Dependencies
```shell
conda install PACKAGE
conda env export --no-builds | grep -v "prefix" > environment.yml
```

### Testing
```shell
pytest
```

### Documenting
- Save raw project euler post content before submitting since they are non-permanent.
