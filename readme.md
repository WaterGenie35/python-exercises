# Python Exercises

Just some generic programming exercises using Python.

## Exercises

- [LeetCode](https://leetcode.com/problemset/)
  - [NeetCode](https://neetcode.io/practice) subset

## Environment

- [Miniconda](https://docs.anaconda.com/miniconda/index.html#latest-miniconda-installer-links)

```shell
conda env create -f environment.yml
conda activate python-exercises
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
