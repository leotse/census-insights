import os


def get_db_url():
    stage = os.environ.get("STAGE") or "dev"
    if stage == "dev":
        return "postgres://postgres@db/census_canada"
    elif stage == "staging":
        return "postgres://postgres@census-db/census_canada"
    raise ValueError(f"unsupported stage: {stage}")
