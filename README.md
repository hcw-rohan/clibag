# Command Line Interface Based Adventure Game (CLIBAG) Yes it's a terrible title

Framework for building a Text based adventure game that runs from the command line. Uses a Flask API to serve decisions/narrative etc.

## Getting Started

You'll need Python3, Flask and the requests library installed. Once downloaded, open up the server directory and get the Flask server running

```
export FLASK_APP=api.py
export FLASK_DEBUG=1
flask run
```

Then head back to the root directory and run the install script.

```
./install.sh
```

Then run the game
```
clibag
```

### Prerequisites

Python3, Flask, requests, colorama.

On apt-get platforms (you will proabably need sudo)

```
apt-get install python3 pip3
pip3 install flask requests colorama
```

### Installing

See above


## Built With

* [Flask](http://flask.pocoo.org/)

## Contributing

Please read [CONTRIBUTING.md](CONTRUBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/hcw-rohan/clibag/tags). 

## Authors

* **Rohan Latimer** - *Initial work* - [High Country Web](https://highcountryweb.com.au

See also the list of [contributors](https://github.com/hcw-rohan/clibag/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENCE.md](LICENCE.md) file for details

## Acknowledgments

* TBC
