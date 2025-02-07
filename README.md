# mini-rag

This is a minimal implementation of the RAG model for question answering.

## Requirements

- Python 3.8 or later

## Install Python using Miniconda

1) Download Miniconda from [here](https://docs.anaconda.com/miniconda/install/)

2) Create new environment using following command:
```bash
$ conda create -n mini-rag python=3.8
```
3) Activate the environment using the following command:
```bash
$ conda activate mini-rag
```
## Installation

### Install required packages using following command

```bash
$ pip install -r requirements.txt
```
### Setup environment variables
```bash
$ cp .env.example .env
```
Set your environments variables in the `.env` file. Like `OPEN_API_KEY` value.

## Run the FastAPI server

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

## POSTMAN collection

Download the POSTMAN collection from [/assets/mini-rag-app.postman_collection.json](/assets/mini-rag-app.postman_collection.json)