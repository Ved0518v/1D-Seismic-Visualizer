# 1D Seismic Trace Visualizer

A Python-based forward modeling engine that simulates 1D seismic traces and acoustic wave propagation. 

This project bridges the gap between theoretical classroom geophysics and the practical, software-based data science workflows used in the modern petroleum industry. 

## Overview
Instead of relying on pre-built commercial software, this script mathematically simulates how seismic soundwaves interact with underground rock boundaries (acoustic impedance contrasts). By applying a 30 Hz Ricker wavelet and the discrete convolutional theorem, the engine generates industry-standard "wiggle traces" that help identify potential hydrocarbon pay zones.

## Tech Stack
* **Language:** Python
* **Libraries:** NumPy (vectorized array mathematics), Matplotlib (variable area wiggle trace visualization)

## Repository Contents
* `trace_model.py`: The core Python script containing the wavelet generation, earth reflectivity model, and convolution algorithm.
* `Detailed_Seismic_Report.pdf`: A comprehensive 15-page technical report detailing the petrophysics, mathematical architecture, and geological interpretation of the generated outputs.

## Author
**Ved Dipakkumar Parmar**  
B.Tech Petroleum Engineering  
Pandit Deendayal Energy University (PDEU)  
Documentation Coordinator, SEG × SPG × EAGE Student Chapter
