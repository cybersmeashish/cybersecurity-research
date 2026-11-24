"""Three-state AND-precondition evaluator for a synthetic acyclic attack graph.

This is not a cloud IAM-policy evaluator or exploit scanner. Effective decisions
must already be normalized by a reviewer; absent evidence remains unknown.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

STATES = {True: "reachable", False: "blocked", None: "unknown"}

def conjunction(values):
    if any(value is False for value in values):
        return False
    if all(value is True for value in values):
        return True
    return None

def validate_chain(chain):
    if chain.get("schema_version") != 1:
        raise ValueError("Unsupported schema version")
    definitions = chain.get("fact_definitions")
    if not isinstance(definitions, dict) or not definitions:
        raise ValueError("Fact definitions required")
    known = set(definitions)
    ids = set()
    rules = chain.get("rules")
    if not isinstance(rules, list) or not rules:
        raise ValueError("Rules required")
    for rule in rules:
        if not isinstance(rule, dict) or not isinstance(rule.get("id"), str):
            raise ValueError("Invalid rule")
        requirements = rule.get("requires")
        produced = rule.get("produces")
        if rule["id"] in ids:
            raise ValueError("Duplicate rule id")
        ids.add(rule["id"])
        if not isinstance(requirements, list) or not requirements:
            raise ValueError("A rule needs at least one precondition")
        if len(set(requirements)) != len(requirements):
            raise ValueError("Duplicate precondition")
        if any(not isinstance(key, str) or key not in known for key in requirements):
            raise ValueError("Unknown or non-topological precondition")
        if not isinstance(produced, str) or produced in known:
            raise ValueError("Derived node collision or cycle")
        known.add(produced)
    if chain.get("target") not in known - set(definitions):
        raise ValueError("Target must be a derived node")

def evaluate(chain, facts):
    validate_chain(chain)
    if not isinstance(facts, dict):
        raise ValueError("Facts must be an object")
    if set(facts) - set(chain["fact_definitions"]):
        raise ValueError("Unexpected fact or attempted derived-node override")
    for value in facts.values():
        if value is not None and type(value) is not bool:
            raise ValueError("Only true, false and null are supported")
    nodes = {key: facts.get(key) for key in chain["fact_definitions"]}
    trace = []
    for rule in chain["rules"]:
        value = conjunction([nodes[key] for key in rule["requires"]])
        nodes[rule["produces"]] = value
        trace.append({"rule_id": rule["id"], "produces": rule["produces"],
                      "outcome": STATES[value],
                      "preconditions": {key: STATES[nodes[key]] for key in rule["requires"]}})
    return {"chain_id": chain["id"], "outcome": STATES[nodes[chain["target"]]],
            "target": chain["target"], "trace": trace,
            "missing_facts": sorted(key for key in chain["fact_definitions"] if nodes[key] is None),
            "false_facts": sorted(key for key in chain["fact_definitions"] if nodes[key] is False),
            "scope": "synthetic reference model; not a provider finding"}

def evaluate_fixture(chains, fixture):
    if fixture.get("schema_version") != 1 or fixture.get("evidence_kind") != "synthetic":
        raise ValueError("Version 1 accepts synthetic evidence only")
    if fixture.get("chain_id") not in chains:
        raise ValueError("Unknown chain")
    result = evaluate(chains[fixture["chain_id"]], fixture.get("facts"))
    return {"fixture_id": fixture["id"], "expected_outcome": fixture["expected_outcome"],
            **result, "matches_expected": result["outcome"] == fixture["expected_outcome"]}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chains", type=Path, required=True)
    parser.add_argument("--fixtures", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    chains = {c["id"]: c for c in json.loads(args.chains.read_text())}
    results = [evaluate_fixture(chains, f) for f in json.loads(args.fixtures.read_text())]
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(results, indent=2) + "\n")
    if not all(r["matches_expected"] for r in results):
        raise SystemExit("Fixture expectations failed")
    print(json.dumps({"fixtures": len(results), "all_match": True}))

if __name__ == "__main__":
    main()
