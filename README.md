To run the tests locally:
`export BROWSER=chrome`
`python3 HoeWarmIsHetInDelft.py`

Building the project for docker:

From the terminal, at the top of the project dir
`docker build .`

`docker-compose up`

Environment Variables:

`BROWSER`
Set at docker-compose under 'environment'
OR 
Set at config.yml to run it locally
`env`
Set to local or docker

Chromedriver is installed using homebrew on Mac and it was added to the $PATH.
So the path to the chromedriver is not required to be added to the ChromeOptions
On Docker, chrome is a separate node registering to selenium-hub.

More options to run from docker:
If selenium-hub and chrome are already running and there are changes to the test project.
To test only the changes we can re-build the test project alone and run the tests.

Building the docker image:
`docker build -t uitests_temperature_tests .`

Running the tests:
`docker run -d uitests_temperature_tests`

Need to find a mechanism to validate the gitlab-ci.yml file.
Can be done by installing a runner.
