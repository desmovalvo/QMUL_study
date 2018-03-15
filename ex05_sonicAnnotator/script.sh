#!/bin/bash

for plugin in $(sonic-annotator -l); do sonic-annotator -s $plugin > $plugin.n3 ; done
