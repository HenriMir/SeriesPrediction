# Bitcoin Timeseries Prediction

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

#### Data
The data is taken from Kaggle:  
https://www.kaggle.com/mczielinski/bitcoin-historical-data
but can be any csv from financial data

website: https://www.dukascopy.com/swiss/english/marketwatch/historical/
good for FOREX data, ask, bid and volume per 15 minutes for few currencies (but not EURUSD)


### models

each model is contained in a script and posses a function "predict" that takes a panda dataframe and predict the "Open" value of the next time interval


### TODO

- RAjouter de quoi avoir un intervalle de temps stable à la srote de load_csv
- Rajouter dans le script preprocessing une fonction qui coupe les données selon leur date
- Rajouter dans le script preprocessing une fonction qui interpole les données manquantes (ex les we
dans le cas du FOREX ou des actions)
- Ecrire une métrique mathématique pour comparer deux séries temporelles 
- Ecrire un script naive_predictor comme benchmark avec comme seule stratégie une moyenne glissante sur les 
dernières réalisations

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

