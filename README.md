# Ingenieria del Software II - Template

![GHA Status](https://github.com/uca-argentina/project-template/actions/workflows/GHA.yml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/uca-argentina/project-template/badge.svg?branch=master)](https://coveralls.io/github/uca-argentina/project-template?branch=master)

## pathroute
├── app
│   ├── controllers
│   │       ├──food_controller
│   │       ├──user_controller
│   ├── models
│   │       ├──user
│   │       ├──food
│   ├── service
│   │       ├──food_service
│   │       ├──user_service
│   ├── auth                              !for user authentication
│   ├── routes                            !all routes are listed here
│   ├── main                              !use for initializa the app and conect to react app
│   └── config                            !initalize app here and connect with firebase credentials

## download the firebase credentials
Go to your firebase configuration => proyect configuration => service accounts (cuentas de servicio) => click on pyhton and download the file in ur computer, then add it to the proyect at the readme level.

## fill your .env with the api key!
the api key is in proyect configuration and the .env is at the same level as the readme.md

