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

```bash```
git clone //
Make sure you are in the directory.
cd Java2Bedrock/java2bedrock

## Notice

Only connect to servers you own or have explicit permission to access.

Do not use this project to bypass server restrictions or access unauthorized systems.

## Credits

Java2Bedrock uses protocol information and research from:

- CloudburstMC Protocol
- GeyserMC
- Minecraft protocol documentation

This project is independently developed and is not affiliated with Mojang Studios, Microsoft, GeyserMC, or CloudburstMC.
