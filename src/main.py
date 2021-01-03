import csv
from pprint import pprint

from stats_utils import get_age_group_stats


def iterate_census_csv():
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
    for row in iterate_census_csv():
        area_stat_offset = i % num_stats_per_area
        area_stats.append(row)
        if area_stat_offset == (num_stats_per_area - 1):
            yield area_stats
            area_stats = list()
        i += 1


if __name__ == "__main__":
    i = 0
    for area_stats in iterate_census_area():
        if i >= 10:
            break

        print(f"geo_level: {area_stats[0]['geo_level']}")
        print(f"geo_code: {area_stats[0]['geo_code']}")
        print(f"geo_name: {area_stats[0]['geo_name']}")

        print("age groups")
        pprint(get_age_group_stats(area_stats))
        print()

        i += 1
        break
