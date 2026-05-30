
# GiAtlas

GiAtlas is a full-stack geospatial data exploration platform combining PostGIS, Flask, React (Leaflet), and a local LLM-driven SQL generation pipeline for natural language querying and interactive map visualization of spatial datasets.

The system is designed around constrained SQL execution over PostGIS with safety validation and deterministic geospatial rendering.

## Overview

GiAtlas consists of four components:

- Frontend: React + Leaflet UI for map-based exploration
- Backend: Flask API for geospatial query execution and dataset serving
- Database: PostgreSQL + PostGIS for spatial storage and queries
- LLM Router: Django + llama.cpp service for natural language to SQL translation

## Architecture

User input → React → Flask API → LLM-generated SQL → validation layer → PostGIS → GeoJSON → Leaflet rendering

Key constraints on generated SQL:
- Only SELECT queries allowed
- Must return a geometry column
- Only whitelisted tables are accessible
- All queries are sanitized before execution

## Features

Frontend:
- React + TypeScript interface
- Leaflet-based interactive map rendering
- Dynamic GeoJSON loading from backend
- Query input for natural language geospatial search

Backend:
- Flask API for GeoJSON and dataset endpoints
- GeoPandas for spatial processing
- PostGIS integration for spatial queries
- Natural Earth ingestion pipeline
- Fallback handling for invalid or unsafe queries

LLM Integration:
- Local inference via llama.cpp (Qwen model)
- Natural language to PostGIS SQL translation
- Constrained prompting for safe query generation
- SQL sanitization and validation layer
- Optional external model support

Database:
- PostgreSQL 16 with PostGIS extension
- Spatial datasets:
  - coastline
  - rivers and lake centerlines
  - ocean and land layers

## API

POST /api/query
Executes a natural language or structured query.

Request:
{
  "file_name": "Combine rivers and lakes with coastline within 100 meters of a river mouth."
}

Response:
GeoJSON FeatureCollection

POST /api/save_image
Triggers ingestion of Natural Earth datasets.

Request:
{
  "file_name": "rivers"
}

GET /geojson/<name>
Returns GeoJSON for a stored dataset.

## Deployment

Docker Compose services:

Frontend: localhost:5173 
Backend: localhost:5002 
PostGIS: localhost:5433
Adminer: localhost:8080
LLM API: localhost:8000 

Run:

docker compose up --build

## Design Notes

- LLM output is strictly constrained to prevent unsafe SQL execution
- Spatial queries are limited to controlled schemas
- GeoJSON is normalized to EPSG:4326 for Leaflet compatibility
- Backend includes fallback behavior for model failures
- System is designed for local-first reproducibility

## Tech Stack

React, TypeScript, Leaflet
Flask, GeoPandas
PostgreSQL, PostGIS
Django (LLM router)
llama.cpp (local inference)
Docker Compose

## Project Structure

client/        React frontend
webserver/     Flask API + geospatial logic
llm-router/    LLM inference service
docker-compose.yml

## Future Work

- Query caching for repeated spatial operations
- Vector tile rendering for improved performance
- Streaming LLM responses for interactive refinement
- Expanded dataset ingestion
- Multi-user access control
