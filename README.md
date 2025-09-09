# Pymoo subprocesses

## Requirements
Install with
```pip install -r requirements.txt```

## ElementWise
Individual members of the population are evaluated with _subprocess.check_output_ which can call any terminal command
There is a threaded and a non-threaded version
These return the values via printing to the terminal as that is what _check_output_ returns

## Whole Population
These pass the whole population to the subprocesses to be used at once
One returns in a file and the other via the same terminal way as elementwise but with a bit of string manipulation to get it back into an array
