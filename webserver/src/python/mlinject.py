from flask import Flask, send_file, jsonify, make_response
from flask_cors import CORS

import requests

import geopandas as gpd

import src.python.basicplotutil as bpl
import src.python.db.util as bdb

def llmqueryshapedb(query: str) -> gpd.GeoDataFrame:
    
    table_names = ["coastline", "rivers_lake_centerlines", "ocean"]
    table_names_public = ["public." + table for table in table_names]
    
    system = f"""
        PostGIS SQL generator.

        Tables:
        {", ".join(table_names_public)}

        Rules:
        - Output ONLY one SQL SELECT statement.
        - No markdown, no backticks, no explanation.
        - No writes (INSERT/UPDATE/DELETE/DDL).
        - Use ONLY given tables/columns.
        - Must return a column named geometry
        - Must be valid PostGIS SQL.

        Examples:
        show coastline -> SELECT geometry FROM public.coastline;
    """
    
    prompt={
        "system":system,
        "user":query
    }
            
    print(prompt)

    resp = requests.post(
        "http://host.docker.internal:8000/api/chat",
        json=prompt
    )
    resp.raise_for_status()
    sql_query = resp.json().get("text", "")
    
    sql_query = (
        sql_query
        .replace("```sql", "")
        .replace("```", "")
        .strip())
    
    blocked = [
        "drop",
        "delete",
        "update",
        "insert",
        "alter",
        "truncate"
    ]

    lowered = sql_query.lower()

    if any(word in lowered for word in blocked):
        raise ValueError("Dangerous SQL detected")
    
    if not sql_query.lower().startswith("select"):
        raise ValueError("Only SELECT queries allowed")
    
    print(sql_query)
    
    return bdb.run_query(sql_query)
    
    