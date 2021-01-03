import csv
from typing import Dict, List

from utils.data_utils import parseInt


def _iterate_census_csv():
    path_csv = "/data/98-401-X2016044_eng_CSV/98-401-X2016044_English_CSV_data.csv"
    with open(path_csv, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield {
                "year": row["CENSUS_YEAR"],
                "geo_code": row["GEO_CODE (POR)"],
                "geo_level": row["GEO_LEVEL"],
                "geo_name": row["GEO_NAME"],
                "member_id": row["Member ID: Profile of Dissemination Areas (2247)"],
                "name": row["DIM: Profile of Dissemination Areas (2247)"],
                "value": row["Dim: Sex (3): Member ID: [1]: Total - Sex"],
                "value_male": row["Dim: Sex (3): Member ID: [2]: Male"],
                "value_female": row["Dim: Sex (3): Member ID: [3]: Female"],
            }


def iterate_census_area():
    num_stats_per_area = 2247
    i, area_stats = 0, list()
    for row in _iterate_census_csv():
        area_stat_offset = i % num_stats_per_area
        area_stats.append(row)
        if area_stat_offset == (num_stats_per_area - 1):
            yield area_stats
            area_stats = list()
        i += 1


def get_age_group_stats(area_stats: List[Dict[str, int]]):
    return {
        "id": None,
        "year": parseInt(area_stats[0]["year"]),
        "geo_level": parseInt(area_stats[0]["geo_level"]),
        "geo_code": area_stats[0]["geo_code"],
        "geo_name": area_stats[0]["geo_name"],
        "total": parseInt(area_stats[7]["value"]),
        "age_0_to_4": parseInt(area_stats[9]["value"]),
        "age_5_to_9": parseInt(area_stats[10]["value"]),
        "age_10_to_14": parseInt(area_stats[11]["value"]),
        "age_15_to_19": parseInt(area_stats[13]["value"]),
        "age_20_to_24": parseInt(area_stats[14]["value"]),
        "age_25_to_29": parseInt(area_stats[15]["value"]),
        "age_30_to_34": parseInt(area_stats[16]["value"]),
        "age_35_to_39": parseInt(area_stats[17]["value"]),
        "age_40_to_44": parseInt(area_stats[18]["value"]),
        "age_45_to_49": parseInt(area_stats[19]["value"]),
        "age_50_to_54": parseInt(area_stats[20]["value"]),
        "age_55_to_59": parseInt(area_stats[21]["value"]),
        "age_60_to_64": parseInt(area_stats[22]["value"]),
        "age_65_to_69": parseInt(area_stats[24]["value"]),
        "age_70_to_74": parseInt(area_stats[25]["value"]),
        "age_75_to_79": parseInt(area_stats[26]["value"]),
        "age_80_to_84": parseInt(area_stats[27]["value"]),
        "age_85_plus": parseInt(area_stats[28]["value"]),
    }
