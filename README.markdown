# `pythonkc.github.io-src`
---
This is the source repository for the `pythonkc.github.io` GitHub Pages output repostitory.

## How to generate the site
---
Make sure you are in the top-level directory of the repoistory.
```shell
$ pelican content/
```

## How to view the site locally
---
Make sure you are in the top-level directory of the repository.
```shell
$ cd output
$ python -m pelican.server
```
Visit `http://localhost:8000` in your browser.

## How to deploy to `https://pythonkc.github.io`
Make sure you are in the top-level directory of the repository.
```shell
$ ghp-import output
$ git push https://github.com/pythonkc/pythonkc.github.io.git gh-pages:master --force
```
Visit `https://pythonkc.github.io` to verify the deployment.
