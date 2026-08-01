# Java2Bedrock

## Vision

Java2Bedrock is a commercial reverse-Geyser platform.

Its goal is to allow Java Edition players to join Bedrock Edition
servers by translating protocols, packets, gameplay, resources,
entities, inventories and world data in real time.

The Python project builds registries, mappings and tooling used by
the runtime translator.

The runtime translator will eventually be written in Java.

-------------------------------------------------------

## Project Goals

b
" Commercial quality
b
" Modular architecture
b
" Fast
b
" Version independent
b
" Easy to extend
b
" Automatic addon support
b
" Automatic mapping generation

-------------------------------------------------------

## Current Architecture

core/

loaders/
registries/

Current registry:
b
" Blocks

Current loaders:
b
" Server
b
" Addons
b
" Resources

-------------------------------------------------------

## Coding Style

Every loader does ONE job.

Registries never load files.

Loaders never contain mappings.

Everything is modular.

Debug functions stay separate.

No giant files.

-------------------------------------------------------

## Current Progress

bbbbbbbb-------------------------------------------------------

## Next Goals

Item Registry

Entity Registry

Recipe Registry

Biome Registry

Chunk Parser

Runtime ID Mapping

-------------------------------------------------------

## Long-term Vision

Python

b


Generated Registries

b


Java Runtime

b


Java Client b
 Bedrock Server
