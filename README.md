# Randomizer
Generate pseudo-random numbers in an easy and customizable way

## Usage
Download the Randomizer.py file. Run it with python3. By default, it simulates a single, six-sided, die roll (1-6 inclusive). You can use use the command line options to change parameters. See below:

   

    positional arguments:
     numDigits    Number of random values to get

    optional arguments:
      -h, --help   show this help message and exit
      -a [A]       Sets lower limit, default 1 or 0 when not specified
      -b B         The upper limit for the randomizer. Default 6
      -z           Sets to a 0-9 spread rather than default 1-6. overrides -a,-b
      -s, --stats  Prints statistics of random numbers
      --sum        Prints sum of generated values
      --sort       Sorts values lowest to highest
      --rsort      Sorts values highest to lowest
      --seed SEED  Sets the seed to a specific value, maybe for debugging
               purposes?

You can also run it with python2, but will need to install the statistics package to get statistics.
