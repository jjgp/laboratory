# Laboratory

## Getting Started

### Installing dependencies

Currently there's a `conda` environment to support an Apple M1 device. Prior to
installing, follow the instructions to use the [tensorflow-metal PluggableDevice](https://developer.apple.com/metal/tensorflow-plugin/)
for accelerated training. It does require using macOS Monterey and [Miniforge](https://github.com/conda-forge/miniforge).
Given the prerequisites listed in the Apple developer docs, use the following command
to create the `conda` environment:

```
conda env create -f enrivonment.m1.yml
```

### Using `pre-commit`

This project uses the [pre-commit](https://pre-commit.com/) to automate tedium and
enforce code quality standards. The `pre-commit` dependency is available in the `conda`
environments. To install the `pre-commit` git hook run:

```
pre-commit install
```

It may be useful to run `pre-commit` outside of a `git` hook. To do so run read up on
the usage:

```
pre-commit run --help
```

### Unit testing

The `conda` environments include [`pytest`](https://docs.pytest.org/en/6.2.x/contents.html#)
and [`testbook`](https://testbook.readthedocs.io/en/latest/index.html). This allows for
the unit testing of notebooks in addition to python modules. The tests may also be ran
by simply using `pytest` or the VS Code UI.
