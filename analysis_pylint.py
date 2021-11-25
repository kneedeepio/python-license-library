import os
import sys
from pylint import epylint as lint

# Get a list of all python files in the project
print('Compiling list of modules...')
MODULES = []
for i in os.walk(os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))):
    path, folders, files = i
    for file in files:
        if file.endswith('.py'):
            MODULES.append(os.path.join(path, file))

# Run PyLint on all of the modules, keeping the output
RESULTS = {}
ERRORS = []
print("Analyzing modules with PyLint...")
for mod in MODULES:
    print(mod)
    (stdout, stderr) = lint.py_run(mod, return_std=True) # Need to update this to specify the pylintrc at the repo base.
    RESULTS[mod] = stdout
    ERRORS.append(stderr)

# Generate a report to save in the project, keeping track of scores
print('Generating report...')
REPORT = ''
SCORES = []
for mod in RESULTS:
    res = RESULTS[mod].read()
    REPORT += '{}\n'.format(mod)
    REPORT += res.replace(' {}:'.format(mod), 'line ')
    REPORT += '\n\n'

    # Get the score of the result
    score_line = res.strip().split('\n')[-1]
    if score_line:
        score = float(score_line.split()[6].split('/')[0])
        SCORES.append(score)

# Create a summary of the analysis
ANALYSIS = 'Files analyzed: {}\nAverage score: {}\n\n'.format(str(len(SCORES)), str(sum(SCORES)/len(SCORES)))
REPORT = REPORT + ANALYSIS

# Dump report to console
print(REPORT)

# Exit with a non-zero code if a score was too low
if min(SCORES) < 6:
    print('Analysis score too low, exiting with error code 1')
    sys.exit(1)
sys.exit(0)
