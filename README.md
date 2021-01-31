# datasette-ripgrep-ets

A [datasette-ripgrep](https://github.com/simonw/datasette-ripgrep) instance for
the [Enthought Tool Suite](https://docs.enthought.com/ets/) repositories. There
should be an instance running at
[https://datasette-ripgrep-ets-alicuzwd4a-uc.a.run.app/-/ripgrep](https://datasette-ripgrep-ets-alicuzwd4a-uc.a.run.app/-/ripgrep).


## Creating Development Environment

```
edm env create datasette-ripgrep-ets
edm shell -e datasette-ripgrep-ets
pip install -r requirements.txt
datasette install datasette-ripgrep
```

## Download Source Code

Download the source of the repos that you want to be able to search.

```
./download_source.sh
```

## Deploy to Google Cloud Run

Install the [`gcloud` cli](https://cloud.google.com/sdk). Execute:

```
gcloud config set run/region us-central1
gcloud config set project datasette-ripgrep-ets
datasette publish cloudrun \
          --metadata metadata.yml \
          --static all:all \
          --install=https://github.com/simonw/datasette-ripgrep/archive/main.zip \
          --apt-get-install ripgrep \
          --service datasette-ripgrep-ets
```

Note: If you run into issues with the service, try publishing without the `--service`
option the first time. Datasette will walk you through the service creation
process. Only completed, add back the `--service` option. Subsequent
deployments will replace the previous one.

## Update Requirements

Add new top-level requirements to `requirements-to-freeze.txt` first, then
freeze the environment with exact version numbers.

```
pip install -U -r requirements-to-freeze.txt
pip freeze > requirements.txt
```


