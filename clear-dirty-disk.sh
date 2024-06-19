#!/bin/bash
# $1 : disk path

sudo ntfsfix --clear-dirty $1
