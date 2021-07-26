# Radiography-Classification
Radiography Classification for COVID-19 positive cases along with Normal and Viral Pneumonia 
Use of CNN to detect COVID-19 through radiography and/or computed tomography images


## Demo

### Data
https://mega.nz/folder/1sJVFCxL#SnbpwYFJDN_k0mQ9RcJJOQ

### APP
*first prediction may return an error, as the api is hosted on heroku and it ends up in the sleep state when there is no traffic*

https://rad-class-app.herokuapp.com/


## Docker image

### APP
```
docker pull tgopedrosa/radiographyclassificaiton-app
docker run tgopedrosa/radiographyclassificaiton-app
```
or
```
cd app/
docker build --tag rad-class-app .
docker run rad-class-app
``` 

### API
```
docker pull tgopedrosa/radiographyclassificaiton-api
docker run tgopedrosa/radiographyclassificaiton-api
```
or
```
cd api/
docker build --tag rad-class-api .
docker run rad-class-api
``` 
