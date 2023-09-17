# kessel

## What this is

Minimal dependency python wsgi-compatible web framework with the tried
and tested fluid-container-inspired name. This is pretty crude, so I decided
to go with 'kessel', german for 'cauldron'.

DISCLAIMER

This project is mainly a learning effort and should not be used in any
reliability- oder security-critical context.

## Features

* minimal web framework, can be anything you want.

* token auth with [pyJWT](https://pypi.org/project/PyJWT/)

* modularisation can be achieved with [recipes](#recipes)

* thread-local app context for handling `current_user`,
`current_request`, etc.

* small and readable codebase

# installation

```bash
pip install kessel
```

# usage

TODO

## recipes

TODO

## Encoding & Decoding Tokens with RS256 (RSA)

TODO

```bash
mkdir test-app && \
openssl genrsa -out test-app/private.pem 2048
```
