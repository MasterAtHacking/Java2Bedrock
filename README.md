# Java2Bedrock

Java2Bedrock is an experimental Minecraft compatibility layer that aims to allow Minecraft Java Edition clients to connect to Bedrock Dedicated Servers.

The project focuses on protocol translation, packet handling, registry generation, and compatibility between the Java and Bedrock ecosystems.

## Repository

Source code:

https://github.com/MasterAtHacking/Java2Bedrock

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

```text
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
```

Supporting systems:

- Registry generation
- Block and item mappings
- Addon analysis
- Resource conversion tools

## Development

Java2Bedrock is currently in active development.

The project is intended for development, testing, and research purposes.

## Installation

### Requirements

- Python 3.9+
- Git
- Minecraft Java Edition client (for testing)
- Bedrock Dedicated Server (for future translation testing)

### Installing Git

Linux:

Alpine:
```bash
apk add git
```

Ubuntu/Debian:
```bash
sudo apt install git
```

Fedora:
```bash
sudo dnf install git
```

Arch:
```bash
sudo pacman -S git
```

Homebrew:
```bash
brew install git
```

Windows:

Install Git from:

https://git-scm.com/

### Installing Python 3

Linux:

Alpine:
```bash
apk add python3
```

Ubuntu/Debian:
```bash
sudo apt install -y python3 python3-pip
```

Fedora:
```bash
sudo dnf install -y python3 python3-pip
```

Arch/Manjaro:
```bash
sudo pacman -S python python-pip
```

Homebrew:
```bash
brew install python3
```

Windows:

Install Python from:

https://www.python.org/downloads/

### Clone the Repository

```bash
git clone https://github.com/MasterAtHacking/Java2Bedrock.git
```

Enter the project folder:

```bash
cd Java2Bedrock/java2bedrock
```

## Running the Runtime

Start the Java2Bedrock runtime:

```bash
python3 -m runtime.server
```

The runtime will start listening for Java Edition connections.

## Running the Test Client

Java2Bedrock includes a development test client for testing the connection:

```bash
python3 -m runtime.java.test_client
```

The test client verifies:

- Java handshake handling
- Login state handling
- Configuration state handling
- PLAY state transitions
- Packet pipeline processing

## Version

Current version:

0.0.1-alpha

## Development Status

Java2Bedrock is currently in pre-alpha.

Installation is intended for developers and testers. Features may be incomplete or change between versions.

## Notice

Only connect to servers you own or have explicit permission to access.

Do not use this project to bypass server restrictions or access unauthorized systems.

## Credits

Java2Bedrock uses protocol information and research from:

- CloudburstMC Protocol
- GeyserMC
- Minecraft protocol documentation

This project is independently developed and is not affiliated with Mojang Studios, Microsoft, GeyserMC, or CloudburstMC.
