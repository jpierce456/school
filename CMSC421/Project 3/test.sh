#!/usr/bin/bash
chmod a+x bayes.py
cp bayes.py bayes
chmod a+x bayes
echo './bayes train.data classify.data'
./bayes train.data classify.data