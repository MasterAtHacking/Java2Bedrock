# Java2Bedrock

Java2Bedrock is an experimental Minecraft compatibility layer that aims to allow Minecraft Java Edition clients to connect to Bedrock Dedicated Servers.

The project focuses on protocol translation, packet handling, registry generation, and compatibility between the Java and Bedrock ecosystems.

## Goals

- Java Edition client compatibility
- Bedrock Dedicated Server support
- Java ↔ Bedrock packet translation
- Automatic registry and mapping generation
- Resource pack translation
- Behavior pack and addon adaptation
- Extensible translator API
- Version-independent architecture

## Current Status

🚧 Pre-alpha

Current progress:

✅ Java server listener  
✅ Connection session management  
✅ Java handshake handling  
✅ Login state handling  
✅ Configuration state handling  
✅ Java PLAY state detection  
✅ Packet pipeline system  
✅ Packet validation framework  
✅ Registry and mapping foundations  

Currently being developed:

- Java packet decoding
- Bedrock network connection
- Packet translators
- Entity translation
- Chunk translation
- Inventory translation
- Resource pack conversion

## Architecture

Java2Bedrock is designed as a modular translation system:

Java Client
|
v
Java Protocol Handler
|
v
Packet Pipeline
|
v
Translator Layer
|
v
Bedrock Protocol Handler
|
v
Bedrock Dedicated Server


Supporting systems:

- Registry generation
- Block and item mappings
- Addon analysis
- Resource conversion tools

## Development

Java2Bedrock is currently in active development.

The project is not ready for production servers yet.


## Installation

### Requirements

- Python 3.9+
- Git
- Minecraft Java Edition client (for testing)
- Bedrock Dedicated Server (for future translation testing)

### Clone the Repository

Make sure you have Git and Python3:

To install ”Git”

```apk add git``` on linux, ```sudo apt install git``` on Ubuntu, ```sudo dnf install git``` on Fedora, ```sudo apt-get install git``` on Debian, ```sudo pacman -S git``` on Arch, and if you have HomeBrew, use ```brew install git```. On Windows, you can install Git using the Git installer. 
Go to this link for help with installing git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git


To install ”Python3”

```apk add python3``` on Linux,  ```udo apt install -y python3 python3-pip``` on Ubuntu and Debian, ```sudo dnf install -y python3 python3-pip``` on Fedora, ```sudo pacman -S python python-pip``` on Arch and Manjaro, and if you have HomeBrew, use ```brew install python3```. On Windows, install Python from the Microsoft Store / python.org installer.
Go to this link for help with installing python3: https://www.python.org/downloads/

```bash```

Clone the repo

```git clone https://github.com/MasterAtHacking/Java2Bedrock.git```

Make sure you are in the folder

```cd Java2Bedrock/java2bedrock```
### Running the Runtime

Start the Java2Bedrock runtime:

```python3 -m runtime.server```

The runtime will start listening for Java Edition connections.
### Running the Test Client
Java2Bedrock includes a development test client if you don’t have 
“Minecraft: Java Edition” or just want to quick test the connection:

```python3 -m runtime.java.test_client```

The test client is used to verify:
- Java handshake handling

- Login state handling

- Configuration state handling

- PLAY state transitions

- Packet pipeline processing

### Development Status
Java2Bedrock is currently in pre-alpha. Installation is intended for developers and testers. Features may be incomplete or change between versions.

## Notice

Only connect to servers you own or have explicit permission to access.

Do not use this project to bypass server restrictions or access unauthorized systems.

## Credits

Java2Bedrock uses protocol information and research from:

- CloudburstMC Protocol
- GeyserMC
- Minecraft protocol documentation

This project is independently developed and is not affiliated with Mojang Studios, Microsoft, GeyserMC, or CloudburstMC.
