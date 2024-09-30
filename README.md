# Raspberry Pi-Based Private Cloud Storage with Client-Side Encryption

A Raspberry Pi-based private cloud storage system utilizing client-side encryption for enhanced data security. This system is designed to give users full control over their data, avoiding third-party cloud providers while ensuring a secure environment.

<img src="./GITHUB%20project%20poster.png" alt="Project Logo" width="400" height="500">

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Documentation](#documentation)
4. [Setup and Installation](#setup-and-installation)
5. [Usage](#usage)
6. [User-Specific Scripts](#user-specific-scripts)
7. [Contributing](#contributing)

## Overview
This project leverages the Raspberry Pi platform to create a private cloud storage solution for small businesses or individuals who want full control over their data. With a focus on security, the system uses client-side encryption to ensure that sensitive information is encrypted before it's ever uploaded.

## Features
- Full user control over cloud storage
- AES-256 client-side encryption for data protection
- User-friendly system for uploading, managing, and encrypting files
- Dockerized Nextcloud for easy management and scalability
- Detailed documentation for setup and usage

## Documentation
- [User Guide](./docs/User%20Guide.pdf) - Instructions on how to use the system
- [Setup and Installation Guide](./docs/Setup%20and%20Installation%20Guide.pdf) - Detailed steps for setting up the Raspberry Pi-based system

## Setup and Installation
To set up the system on your Raspberry Pi, follow the detailed steps provided in the [Setup and Installation Guide](./docs/Setup%20and%20Installation%20Guide.pdf). This guide includes instructions for setting up Docker, installing Nextcloud, and configuring encryption.

## Usage
Refer to the [User Guide](./docs/User%20Guide.pdf) for detailed instructions on how to use the system, including uploading files, encrypting data, and accessing the private cloud.

## User-Specific Scripts
Each user has tailored encryption and decryption scripts. You can find the individual scripts in their respective directories below:

- **[Test User 1](./User%20Script/Test%20User%201)** - User 1's encryption and decryption scripts
- **[Test User 2](./User%20Script/Test%20User%202)** - User 2's encryption and decryption scripts

Ensure you access the correct directory for the specific user’s script.

## Contributing
Contributions are welcome. Feel free to fork the repository and submit a pull request. Thank you!
