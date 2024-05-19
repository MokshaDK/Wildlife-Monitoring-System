# Distributed Wildlife-Monitoring-System

## Introduction

Wildlife conservation and monitoring face significant challenges due to environmental concerns like climate change, illegal hunting, and poaching. This project aims to develop an innovative solution to track and monitor animal populations by leveraging distributed computing principles.

## Background Theory

The project follows the principle of maintaining a single-system view in distributed computing, ensuring consistency and simplicity for users interacting with the system.

## Methodology

### Architecture Overview

The distributed system architecture comprises a client machine, middleware, and distributed servers. Each component plays a crucial role in the data processing workflow.

### Working of the System

1. The client machine initiates a data processing task by sending images from camera traps to the middleware.
2. Middleware distributes images to distributed servers, each assigned to identify specific animals.
3. Servers process images concurrently and send results back to middleware, which aggregates them and sends them to the client for further analysis.

## Results and Discussion

### Model Training

- YOLO models were trained for detecting dogs, cats, and birds using collected datasets.
- Training involved image labeling, model architecture configuration, and parameter optimization.

### Inference and Counting

- Trained models performed inference on test images, identifying animal presence and counting occurrences.
- Separate CSV files were generated for each animal class containing image filenames and counts.

### Middleware Integration

- Middleware application combined separate CSV files into a single consolidated CSV file, ensuring proper formatting and alignment of data.

### User Interaction

- Combined CSV file containing animal occurrence counts was made available to users for download and analysis.

## Conclusion and Future Enhancements

The project demonstrates the potential of distributed computing in wildlife monitoring, maintaining transparency and simplicity for users. Future enhancements may include scalability improvements and integration with advanced analytics tools.

