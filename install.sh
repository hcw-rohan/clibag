#!/bin/bash
chmod +x clibag.py
echo "alias clibag='python3 ${PWD}/clibag.py'" >> ~/.bashrc
exec bash