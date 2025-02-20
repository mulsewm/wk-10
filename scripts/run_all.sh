#!/bin/bash
echo "Executing full analysis pipeline..."
python3 src/analysis.py
python3 src/models.py
