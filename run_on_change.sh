#!/bin/bash

while true; do
    fswatch -1 bong_generator.py
    python create_series_x.py
done
