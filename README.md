# Description of your project!

Edit the pyproject.toml file to reflect organisation of your project.

If you want a command line interface, those are specified under `project.scripts` section (line 31).

The `src/myproject/cli.py` presents an example of a command line application that uses `SciTrack` for logging, and `click` for specifying the interface.

Once you have edited this toml (making sure you've added it and any others you need into your project repository), you can do a "developer" install as

```
$ flit install -s --python `which python`
```

When it's correctly installed, you can run the following

```
$ myproject demo-echo "blah blah"
blah blah
```
where the output will be blue.

## Testing

I've included a test file that uses the `click` test runner. I have also included a `noxfile.py`

In the top-level directory, the following commands will run the tests

```
$ pytest
```

or

```
$ nox -s test-3.10
```

which will also generate a xml formatted coverage report. This is useful within a GitHub action for upload to codecov.

or

```
$ nox -s testcov
```

Which will produce a coverage report in html format in the top level directory.
