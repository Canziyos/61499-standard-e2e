import json
from pathlib import Path

SCHEMA_PATH = Path("timing_model/schema/timing-graph.schema.json")

def show(name, sch):
    print(f"\n== {name} ==")
    print("type:", sch.get("type"))
    if "properties" in sch and isinstance(sch["properties"], dict):
        print("properties:", list(sch["properties"].keys()))
    if "items" in sch and isinstance(sch["items"], dict):
        it = sch["items"]
        print("items keys:", list(it.keys()))
        if "properties" in it and isinstance(it["properties"], dict):
            print("item.properties:", list(it["properties"].keys()))
        if "$ref" in it:
            print("item.$ref:", it["$ref"])
    if "$ref" in sch:
        print("$ref:", sch["$ref"])

def main():
    s = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    print("schema file:", SCHEMA_PATH)
    print("top-level keys:", list(s.keys()))
    props = s.get("properties", {})
    print("top-level properties:", list(props.keys()))

    for k in ["meta", "assumptions", "nodes", "edges"]:
        show(k, props.get(k, {}))

if __name__ == "__main__":
    main()
