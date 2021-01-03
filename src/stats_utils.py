from typing import Dict, List

from utils import parseInt


def get_age_group_stats(area_stats: List[Dict[str, int]]):
    return {
        "0_to_4": parseInt(area_stats[9]["value"]),
        "5_to_9": parseInt(area_stats[10]["value"]),
        "10_to_14": parseInt(area_stats[11]["value"]),
        "15_to_19": parseInt(area_stats[13]["value"]),
        "20_to_24": parseInt(area_stats[14]["value"]),
        "25_to_29": parseInt(area_stats[15]["value"]),
        "30_to_34": parseInt(area_stats[16]["value"]),
        "35_to_39": parseInt(area_stats[17]["value"]),
        "40_to_44": parseInt(area_stats[18]["value"]),
        "45_to_49": parseInt(area_stats[19]["value"]),
        "50_to_54": parseInt(area_stats[20]["value"]),
        "55_to_59": parseInt(area_stats[21]["value"]),
        "60_to_64": parseInt(area_stats[22]["value"]),
        "65_to_69": parseInt(area_stats[24]["value"]),
        "70_to_74": parseInt(area_stats[25]["value"]),
        "75_to_79": parseInt(area_stats[26]["value"]),
        "80_to_84": parseInt(area_stats[27]["value"]),
        "85_plus": parseInt(area_stats[28]["value"]),
    }
