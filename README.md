# _Another Day, Another Distro (2AD)_

**2AD** is an API developed as a study case of **FastAPI**, a Python framework for API development. 

My squad had a problem choosing a Python framework to develop API's, resulting in projects developed using Django and others using Flask. So we've decided to create a POC hoping to achieve a standard in API's implementation. 

This doc describes the process of development using FastAPI and explains the base structure of the project, so it can be used as a scaffold in further implementations.

About the project itself: recently I've found out that there's no API to get info about Linux Distributions. This information shocked me because there's an API for absolutely anything nowadays. So I've decided to match the desire of create a Linux Distro Data API and the task I was assigned for (i.e write an ADR justifiying the use o FastAPI within my squad). The result of this match was the _Another Day, Another Distro (2AD)_ API.

The documentation of the API can be found at the end point _'/docs'_, it was generated automatically by **FastAPI** usign **Swagger**. In the project structure there's a folder called _docs_ where you can find details about the project itself - like design and implementation choices.
