#!/usr/bin/env bash

ascii2der -i encrypted-modified.ascii -o encrypted-modified.der
base64 encrypted-modified.der > encrypted-modified.base64
cat encrypted-modified.base64
