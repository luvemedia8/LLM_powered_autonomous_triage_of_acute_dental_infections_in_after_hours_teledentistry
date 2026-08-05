from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ClinicalSignal:
    key: str
    condition: str
    phrase: str
    level: int
    source: str
    group: str


SIGNALS = (
    ClinicalSignal(
        "periapical_abscess_00_00", "periapical_abscess", "localised swelling", 1, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_00_01", "periapical_abscess", "localised swelling", 2, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_00_02", "periapical_abscess", "localised swelling", 3, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_00_03", "periapical_abscess", "localised swelling", 4, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_00_04", "periapical_abscess", "localised swelling", 5, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_00_05", "periapical_abscess", "localised swelling", 1, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_00_06", "periapical_abscess", "localised swelling", 2, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_00_07", "periapical_abscess", "localised swelling", 3, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_00_08", "periapical_abscess", "localised swelling", 4, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_00_09", "periapical_abscess", "localised swelling", 5, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_00_10", "periapical_abscess", "localised swelling", 1, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_00_11", "periapical_abscess", "localised swelling", 2, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_00_12", "periapical_abscess", "localised swelling", 3, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_00_13", "periapical_abscess", "localised swelling", 4, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_00_14", "periapical_abscess", "localised swelling", 5, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_00_15", "periapical_abscess", "localised swelling", 1, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_00_16", "periapical_abscess", "localised swelling", 2, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_00_17", "periapical_abscess", "localised swelling", 3, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_00_18", "periapical_abscess", "localised swelling", 4, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_00_19", "periapical_abscess", "localised swelling", 5, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_00_20", "periapical_abscess", "localised swelling", 1, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_00_21", "periapical_abscess", "localised swelling", 2, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_00_22", "periapical_abscess", "localised swelling", 3, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_00_23", "periapical_abscess", "localised swelling", 4, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_01_00", "periapical_abscess", "progressive swelling", 2, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_01_01", "periapical_abscess", "progressive swelling", 3, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_01_02", "periapical_abscess", "progressive swelling", 4, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_01_03", "periapical_abscess", "progressive swelling", 5, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_01_04", "periapical_abscess", "progressive swelling", 1, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_01_05", "periapical_abscess", "progressive swelling", 2, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_01_06", "periapical_abscess", "progressive swelling", 3, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_01_07", "periapical_abscess", "progressive swelling", 4, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_01_08", "periapical_abscess", "progressive swelling", 5, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_01_09", "periapical_abscess", "progressive swelling", 1, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_01_10", "periapical_abscess", "progressive swelling", 2, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_01_11", "periapical_abscess", "progressive swelling", 3, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_01_12", "periapical_abscess", "progressive swelling", 4, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_01_13", "periapical_abscess", "progressive swelling", 5, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_01_14", "periapical_abscess", "progressive swelling", 1, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_01_15", "periapical_abscess", "progressive swelling", 2, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_01_16", "periapical_abscess", "progressive swelling", 3, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_01_17", "periapical_abscess", "progressive swelling", 4, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_01_18", "periapical_abscess", "progressive swelling", 5, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_01_19", "periapical_abscess", "progressive swelling", 1, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_01_20", "periapical_abscess", "progressive swelling", 2, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_01_21", "periapical_abscess", "progressive swelling", 3, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_01_22", "periapical_abscess", "progressive swelling", 4, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_01_23", "periapical_abscess", "progressive swelling", 5, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_02_00", "periapical_abscess", "moderate pain", 3, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_02_01", "periapical_abscess", "moderate pain", 4, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_02_02", "periapical_abscess", "moderate pain", 5, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_02_03", "periapical_abscess", "moderate pain", 1, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_02_04", "periapical_abscess", "moderate pain", 2, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_02_05", "periapical_abscess", "moderate pain", 3, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_02_06", "periapical_abscess", "moderate pain", 4, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_02_07", "periapical_abscess", "moderate pain", 5, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_02_08", "periapical_abscess", "moderate pain", 1, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_02_09", "periapical_abscess", "moderate pain", 2, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_02_10", "periapical_abscess", "moderate pain", 3, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_02_11", "periapical_abscess", "moderate pain", 4, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_02_12", "periapical_abscess", "moderate pain", 5, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_02_13", "periapical_abscess", "moderate pain", 1, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_02_14", "periapical_abscess", "moderate pain", 2, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_02_15", "periapical_abscess", "moderate pain", 3, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_02_16", "periapical_abscess", "moderate pain", 4, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_02_17", "periapical_abscess", "moderate pain", 5, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_02_18", "periapical_abscess", "moderate pain", 1, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_02_19", "periapical_abscess", "moderate pain", 2, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_02_20", "periapical_abscess", "moderate pain", 3, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_02_21", "periapical_abscess", "moderate pain", 4, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_02_22", "periapical_abscess", "moderate pain", 5, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_02_23", "periapical_abscess", "moderate pain", 1, "AAE", "D1"
    ),
    ClinicalSignal("periapical_abscess_03_00", "periapical_abscess", "high fever", 4, "IADT", "D1"),
    ClinicalSignal("periapical_abscess_03_01", "periapical_abscess", "high fever", 5, "IADT", "D1"),
    ClinicalSignal("periapical_abscess_03_02", "periapical_abscess", "high fever", 1, "IADT", "D1"),
    ClinicalSignal("periapical_abscess_03_03", "periapical_abscess", "high fever", 2, "IADT", "D1"),
    ClinicalSignal("periapical_abscess_03_04", "periapical_abscess", "high fever", 3, "IADT", "D1"),
    ClinicalSignal("periapical_abscess_03_05", "periapical_abscess", "high fever", 4, "IADT", "D1"),
    ClinicalSignal("periapical_abscess_03_06", "periapical_abscess", "high fever", 5, "IADT", "D1"),
    ClinicalSignal("periapical_abscess_03_07", "periapical_abscess", "high fever", 1, "IADT", "D1"),
    ClinicalSignal("periapical_abscess_03_08", "periapical_abscess", "high fever", 2, "IADT", "D1"),
    ClinicalSignal("periapical_abscess_03_09", "periapical_abscess", "high fever", 3, "IADT", "D1"),
    ClinicalSignal("periapical_abscess_03_10", "periapical_abscess", "high fever", 4, "IADT", "D1"),
    ClinicalSignal("periapical_abscess_03_11", "periapical_abscess", "high fever", 5, "IADT", "D1"),
    ClinicalSignal("periapical_abscess_03_12", "periapical_abscess", "high fever", 1, "IADT", "D1"),
    ClinicalSignal("periapical_abscess_03_13", "periapical_abscess", "high fever", 2, "IADT", "D1"),
    ClinicalSignal("periapical_abscess_03_14", "periapical_abscess", "high fever", 3, "IADT", "D1"),
    ClinicalSignal("periapical_abscess_03_15", "periapical_abscess", "high fever", 4, "IADT", "D1"),
    ClinicalSignal("periapical_abscess_03_16", "periapical_abscess", "high fever", 5, "IADT", "D1"),
    ClinicalSignal("periapical_abscess_03_17", "periapical_abscess", "high fever", 1, "IADT", "D1"),
    ClinicalSignal("periapical_abscess_03_18", "periapical_abscess", "high fever", 2, "IADT", "D1"),
    ClinicalSignal("periapical_abscess_03_19", "periapical_abscess", "high fever", 3, "IADT", "D1"),
    ClinicalSignal("periapical_abscess_03_20", "periapical_abscess", "high fever", 4, "IADT", "D1"),
    ClinicalSignal("periapical_abscess_03_21", "periapical_abscess", "high fever", 5, "IADT", "D1"),
    ClinicalSignal("periapical_abscess_03_22", "periapical_abscess", "high fever", 1, "IADT", "D1"),
    ClinicalSignal("periapical_abscess_03_23", "periapical_abscess", "high fever", 2, "IADT", "D1"),
    ClinicalSignal(
        "periapical_abscess_04_00", "periapical_abscess", "significant trismus", 5, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_04_01", "periapical_abscess", "significant trismus", 1, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_04_02", "periapical_abscess", "significant trismus", 2, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_04_03", "periapical_abscess", "significant trismus", 3, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_04_04", "periapical_abscess", "significant trismus", 4, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_04_05", "periapical_abscess", "significant trismus", 5, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_04_06", "periapical_abscess", "significant trismus", 1, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_04_07", "periapical_abscess", "significant trismus", 2, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_04_08", "periapical_abscess", "significant trismus", 3, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_04_09", "periapical_abscess", "significant trismus", 4, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_04_10", "periapical_abscess", "significant trismus", 5, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_04_11", "periapical_abscess", "significant trismus", 1, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_04_12", "periapical_abscess", "significant trismus", 2, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_04_13", "periapical_abscess", "significant trismus", 3, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_04_14", "periapical_abscess", "significant trismus", 4, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_04_15", "periapical_abscess", "significant trismus", 5, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_04_16", "periapical_abscess", "significant trismus", 1, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_04_17", "periapical_abscess", "significant trismus", 2, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_04_18", "periapical_abscess", "significant trismus", 3, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_04_19", "periapical_abscess", "significant trismus", 4, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_04_20", "periapical_abscess", "significant trismus", 5, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_04_21", "periapical_abscess", "significant trismus", 1, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_04_22", "periapical_abscess", "significant trismus", 2, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_04_23", "periapical_abscess", "significant trismus", 3, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_05_00", "periapical_abscess", "difficulty swallowing", 1, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_05_01", "periapical_abscess", "difficulty swallowing", 2, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_05_02", "periapical_abscess", "difficulty swallowing", 3, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_05_03", "periapical_abscess", "difficulty swallowing", 4, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_05_04", "periapical_abscess", "difficulty swallowing", 5, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_05_05", "periapical_abscess", "difficulty swallowing", 1, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_05_06", "periapical_abscess", "difficulty swallowing", 2, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_05_07", "periapical_abscess", "difficulty swallowing", 3, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_05_08", "periapical_abscess", "difficulty swallowing", 4, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_05_09", "periapical_abscess", "difficulty swallowing", 5, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_05_10", "periapical_abscess", "difficulty swallowing", 1, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_05_11", "periapical_abscess", "difficulty swallowing", 2, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_05_12", "periapical_abscess", "difficulty swallowing", 3, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_05_13", "periapical_abscess", "difficulty swallowing", 4, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_05_14", "periapical_abscess", "difficulty swallowing", 5, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_05_15", "periapical_abscess", "difficulty swallowing", 1, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_05_16", "periapical_abscess", "difficulty swallowing", 2, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_05_17", "periapical_abscess", "difficulty swallowing", 3, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_05_18", "periapical_abscess", "difficulty swallowing", 4, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_05_19", "periapical_abscess", "difficulty swallowing", 5, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_05_20", "periapical_abscess", "difficulty swallowing", 1, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_05_21", "periapical_abscess", "difficulty swallowing", 2, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_05_22", "periapical_abscess", "difficulty swallowing", 3, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_05_23", "periapical_abscess", "difficulty swallowing", 4, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_06_00", "periapical_abscess", "airway noise", 2, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_06_01", "periapical_abscess", "airway noise", 3, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_06_02", "periapical_abscess", "airway noise", 4, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_06_03", "periapical_abscess", "airway noise", 5, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_06_04", "periapical_abscess", "airway noise", 1, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_06_05", "periapical_abscess", "airway noise", 2, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_06_06", "periapical_abscess", "airway noise", 3, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_06_07", "periapical_abscess", "airway noise", 4, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_06_08", "periapical_abscess", "airway noise", 5, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_06_09", "periapical_abscess", "airway noise", 1, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_06_10", "periapical_abscess", "airway noise", 2, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_06_11", "periapical_abscess", "airway noise", 3, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_06_12", "periapical_abscess", "airway noise", 4, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_06_13", "periapical_abscess", "airway noise", 5, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_06_14", "periapical_abscess", "airway noise", 1, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_06_15", "periapical_abscess", "airway noise", 2, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_06_16", "periapical_abscess", "airway noise", 3, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_06_17", "periapical_abscess", "airway noise", 4, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_06_18", "periapical_abscess", "airway noise", 5, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_06_19", "periapical_abscess", "airway noise", 1, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_06_20", "periapical_abscess", "airway noise", 2, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_06_21", "periapical_abscess", "airway noise", 3, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_06_22", "periapical_abscess", "airway noise", 4, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_06_23", "periapical_abscess", "airway noise", 5, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_07_00", "periapical_abscess", "uncontrolled bleeding", 3, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_07_01", "periapical_abscess", "uncontrolled bleeding", 4, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_07_02", "periapical_abscess", "uncontrolled bleeding", 5, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_07_03", "periapical_abscess", "uncontrolled bleeding", 1, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_07_04", "periapical_abscess", "uncontrolled bleeding", 2, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_07_05", "periapical_abscess", "uncontrolled bleeding", 3, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_07_06", "periapical_abscess", "uncontrolled bleeding", 4, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_07_07", "periapical_abscess", "uncontrolled bleeding", 5, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_07_08", "periapical_abscess", "uncontrolled bleeding", 1, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_07_09", "periapical_abscess", "uncontrolled bleeding", 2, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_07_10", "periapical_abscess", "uncontrolled bleeding", 3, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_07_11", "periapical_abscess", "uncontrolled bleeding", 4, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_07_12", "periapical_abscess", "uncontrolled bleeding", 5, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_07_13", "periapical_abscess", "uncontrolled bleeding", 1, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_07_14", "periapical_abscess", "uncontrolled bleeding", 2, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_07_15", "periapical_abscess", "uncontrolled bleeding", 3, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_07_16", "periapical_abscess", "uncontrolled bleeding", 4, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_07_17", "periapical_abscess", "uncontrolled bleeding", 5, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_07_18", "periapical_abscess", "uncontrolled bleeding", 1, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_07_19", "periapical_abscess", "uncontrolled bleeding", 2, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_07_20", "periapical_abscess", "uncontrolled bleeding", 3, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_07_21", "periapical_abscess", "uncontrolled bleeding", 4, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_07_22", "periapical_abscess", "uncontrolled bleeding", 5, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_07_23", "periapical_abscess", "uncontrolled bleeding", 1, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_08_00", "periapical_abscess", "minor sensitivity", 4, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_08_01", "periapical_abscess", "minor sensitivity", 5, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_08_02", "periapical_abscess", "minor sensitivity", 1, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_08_03", "periapical_abscess", "minor sensitivity", 2, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_08_04", "periapical_abscess", "minor sensitivity", 3, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_08_05", "periapical_abscess", "minor sensitivity", 4, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_08_06", "periapical_abscess", "minor sensitivity", 5, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_08_07", "periapical_abscess", "minor sensitivity", 1, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_08_08", "periapical_abscess", "minor sensitivity", 2, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_08_09", "periapical_abscess", "minor sensitivity", 3, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_08_10", "periapical_abscess", "minor sensitivity", 4, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_08_11", "periapical_abscess", "minor sensitivity", 5, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_08_12", "periapical_abscess", "minor sensitivity", 1, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_08_13", "periapical_abscess", "minor sensitivity", 2, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_08_14", "periapical_abscess", "minor sensitivity", 3, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_08_15", "periapical_abscess", "minor sensitivity", 4, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_08_16", "periapical_abscess", "minor sensitivity", 5, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_08_17", "periapical_abscess", "minor sensitivity", 1, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_08_18", "periapical_abscess", "minor sensitivity", 2, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_08_19", "periapical_abscess", "minor sensitivity", 3, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_08_20", "periapical_abscess", "minor sensitivity", 4, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_08_21", "periapical_abscess", "minor sensitivity", 5, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_08_22", "periapical_abscess", "minor sensitivity", 1, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_08_23", "periapical_abscess", "minor sensitivity", 2, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_09_00", "periapical_abscess", "preventive enquiry", 5, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_09_01", "periapical_abscess", "preventive enquiry", 1, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_09_02", "periapical_abscess", "preventive enquiry", 2, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_09_03", "periapical_abscess", "preventive enquiry", 3, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_09_04", "periapical_abscess", "preventive enquiry", 4, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_09_05", "periapical_abscess", "preventive enquiry", 5, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_09_06", "periapical_abscess", "preventive enquiry", 1, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_09_07", "periapical_abscess", "preventive enquiry", 2, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_09_08", "periapical_abscess", "preventive enquiry", 3, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_09_09", "periapical_abscess", "preventive enquiry", 4, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_09_10", "periapical_abscess", "preventive enquiry", 5, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_09_11", "periapical_abscess", "preventive enquiry", 1, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_09_12", "periapical_abscess", "preventive enquiry", 2, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_09_13", "periapical_abscess", "preventive enquiry", 3, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_09_14", "periapical_abscess", "preventive enquiry", 4, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_09_15", "periapical_abscess", "preventive enquiry", 5, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_09_16", "periapical_abscess", "preventive enquiry", 1, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_09_17", "periapical_abscess", "preventive enquiry", 2, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_09_18", "periapical_abscess", "preventive enquiry", 3, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_09_19", "periapical_abscess", "preventive enquiry", 4, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_09_20", "periapical_abscess", "preventive enquiry", 5, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_09_21", "periapical_abscess", "preventive enquiry", 1, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_09_22", "periapical_abscess", "preventive enquiry", 2, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_09_23", "periapical_abscess", "preventive enquiry", 3, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_10_00", "periapical_abscess", "facial asymmetry", 1, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_10_01", "periapical_abscess", "facial asymmetry", 2, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_10_02", "periapical_abscess", "facial asymmetry", 3, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_10_03", "periapical_abscess", "facial asymmetry", 4, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_10_04", "periapical_abscess", "facial asymmetry", 5, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_10_05", "periapical_abscess", "facial asymmetry", 1, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_10_06", "periapical_abscess", "facial asymmetry", 2, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_10_07", "periapical_abscess", "facial asymmetry", 3, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_10_08", "periapical_abscess", "facial asymmetry", 4, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_10_09", "periapical_abscess", "facial asymmetry", 5, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_10_10", "periapical_abscess", "facial asymmetry", 1, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_10_11", "periapical_abscess", "facial asymmetry", 2, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_10_12", "periapical_abscess", "facial asymmetry", 3, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_10_13", "periapical_abscess", "facial asymmetry", 4, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_10_14", "periapical_abscess", "facial asymmetry", 5, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_10_15", "periapical_abscess", "facial asymmetry", 1, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_10_16", "periapical_abscess", "facial asymmetry", 2, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_10_17", "periapical_abscess", "facial asymmetry", 3, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_10_18", "periapical_abscess", "facial asymmetry", 4, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_10_19", "periapical_abscess", "facial asymmetry", 5, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_10_20", "periapical_abscess", "facial asymmetry", 1, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_10_21", "periapical_abscess", "facial asymmetry", 2, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_10_22", "periapical_abscess", "facial asymmetry", 3, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_10_23", "periapical_abscess", "facial asymmetry", 4, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_11_00",
        "periapical_abscess",
        "floor of mouth elevation",
        2,
        "IADT",
        "D1",
    ),
    ClinicalSignal(
        "periapical_abscess_11_01",
        "periapical_abscess",
        "floor of mouth elevation",
        3,
        "IADT",
        "D1",
    ),
    ClinicalSignal(
        "periapical_abscess_11_02",
        "periapical_abscess",
        "floor of mouth elevation",
        4,
        "IADT",
        "D1",
    ),
    ClinicalSignal(
        "periapical_abscess_11_03",
        "periapical_abscess",
        "floor of mouth elevation",
        5,
        "IADT",
        "D1",
    ),
    ClinicalSignal(
        "periapical_abscess_11_04",
        "periapical_abscess",
        "floor of mouth elevation",
        1,
        "IADT",
        "D1",
    ),
    ClinicalSignal(
        "periapical_abscess_11_05",
        "periapical_abscess",
        "floor of mouth elevation",
        2,
        "IADT",
        "D1",
    ),
    ClinicalSignal(
        "periapical_abscess_11_06",
        "periapical_abscess",
        "floor of mouth elevation",
        3,
        "IADT",
        "D1",
    ),
    ClinicalSignal(
        "periapical_abscess_11_07",
        "periapical_abscess",
        "floor of mouth elevation",
        4,
        "IADT",
        "D1",
    ),
    ClinicalSignal(
        "periapical_abscess_11_08",
        "periapical_abscess",
        "floor of mouth elevation",
        5,
        "IADT",
        "D1",
    ),
    ClinicalSignal(
        "periapical_abscess_11_09",
        "periapical_abscess",
        "floor of mouth elevation",
        1,
        "IADT",
        "D1",
    ),
    ClinicalSignal(
        "periapical_abscess_11_10",
        "periapical_abscess",
        "floor of mouth elevation",
        2,
        "IADT",
        "D1",
    ),
    ClinicalSignal(
        "periapical_abscess_11_11",
        "periapical_abscess",
        "floor of mouth elevation",
        3,
        "IADT",
        "D1",
    ),
    ClinicalSignal(
        "periapical_abscess_11_12",
        "periapical_abscess",
        "floor of mouth elevation",
        4,
        "IADT",
        "D1",
    ),
    ClinicalSignal(
        "periapical_abscess_11_13",
        "periapical_abscess",
        "floor of mouth elevation",
        5,
        "IADT",
        "D1",
    ),
    ClinicalSignal(
        "periapical_abscess_11_14",
        "periapical_abscess",
        "floor of mouth elevation",
        1,
        "IADT",
        "D1",
    ),
    ClinicalSignal(
        "periapical_abscess_11_15",
        "periapical_abscess",
        "floor of mouth elevation",
        2,
        "IADT",
        "D1",
    ),
    ClinicalSignal(
        "periapical_abscess_11_16",
        "periapical_abscess",
        "floor of mouth elevation",
        3,
        "IADT",
        "D1",
    ),
    ClinicalSignal(
        "periapical_abscess_11_17",
        "periapical_abscess",
        "floor of mouth elevation",
        4,
        "IADT",
        "D1",
    ),
    ClinicalSignal(
        "periapical_abscess_11_18",
        "periapical_abscess",
        "floor of mouth elevation",
        5,
        "IADT",
        "D1",
    ),
    ClinicalSignal(
        "periapical_abscess_11_19",
        "periapical_abscess",
        "floor of mouth elevation",
        1,
        "IADT",
        "D1",
    ),
    ClinicalSignal(
        "periapical_abscess_11_20",
        "periapical_abscess",
        "floor of mouth elevation",
        2,
        "IADT",
        "D1",
    ),
    ClinicalSignal(
        "periapical_abscess_11_21",
        "periapical_abscess",
        "floor of mouth elevation",
        3,
        "IADT",
        "D1",
    ),
    ClinicalSignal(
        "periapical_abscess_11_22",
        "periapical_abscess",
        "floor of mouth elevation",
        4,
        "IADT",
        "D1",
    ),
    ClinicalSignal(
        "periapical_abscess_11_23",
        "periapical_abscess",
        "floor of mouth elevation",
        5,
        "IADT",
        "D1",
    ),
    ClinicalSignal(
        "periapical_abscess_12_00", "periapical_abscess", "tongue displacement", 3, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_12_01", "periapical_abscess", "tongue displacement", 4, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_12_02", "periapical_abscess", "tongue displacement", 5, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_12_03", "periapical_abscess", "tongue displacement", 1, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_12_04", "periapical_abscess", "tongue displacement", 2, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_12_05", "periapical_abscess", "tongue displacement", 3, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_12_06", "periapical_abscess", "tongue displacement", 4, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_12_07", "periapical_abscess", "tongue displacement", 5, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_12_08", "periapical_abscess", "tongue displacement", 1, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_12_09", "periapical_abscess", "tongue displacement", 2, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_12_10", "periapical_abscess", "tongue displacement", 3, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_12_11", "periapical_abscess", "tongue displacement", 4, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_12_12", "periapical_abscess", "tongue displacement", 5, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_12_13", "periapical_abscess", "tongue displacement", 1, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_12_14", "periapical_abscess", "tongue displacement", 2, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_12_15", "periapical_abscess", "tongue displacement", 3, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_12_16", "periapical_abscess", "tongue displacement", 4, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_12_17", "periapical_abscess", "tongue displacement", 5, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_12_18", "periapical_abscess", "tongue displacement", 1, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_12_19", "periapical_abscess", "tongue displacement", 2, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_12_20", "periapical_abscess", "tongue displacement", 3, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_12_21", "periapical_abscess", "tongue displacement", 4, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_12_22", "periapical_abscess", "tongue displacement", 5, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_12_23", "periapical_abscess", "tongue displacement", 1, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_13_00", "periapical_abscess", "slow progression", 4, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_13_01", "periapical_abscess", "slow progression", 5, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_13_02", "periapical_abscess", "slow progression", 1, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_13_03", "periapical_abscess", "slow progression", 2, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_13_04", "periapical_abscess", "slow progression", 3, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_13_05", "periapical_abscess", "slow progression", 4, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_13_06", "periapical_abscess", "slow progression", 5, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_13_07", "periapical_abscess", "slow progression", 1, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_13_08", "periapical_abscess", "slow progression", 2, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_13_09", "periapical_abscess", "slow progression", 3, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_13_10", "periapical_abscess", "slow progression", 4, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_13_11", "periapical_abscess", "slow progression", 5, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_13_12", "periapical_abscess", "slow progression", 1, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_13_13", "periapical_abscess", "slow progression", 2, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_13_14", "periapical_abscess", "slow progression", 3, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_13_15", "periapical_abscess", "slow progression", 4, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_13_16", "periapical_abscess", "slow progression", 5, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_13_17", "periapical_abscess", "slow progression", 1, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_13_18", "periapical_abscess", "slow progression", 2, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_13_19", "periapical_abscess", "slow progression", 3, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_13_20", "periapical_abscess", "slow progression", 4, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_13_21", "periapical_abscess", "slow progression", 5, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_13_22", "periapical_abscess", "slow progression", 1, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_13_23", "periapical_abscess", "slow progression", 2, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_14_00", "periapical_abscess", "rapid progression", 5, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_14_01", "periapical_abscess", "rapid progression", 1, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_14_02", "periapical_abscess", "rapid progression", 2, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_14_03", "periapical_abscess", "rapid progression", 3, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_14_04", "periapical_abscess", "rapid progression", 4, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_14_05", "periapical_abscess", "rapid progression", 5, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_14_06", "periapical_abscess", "rapid progression", 1, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_14_07", "periapical_abscess", "rapid progression", 2, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_14_08", "periapical_abscess", "rapid progression", 3, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_14_09", "periapical_abscess", "rapid progression", 4, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_14_10", "periapical_abscess", "rapid progression", 5, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_14_11", "periapical_abscess", "rapid progression", 1, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_14_12", "periapical_abscess", "rapid progression", 2, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_14_13", "periapical_abscess", "rapid progression", 3, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_14_14", "periapical_abscess", "rapid progression", 4, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_14_15", "periapical_abscess", "rapid progression", 5, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_14_16", "periapical_abscess", "rapid progression", 1, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_14_17", "periapical_abscess", "rapid progression", 2, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_14_18", "periapical_abscess", "rapid progression", 3, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_14_19", "periapical_abscess", "rapid progression", 4, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_14_20", "periapical_abscess", "rapid progression", 5, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_14_21", "periapical_abscess", "rapid progression", 1, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_14_22", "periapical_abscess", "rapid progression", 2, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_14_23", "periapical_abscess", "rapid progression", 3, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_15_00", "periapical_abscess", "attenuated inflammation", 1, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_15_01", "periapical_abscess", "attenuated inflammation", 2, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_15_02", "periapical_abscess", "attenuated inflammation", 3, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_15_03", "periapical_abscess", "attenuated inflammation", 4, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_15_04", "periapical_abscess", "attenuated inflammation", 5, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_15_05", "periapical_abscess", "attenuated inflammation", 1, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_15_06", "periapical_abscess", "attenuated inflammation", 2, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_15_07", "periapical_abscess", "attenuated inflammation", 3, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_15_08", "periapical_abscess", "attenuated inflammation", 4, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_15_09", "periapical_abscess", "attenuated inflammation", 5, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_15_10", "periapical_abscess", "attenuated inflammation", 1, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_15_11", "periapical_abscess", "attenuated inflammation", 2, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_15_12", "periapical_abscess", "attenuated inflammation", 3, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_15_13", "periapical_abscess", "attenuated inflammation", 4, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_15_14", "periapical_abscess", "attenuated inflammation", 5, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_15_15", "periapical_abscess", "attenuated inflammation", 1, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_15_16", "periapical_abscess", "attenuated inflammation", 2, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_15_17", "periapical_abscess", "attenuated inflammation", 3, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_15_18", "periapical_abscess", "attenuated inflammation", 4, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_15_19", "periapical_abscess", "attenuated inflammation", 5, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_15_20", "periapical_abscess", "attenuated inflammation", 1, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_15_21", "periapical_abscess", "attenuated inflammation", 2, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_15_22", "periapical_abscess", "attenuated inflammation", 3, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_15_23", "periapical_abscess", "attenuated inflammation", 4, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_16_00", "periapical_abscess", "delayed onset", 2, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_16_01", "periapical_abscess", "delayed onset", 3, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_16_02", "periapical_abscess", "delayed onset", 4, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_16_03", "periapical_abscess", "delayed onset", 5, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_16_04", "periapical_abscess", "delayed onset", 1, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_16_05", "periapical_abscess", "delayed onset", 2, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_16_06", "periapical_abscess", "delayed onset", 3, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_16_07", "periapical_abscess", "delayed onset", 4, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_16_08", "periapical_abscess", "delayed onset", 5, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_16_09", "periapical_abscess", "delayed onset", 1, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_16_10", "periapical_abscess", "delayed onset", 2, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_16_11", "periapical_abscess", "delayed onset", 3, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_16_12", "periapical_abscess", "delayed onset", 4, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_16_13", "periapical_abscess", "delayed onset", 5, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_16_14", "periapical_abscess", "delayed onset", 1, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_16_15", "periapical_abscess", "delayed onset", 2, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_16_16", "periapical_abscess", "delayed onset", 3, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_16_17", "periapical_abscess", "delayed onset", 4, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_16_18", "periapical_abscess", "delayed onset", 5, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_16_19", "periapical_abscess", "delayed onset", 1, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_16_20", "periapical_abscess", "delayed onset", 2, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_16_21", "periapical_abscess", "delayed onset", 3, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_16_22", "periapical_abscess", "delayed onset", 4, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_16_23", "periapical_abscess", "delayed onset", 5, "ADA", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_17_00", "periapical_abscess", "medical vulnerability", 3, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_17_01", "periapical_abscess", "medical vulnerability", 4, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_17_02", "periapical_abscess", "medical vulnerability", 5, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_17_03", "periapical_abscess", "medical vulnerability", 1, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_17_04", "periapical_abscess", "medical vulnerability", 2, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_17_05", "periapical_abscess", "medical vulnerability", 3, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_17_06", "periapical_abscess", "medical vulnerability", 4, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_17_07", "periapical_abscess", "medical vulnerability", 5, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_17_08", "periapical_abscess", "medical vulnerability", 1, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_17_09", "periapical_abscess", "medical vulnerability", 2, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_17_10", "periapical_abscess", "medical vulnerability", 3, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_17_11", "periapical_abscess", "medical vulnerability", 4, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_17_12", "periapical_abscess", "medical vulnerability", 5, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_17_13", "periapical_abscess", "medical vulnerability", 1, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_17_14", "periapical_abscess", "medical vulnerability", 2, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_17_15", "periapical_abscess", "medical vulnerability", 3, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_17_16", "periapical_abscess", "medical vulnerability", 4, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_17_17", "periapical_abscess", "medical vulnerability", 5, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_17_18", "periapical_abscess", "medical vulnerability", 1, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_17_19", "periapical_abscess", "medical vulnerability", 2, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_17_20", "periapical_abscess", "medical vulnerability", 3, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_17_21", "periapical_abscess", "medical vulnerability", 4, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_17_22", "periapical_abscess", "medical vulnerability", 5, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_17_23", "periapical_abscess", "medical vulnerability", 1, "AAPD", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_18_00", "periapical_abscess", "controlled symptoms", 4, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_18_01", "periapical_abscess", "controlled symptoms", 5, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_18_02", "periapical_abscess", "controlled symptoms", 1, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_18_03", "periapical_abscess", "controlled symptoms", 2, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_18_04", "periapical_abscess", "controlled symptoms", 3, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_18_05", "periapical_abscess", "controlled symptoms", 4, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_18_06", "periapical_abscess", "controlled symptoms", 5, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_18_07", "periapical_abscess", "controlled symptoms", 1, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_18_08", "periapical_abscess", "controlled symptoms", 2, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_18_09", "periapical_abscess", "controlled symptoms", 3, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_18_10", "periapical_abscess", "controlled symptoms", 4, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_18_11", "periapical_abscess", "controlled symptoms", 5, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_18_12", "periapical_abscess", "controlled symptoms", 1, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_18_13", "periapical_abscess", "controlled symptoms", 2, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_18_14", "periapical_abscess", "controlled symptoms", 3, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_18_15", "periapical_abscess", "controlled symptoms", 4, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_18_16", "periapical_abscess", "controlled symptoms", 5, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_18_17", "periapical_abscess", "controlled symptoms", 1, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_18_18", "periapical_abscess", "controlled symptoms", 2, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_18_19", "periapical_abscess", "controlled symptoms", 3, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_18_20", "periapical_abscess", "controlled symptoms", 4, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_18_21", "periapical_abscess", "controlled symptoms", 5, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_18_22", "periapical_abscess", "controlled symptoms", 1, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_18_23", "periapical_abscess", "controlled symptoms", 2, "AAE", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_19_00", "periapical_abscess", "systemic illness", 5, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_19_01", "periapical_abscess", "systemic illness", 1, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_19_02", "periapical_abscess", "systemic illness", 2, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_19_03", "periapical_abscess", "systemic illness", 3, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_19_04", "periapical_abscess", "systemic illness", 4, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_19_05", "periapical_abscess", "systemic illness", 5, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_19_06", "periapical_abscess", "systemic illness", 1, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_19_07", "periapical_abscess", "systemic illness", 2, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_19_08", "periapical_abscess", "systemic illness", 3, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_19_09", "periapical_abscess", "systemic illness", 4, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_19_10", "periapical_abscess", "systemic illness", 5, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_19_11", "periapical_abscess", "systemic illness", 1, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_19_12", "periapical_abscess", "systemic illness", 2, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_19_13", "periapical_abscess", "systemic illness", 3, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_19_14", "periapical_abscess", "systemic illness", 4, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_19_15", "periapical_abscess", "systemic illness", 5, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_19_16", "periapical_abscess", "systemic illness", 1, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_19_17", "periapical_abscess", "systemic illness", 2, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_19_18", "periapical_abscess", "systemic illness", 3, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_19_19", "periapical_abscess", "systemic illness", 4, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_19_20", "periapical_abscess", "systemic illness", 5, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_19_21", "periapical_abscess", "systemic illness", 1, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_19_22", "periapical_abscess", "systemic illness", 2, "IADT", "D1"
    ),
    ClinicalSignal(
        "periapical_abscess_19_23", "periapical_abscess", "systemic illness", 3, "IADT", "D1"
    ),
    ClinicalSignal(
        "fascial_space_infection_00_00",
        "fascial_space_infection",
        "localised swelling",
        2,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_00_01",
        "fascial_space_infection",
        "localised swelling",
        3,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_00_02",
        "fascial_space_infection",
        "localised swelling",
        4,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_00_03",
        "fascial_space_infection",
        "localised swelling",
        5,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_00_04",
        "fascial_space_infection",
        "localised swelling",
        1,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_00_05",
        "fascial_space_infection",
        "localised swelling",
        2,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_00_06",
        "fascial_space_infection",
        "localised swelling",
        3,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_00_07",
        "fascial_space_infection",
        "localised swelling",
        4,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_00_08",
        "fascial_space_infection",
        "localised swelling",
        5,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_00_09",
        "fascial_space_infection",
        "localised swelling",
        1,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_00_10",
        "fascial_space_infection",
        "localised swelling",
        2,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_00_11",
        "fascial_space_infection",
        "localised swelling",
        3,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_00_12",
        "fascial_space_infection",
        "localised swelling",
        4,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_00_13",
        "fascial_space_infection",
        "localised swelling",
        5,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_00_14",
        "fascial_space_infection",
        "localised swelling",
        1,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_00_15",
        "fascial_space_infection",
        "localised swelling",
        2,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_00_16",
        "fascial_space_infection",
        "localised swelling",
        3,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_00_17",
        "fascial_space_infection",
        "localised swelling",
        4,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_00_18",
        "fascial_space_infection",
        "localised swelling",
        5,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_00_19",
        "fascial_space_infection",
        "localised swelling",
        1,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_00_20",
        "fascial_space_infection",
        "localised swelling",
        2,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_00_21",
        "fascial_space_infection",
        "localised swelling",
        3,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_00_22",
        "fascial_space_infection",
        "localised swelling",
        4,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_00_23",
        "fascial_space_infection",
        "localised swelling",
        5,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_01_00",
        "fascial_space_infection",
        "progressive swelling",
        3,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_01_01",
        "fascial_space_infection",
        "progressive swelling",
        4,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_01_02",
        "fascial_space_infection",
        "progressive swelling",
        5,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_01_03",
        "fascial_space_infection",
        "progressive swelling",
        1,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_01_04",
        "fascial_space_infection",
        "progressive swelling",
        2,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_01_05",
        "fascial_space_infection",
        "progressive swelling",
        3,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_01_06",
        "fascial_space_infection",
        "progressive swelling",
        4,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_01_07",
        "fascial_space_infection",
        "progressive swelling",
        5,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_01_08",
        "fascial_space_infection",
        "progressive swelling",
        1,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_01_09",
        "fascial_space_infection",
        "progressive swelling",
        2,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_01_10",
        "fascial_space_infection",
        "progressive swelling",
        3,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_01_11",
        "fascial_space_infection",
        "progressive swelling",
        4,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_01_12",
        "fascial_space_infection",
        "progressive swelling",
        5,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_01_13",
        "fascial_space_infection",
        "progressive swelling",
        1,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_01_14",
        "fascial_space_infection",
        "progressive swelling",
        2,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_01_15",
        "fascial_space_infection",
        "progressive swelling",
        3,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_01_16",
        "fascial_space_infection",
        "progressive swelling",
        4,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_01_17",
        "fascial_space_infection",
        "progressive swelling",
        5,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_01_18",
        "fascial_space_infection",
        "progressive swelling",
        1,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_01_19",
        "fascial_space_infection",
        "progressive swelling",
        2,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_01_20",
        "fascial_space_infection",
        "progressive swelling",
        3,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_01_21",
        "fascial_space_infection",
        "progressive swelling",
        4,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_01_22",
        "fascial_space_infection",
        "progressive swelling",
        5,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_01_23",
        "fascial_space_infection",
        "progressive swelling",
        1,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_02_00", "fascial_space_infection", "moderate pain", 4, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_02_01", "fascial_space_infection", "moderate pain", 5, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_02_02", "fascial_space_infection", "moderate pain", 1, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_02_03", "fascial_space_infection", "moderate pain", 2, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_02_04", "fascial_space_infection", "moderate pain", 3, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_02_05", "fascial_space_infection", "moderate pain", 4, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_02_06", "fascial_space_infection", "moderate pain", 5, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_02_07", "fascial_space_infection", "moderate pain", 1, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_02_08", "fascial_space_infection", "moderate pain", 2, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_02_09", "fascial_space_infection", "moderate pain", 3, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_02_10", "fascial_space_infection", "moderate pain", 4, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_02_11", "fascial_space_infection", "moderate pain", 5, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_02_12", "fascial_space_infection", "moderate pain", 1, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_02_13", "fascial_space_infection", "moderate pain", 2, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_02_14", "fascial_space_infection", "moderate pain", 3, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_02_15", "fascial_space_infection", "moderate pain", 4, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_02_16", "fascial_space_infection", "moderate pain", 5, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_02_17", "fascial_space_infection", "moderate pain", 1, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_02_18", "fascial_space_infection", "moderate pain", 2, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_02_19", "fascial_space_infection", "moderate pain", 3, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_02_20", "fascial_space_infection", "moderate pain", 4, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_02_21", "fascial_space_infection", "moderate pain", 5, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_02_22", "fascial_space_infection", "moderate pain", 1, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_02_23", "fascial_space_infection", "moderate pain", 2, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_03_00", "fascial_space_infection", "high fever", 5, "ADA", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_03_01", "fascial_space_infection", "high fever", 1, "ADA", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_03_02", "fascial_space_infection", "high fever", 2, "ADA", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_03_03", "fascial_space_infection", "high fever", 3, "ADA", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_03_04", "fascial_space_infection", "high fever", 4, "ADA", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_03_05", "fascial_space_infection", "high fever", 5, "ADA", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_03_06", "fascial_space_infection", "high fever", 1, "ADA", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_03_07", "fascial_space_infection", "high fever", 2, "ADA", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_03_08", "fascial_space_infection", "high fever", 3, "ADA", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_03_09", "fascial_space_infection", "high fever", 4, "ADA", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_03_10", "fascial_space_infection", "high fever", 5, "ADA", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_03_11", "fascial_space_infection", "high fever", 1, "ADA", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_03_12", "fascial_space_infection", "high fever", 2, "ADA", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_03_13", "fascial_space_infection", "high fever", 3, "ADA", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_03_14", "fascial_space_infection", "high fever", 4, "ADA", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_03_15", "fascial_space_infection", "high fever", 5, "ADA", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_03_16", "fascial_space_infection", "high fever", 1, "ADA", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_03_17", "fascial_space_infection", "high fever", 2, "ADA", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_03_18", "fascial_space_infection", "high fever", 3, "ADA", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_03_19", "fascial_space_infection", "high fever", 4, "ADA", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_03_20", "fascial_space_infection", "high fever", 5, "ADA", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_03_21", "fascial_space_infection", "high fever", 1, "ADA", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_03_22", "fascial_space_infection", "high fever", 2, "ADA", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_03_23", "fascial_space_infection", "high fever", 3, "ADA", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_04_00",
        "fascial_space_infection",
        "significant trismus",
        1,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_04_01",
        "fascial_space_infection",
        "significant trismus",
        2,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_04_02",
        "fascial_space_infection",
        "significant trismus",
        3,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_04_03",
        "fascial_space_infection",
        "significant trismus",
        4,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_04_04",
        "fascial_space_infection",
        "significant trismus",
        5,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_04_05",
        "fascial_space_infection",
        "significant trismus",
        1,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_04_06",
        "fascial_space_infection",
        "significant trismus",
        2,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_04_07",
        "fascial_space_infection",
        "significant trismus",
        3,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_04_08",
        "fascial_space_infection",
        "significant trismus",
        4,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_04_09",
        "fascial_space_infection",
        "significant trismus",
        5,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_04_10",
        "fascial_space_infection",
        "significant trismus",
        1,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_04_11",
        "fascial_space_infection",
        "significant trismus",
        2,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_04_12",
        "fascial_space_infection",
        "significant trismus",
        3,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_04_13",
        "fascial_space_infection",
        "significant trismus",
        4,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_04_14",
        "fascial_space_infection",
        "significant trismus",
        5,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_04_15",
        "fascial_space_infection",
        "significant trismus",
        1,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_04_16",
        "fascial_space_infection",
        "significant trismus",
        2,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_04_17",
        "fascial_space_infection",
        "significant trismus",
        3,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_04_18",
        "fascial_space_infection",
        "significant trismus",
        4,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_04_19",
        "fascial_space_infection",
        "significant trismus",
        5,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_04_20",
        "fascial_space_infection",
        "significant trismus",
        1,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_04_21",
        "fascial_space_infection",
        "significant trismus",
        2,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_04_22",
        "fascial_space_infection",
        "significant trismus",
        3,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_04_23",
        "fascial_space_infection",
        "significant trismus",
        4,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_05_00",
        "fascial_space_infection",
        "difficulty swallowing",
        2,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_05_01",
        "fascial_space_infection",
        "difficulty swallowing",
        3,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_05_02",
        "fascial_space_infection",
        "difficulty swallowing",
        4,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_05_03",
        "fascial_space_infection",
        "difficulty swallowing",
        5,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_05_04",
        "fascial_space_infection",
        "difficulty swallowing",
        1,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_05_05",
        "fascial_space_infection",
        "difficulty swallowing",
        2,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_05_06",
        "fascial_space_infection",
        "difficulty swallowing",
        3,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_05_07",
        "fascial_space_infection",
        "difficulty swallowing",
        4,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_05_08",
        "fascial_space_infection",
        "difficulty swallowing",
        5,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_05_09",
        "fascial_space_infection",
        "difficulty swallowing",
        1,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_05_10",
        "fascial_space_infection",
        "difficulty swallowing",
        2,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_05_11",
        "fascial_space_infection",
        "difficulty swallowing",
        3,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_05_12",
        "fascial_space_infection",
        "difficulty swallowing",
        4,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_05_13",
        "fascial_space_infection",
        "difficulty swallowing",
        5,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_05_14",
        "fascial_space_infection",
        "difficulty swallowing",
        1,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_05_15",
        "fascial_space_infection",
        "difficulty swallowing",
        2,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_05_16",
        "fascial_space_infection",
        "difficulty swallowing",
        3,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_05_17",
        "fascial_space_infection",
        "difficulty swallowing",
        4,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_05_18",
        "fascial_space_infection",
        "difficulty swallowing",
        5,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_05_19",
        "fascial_space_infection",
        "difficulty swallowing",
        1,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_05_20",
        "fascial_space_infection",
        "difficulty swallowing",
        2,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_05_21",
        "fascial_space_infection",
        "difficulty swallowing",
        3,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_05_22",
        "fascial_space_infection",
        "difficulty swallowing",
        4,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_05_23",
        "fascial_space_infection",
        "difficulty swallowing",
        5,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_06_00", "fascial_space_infection", "airway noise", 3, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_06_01", "fascial_space_infection", "airway noise", 4, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_06_02", "fascial_space_infection", "airway noise", 5, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_06_03", "fascial_space_infection", "airway noise", 1, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_06_04", "fascial_space_infection", "airway noise", 2, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_06_05", "fascial_space_infection", "airway noise", 3, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_06_06", "fascial_space_infection", "airway noise", 4, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_06_07", "fascial_space_infection", "airway noise", 5, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_06_08", "fascial_space_infection", "airway noise", 1, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_06_09", "fascial_space_infection", "airway noise", 2, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_06_10", "fascial_space_infection", "airway noise", 3, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_06_11", "fascial_space_infection", "airway noise", 4, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_06_12", "fascial_space_infection", "airway noise", 5, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_06_13", "fascial_space_infection", "airway noise", 1, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_06_14", "fascial_space_infection", "airway noise", 2, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_06_15", "fascial_space_infection", "airway noise", 3, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_06_16", "fascial_space_infection", "airway noise", 4, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_06_17", "fascial_space_infection", "airway noise", 5, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_06_18", "fascial_space_infection", "airway noise", 1, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_06_19", "fascial_space_infection", "airway noise", 2, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_06_20", "fascial_space_infection", "airway noise", 3, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_06_21", "fascial_space_infection", "airway noise", 4, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_06_22", "fascial_space_infection", "airway noise", 5, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_06_23", "fascial_space_infection", "airway noise", 1, "IADT", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_07_00",
        "fascial_space_infection",
        "uncontrolled bleeding",
        4,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_07_01",
        "fascial_space_infection",
        "uncontrolled bleeding",
        5,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_07_02",
        "fascial_space_infection",
        "uncontrolled bleeding",
        1,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_07_03",
        "fascial_space_infection",
        "uncontrolled bleeding",
        2,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_07_04",
        "fascial_space_infection",
        "uncontrolled bleeding",
        3,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_07_05",
        "fascial_space_infection",
        "uncontrolled bleeding",
        4,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_07_06",
        "fascial_space_infection",
        "uncontrolled bleeding",
        5,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_07_07",
        "fascial_space_infection",
        "uncontrolled bleeding",
        1,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_07_08",
        "fascial_space_infection",
        "uncontrolled bleeding",
        2,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_07_09",
        "fascial_space_infection",
        "uncontrolled bleeding",
        3,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_07_10",
        "fascial_space_infection",
        "uncontrolled bleeding",
        4,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_07_11",
        "fascial_space_infection",
        "uncontrolled bleeding",
        5,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_07_12",
        "fascial_space_infection",
        "uncontrolled bleeding",
        1,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_07_13",
        "fascial_space_infection",
        "uncontrolled bleeding",
        2,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_07_14",
        "fascial_space_infection",
        "uncontrolled bleeding",
        3,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_07_15",
        "fascial_space_infection",
        "uncontrolled bleeding",
        4,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_07_16",
        "fascial_space_infection",
        "uncontrolled bleeding",
        5,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_07_17",
        "fascial_space_infection",
        "uncontrolled bleeding",
        1,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_07_18",
        "fascial_space_infection",
        "uncontrolled bleeding",
        2,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_07_19",
        "fascial_space_infection",
        "uncontrolled bleeding",
        3,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_07_20",
        "fascial_space_infection",
        "uncontrolled bleeding",
        4,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_07_21",
        "fascial_space_infection",
        "uncontrolled bleeding",
        5,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_07_22",
        "fascial_space_infection",
        "uncontrolled bleeding",
        1,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_07_23",
        "fascial_space_infection",
        "uncontrolled bleeding",
        2,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_08_00",
        "fascial_space_infection",
        "minor sensitivity",
        5,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_08_01",
        "fascial_space_infection",
        "minor sensitivity",
        1,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_08_02",
        "fascial_space_infection",
        "minor sensitivity",
        2,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_08_03",
        "fascial_space_infection",
        "minor sensitivity",
        3,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_08_04",
        "fascial_space_infection",
        "minor sensitivity",
        4,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_08_05",
        "fascial_space_infection",
        "minor sensitivity",
        5,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_08_06",
        "fascial_space_infection",
        "minor sensitivity",
        1,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_08_07",
        "fascial_space_infection",
        "minor sensitivity",
        2,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_08_08",
        "fascial_space_infection",
        "minor sensitivity",
        3,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_08_09",
        "fascial_space_infection",
        "minor sensitivity",
        4,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_08_10",
        "fascial_space_infection",
        "minor sensitivity",
        5,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_08_11",
        "fascial_space_infection",
        "minor sensitivity",
        1,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_08_12",
        "fascial_space_infection",
        "minor sensitivity",
        2,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_08_13",
        "fascial_space_infection",
        "minor sensitivity",
        3,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_08_14",
        "fascial_space_infection",
        "minor sensitivity",
        4,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_08_15",
        "fascial_space_infection",
        "minor sensitivity",
        5,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_08_16",
        "fascial_space_infection",
        "minor sensitivity",
        1,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_08_17",
        "fascial_space_infection",
        "minor sensitivity",
        2,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_08_18",
        "fascial_space_infection",
        "minor sensitivity",
        3,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_08_19",
        "fascial_space_infection",
        "minor sensitivity",
        4,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_08_20",
        "fascial_space_infection",
        "minor sensitivity",
        5,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_08_21",
        "fascial_space_infection",
        "minor sensitivity",
        1,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_08_22",
        "fascial_space_infection",
        "minor sensitivity",
        2,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_08_23",
        "fascial_space_infection",
        "minor sensitivity",
        3,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_09_00",
        "fascial_space_infection",
        "preventive enquiry",
        1,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_09_01",
        "fascial_space_infection",
        "preventive enquiry",
        2,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_09_02",
        "fascial_space_infection",
        "preventive enquiry",
        3,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_09_03",
        "fascial_space_infection",
        "preventive enquiry",
        4,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_09_04",
        "fascial_space_infection",
        "preventive enquiry",
        5,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_09_05",
        "fascial_space_infection",
        "preventive enquiry",
        1,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_09_06",
        "fascial_space_infection",
        "preventive enquiry",
        2,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_09_07",
        "fascial_space_infection",
        "preventive enquiry",
        3,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_09_08",
        "fascial_space_infection",
        "preventive enquiry",
        4,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_09_09",
        "fascial_space_infection",
        "preventive enquiry",
        5,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_09_10",
        "fascial_space_infection",
        "preventive enquiry",
        1,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_09_11",
        "fascial_space_infection",
        "preventive enquiry",
        2,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_09_12",
        "fascial_space_infection",
        "preventive enquiry",
        3,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_09_13",
        "fascial_space_infection",
        "preventive enquiry",
        4,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_09_14",
        "fascial_space_infection",
        "preventive enquiry",
        5,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_09_15",
        "fascial_space_infection",
        "preventive enquiry",
        1,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_09_16",
        "fascial_space_infection",
        "preventive enquiry",
        2,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_09_17",
        "fascial_space_infection",
        "preventive enquiry",
        3,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_09_18",
        "fascial_space_infection",
        "preventive enquiry",
        4,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_09_19",
        "fascial_space_infection",
        "preventive enquiry",
        5,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_09_20",
        "fascial_space_infection",
        "preventive enquiry",
        1,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_09_21",
        "fascial_space_infection",
        "preventive enquiry",
        2,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_09_22",
        "fascial_space_infection",
        "preventive enquiry",
        3,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_09_23",
        "fascial_space_infection",
        "preventive enquiry",
        4,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_10_00",
        "fascial_space_infection",
        "facial asymmetry",
        2,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_10_01",
        "fascial_space_infection",
        "facial asymmetry",
        3,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_10_02",
        "fascial_space_infection",
        "facial asymmetry",
        4,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_10_03",
        "fascial_space_infection",
        "facial asymmetry",
        5,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_10_04",
        "fascial_space_infection",
        "facial asymmetry",
        1,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_10_05",
        "fascial_space_infection",
        "facial asymmetry",
        2,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_10_06",
        "fascial_space_infection",
        "facial asymmetry",
        3,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_10_07",
        "fascial_space_infection",
        "facial asymmetry",
        4,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_10_08",
        "fascial_space_infection",
        "facial asymmetry",
        5,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_10_09",
        "fascial_space_infection",
        "facial asymmetry",
        1,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_10_10",
        "fascial_space_infection",
        "facial asymmetry",
        2,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_10_11",
        "fascial_space_infection",
        "facial asymmetry",
        3,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_10_12",
        "fascial_space_infection",
        "facial asymmetry",
        4,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_10_13",
        "fascial_space_infection",
        "facial asymmetry",
        5,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_10_14",
        "fascial_space_infection",
        "facial asymmetry",
        1,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_10_15",
        "fascial_space_infection",
        "facial asymmetry",
        2,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_10_16",
        "fascial_space_infection",
        "facial asymmetry",
        3,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_10_17",
        "fascial_space_infection",
        "facial asymmetry",
        4,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_10_18",
        "fascial_space_infection",
        "facial asymmetry",
        5,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_10_19",
        "fascial_space_infection",
        "facial asymmetry",
        1,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_10_20",
        "fascial_space_infection",
        "facial asymmetry",
        2,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_10_21",
        "fascial_space_infection",
        "facial asymmetry",
        3,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_10_22",
        "fascial_space_infection",
        "facial asymmetry",
        4,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_10_23",
        "fascial_space_infection",
        "facial asymmetry",
        5,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_11_00",
        "fascial_space_infection",
        "floor of mouth elevation",
        3,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_11_01",
        "fascial_space_infection",
        "floor of mouth elevation",
        4,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_11_02",
        "fascial_space_infection",
        "floor of mouth elevation",
        5,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_11_03",
        "fascial_space_infection",
        "floor of mouth elevation",
        1,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_11_04",
        "fascial_space_infection",
        "floor of mouth elevation",
        2,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_11_05",
        "fascial_space_infection",
        "floor of mouth elevation",
        3,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_11_06",
        "fascial_space_infection",
        "floor of mouth elevation",
        4,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_11_07",
        "fascial_space_infection",
        "floor of mouth elevation",
        5,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_11_08",
        "fascial_space_infection",
        "floor of mouth elevation",
        1,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_11_09",
        "fascial_space_infection",
        "floor of mouth elevation",
        2,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_11_10",
        "fascial_space_infection",
        "floor of mouth elevation",
        3,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_11_11",
        "fascial_space_infection",
        "floor of mouth elevation",
        4,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_11_12",
        "fascial_space_infection",
        "floor of mouth elevation",
        5,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_11_13",
        "fascial_space_infection",
        "floor of mouth elevation",
        1,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_11_14",
        "fascial_space_infection",
        "floor of mouth elevation",
        2,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_11_15",
        "fascial_space_infection",
        "floor of mouth elevation",
        3,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_11_16",
        "fascial_space_infection",
        "floor of mouth elevation",
        4,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_11_17",
        "fascial_space_infection",
        "floor of mouth elevation",
        5,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_11_18",
        "fascial_space_infection",
        "floor of mouth elevation",
        1,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_11_19",
        "fascial_space_infection",
        "floor of mouth elevation",
        2,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_11_20",
        "fascial_space_infection",
        "floor of mouth elevation",
        3,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_11_21",
        "fascial_space_infection",
        "floor of mouth elevation",
        4,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_11_22",
        "fascial_space_infection",
        "floor of mouth elevation",
        5,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_11_23",
        "fascial_space_infection",
        "floor of mouth elevation",
        1,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_12_00",
        "fascial_space_infection",
        "tongue displacement",
        4,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_12_01",
        "fascial_space_infection",
        "tongue displacement",
        5,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_12_02",
        "fascial_space_infection",
        "tongue displacement",
        1,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_12_03",
        "fascial_space_infection",
        "tongue displacement",
        2,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_12_04",
        "fascial_space_infection",
        "tongue displacement",
        3,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_12_05",
        "fascial_space_infection",
        "tongue displacement",
        4,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_12_06",
        "fascial_space_infection",
        "tongue displacement",
        5,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_12_07",
        "fascial_space_infection",
        "tongue displacement",
        1,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_12_08",
        "fascial_space_infection",
        "tongue displacement",
        2,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_12_09",
        "fascial_space_infection",
        "tongue displacement",
        3,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_12_10",
        "fascial_space_infection",
        "tongue displacement",
        4,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_12_11",
        "fascial_space_infection",
        "tongue displacement",
        5,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_12_12",
        "fascial_space_infection",
        "tongue displacement",
        1,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_12_13",
        "fascial_space_infection",
        "tongue displacement",
        2,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_12_14",
        "fascial_space_infection",
        "tongue displacement",
        3,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_12_15",
        "fascial_space_infection",
        "tongue displacement",
        4,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_12_16",
        "fascial_space_infection",
        "tongue displacement",
        5,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_12_17",
        "fascial_space_infection",
        "tongue displacement",
        1,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_12_18",
        "fascial_space_infection",
        "tongue displacement",
        2,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_12_19",
        "fascial_space_infection",
        "tongue displacement",
        3,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_12_20",
        "fascial_space_infection",
        "tongue displacement",
        4,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_12_21",
        "fascial_space_infection",
        "tongue displacement",
        5,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_12_22",
        "fascial_space_infection",
        "tongue displacement",
        1,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_12_23",
        "fascial_space_infection",
        "tongue displacement",
        2,
        "AAPD",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_13_00",
        "fascial_space_infection",
        "slow progression",
        5,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_13_01",
        "fascial_space_infection",
        "slow progression",
        1,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_13_02",
        "fascial_space_infection",
        "slow progression",
        2,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_13_03",
        "fascial_space_infection",
        "slow progression",
        3,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_13_04",
        "fascial_space_infection",
        "slow progression",
        4,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_13_05",
        "fascial_space_infection",
        "slow progression",
        5,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_13_06",
        "fascial_space_infection",
        "slow progression",
        1,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_13_07",
        "fascial_space_infection",
        "slow progression",
        2,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_13_08",
        "fascial_space_infection",
        "slow progression",
        3,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_13_09",
        "fascial_space_infection",
        "slow progression",
        4,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_13_10",
        "fascial_space_infection",
        "slow progression",
        5,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_13_11",
        "fascial_space_infection",
        "slow progression",
        1,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_13_12",
        "fascial_space_infection",
        "slow progression",
        2,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_13_13",
        "fascial_space_infection",
        "slow progression",
        3,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_13_14",
        "fascial_space_infection",
        "slow progression",
        4,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_13_15",
        "fascial_space_infection",
        "slow progression",
        5,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_13_16",
        "fascial_space_infection",
        "slow progression",
        1,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_13_17",
        "fascial_space_infection",
        "slow progression",
        2,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_13_18",
        "fascial_space_infection",
        "slow progression",
        3,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_13_19",
        "fascial_space_infection",
        "slow progression",
        4,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_13_20",
        "fascial_space_infection",
        "slow progression",
        5,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_13_21",
        "fascial_space_infection",
        "slow progression",
        1,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_13_22",
        "fascial_space_infection",
        "slow progression",
        2,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_13_23",
        "fascial_space_infection",
        "slow progression",
        3,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_14_00",
        "fascial_space_infection",
        "rapid progression",
        1,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_14_01",
        "fascial_space_infection",
        "rapid progression",
        2,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_14_02",
        "fascial_space_infection",
        "rapid progression",
        3,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_14_03",
        "fascial_space_infection",
        "rapid progression",
        4,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_14_04",
        "fascial_space_infection",
        "rapid progression",
        5,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_14_05",
        "fascial_space_infection",
        "rapid progression",
        1,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_14_06",
        "fascial_space_infection",
        "rapid progression",
        2,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_14_07",
        "fascial_space_infection",
        "rapid progression",
        3,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_14_08",
        "fascial_space_infection",
        "rapid progression",
        4,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_14_09",
        "fascial_space_infection",
        "rapid progression",
        5,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_14_10",
        "fascial_space_infection",
        "rapid progression",
        1,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_14_11",
        "fascial_space_infection",
        "rapid progression",
        2,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_14_12",
        "fascial_space_infection",
        "rapid progression",
        3,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_14_13",
        "fascial_space_infection",
        "rapid progression",
        4,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_14_14",
        "fascial_space_infection",
        "rapid progression",
        5,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_14_15",
        "fascial_space_infection",
        "rapid progression",
        1,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_14_16",
        "fascial_space_infection",
        "rapid progression",
        2,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_14_17",
        "fascial_space_infection",
        "rapid progression",
        3,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_14_18",
        "fascial_space_infection",
        "rapid progression",
        4,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_14_19",
        "fascial_space_infection",
        "rapid progression",
        5,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_14_20",
        "fascial_space_infection",
        "rapid progression",
        1,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_14_21",
        "fascial_space_infection",
        "rapid progression",
        2,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_14_22",
        "fascial_space_infection",
        "rapid progression",
        3,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_14_23",
        "fascial_space_infection",
        "rapid progression",
        4,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_15_00",
        "fascial_space_infection",
        "attenuated inflammation",
        2,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_15_01",
        "fascial_space_infection",
        "attenuated inflammation",
        3,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_15_02",
        "fascial_space_infection",
        "attenuated inflammation",
        4,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_15_03",
        "fascial_space_infection",
        "attenuated inflammation",
        5,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_15_04",
        "fascial_space_infection",
        "attenuated inflammation",
        1,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_15_05",
        "fascial_space_infection",
        "attenuated inflammation",
        2,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_15_06",
        "fascial_space_infection",
        "attenuated inflammation",
        3,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_15_07",
        "fascial_space_infection",
        "attenuated inflammation",
        4,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_15_08",
        "fascial_space_infection",
        "attenuated inflammation",
        5,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_15_09",
        "fascial_space_infection",
        "attenuated inflammation",
        1,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_15_10",
        "fascial_space_infection",
        "attenuated inflammation",
        2,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_15_11",
        "fascial_space_infection",
        "attenuated inflammation",
        3,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_15_12",
        "fascial_space_infection",
        "attenuated inflammation",
        4,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_15_13",
        "fascial_space_infection",
        "attenuated inflammation",
        5,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_15_14",
        "fascial_space_infection",
        "attenuated inflammation",
        1,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_15_15",
        "fascial_space_infection",
        "attenuated inflammation",
        2,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_15_16",
        "fascial_space_infection",
        "attenuated inflammation",
        3,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_15_17",
        "fascial_space_infection",
        "attenuated inflammation",
        4,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_15_18",
        "fascial_space_infection",
        "attenuated inflammation",
        5,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_15_19",
        "fascial_space_infection",
        "attenuated inflammation",
        1,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_15_20",
        "fascial_space_infection",
        "attenuated inflammation",
        2,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_15_21",
        "fascial_space_infection",
        "attenuated inflammation",
        3,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_15_22",
        "fascial_space_infection",
        "attenuated inflammation",
        4,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_15_23",
        "fascial_space_infection",
        "attenuated inflammation",
        5,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_16_00", "fascial_space_infection", "delayed onset", 3, "AAPD", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_16_01", "fascial_space_infection", "delayed onset", 4, "AAPD", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_16_02", "fascial_space_infection", "delayed onset", 5, "AAPD", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_16_03", "fascial_space_infection", "delayed onset", 1, "AAPD", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_16_04", "fascial_space_infection", "delayed onset", 2, "AAPD", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_16_05", "fascial_space_infection", "delayed onset", 3, "AAPD", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_16_06", "fascial_space_infection", "delayed onset", 4, "AAPD", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_16_07", "fascial_space_infection", "delayed onset", 5, "AAPD", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_16_08", "fascial_space_infection", "delayed onset", 1, "AAPD", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_16_09", "fascial_space_infection", "delayed onset", 2, "AAPD", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_16_10", "fascial_space_infection", "delayed onset", 3, "AAPD", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_16_11", "fascial_space_infection", "delayed onset", 4, "AAPD", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_16_12", "fascial_space_infection", "delayed onset", 5, "AAPD", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_16_13", "fascial_space_infection", "delayed onset", 1, "AAPD", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_16_14", "fascial_space_infection", "delayed onset", 2, "AAPD", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_16_15", "fascial_space_infection", "delayed onset", 3, "AAPD", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_16_16", "fascial_space_infection", "delayed onset", 4, "AAPD", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_16_17", "fascial_space_infection", "delayed onset", 5, "AAPD", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_16_18", "fascial_space_infection", "delayed onset", 1, "AAPD", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_16_19", "fascial_space_infection", "delayed onset", 2, "AAPD", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_16_20", "fascial_space_infection", "delayed onset", 3, "AAPD", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_16_21", "fascial_space_infection", "delayed onset", 4, "AAPD", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_16_22", "fascial_space_infection", "delayed onset", 5, "AAPD", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_16_23", "fascial_space_infection", "delayed onset", 1, "AAPD", "D2"
    ),
    ClinicalSignal(
        "fascial_space_infection_17_00",
        "fascial_space_infection",
        "medical vulnerability",
        4,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_17_01",
        "fascial_space_infection",
        "medical vulnerability",
        5,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_17_02",
        "fascial_space_infection",
        "medical vulnerability",
        1,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_17_03",
        "fascial_space_infection",
        "medical vulnerability",
        2,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_17_04",
        "fascial_space_infection",
        "medical vulnerability",
        3,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_17_05",
        "fascial_space_infection",
        "medical vulnerability",
        4,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_17_06",
        "fascial_space_infection",
        "medical vulnerability",
        5,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_17_07",
        "fascial_space_infection",
        "medical vulnerability",
        1,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_17_08",
        "fascial_space_infection",
        "medical vulnerability",
        2,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_17_09",
        "fascial_space_infection",
        "medical vulnerability",
        3,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_17_10",
        "fascial_space_infection",
        "medical vulnerability",
        4,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_17_11",
        "fascial_space_infection",
        "medical vulnerability",
        5,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_17_12",
        "fascial_space_infection",
        "medical vulnerability",
        1,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_17_13",
        "fascial_space_infection",
        "medical vulnerability",
        2,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_17_14",
        "fascial_space_infection",
        "medical vulnerability",
        3,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_17_15",
        "fascial_space_infection",
        "medical vulnerability",
        4,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_17_16",
        "fascial_space_infection",
        "medical vulnerability",
        5,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_17_17",
        "fascial_space_infection",
        "medical vulnerability",
        1,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_17_18",
        "fascial_space_infection",
        "medical vulnerability",
        2,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_17_19",
        "fascial_space_infection",
        "medical vulnerability",
        3,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_17_20",
        "fascial_space_infection",
        "medical vulnerability",
        4,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_17_21",
        "fascial_space_infection",
        "medical vulnerability",
        5,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_17_22",
        "fascial_space_infection",
        "medical vulnerability",
        1,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_17_23",
        "fascial_space_infection",
        "medical vulnerability",
        2,
        "AAE",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_18_00",
        "fascial_space_infection",
        "controlled symptoms",
        5,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_18_01",
        "fascial_space_infection",
        "controlled symptoms",
        1,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_18_02",
        "fascial_space_infection",
        "controlled symptoms",
        2,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_18_03",
        "fascial_space_infection",
        "controlled symptoms",
        3,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_18_04",
        "fascial_space_infection",
        "controlled symptoms",
        4,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_18_05",
        "fascial_space_infection",
        "controlled symptoms",
        5,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_18_06",
        "fascial_space_infection",
        "controlled symptoms",
        1,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_18_07",
        "fascial_space_infection",
        "controlled symptoms",
        2,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_18_08",
        "fascial_space_infection",
        "controlled symptoms",
        3,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_18_09",
        "fascial_space_infection",
        "controlled symptoms",
        4,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_18_10",
        "fascial_space_infection",
        "controlled symptoms",
        5,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_18_11",
        "fascial_space_infection",
        "controlled symptoms",
        1,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_18_12",
        "fascial_space_infection",
        "controlled symptoms",
        2,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_18_13",
        "fascial_space_infection",
        "controlled symptoms",
        3,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_18_14",
        "fascial_space_infection",
        "controlled symptoms",
        4,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_18_15",
        "fascial_space_infection",
        "controlled symptoms",
        5,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_18_16",
        "fascial_space_infection",
        "controlled symptoms",
        1,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_18_17",
        "fascial_space_infection",
        "controlled symptoms",
        2,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_18_18",
        "fascial_space_infection",
        "controlled symptoms",
        3,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_18_19",
        "fascial_space_infection",
        "controlled symptoms",
        4,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_18_20",
        "fascial_space_infection",
        "controlled symptoms",
        5,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_18_21",
        "fascial_space_infection",
        "controlled symptoms",
        1,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_18_22",
        "fascial_space_infection",
        "controlled symptoms",
        2,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_18_23",
        "fascial_space_infection",
        "controlled symptoms",
        3,
        "IADT",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_19_00",
        "fascial_space_infection",
        "systemic illness",
        1,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_19_01",
        "fascial_space_infection",
        "systemic illness",
        2,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_19_02",
        "fascial_space_infection",
        "systemic illness",
        3,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_19_03",
        "fascial_space_infection",
        "systemic illness",
        4,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_19_04",
        "fascial_space_infection",
        "systemic illness",
        5,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_19_05",
        "fascial_space_infection",
        "systemic illness",
        1,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_19_06",
        "fascial_space_infection",
        "systemic illness",
        2,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_19_07",
        "fascial_space_infection",
        "systemic illness",
        3,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_19_08",
        "fascial_space_infection",
        "systemic illness",
        4,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_19_09",
        "fascial_space_infection",
        "systemic illness",
        5,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_19_10",
        "fascial_space_infection",
        "systemic illness",
        1,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_19_11",
        "fascial_space_infection",
        "systemic illness",
        2,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_19_12",
        "fascial_space_infection",
        "systemic illness",
        3,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_19_13",
        "fascial_space_infection",
        "systemic illness",
        4,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_19_14",
        "fascial_space_infection",
        "systemic illness",
        5,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_19_15",
        "fascial_space_infection",
        "systemic illness",
        1,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_19_16",
        "fascial_space_infection",
        "systemic illness",
        2,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_19_17",
        "fascial_space_infection",
        "systemic illness",
        3,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_19_18",
        "fascial_space_infection",
        "systemic illness",
        4,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_19_19",
        "fascial_space_infection",
        "systemic illness",
        5,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_19_20",
        "fascial_space_infection",
        "systemic illness",
        1,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_19_21",
        "fascial_space_infection",
        "systemic illness",
        2,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_19_22",
        "fascial_space_infection",
        "systemic illness",
        3,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "fascial_space_infection_19_23",
        "fascial_space_infection",
        "systemic illness",
        4,
        "ADA",
        "D2",
    ),
    ClinicalSignal(
        "post_extraction_00_00", "post_extraction", "localised swelling", 3, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_00_01", "post_extraction", "localised swelling", 4, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_00_02", "post_extraction", "localised swelling", 5, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_00_03", "post_extraction", "localised swelling", 1, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_00_04", "post_extraction", "localised swelling", 2, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_00_05", "post_extraction", "localised swelling", 3, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_00_06", "post_extraction", "localised swelling", 4, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_00_07", "post_extraction", "localised swelling", 5, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_00_08", "post_extraction", "localised swelling", 1, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_00_09", "post_extraction", "localised swelling", 2, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_00_10", "post_extraction", "localised swelling", 3, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_00_11", "post_extraction", "localised swelling", 4, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_00_12", "post_extraction", "localised swelling", 5, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_00_13", "post_extraction", "localised swelling", 1, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_00_14", "post_extraction", "localised swelling", 2, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_00_15", "post_extraction", "localised swelling", 3, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_00_16", "post_extraction", "localised swelling", 4, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_00_17", "post_extraction", "localised swelling", 5, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_00_18", "post_extraction", "localised swelling", 1, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_00_19", "post_extraction", "localised swelling", 2, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_00_20", "post_extraction", "localised swelling", 3, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_00_21", "post_extraction", "localised swelling", 4, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_00_22", "post_extraction", "localised swelling", 5, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_00_23", "post_extraction", "localised swelling", 1, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_01_00", "post_extraction", "progressive swelling", 4, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_01_01", "post_extraction", "progressive swelling", 5, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_01_02", "post_extraction", "progressive swelling", 1, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_01_03", "post_extraction", "progressive swelling", 2, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_01_04", "post_extraction", "progressive swelling", 3, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_01_05", "post_extraction", "progressive swelling", 4, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_01_06", "post_extraction", "progressive swelling", 5, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_01_07", "post_extraction", "progressive swelling", 1, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_01_08", "post_extraction", "progressive swelling", 2, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_01_09", "post_extraction", "progressive swelling", 3, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_01_10", "post_extraction", "progressive swelling", 4, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_01_11", "post_extraction", "progressive swelling", 5, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_01_12", "post_extraction", "progressive swelling", 1, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_01_13", "post_extraction", "progressive swelling", 2, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_01_14", "post_extraction", "progressive swelling", 3, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_01_15", "post_extraction", "progressive swelling", 4, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_01_16", "post_extraction", "progressive swelling", 5, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_01_17", "post_extraction", "progressive swelling", 1, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_01_18", "post_extraction", "progressive swelling", 2, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_01_19", "post_extraction", "progressive swelling", 3, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_01_20", "post_extraction", "progressive swelling", 4, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_01_21", "post_extraction", "progressive swelling", 5, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_01_22", "post_extraction", "progressive swelling", 1, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_01_23", "post_extraction", "progressive swelling", 2, "IADT", "D3"
    ),
    ClinicalSignal("post_extraction_02_00", "post_extraction", "moderate pain", 5, "ADA", "D3"),
    ClinicalSignal("post_extraction_02_01", "post_extraction", "moderate pain", 1, "ADA", "D3"),
    ClinicalSignal("post_extraction_02_02", "post_extraction", "moderate pain", 2, "ADA", "D3"),
    ClinicalSignal("post_extraction_02_03", "post_extraction", "moderate pain", 3, "ADA", "D3"),
    ClinicalSignal("post_extraction_02_04", "post_extraction", "moderate pain", 4, "ADA", "D3"),
    ClinicalSignal("post_extraction_02_05", "post_extraction", "moderate pain", 5, "ADA", "D3"),
    ClinicalSignal("post_extraction_02_06", "post_extraction", "moderate pain", 1, "ADA", "D3"),
    ClinicalSignal("post_extraction_02_07", "post_extraction", "moderate pain", 2, "ADA", "D3"),
    ClinicalSignal("post_extraction_02_08", "post_extraction", "moderate pain", 3, "ADA", "D3"),
    ClinicalSignal("post_extraction_02_09", "post_extraction", "moderate pain", 4, "ADA", "D3"),
    ClinicalSignal("post_extraction_02_10", "post_extraction", "moderate pain", 5, "ADA", "D3"),
    ClinicalSignal("post_extraction_02_11", "post_extraction", "moderate pain", 1, "ADA", "D3"),
    ClinicalSignal("post_extraction_02_12", "post_extraction", "moderate pain", 2, "ADA", "D3"),
    ClinicalSignal("post_extraction_02_13", "post_extraction", "moderate pain", 3, "ADA", "D3"),
    ClinicalSignal("post_extraction_02_14", "post_extraction", "moderate pain", 4, "ADA", "D3"),
    ClinicalSignal("post_extraction_02_15", "post_extraction", "moderate pain", 5, "ADA", "D3"),
    ClinicalSignal("post_extraction_02_16", "post_extraction", "moderate pain", 1, "ADA", "D3"),
    ClinicalSignal("post_extraction_02_17", "post_extraction", "moderate pain", 2, "ADA", "D3"),
    ClinicalSignal("post_extraction_02_18", "post_extraction", "moderate pain", 3, "ADA", "D3"),
    ClinicalSignal("post_extraction_02_19", "post_extraction", "moderate pain", 4, "ADA", "D3"),
    ClinicalSignal("post_extraction_02_20", "post_extraction", "moderate pain", 5, "ADA", "D3"),
    ClinicalSignal("post_extraction_02_21", "post_extraction", "moderate pain", 1, "ADA", "D3"),
    ClinicalSignal("post_extraction_02_22", "post_extraction", "moderate pain", 2, "ADA", "D3"),
    ClinicalSignal("post_extraction_02_23", "post_extraction", "moderate pain", 3, "ADA", "D3"),
    ClinicalSignal("post_extraction_03_00", "post_extraction", "high fever", 1, "AAPD", "D3"),
    ClinicalSignal("post_extraction_03_01", "post_extraction", "high fever", 2, "AAPD", "D3"),
    ClinicalSignal("post_extraction_03_02", "post_extraction", "high fever", 3, "AAPD", "D3"),
    ClinicalSignal("post_extraction_03_03", "post_extraction", "high fever", 4, "AAPD", "D3"),
    ClinicalSignal("post_extraction_03_04", "post_extraction", "high fever", 5, "AAPD", "D3"),
    ClinicalSignal("post_extraction_03_05", "post_extraction", "high fever", 1, "AAPD", "D3"),
    ClinicalSignal("post_extraction_03_06", "post_extraction", "high fever", 2, "AAPD", "D3"),
    ClinicalSignal("post_extraction_03_07", "post_extraction", "high fever", 3, "AAPD", "D3"),
    ClinicalSignal("post_extraction_03_08", "post_extraction", "high fever", 4, "AAPD", "D3"),
    ClinicalSignal("post_extraction_03_09", "post_extraction", "high fever", 5, "AAPD", "D3"),
    ClinicalSignal("post_extraction_03_10", "post_extraction", "high fever", 1, "AAPD", "D3"),
    ClinicalSignal("post_extraction_03_11", "post_extraction", "high fever", 2, "AAPD", "D3"),
    ClinicalSignal("post_extraction_03_12", "post_extraction", "high fever", 3, "AAPD", "D3"),
    ClinicalSignal("post_extraction_03_13", "post_extraction", "high fever", 4, "AAPD", "D3"),
    ClinicalSignal("post_extraction_03_14", "post_extraction", "high fever", 5, "AAPD", "D3"),
    ClinicalSignal("post_extraction_03_15", "post_extraction", "high fever", 1, "AAPD", "D3"),
    ClinicalSignal("post_extraction_03_16", "post_extraction", "high fever", 2, "AAPD", "D3"),
    ClinicalSignal("post_extraction_03_17", "post_extraction", "high fever", 3, "AAPD", "D3"),
    ClinicalSignal("post_extraction_03_18", "post_extraction", "high fever", 4, "AAPD", "D3"),
    ClinicalSignal("post_extraction_03_19", "post_extraction", "high fever", 5, "AAPD", "D3"),
    ClinicalSignal("post_extraction_03_20", "post_extraction", "high fever", 1, "AAPD", "D3"),
    ClinicalSignal("post_extraction_03_21", "post_extraction", "high fever", 2, "AAPD", "D3"),
    ClinicalSignal("post_extraction_03_22", "post_extraction", "high fever", 3, "AAPD", "D3"),
    ClinicalSignal("post_extraction_03_23", "post_extraction", "high fever", 4, "AAPD", "D3"),
    ClinicalSignal(
        "post_extraction_04_00", "post_extraction", "significant trismus", 2, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_04_01", "post_extraction", "significant trismus", 3, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_04_02", "post_extraction", "significant trismus", 4, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_04_03", "post_extraction", "significant trismus", 5, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_04_04", "post_extraction", "significant trismus", 1, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_04_05", "post_extraction", "significant trismus", 2, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_04_06", "post_extraction", "significant trismus", 3, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_04_07", "post_extraction", "significant trismus", 4, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_04_08", "post_extraction", "significant trismus", 5, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_04_09", "post_extraction", "significant trismus", 1, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_04_10", "post_extraction", "significant trismus", 2, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_04_11", "post_extraction", "significant trismus", 3, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_04_12", "post_extraction", "significant trismus", 4, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_04_13", "post_extraction", "significant trismus", 5, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_04_14", "post_extraction", "significant trismus", 1, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_04_15", "post_extraction", "significant trismus", 2, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_04_16", "post_extraction", "significant trismus", 3, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_04_17", "post_extraction", "significant trismus", 4, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_04_18", "post_extraction", "significant trismus", 5, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_04_19", "post_extraction", "significant trismus", 1, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_04_20", "post_extraction", "significant trismus", 2, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_04_21", "post_extraction", "significant trismus", 3, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_04_22", "post_extraction", "significant trismus", 4, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_04_23", "post_extraction", "significant trismus", 5, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_05_00", "post_extraction", "difficulty swallowing", 3, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_05_01", "post_extraction", "difficulty swallowing", 4, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_05_02", "post_extraction", "difficulty swallowing", 5, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_05_03", "post_extraction", "difficulty swallowing", 1, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_05_04", "post_extraction", "difficulty swallowing", 2, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_05_05", "post_extraction", "difficulty swallowing", 3, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_05_06", "post_extraction", "difficulty swallowing", 4, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_05_07", "post_extraction", "difficulty swallowing", 5, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_05_08", "post_extraction", "difficulty swallowing", 1, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_05_09", "post_extraction", "difficulty swallowing", 2, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_05_10", "post_extraction", "difficulty swallowing", 3, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_05_11", "post_extraction", "difficulty swallowing", 4, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_05_12", "post_extraction", "difficulty swallowing", 5, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_05_13", "post_extraction", "difficulty swallowing", 1, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_05_14", "post_extraction", "difficulty swallowing", 2, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_05_15", "post_extraction", "difficulty swallowing", 3, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_05_16", "post_extraction", "difficulty swallowing", 4, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_05_17", "post_extraction", "difficulty swallowing", 5, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_05_18", "post_extraction", "difficulty swallowing", 1, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_05_19", "post_extraction", "difficulty swallowing", 2, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_05_20", "post_extraction", "difficulty swallowing", 3, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_05_21", "post_extraction", "difficulty swallowing", 4, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_05_22", "post_extraction", "difficulty swallowing", 5, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_05_23", "post_extraction", "difficulty swallowing", 1, "IADT", "D3"
    ),
    ClinicalSignal("post_extraction_06_00", "post_extraction", "airway noise", 4, "ADA", "D3"),
    ClinicalSignal("post_extraction_06_01", "post_extraction", "airway noise", 5, "ADA", "D3"),
    ClinicalSignal("post_extraction_06_02", "post_extraction", "airway noise", 1, "ADA", "D3"),
    ClinicalSignal("post_extraction_06_03", "post_extraction", "airway noise", 2, "ADA", "D3"),
    ClinicalSignal("post_extraction_06_04", "post_extraction", "airway noise", 3, "ADA", "D3"),
    ClinicalSignal("post_extraction_06_05", "post_extraction", "airway noise", 4, "ADA", "D3"),
    ClinicalSignal("post_extraction_06_06", "post_extraction", "airway noise", 5, "ADA", "D3"),
    ClinicalSignal("post_extraction_06_07", "post_extraction", "airway noise", 1, "ADA", "D3"),
    ClinicalSignal("post_extraction_06_08", "post_extraction", "airway noise", 2, "ADA", "D3"),
    ClinicalSignal("post_extraction_06_09", "post_extraction", "airway noise", 3, "ADA", "D3"),
    ClinicalSignal("post_extraction_06_10", "post_extraction", "airway noise", 4, "ADA", "D3"),
    ClinicalSignal("post_extraction_06_11", "post_extraction", "airway noise", 5, "ADA", "D3"),
    ClinicalSignal("post_extraction_06_12", "post_extraction", "airway noise", 1, "ADA", "D3"),
    ClinicalSignal("post_extraction_06_13", "post_extraction", "airway noise", 2, "ADA", "D3"),
    ClinicalSignal("post_extraction_06_14", "post_extraction", "airway noise", 3, "ADA", "D3"),
    ClinicalSignal("post_extraction_06_15", "post_extraction", "airway noise", 4, "ADA", "D3"),
    ClinicalSignal("post_extraction_06_16", "post_extraction", "airway noise", 5, "ADA", "D3"),
    ClinicalSignal("post_extraction_06_17", "post_extraction", "airway noise", 1, "ADA", "D3"),
    ClinicalSignal("post_extraction_06_18", "post_extraction", "airway noise", 2, "ADA", "D3"),
    ClinicalSignal("post_extraction_06_19", "post_extraction", "airway noise", 3, "ADA", "D3"),
    ClinicalSignal("post_extraction_06_20", "post_extraction", "airway noise", 4, "ADA", "D3"),
    ClinicalSignal("post_extraction_06_21", "post_extraction", "airway noise", 5, "ADA", "D3"),
    ClinicalSignal("post_extraction_06_22", "post_extraction", "airway noise", 1, "ADA", "D3"),
    ClinicalSignal("post_extraction_06_23", "post_extraction", "airway noise", 2, "ADA", "D3"),
    ClinicalSignal(
        "post_extraction_07_00", "post_extraction", "uncontrolled bleeding", 5, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_07_01", "post_extraction", "uncontrolled bleeding", 1, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_07_02", "post_extraction", "uncontrolled bleeding", 2, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_07_03", "post_extraction", "uncontrolled bleeding", 3, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_07_04", "post_extraction", "uncontrolled bleeding", 4, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_07_05", "post_extraction", "uncontrolled bleeding", 5, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_07_06", "post_extraction", "uncontrolled bleeding", 1, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_07_07", "post_extraction", "uncontrolled bleeding", 2, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_07_08", "post_extraction", "uncontrolled bleeding", 3, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_07_09", "post_extraction", "uncontrolled bleeding", 4, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_07_10", "post_extraction", "uncontrolled bleeding", 5, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_07_11", "post_extraction", "uncontrolled bleeding", 1, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_07_12", "post_extraction", "uncontrolled bleeding", 2, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_07_13", "post_extraction", "uncontrolled bleeding", 3, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_07_14", "post_extraction", "uncontrolled bleeding", 4, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_07_15", "post_extraction", "uncontrolled bleeding", 5, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_07_16", "post_extraction", "uncontrolled bleeding", 1, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_07_17", "post_extraction", "uncontrolled bleeding", 2, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_07_18", "post_extraction", "uncontrolled bleeding", 3, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_07_19", "post_extraction", "uncontrolled bleeding", 4, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_07_20", "post_extraction", "uncontrolled bleeding", 5, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_07_21", "post_extraction", "uncontrolled bleeding", 1, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_07_22", "post_extraction", "uncontrolled bleeding", 2, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_07_23", "post_extraction", "uncontrolled bleeding", 3, "AAPD", "D3"
    ),
    ClinicalSignal("post_extraction_08_00", "post_extraction", "minor sensitivity", 1, "AAE", "D3"),
    ClinicalSignal("post_extraction_08_01", "post_extraction", "minor sensitivity", 2, "AAE", "D3"),
    ClinicalSignal("post_extraction_08_02", "post_extraction", "minor sensitivity", 3, "AAE", "D3"),
    ClinicalSignal("post_extraction_08_03", "post_extraction", "minor sensitivity", 4, "AAE", "D3"),
    ClinicalSignal("post_extraction_08_04", "post_extraction", "minor sensitivity", 5, "AAE", "D3"),
    ClinicalSignal("post_extraction_08_05", "post_extraction", "minor sensitivity", 1, "AAE", "D3"),
    ClinicalSignal("post_extraction_08_06", "post_extraction", "minor sensitivity", 2, "AAE", "D3"),
    ClinicalSignal("post_extraction_08_07", "post_extraction", "minor sensitivity", 3, "AAE", "D3"),
    ClinicalSignal("post_extraction_08_08", "post_extraction", "minor sensitivity", 4, "AAE", "D3"),
    ClinicalSignal("post_extraction_08_09", "post_extraction", "minor sensitivity", 5, "AAE", "D3"),
    ClinicalSignal("post_extraction_08_10", "post_extraction", "minor sensitivity", 1, "AAE", "D3"),
    ClinicalSignal("post_extraction_08_11", "post_extraction", "minor sensitivity", 2, "AAE", "D3"),
    ClinicalSignal("post_extraction_08_12", "post_extraction", "minor sensitivity", 3, "AAE", "D3"),
    ClinicalSignal("post_extraction_08_13", "post_extraction", "minor sensitivity", 4, "AAE", "D3"),
    ClinicalSignal("post_extraction_08_14", "post_extraction", "minor sensitivity", 5, "AAE", "D3"),
    ClinicalSignal("post_extraction_08_15", "post_extraction", "minor sensitivity", 1, "AAE", "D3"),
    ClinicalSignal("post_extraction_08_16", "post_extraction", "minor sensitivity", 2, "AAE", "D3"),
    ClinicalSignal("post_extraction_08_17", "post_extraction", "minor sensitivity", 3, "AAE", "D3"),
    ClinicalSignal("post_extraction_08_18", "post_extraction", "minor sensitivity", 4, "AAE", "D3"),
    ClinicalSignal("post_extraction_08_19", "post_extraction", "minor sensitivity", 5, "AAE", "D3"),
    ClinicalSignal("post_extraction_08_20", "post_extraction", "minor sensitivity", 1, "AAE", "D3"),
    ClinicalSignal("post_extraction_08_21", "post_extraction", "minor sensitivity", 2, "AAE", "D3"),
    ClinicalSignal("post_extraction_08_22", "post_extraction", "minor sensitivity", 3, "AAE", "D3"),
    ClinicalSignal("post_extraction_08_23", "post_extraction", "minor sensitivity", 4, "AAE", "D3"),
    ClinicalSignal(
        "post_extraction_09_00", "post_extraction", "preventive enquiry", 2, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_09_01", "post_extraction", "preventive enquiry", 3, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_09_02", "post_extraction", "preventive enquiry", 4, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_09_03", "post_extraction", "preventive enquiry", 5, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_09_04", "post_extraction", "preventive enquiry", 1, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_09_05", "post_extraction", "preventive enquiry", 2, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_09_06", "post_extraction", "preventive enquiry", 3, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_09_07", "post_extraction", "preventive enquiry", 4, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_09_08", "post_extraction", "preventive enquiry", 5, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_09_09", "post_extraction", "preventive enquiry", 1, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_09_10", "post_extraction", "preventive enquiry", 2, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_09_11", "post_extraction", "preventive enquiry", 3, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_09_12", "post_extraction", "preventive enquiry", 4, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_09_13", "post_extraction", "preventive enquiry", 5, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_09_14", "post_extraction", "preventive enquiry", 1, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_09_15", "post_extraction", "preventive enquiry", 2, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_09_16", "post_extraction", "preventive enquiry", 3, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_09_17", "post_extraction", "preventive enquiry", 4, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_09_18", "post_extraction", "preventive enquiry", 5, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_09_19", "post_extraction", "preventive enquiry", 1, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_09_20", "post_extraction", "preventive enquiry", 2, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_09_21", "post_extraction", "preventive enquiry", 3, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_09_22", "post_extraction", "preventive enquiry", 4, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_09_23", "post_extraction", "preventive enquiry", 5, "IADT", "D3"
    ),
    ClinicalSignal("post_extraction_10_00", "post_extraction", "facial asymmetry", 3, "ADA", "D3"),
    ClinicalSignal("post_extraction_10_01", "post_extraction", "facial asymmetry", 4, "ADA", "D3"),
    ClinicalSignal("post_extraction_10_02", "post_extraction", "facial asymmetry", 5, "ADA", "D3"),
    ClinicalSignal("post_extraction_10_03", "post_extraction", "facial asymmetry", 1, "ADA", "D3"),
    ClinicalSignal("post_extraction_10_04", "post_extraction", "facial asymmetry", 2, "ADA", "D3"),
    ClinicalSignal("post_extraction_10_05", "post_extraction", "facial asymmetry", 3, "ADA", "D3"),
    ClinicalSignal("post_extraction_10_06", "post_extraction", "facial asymmetry", 4, "ADA", "D3"),
    ClinicalSignal("post_extraction_10_07", "post_extraction", "facial asymmetry", 5, "ADA", "D3"),
    ClinicalSignal("post_extraction_10_08", "post_extraction", "facial asymmetry", 1, "ADA", "D3"),
    ClinicalSignal("post_extraction_10_09", "post_extraction", "facial asymmetry", 2, "ADA", "D3"),
    ClinicalSignal("post_extraction_10_10", "post_extraction", "facial asymmetry", 3, "ADA", "D3"),
    ClinicalSignal("post_extraction_10_11", "post_extraction", "facial asymmetry", 4, "ADA", "D3"),
    ClinicalSignal("post_extraction_10_12", "post_extraction", "facial asymmetry", 5, "ADA", "D3"),
    ClinicalSignal("post_extraction_10_13", "post_extraction", "facial asymmetry", 1, "ADA", "D3"),
    ClinicalSignal("post_extraction_10_14", "post_extraction", "facial asymmetry", 2, "ADA", "D3"),
    ClinicalSignal("post_extraction_10_15", "post_extraction", "facial asymmetry", 3, "ADA", "D3"),
    ClinicalSignal("post_extraction_10_16", "post_extraction", "facial asymmetry", 4, "ADA", "D3"),
    ClinicalSignal("post_extraction_10_17", "post_extraction", "facial asymmetry", 5, "ADA", "D3"),
    ClinicalSignal("post_extraction_10_18", "post_extraction", "facial asymmetry", 1, "ADA", "D3"),
    ClinicalSignal("post_extraction_10_19", "post_extraction", "facial asymmetry", 2, "ADA", "D3"),
    ClinicalSignal("post_extraction_10_20", "post_extraction", "facial asymmetry", 3, "ADA", "D3"),
    ClinicalSignal("post_extraction_10_21", "post_extraction", "facial asymmetry", 4, "ADA", "D3"),
    ClinicalSignal("post_extraction_10_22", "post_extraction", "facial asymmetry", 5, "ADA", "D3"),
    ClinicalSignal("post_extraction_10_23", "post_extraction", "facial asymmetry", 1, "ADA", "D3"),
    ClinicalSignal(
        "post_extraction_11_00", "post_extraction", "floor of mouth elevation", 4, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_11_01", "post_extraction", "floor of mouth elevation", 5, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_11_02", "post_extraction", "floor of mouth elevation", 1, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_11_03", "post_extraction", "floor of mouth elevation", 2, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_11_04", "post_extraction", "floor of mouth elevation", 3, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_11_05", "post_extraction", "floor of mouth elevation", 4, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_11_06", "post_extraction", "floor of mouth elevation", 5, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_11_07", "post_extraction", "floor of mouth elevation", 1, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_11_08", "post_extraction", "floor of mouth elevation", 2, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_11_09", "post_extraction", "floor of mouth elevation", 3, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_11_10", "post_extraction", "floor of mouth elevation", 4, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_11_11", "post_extraction", "floor of mouth elevation", 5, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_11_12", "post_extraction", "floor of mouth elevation", 1, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_11_13", "post_extraction", "floor of mouth elevation", 2, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_11_14", "post_extraction", "floor of mouth elevation", 3, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_11_15", "post_extraction", "floor of mouth elevation", 4, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_11_16", "post_extraction", "floor of mouth elevation", 5, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_11_17", "post_extraction", "floor of mouth elevation", 1, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_11_18", "post_extraction", "floor of mouth elevation", 2, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_11_19", "post_extraction", "floor of mouth elevation", 3, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_11_20", "post_extraction", "floor of mouth elevation", 4, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_11_21", "post_extraction", "floor of mouth elevation", 5, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_11_22", "post_extraction", "floor of mouth elevation", 1, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_11_23", "post_extraction", "floor of mouth elevation", 2, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_12_00", "post_extraction", "tongue displacement", 5, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_12_01", "post_extraction", "tongue displacement", 1, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_12_02", "post_extraction", "tongue displacement", 2, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_12_03", "post_extraction", "tongue displacement", 3, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_12_04", "post_extraction", "tongue displacement", 4, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_12_05", "post_extraction", "tongue displacement", 5, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_12_06", "post_extraction", "tongue displacement", 1, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_12_07", "post_extraction", "tongue displacement", 2, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_12_08", "post_extraction", "tongue displacement", 3, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_12_09", "post_extraction", "tongue displacement", 4, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_12_10", "post_extraction", "tongue displacement", 5, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_12_11", "post_extraction", "tongue displacement", 1, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_12_12", "post_extraction", "tongue displacement", 2, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_12_13", "post_extraction", "tongue displacement", 3, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_12_14", "post_extraction", "tongue displacement", 4, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_12_15", "post_extraction", "tongue displacement", 5, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_12_16", "post_extraction", "tongue displacement", 1, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_12_17", "post_extraction", "tongue displacement", 2, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_12_18", "post_extraction", "tongue displacement", 3, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_12_19", "post_extraction", "tongue displacement", 4, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_12_20", "post_extraction", "tongue displacement", 5, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_12_21", "post_extraction", "tongue displacement", 1, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_12_22", "post_extraction", "tongue displacement", 2, "AAE", "D3"
    ),
    ClinicalSignal(
        "post_extraction_12_23", "post_extraction", "tongue displacement", 3, "AAE", "D3"
    ),
    ClinicalSignal("post_extraction_13_00", "post_extraction", "slow progression", 1, "IADT", "D3"),
    ClinicalSignal("post_extraction_13_01", "post_extraction", "slow progression", 2, "IADT", "D3"),
    ClinicalSignal("post_extraction_13_02", "post_extraction", "slow progression", 3, "IADT", "D3"),
    ClinicalSignal("post_extraction_13_03", "post_extraction", "slow progression", 4, "IADT", "D3"),
    ClinicalSignal("post_extraction_13_04", "post_extraction", "slow progression", 5, "IADT", "D3"),
    ClinicalSignal("post_extraction_13_05", "post_extraction", "slow progression", 1, "IADT", "D3"),
    ClinicalSignal("post_extraction_13_06", "post_extraction", "slow progression", 2, "IADT", "D3"),
    ClinicalSignal("post_extraction_13_07", "post_extraction", "slow progression", 3, "IADT", "D3"),
    ClinicalSignal("post_extraction_13_08", "post_extraction", "slow progression", 4, "IADT", "D3"),
    ClinicalSignal("post_extraction_13_09", "post_extraction", "slow progression", 5, "IADT", "D3"),
    ClinicalSignal("post_extraction_13_10", "post_extraction", "slow progression", 1, "IADT", "D3"),
    ClinicalSignal("post_extraction_13_11", "post_extraction", "slow progression", 2, "IADT", "D3"),
    ClinicalSignal("post_extraction_13_12", "post_extraction", "slow progression", 3, "IADT", "D3"),
    ClinicalSignal("post_extraction_13_13", "post_extraction", "slow progression", 4, "IADT", "D3"),
    ClinicalSignal("post_extraction_13_14", "post_extraction", "slow progression", 5, "IADT", "D3"),
    ClinicalSignal("post_extraction_13_15", "post_extraction", "slow progression", 1, "IADT", "D3"),
    ClinicalSignal("post_extraction_13_16", "post_extraction", "slow progression", 2, "IADT", "D3"),
    ClinicalSignal("post_extraction_13_17", "post_extraction", "slow progression", 3, "IADT", "D3"),
    ClinicalSignal("post_extraction_13_18", "post_extraction", "slow progression", 4, "IADT", "D3"),
    ClinicalSignal("post_extraction_13_19", "post_extraction", "slow progression", 5, "IADT", "D3"),
    ClinicalSignal("post_extraction_13_20", "post_extraction", "slow progression", 1, "IADT", "D3"),
    ClinicalSignal("post_extraction_13_21", "post_extraction", "slow progression", 2, "IADT", "D3"),
    ClinicalSignal("post_extraction_13_22", "post_extraction", "slow progression", 3, "IADT", "D3"),
    ClinicalSignal("post_extraction_13_23", "post_extraction", "slow progression", 4, "IADT", "D3"),
    ClinicalSignal("post_extraction_14_00", "post_extraction", "rapid progression", 2, "ADA", "D3"),
    ClinicalSignal("post_extraction_14_01", "post_extraction", "rapid progression", 3, "ADA", "D3"),
    ClinicalSignal("post_extraction_14_02", "post_extraction", "rapid progression", 4, "ADA", "D3"),
    ClinicalSignal("post_extraction_14_03", "post_extraction", "rapid progression", 5, "ADA", "D3"),
    ClinicalSignal("post_extraction_14_04", "post_extraction", "rapid progression", 1, "ADA", "D3"),
    ClinicalSignal("post_extraction_14_05", "post_extraction", "rapid progression", 2, "ADA", "D3"),
    ClinicalSignal("post_extraction_14_06", "post_extraction", "rapid progression", 3, "ADA", "D3"),
    ClinicalSignal("post_extraction_14_07", "post_extraction", "rapid progression", 4, "ADA", "D3"),
    ClinicalSignal("post_extraction_14_08", "post_extraction", "rapid progression", 5, "ADA", "D3"),
    ClinicalSignal("post_extraction_14_09", "post_extraction", "rapid progression", 1, "ADA", "D3"),
    ClinicalSignal("post_extraction_14_10", "post_extraction", "rapid progression", 2, "ADA", "D3"),
    ClinicalSignal("post_extraction_14_11", "post_extraction", "rapid progression", 3, "ADA", "D3"),
    ClinicalSignal("post_extraction_14_12", "post_extraction", "rapid progression", 4, "ADA", "D3"),
    ClinicalSignal("post_extraction_14_13", "post_extraction", "rapid progression", 5, "ADA", "D3"),
    ClinicalSignal("post_extraction_14_14", "post_extraction", "rapid progression", 1, "ADA", "D3"),
    ClinicalSignal("post_extraction_14_15", "post_extraction", "rapid progression", 2, "ADA", "D3"),
    ClinicalSignal("post_extraction_14_16", "post_extraction", "rapid progression", 3, "ADA", "D3"),
    ClinicalSignal("post_extraction_14_17", "post_extraction", "rapid progression", 4, "ADA", "D3"),
    ClinicalSignal("post_extraction_14_18", "post_extraction", "rapid progression", 5, "ADA", "D3"),
    ClinicalSignal("post_extraction_14_19", "post_extraction", "rapid progression", 1, "ADA", "D3"),
    ClinicalSignal("post_extraction_14_20", "post_extraction", "rapid progression", 2, "ADA", "D3"),
    ClinicalSignal("post_extraction_14_21", "post_extraction", "rapid progression", 3, "ADA", "D3"),
    ClinicalSignal("post_extraction_14_22", "post_extraction", "rapid progression", 4, "ADA", "D3"),
    ClinicalSignal("post_extraction_14_23", "post_extraction", "rapid progression", 5, "ADA", "D3"),
    ClinicalSignal(
        "post_extraction_15_00", "post_extraction", "attenuated inflammation", 3, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_15_01", "post_extraction", "attenuated inflammation", 4, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_15_02", "post_extraction", "attenuated inflammation", 5, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_15_03", "post_extraction", "attenuated inflammation", 1, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_15_04", "post_extraction", "attenuated inflammation", 2, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_15_05", "post_extraction", "attenuated inflammation", 3, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_15_06", "post_extraction", "attenuated inflammation", 4, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_15_07", "post_extraction", "attenuated inflammation", 5, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_15_08", "post_extraction", "attenuated inflammation", 1, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_15_09", "post_extraction", "attenuated inflammation", 2, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_15_10", "post_extraction", "attenuated inflammation", 3, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_15_11", "post_extraction", "attenuated inflammation", 4, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_15_12", "post_extraction", "attenuated inflammation", 5, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_15_13", "post_extraction", "attenuated inflammation", 1, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_15_14", "post_extraction", "attenuated inflammation", 2, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_15_15", "post_extraction", "attenuated inflammation", 3, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_15_16", "post_extraction", "attenuated inflammation", 4, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_15_17", "post_extraction", "attenuated inflammation", 5, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_15_18", "post_extraction", "attenuated inflammation", 1, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_15_19", "post_extraction", "attenuated inflammation", 2, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_15_20", "post_extraction", "attenuated inflammation", 3, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_15_21", "post_extraction", "attenuated inflammation", 4, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_15_22", "post_extraction", "attenuated inflammation", 5, "AAPD", "D3"
    ),
    ClinicalSignal(
        "post_extraction_15_23", "post_extraction", "attenuated inflammation", 1, "AAPD", "D3"
    ),
    ClinicalSignal("post_extraction_16_00", "post_extraction", "delayed onset", 4, "AAE", "D3"),
    ClinicalSignal("post_extraction_16_01", "post_extraction", "delayed onset", 5, "AAE", "D3"),
    ClinicalSignal("post_extraction_16_02", "post_extraction", "delayed onset", 1, "AAE", "D3"),
    ClinicalSignal("post_extraction_16_03", "post_extraction", "delayed onset", 2, "AAE", "D3"),
    ClinicalSignal("post_extraction_16_04", "post_extraction", "delayed onset", 3, "AAE", "D3"),
    ClinicalSignal("post_extraction_16_05", "post_extraction", "delayed onset", 4, "AAE", "D3"),
    ClinicalSignal("post_extraction_16_06", "post_extraction", "delayed onset", 5, "AAE", "D3"),
    ClinicalSignal("post_extraction_16_07", "post_extraction", "delayed onset", 1, "AAE", "D3"),
    ClinicalSignal("post_extraction_16_08", "post_extraction", "delayed onset", 2, "AAE", "D3"),
    ClinicalSignal("post_extraction_16_09", "post_extraction", "delayed onset", 3, "AAE", "D3"),
    ClinicalSignal("post_extraction_16_10", "post_extraction", "delayed onset", 4, "AAE", "D3"),
    ClinicalSignal("post_extraction_16_11", "post_extraction", "delayed onset", 5, "AAE", "D3"),
    ClinicalSignal("post_extraction_16_12", "post_extraction", "delayed onset", 1, "AAE", "D3"),
    ClinicalSignal("post_extraction_16_13", "post_extraction", "delayed onset", 2, "AAE", "D3"),
    ClinicalSignal("post_extraction_16_14", "post_extraction", "delayed onset", 3, "AAE", "D3"),
    ClinicalSignal("post_extraction_16_15", "post_extraction", "delayed onset", 4, "AAE", "D3"),
    ClinicalSignal("post_extraction_16_16", "post_extraction", "delayed onset", 5, "AAE", "D3"),
    ClinicalSignal("post_extraction_16_17", "post_extraction", "delayed onset", 1, "AAE", "D3"),
    ClinicalSignal("post_extraction_16_18", "post_extraction", "delayed onset", 2, "AAE", "D3"),
    ClinicalSignal("post_extraction_16_19", "post_extraction", "delayed onset", 3, "AAE", "D3"),
    ClinicalSignal("post_extraction_16_20", "post_extraction", "delayed onset", 4, "AAE", "D3"),
    ClinicalSignal("post_extraction_16_21", "post_extraction", "delayed onset", 5, "AAE", "D3"),
    ClinicalSignal("post_extraction_16_22", "post_extraction", "delayed onset", 1, "AAE", "D3"),
    ClinicalSignal("post_extraction_16_23", "post_extraction", "delayed onset", 2, "AAE", "D3"),
    ClinicalSignal(
        "post_extraction_17_00", "post_extraction", "medical vulnerability", 5, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_17_01", "post_extraction", "medical vulnerability", 1, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_17_02", "post_extraction", "medical vulnerability", 2, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_17_03", "post_extraction", "medical vulnerability", 3, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_17_04", "post_extraction", "medical vulnerability", 4, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_17_05", "post_extraction", "medical vulnerability", 5, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_17_06", "post_extraction", "medical vulnerability", 1, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_17_07", "post_extraction", "medical vulnerability", 2, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_17_08", "post_extraction", "medical vulnerability", 3, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_17_09", "post_extraction", "medical vulnerability", 4, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_17_10", "post_extraction", "medical vulnerability", 5, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_17_11", "post_extraction", "medical vulnerability", 1, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_17_12", "post_extraction", "medical vulnerability", 2, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_17_13", "post_extraction", "medical vulnerability", 3, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_17_14", "post_extraction", "medical vulnerability", 4, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_17_15", "post_extraction", "medical vulnerability", 5, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_17_16", "post_extraction", "medical vulnerability", 1, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_17_17", "post_extraction", "medical vulnerability", 2, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_17_18", "post_extraction", "medical vulnerability", 3, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_17_19", "post_extraction", "medical vulnerability", 4, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_17_20", "post_extraction", "medical vulnerability", 5, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_17_21", "post_extraction", "medical vulnerability", 1, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_17_22", "post_extraction", "medical vulnerability", 2, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_17_23", "post_extraction", "medical vulnerability", 3, "IADT", "D3"
    ),
    ClinicalSignal(
        "post_extraction_18_00", "post_extraction", "controlled symptoms", 1, "ADA", "D3"
    ),
    ClinicalSignal(
        "post_extraction_18_01", "post_extraction", "controlled symptoms", 2, "ADA", "D3"
    ),
    ClinicalSignal(
        "post_extraction_18_02", "post_extraction", "controlled symptoms", 3, "ADA", "D3"
    ),
    ClinicalSignal(
        "post_extraction_18_03", "post_extraction", "controlled symptoms", 4, "ADA", "D3"
    ),
    ClinicalSignal(
        "post_extraction_18_04", "post_extraction", "controlled symptoms", 5, "ADA", "D3"
    ),
    ClinicalSignal(
        "post_extraction_18_05", "post_extraction", "controlled symptoms", 1, "ADA", "D3"
    ),
    ClinicalSignal(
        "post_extraction_18_06", "post_extraction", "controlled symptoms", 2, "ADA", "D3"
    ),
    ClinicalSignal(
        "post_extraction_18_07", "post_extraction", "controlled symptoms", 3, "ADA", "D3"
    ),
    ClinicalSignal(
        "post_extraction_18_08", "post_extraction", "controlled symptoms", 4, "ADA", "D3"
    ),
    ClinicalSignal(
        "post_extraction_18_09", "post_extraction", "controlled symptoms", 5, "ADA", "D3"
    ),
    ClinicalSignal(
        "post_extraction_18_10", "post_extraction", "controlled symptoms", 1, "ADA", "D3"
    ),
    ClinicalSignal(
        "post_extraction_18_11", "post_extraction", "controlled symptoms", 2, "ADA", "D3"
    ),
    ClinicalSignal(
        "post_extraction_18_12", "post_extraction", "controlled symptoms", 3, "ADA", "D3"
    ),
    ClinicalSignal(
        "post_extraction_18_13", "post_extraction", "controlled symptoms", 4, "ADA", "D3"
    ),
    ClinicalSignal(
        "post_extraction_18_14", "post_extraction", "controlled symptoms", 5, "ADA", "D3"
    ),
    ClinicalSignal(
        "post_extraction_18_15", "post_extraction", "controlled symptoms", 1, "ADA", "D3"
    ),
    ClinicalSignal(
        "post_extraction_18_16", "post_extraction", "controlled symptoms", 2, "ADA", "D3"
    ),
    ClinicalSignal(
        "post_extraction_18_17", "post_extraction", "controlled symptoms", 3, "ADA", "D3"
    ),
    ClinicalSignal(
        "post_extraction_18_18", "post_extraction", "controlled symptoms", 4, "ADA", "D3"
    ),
    ClinicalSignal(
        "post_extraction_18_19", "post_extraction", "controlled symptoms", 5, "ADA", "D3"
    ),
    ClinicalSignal(
        "post_extraction_18_20", "post_extraction", "controlled symptoms", 1, "ADA", "D3"
    ),
    ClinicalSignal(
        "post_extraction_18_21", "post_extraction", "controlled symptoms", 2, "ADA", "D3"
    ),
    ClinicalSignal(
        "post_extraction_18_22", "post_extraction", "controlled symptoms", 3, "ADA", "D3"
    ),
    ClinicalSignal(
        "post_extraction_18_23", "post_extraction", "controlled symptoms", 4, "ADA", "D3"
    ),
    ClinicalSignal("post_extraction_19_00", "post_extraction", "systemic illness", 2, "AAPD", "D3"),
    ClinicalSignal("post_extraction_19_01", "post_extraction", "systemic illness", 3, "AAPD", "D3"),
    ClinicalSignal("post_extraction_19_02", "post_extraction", "systemic illness", 4, "AAPD", "D3"),
    ClinicalSignal("post_extraction_19_03", "post_extraction", "systemic illness", 5, "AAPD", "D3"),
    ClinicalSignal("post_extraction_19_04", "post_extraction", "systemic illness", 1, "AAPD", "D3"),
    ClinicalSignal("post_extraction_19_05", "post_extraction", "systemic illness", 2, "AAPD", "D3"),
    ClinicalSignal("post_extraction_19_06", "post_extraction", "systemic illness", 3, "AAPD", "D3"),
    ClinicalSignal("post_extraction_19_07", "post_extraction", "systemic illness", 4, "AAPD", "D3"),
    ClinicalSignal("post_extraction_19_08", "post_extraction", "systemic illness", 5, "AAPD", "D3"),
    ClinicalSignal("post_extraction_19_09", "post_extraction", "systemic illness", 1, "AAPD", "D3"),
    ClinicalSignal("post_extraction_19_10", "post_extraction", "systemic illness", 2, "AAPD", "D3"),
    ClinicalSignal("post_extraction_19_11", "post_extraction", "systemic illness", 3, "AAPD", "D3"),
    ClinicalSignal("post_extraction_19_12", "post_extraction", "systemic illness", 4, "AAPD", "D3"),
    ClinicalSignal("post_extraction_19_13", "post_extraction", "systemic illness", 5, "AAPD", "D3"),
    ClinicalSignal("post_extraction_19_14", "post_extraction", "systemic illness", 1, "AAPD", "D3"),
    ClinicalSignal("post_extraction_19_15", "post_extraction", "systemic illness", 2, "AAPD", "D3"),
    ClinicalSignal("post_extraction_19_16", "post_extraction", "systemic illness", 3, "AAPD", "D3"),
    ClinicalSignal("post_extraction_19_17", "post_extraction", "systemic illness", 4, "AAPD", "D3"),
    ClinicalSignal("post_extraction_19_18", "post_extraction", "systemic illness", 5, "AAPD", "D3"),
    ClinicalSignal("post_extraction_19_19", "post_extraction", "systemic illness", 1, "AAPD", "D3"),
    ClinicalSignal("post_extraction_19_20", "post_extraction", "systemic illness", 2, "AAPD", "D3"),
    ClinicalSignal("post_extraction_19_21", "post_extraction", "systemic illness", 3, "AAPD", "D3"),
    ClinicalSignal("post_extraction_19_22", "post_extraction", "systemic illness", 4, "AAPD", "D3"),
    ClinicalSignal("post_extraction_19_23", "post_extraction", "systemic illness", 5, "AAPD", "D3"),
    ClinicalSignal(
        "paediatric_trauma_00_00", "paediatric_trauma", "localised swelling", 4, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_00_01", "paediatric_trauma", "localised swelling", 5, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_00_02", "paediatric_trauma", "localised swelling", 1, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_00_03", "paediatric_trauma", "localised swelling", 2, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_00_04", "paediatric_trauma", "localised swelling", 3, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_00_05", "paediatric_trauma", "localised swelling", 4, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_00_06", "paediatric_trauma", "localised swelling", 5, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_00_07", "paediatric_trauma", "localised swelling", 1, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_00_08", "paediatric_trauma", "localised swelling", 2, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_00_09", "paediatric_trauma", "localised swelling", 3, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_00_10", "paediatric_trauma", "localised swelling", 4, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_00_11", "paediatric_trauma", "localised swelling", 5, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_00_12", "paediatric_trauma", "localised swelling", 1, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_00_13", "paediatric_trauma", "localised swelling", 2, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_00_14", "paediatric_trauma", "localised swelling", 3, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_00_15", "paediatric_trauma", "localised swelling", 4, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_00_16", "paediatric_trauma", "localised swelling", 5, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_00_17", "paediatric_trauma", "localised swelling", 1, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_00_18", "paediatric_trauma", "localised swelling", 2, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_00_19", "paediatric_trauma", "localised swelling", 3, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_00_20", "paediatric_trauma", "localised swelling", 4, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_00_21", "paediatric_trauma", "localised swelling", 5, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_00_22", "paediatric_trauma", "localised swelling", 1, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_00_23", "paediatric_trauma", "localised swelling", 2, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_01_00", "paediatric_trauma", "progressive swelling", 5, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_01_01", "paediatric_trauma", "progressive swelling", 1, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_01_02", "paediatric_trauma", "progressive swelling", 2, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_01_03", "paediatric_trauma", "progressive swelling", 3, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_01_04", "paediatric_trauma", "progressive swelling", 4, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_01_05", "paediatric_trauma", "progressive swelling", 5, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_01_06", "paediatric_trauma", "progressive swelling", 1, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_01_07", "paediatric_trauma", "progressive swelling", 2, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_01_08", "paediatric_trauma", "progressive swelling", 3, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_01_09", "paediatric_trauma", "progressive swelling", 4, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_01_10", "paediatric_trauma", "progressive swelling", 5, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_01_11", "paediatric_trauma", "progressive swelling", 1, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_01_12", "paediatric_trauma", "progressive swelling", 2, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_01_13", "paediatric_trauma", "progressive swelling", 3, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_01_14", "paediatric_trauma", "progressive swelling", 4, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_01_15", "paediatric_trauma", "progressive swelling", 5, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_01_16", "paediatric_trauma", "progressive swelling", 1, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_01_17", "paediatric_trauma", "progressive swelling", 2, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_01_18", "paediatric_trauma", "progressive swelling", 3, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_01_19", "paediatric_trauma", "progressive swelling", 4, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_01_20", "paediatric_trauma", "progressive swelling", 5, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_01_21", "paediatric_trauma", "progressive swelling", 1, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_01_22", "paediatric_trauma", "progressive swelling", 2, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_01_23", "paediatric_trauma", "progressive swelling", 3, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_02_00", "paediatric_trauma", "moderate pain", 1, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_02_01", "paediatric_trauma", "moderate pain", 2, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_02_02", "paediatric_trauma", "moderate pain", 3, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_02_03", "paediatric_trauma", "moderate pain", 4, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_02_04", "paediatric_trauma", "moderate pain", 5, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_02_05", "paediatric_trauma", "moderate pain", 1, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_02_06", "paediatric_trauma", "moderate pain", 2, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_02_07", "paediatric_trauma", "moderate pain", 3, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_02_08", "paediatric_trauma", "moderate pain", 4, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_02_09", "paediatric_trauma", "moderate pain", 5, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_02_10", "paediatric_trauma", "moderate pain", 1, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_02_11", "paediatric_trauma", "moderate pain", 2, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_02_12", "paediatric_trauma", "moderate pain", 3, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_02_13", "paediatric_trauma", "moderate pain", 4, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_02_14", "paediatric_trauma", "moderate pain", 5, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_02_15", "paediatric_trauma", "moderate pain", 1, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_02_16", "paediatric_trauma", "moderate pain", 2, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_02_17", "paediatric_trauma", "moderate pain", 3, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_02_18", "paediatric_trauma", "moderate pain", 4, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_02_19", "paediatric_trauma", "moderate pain", 5, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_02_20", "paediatric_trauma", "moderate pain", 1, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_02_21", "paediatric_trauma", "moderate pain", 2, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_02_22", "paediatric_trauma", "moderate pain", 3, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_02_23", "paediatric_trauma", "moderate pain", 4, "AAPD", "D4"
    ),
    ClinicalSignal("paediatric_trauma_03_00", "paediatric_trauma", "high fever", 2, "AAE", "D4"),
    ClinicalSignal("paediatric_trauma_03_01", "paediatric_trauma", "high fever", 3, "AAE", "D4"),
    ClinicalSignal("paediatric_trauma_03_02", "paediatric_trauma", "high fever", 4, "AAE", "D4"),
    ClinicalSignal("paediatric_trauma_03_03", "paediatric_trauma", "high fever", 5, "AAE", "D4"),
    ClinicalSignal("paediatric_trauma_03_04", "paediatric_trauma", "high fever", 1, "AAE", "D4"),
    ClinicalSignal("paediatric_trauma_03_05", "paediatric_trauma", "high fever", 2, "AAE", "D4"),
    ClinicalSignal("paediatric_trauma_03_06", "paediatric_trauma", "high fever", 3, "AAE", "D4"),
    ClinicalSignal("paediatric_trauma_03_07", "paediatric_trauma", "high fever", 4, "AAE", "D4"),
    ClinicalSignal("paediatric_trauma_03_08", "paediatric_trauma", "high fever", 5, "AAE", "D4"),
    ClinicalSignal("paediatric_trauma_03_09", "paediatric_trauma", "high fever", 1, "AAE", "D4"),
    ClinicalSignal("paediatric_trauma_03_10", "paediatric_trauma", "high fever", 2, "AAE", "D4"),
    ClinicalSignal("paediatric_trauma_03_11", "paediatric_trauma", "high fever", 3, "AAE", "D4"),
    ClinicalSignal("paediatric_trauma_03_12", "paediatric_trauma", "high fever", 4, "AAE", "D4"),
    ClinicalSignal("paediatric_trauma_03_13", "paediatric_trauma", "high fever", 5, "AAE", "D4"),
    ClinicalSignal("paediatric_trauma_03_14", "paediatric_trauma", "high fever", 1, "AAE", "D4"),
    ClinicalSignal("paediatric_trauma_03_15", "paediatric_trauma", "high fever", 2, "AAE", "D4"),
    ClinicalSignal("paediatric_trauma_03_16", "paediatric_trauma", "high fever", 3, "AAE", "D4"),
    ClinicalSignal("paediatric_trauma_03_17", "paediatric_trauma", "high fever", 4, "AAE", "D4"),
    ClinicalSignal("paediatric_trauma_03_18", "paediatric_trauma", "high fever", 5, "AAE", "D4"),
    ClinicalSignal("paediatric_trauma_03_19", "paediatric_trauma", "high fever", 1, "AAE", "D4"),
    ClinicalSignal("paediatric_trauma_03_20", "paediatric_trauma", "high fever", 2, "AAE", "D4"),
    ClinicalSignal("paediatric_trauma_03_21", "paediatric_trauma", "high fever", 3, "AAE", "D4"),
    ClinicalSignal("paediatric_trauma_03_22", "paediatric_trauma", "high fever", 4, "AAE", "D4"),
    ClinicalSignal("paediatric_trauma_03_23", "paediatric_trauma", "high fever", 5, "AAE", "D4"),
    ClinicalSignal(
        "paediatric_trauma_04_00", "paediatric_trauma", "significant trismus", 3, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_04_01", "paediatric_trauma", "significant trismus", 4, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_04_02", "paediatric_trauma", "significant trismus", 5, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_04_03", "paediatric_trauma", "significant trismus", 1, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_04_04", "paediatric_trauma", "significant trismus", 2, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_04_05", "paediatric_trauma", "significant trismus", 3, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_04_06", "paediatric_trauma", "significant trismus", 4, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_04_07", "paediatric_trauma", "significant trismus", 5, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_04_08", "paediatric_trauma", "significant trismus", 1, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_04_09", "paediatric_trauma", "significant trismus", 2, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_04_10", "paediatric_trauma", "significant trismus", 3, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_04_11", "paediatric_trauma", "significant trismus", 4, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_04_12", "paediatric_trauma", "significant trismus", 5, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_04_13", "paediatric_trauma", "significant trismus", 1, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_04_14", "paediatric_trauma", "significant trismus", 2, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_04_15", "paediatric_trauma", "significant trismus", 3, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_04_16", "paediatric_trauma", "significant trismus", 4, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_04_17", "paediatric_trauma", "significant trismus", 5, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_04_18", "paediatric_trauma", "significant trismus", 1, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_04_19", "paediatric_trauma", "significant trismus", 2, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_04_20", "paediatric_trauma", "significant trismus", 3, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_04_21", "paediatric_trauma", "significant trismus", 4, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_04_22", "paediatric_trauma", "significant trismus", 5, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_04_23", "paediatric_trauma", "significant trismus", 1, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_05_00", "paediatric_trauma", "difficulty swallowing", 4, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_05_01", "paediatric_trauma", "difficulty swallowing", 5, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_05_02", "paediatric_trauma", "difficulty swallowing", 1, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_05_03", "paediatric_trauma", "difficulty swallowing", 2, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_05_04", "paediatric_trauma", "difficulty swallowing", 3, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_05_05", "paediatric_trauma", "difficulty swallowing", 4, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_05_06", "paediatric_trauma", "difficulty swallowing", 5, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_05_07", "paediatric_trauma", "difficulty swallowing", 1, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_05_08", "paediatric_trauma", "difficulty swallowing", 2, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_05_09", "paediatric_trauma", "difficulty swallowing", 3, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_05_10", "paediatric_trauma", "difficulty swallowing", 4, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_05_11", "paediatric_trauma", "difficulty swallowing", 5, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_05_12", "paediatric_trauma", "difficulty swallowing", 1, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_05_13", "paediatric_trauma", "difficulty swallowing", 2, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_05_14", "paediatric_trauma", "difficulty swallowing", 3, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_05_15", "paediatric_trauma", "difficulty swallowing", 4, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_05_16", "paediatric_trauma", "difficulty swallowing", 5, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_05_17", "paediatric_trauma", "difficulty swallowing", 1, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_05_18", "paediatric_trauma", "difficulty swallowing", 2, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_05_19", "paediatric_trauma", "difficulty swallowing", 3, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_05_20", "paediatric_trauma", "difficulty swallowing", 4, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_05_21", "paediatric_trauma", "difficulty swallowing", 5, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_05_22", "paediatric_trauma", "difficulty swallowing", 1, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_05_23", "paediatric_trauma", "difficulty swallowing", 2, "ADA", "D4"
    ),
    ClinicalSignal("paediatric_trauma_06_00", "paediatric_trauma", "airway noise", 5, "AAPD", "D4"),
    ClinicalSignal("paediatric_trauma_06_01", "paediatric_trauma", "airway noise", 1, "AAPD", "D4"),
    ClinicalSignal("paediatric_trauma_06_02", "paediatric_trauma", "airway noise", 2, "AAPD", "D4"),
    ClinicalSignal("paediatric_trauma_06_03", "paediatric_trauma", "airway noise", 3, "AAPD", "D4"),
    ClinicalSignal("paediatric_trauma_06_04", "paediatric_trauma", "airway noise", 4, "AAPD", "D4"),
    ClinicalSignal("paediatric_trauma_06_05", "paediatric_trauma", "airway noise", 5, "AAPD", "D4"),
    ClinicalSignal("paediatric_trauma_06_06", "paediatric_trauma", "airway noise", 1, "AAPD", "D4"),
    ClinicalSignal("paediatric_trauma_06_07", "paediatric_trauma", "airway noise", 2, "AAPD", "D4"),
    ClinicalSignal("paediatric_trauma_06_08", "paediatric_trauma", "airway noise", 3, "AAPD", "D4"),
    ClinicalSignal("paediatric_trauma_06_09", "paediatric_trauma", "airway noise", 4, "AAPD", "D4"),
    ClinicalSignal("paediatric_trauma_06_10", "paediatric_trauma", "airway noise", 5, "AAPD", "D4"),
    ClinicalSignal("paediatric_trauma_06_11", "paediatric_trauma", "airway noise", 1, "AAPD", "D4"),
    ClinicalSignal("paediatric_trauma_06_12", "paediatric_trauma", "airway noise", 2, "AAPD", "D4"),
    ClinicalSignal("paediatric_trauma_06_13", "paediatric_trauma", "airway noise", 3, "AAPD", "D4"),
    ClinicalSignal("paediatric_trauma_06_14", "paediatric_trauma", "airway noise", 4, "AAPD", "D4"),
    ClinicalSignal("paediatric_trauma_06_15", "paediatric_trauma", "airway noise", 5, "AAPD", "D4"),
    ClinicalSignal("paediatric_trauma_06_16", "paediatric_trauma", "airway noise", 1, "AAPD", "D4"),
    ClinicalSignal("paediatric_trauma_06_17", "paediatric_trauma", "airway noise", 2, "AAPD", "D4"),
    ClinicalSignal("paediatric_trauma_06_18", "paediatric_trauma", "airway noise", 3, "AAPD", "D4"),
    ClinicalSignal("paediatric_trauma_06_19", "paediatric_trauma", "airway noise", 4, "AAPD", "D4"),
    ClinicalSignal("paediatric_trauma_06_20", "paediatric_trauma", "airway noise", 5, "AAPD", "D4"),
    ClinicalSignal("paediatric_trauma_06_21", "paediatric_trauma", "airway noise", 1, "AAPD", "D4"),
    ClinicalSignal("paediatric_trauma_06_22", "paediatric_trauma", "airway noise", 2, "AAPD", "D4"),
    ClinicalSignal("paediatric_trauma_06_23", "paediatric_trauma", "airway noise", 3, "AAPD", "D4"),
    ClinicalSignal(
        "paediatric_trauma_07_00", "paediatric_trauma", "uncontrolled bleeding", 1, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_07_01", "paediatric_trauma", "uncontrolled bleeding", 2, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_07_02", "paediatric_trauma", "uncontrolled bleeding", 3, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_07_03", "paediatric_trauma", "uncontrolled bleeding", 4, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_07_04", "paediatric_trauma", "uncontrolled bleeding", 5, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_07_05", "paediatric_trauma", "uncontrolled bleeding", 1, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_07_06", "paediatric_trauma", "uncontrolled bleeding", 2, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_07_07", "paediatric_trauma", "uncontrolled bleeding", 3, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_07_08", "paediatric_trauma", "uncontrolled bleeding", 4, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_07_09", "paediatric_trauma", "uncontrolled bleeding", 5, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_07_10", "paediatric_trauma", "uncontrolled bleeding", 1, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_07_11", "paediatric_trauma", "uncontrolled bleeding", 2, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_07_12", "paediatric_trauma", "uncontrolled bleeding", 3, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_07_13", "paediatric_trauma", "uncontrolled bleeding", 4, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_07_14", "paediatric_trauma", "uncontrolled bleeding", 5, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_07_15", "paediatric_trauma", "uncontrolled bleeding", 1, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_07_16", "paediatric_trauma", "uncontrolled bleeding", 2, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_07_17", "paediatric_trauma", "uncontrolled bleeding", 3, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_07_18", "paediatric_trauma", "uncontrolled bleeding", 4, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_07_19", "paediatric_trauma", "uncontrolled bleeding", 5, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_07_20", "paediatric_trauma", "uncontrolled bleeding", 1, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_07_21", "paediatric_trauma", "uncontrolled bleeding", 2, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_07_22", "paediatric_trauma", "uncontrolled bleeding", 3, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_07_23", "paediatric_trauma", "uncontrolled bleeding", 4, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_08_00", "paediatric_trauma", "minor sensitivity", 2, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_08_01", "paediatric_trauma", "minor sensitivity", 3, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_08_02", "paediatric_trauma", "minor sensitivity", 4, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_08_03", "paediatric_trauma", "minor sensitivity", 5, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_08_04", "paediatric_trauma", "minor sensitivity", 1, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_08_05", "paediatric_trauma", "minor sensitivity", 2, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_08_06", "paediatric_trauma", "minor sensitivity", 3, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_08_07", "paediatric_trauma", "minor sensitivity", 4, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_08_08", "paediatric_trauma", "minor sensitivity", 5, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_08_09", "paediatric_trauma", "minor sensitivity", 1, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_08_10", "paediatric_trauma", "minor sensitivity", 2, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_08_11", "paediatric_trauma", "minor sensitivity", 3, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_08_12", "paediatric_trauma", "minor sensitivity", 4, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_08_13", "paediatric_trauma", "minor sensitivity", 5, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_08_14", "paediatric_trauma", "minor sensitivity", 1, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_08_15", "paediatric_trauma", "minor sensitivity", 2, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_08_16", "paediatric_trauma", "minor sensitivity", 3, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_08_17", "paediatric_trauma", "minor sensitivity", 4, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_08_18", "paediatric_trauma", "minor sensitivity", 5, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_08_19", "paediatric_trauma", "minor sensitivity", 1, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_08_20", "paediatric_trauma", "minor sensitivity", 2, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_08_21", "paediatric_trauma", "minor sensitivity", 3, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_08_22", "paediatric_trauma", "minor sensitivity", 4, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_08_23", "paediatric_trauma", "minor sensitivity", 5, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_09_00", "paediatric_trauma", "preventive enquiry", 3, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_09_01", "paediatric_trauma", "preventive enquiry", 4, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_09_02", "paediatric_trauma", "preventive enquiry", 5, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_09_03", "paediatric_trauma", "preventive enquiry", 1, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_09_04", "paediatric_trauma", "preventive enquiry", 2, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_09_05", "paediatric_trauma", "preventive enquiry", 3, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_09_06", "paediatric_trauma", "preventive enquiry", 4, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_09_07", "paediatric_trauma", "preventive enquiry", 5, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_09_08", "paediatric_trauma", "preventive enquiry", 1, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_09_09", "paediatric_trauma", "preventive enquiry", 2, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_09_10", "paediatric_trauma", "preventive enquiry", 3, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_09_11", "paediatric_trauma", "preventive enquiry", 4, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_09_12", "paediatric_trauma", "preventive enquiry", 5, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_09_13", "paediatric_trauma", "preventive enquiry", 1, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_09_14", "paediatric_trauma", "preventive enquiry", 2, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_09_15", "paediatric_trauma", "preventive enquiry", 3, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_09_16", "paediatric_trauma", "preventive enquiry", 4, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_09_17", "paediatric_trauma", "preventive enquiry", 5, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_09_18", "paediatric_trauma", "preventive enquiry", 1, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_09_19", "paediatric_trauma", "preventive enquiry", 2, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_09_20", "paediatric_trauma", "preventive enquiry", 3, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_09_21", "paediatric_trauma", "preventive enquiry", 4, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_09_22", "paediatric_trauma", "preventive enquiry", 5, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_09_23", "paediatric_trauma", "preventive enquiry", 1, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_10_00", "paediatric_trauma", "facial asymmetry", 4, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_10_01", "paediatric_trauma", "facial asymmetry", 5, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_10_02", "paediatric_trauma", "facial asymmetry", 1, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_10_03", "paediatric_trauma", "facial asymmetry", 2, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_10_04", "paediatric_trauma", "facial asymmetry", 3, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_10_05", "paediatric_trauma", "facial asymmetry", 4, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_10_06", "paediatric_trauma", "facial asymmetry", 5, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_10_07", "paediatric_trauma", "facial asymmetry", 1, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_10_08", "paediatric_trauma", "facial asymmetry", 2, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_10_09", "paediatric_trauma", "facial asymmetry", 3, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_10_10", "paediatric_trauma", "facial asymmetry", 4, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_10_11", "paediatric_trauma", "facial asymmetry", 5, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_10_12", "paediatric_trauma", "facial asymmetry", 1, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_10_13", "paediatric_trauma", "facial asymmetry", 2, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_10_14", "paediatric_trauma", "facial asymmetry", 3, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_10_15", "paediatric_trauma", "facial asymmetry", 4, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_10_16", "paediatric_trauma", "facial asymmetry", 5, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_10_17", "paediatric_trauma", "facial asymmetry", 1, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_10_18", "paediatric_trauma", "facial asymmetry", 2, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_10_19", "paediatric_trauma", "facial asymmetry", 3, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_10_20", "paediatric_trauma", "facial asymmetry", 4, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_10_21", "paediatric_trauma", "facial asymmetry", 5, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_10_22", "paediatric_trauma", "facial asymmetry", 1, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_10_23", "paediatric_trauma", "facial asymmetry", 2, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_11_00", "paediatric_trauma", "floor of mouth elevation", 5, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_11_01", "paediatric_trauma", "floor of mouth elevation", 1, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_11_02", "paediatric_trauma", "floor of mouth elevation", 2, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_11_03", "paediatric_trauma", "floor of mouth elevation", 3, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_11_04", "paediatric_trauma", "floor of mouth elevation", 4, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_11_05", "paediatric_trauma", "floor of mouth elevation", 5, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_11_06", "paediatric_trauma", "floor of mouth elevation", 1, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_11_07", "paediatric_trauma", "floor of mouth elevation", 2, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_11_08", "paediatric_trauma", "floor of mouth elevation", 3, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_11_09", "paediatric_trauma", "floor of mouth elevation", 4, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_11_10", "paediatric_trauma", "floor of mouth elevation", 5, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_11_11", "paediatric_trauma", "floor of mouth elevation", 1, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_11_12", "paediatric_trauma", "floor of mouth elevation", 2, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_11_13", "paediatric_trauma", "floor of mouth elevation", 3, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_11_14", "paediatric_trauma", "floor of mouth elevation", 4, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_11_15", "paediatric_trauma", "floor of mouth elevation", 5, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_11_16", "paediatric_trauma", "floor of mouth elevation", 1, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_11_17", "paediatric_trauma", "floor of mouth elevation", 2, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_11_18", "paediatric_trauma", "floor of mouth elevation", 3, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_11_19", "paediatric_trauma", "floor of mouth elevation", 4, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_11_20", "paediatric_trauma", "floor of mouth elevation", 5, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_11_21", "paediatric_trauma", "floor of mouth elevation", 1, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_11_22", "paediatric_trauma", "floor of mouth elevation", 2, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_11_23", "paediatric_trauma", "floor of mouth elevation", 3, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_12_00", "paediatric_trauma", "tongue displacement", 1, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_12_01", "paediatric_trauma", "tongue displacement", 2, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_12_02", "paediatric_trauma", "tongue displacement", 3, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_12_03", "paediatric_trauma", "tongue displacement", 4, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_12_04", "paediatric_trauma", "tongue displacement", 5, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_12_05", "paediatric_trauma", "tongue displacement", 1, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_12_06", "paediatric_trauma", "tongue displacement", 2, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_12_07", "paediatric_trauma", "tongue displacement", 3, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_12_08", "paediatric_trauma", "tongue displacement", 4, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_12_09", "paediatric_trauma", "tongue displacement", 5, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_12_10", "paediatric_trauma", "tongue displacement", 1, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_12_11", "paediatric_trauma", "tongue displacement", 2, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_12_12", "paediatric_trauma", "tongue displacement", 3, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_12_13", "paediatric_trauma", "tongue displacement", 4, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_12_14", "paediatric_trauma", "tongue displacement", 5, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_12_15", "paediatric_trauma", "tongue displacement", 1, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_12_16", "paediatric_trauma", "tongue displacement", 2, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_12_17", "paediatric_trauma", "tongue displacement", 3, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_12_18", "paediatric_trauma", "tongue displacement", 4, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_12_19", "paediatric_trauma", "tongue displacement", 5, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_12_20", "paediatric_trauma", "tongue displacement", 1, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_12_21", "paediatric_trauma", "tongue displacement", 2, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_12_22", "paediatric_trauma", "tongue displacement", 3, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_12_23", "paediatric_trauma", "tongue displacement", 4, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_13_00", "paediatric_trauma", "slow progression", 2, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_13_01", "paediatric_trauma", "slow progression", 3, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_13_02", "paediatric_trauma", "slow progression", 4, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_13_03", "paediatric_trauma", "slow progression", 5, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_13_04", "paediatric_trauma", "slow progression", 1, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_13_05", "paediatric_trauma", "slow progression", 2, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_13_06", "paediatric_trauma", "slow progression", 3, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_13_07", "paediatric_trauma", "slow progression", 4, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_13_08", "paediatric_trauma", "slow progression", 5, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_13_09", "paediatric_trauma", "slow progression", 1, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_13_10", "paediatric_trauma", "slow progression", 2, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_13_11", "paediatric_trauma", "slow progression", 3, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_13_12", "paediatric_trauma", "slow progression", 4, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_13_13", "paediatric_trauma", "slow progression", 5, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_13_14", "paediatric_trauma", "slow progression", 1, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_13_15", "paediatric_trauma", "slow progression", 2, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_13_16", "paediatric_trauma", "slow progression", 3, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_13_17", "paediatric_trauma", "slow progression", 4, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_13_18", "paediatric_trauma", "slow progression", 5, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_13_19", "paediatric_trauma", "slow progression", 1, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_13_20", "paediatric_trauma", "slow progression", 2, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_13_21", "paediatric_trauma", "slow progression", 3, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_13_22", "paediatric_trauma", "slow progression", 4, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_13_23", "paediatric_trauma", "slow progression", 5, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_14_00", "paediatric_trauma", "rapid progression", 3, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_14_01", "paediatric_trauma", "rapid progression", 4, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_14_02", "paediatric_trauma", "rapid progression", 5, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_14_03", "paediatric_trauma", "rapid progression", 1, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_14_04", "paediatric_trauma", "rapid progression", 2, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_14_05", "paediatric_trauma", "rapid progression", 3, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_14_06", "paediatric_trauma", "rapid progression", 4, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_14_07", "paediatric_trauma", "rapid progression", 5, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_14_08", "paediatric_trauma", "rapid progression", 1, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_14_09", "paediatric_trauma", "rapid progression", 2, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_14_10", "paediatric_trauma", "rapid progression", 3, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_14_11", "paediatric_trauma", "rapid progression", 4, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_14_12", "paediatric_trauma", "rapid progression", 5, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_14_13", "paediatric_trauma", "rapid progression", 1, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_14_14", "paediatric_trauma", "rapid progression", 2, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_14_15", "paediatric_trauma", "rapid progression", 3, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_14_16", "paediatric_trauma", "rapid progression", 4, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_14_17", "paediatric_trauma", "rapid progression", 5, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_14_18", "paediatric_trauma", "rapid progression", 1, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_14_19", "paediatric_trauma", "rapid progression", 2, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_14_20", "paediatric_trauma", "rapid progression", 3, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_14_21", "paediatric_trauma", "rapid progression", 4, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_14_22", "paediatric_trauma", "rapid progression", 5, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_14_23", "paediatric_trauma", "rapid progression", 1, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_15_00", "paediatric_trauma", "attenuated inflammation", 4, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_15_01", "paediatric_trauma", "attenuated inflammation", 5, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_15_02", "paediatric_trauma", "attenuated inflammation", 1, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_15_03", "paediatric_trauma", "attenuated inflammation", 2, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_15_04", "paediatric_trauma", "attenuated inflammation", 3, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_15_05", "paediatric_trauma", "attenuated inflammation", 4, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_15_06", "paediatric_trauma", "attenuated inflammation", 5, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_15_07", "paediatric_trauma", "attenuated inflammation", 1, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_15_08", "paediatric_trauma", "attenuated inflammation", 2, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_15_09", "paediatric_trauma", "attenuated inflammation", 3, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_15_10", "paediatric_trauma", "attenuated inflammation", 4, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_15_11", "paediatric_trauma", "attenuated inflammation", 5, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_15_12", "paediatric_trauma", "attenuated inflammation", 1, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_15_13", "paediatric_trauma", "attenuated inflammation", 2, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_15_14", "paediatric_trauma", "attenuated inflammation", 3, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_15_15", "paediatric_trauma", "attenuated inflammation", 4, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_15_16", "paediatric_trauma", "attenuated inflammation", 5, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_15_17", "paediatric_trauma", "attenuated inflammation", 1, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_15_18", "paediatric_trauma", "attenuated inflammation", 2, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_15_19", "paediatric_trauma", "attenuated inflammation", 3, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_15_20", "paediatric_trauma", "attenuated inflammation", 4, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_15_21", "paediatric_trauma", "attenuated inflammation", 5, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_15_22", "paediatric_trauma", "attenuated inflammation", 1, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_15_23", "paediatric_trauma", "attenuated inflammation", 2, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_16_00", "paediatric_trauma", "delayed onset", 5, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_16_01", "paediatric_trauma", "delayed onset", 1, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_16_02", "paediatric_trauma", "delayed onset", 2, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_16_03", "paediatric_trauma", "delayed onset", 3, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_16_04", "paediatric_trauma", "delayed onset", 4, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_16_05", "paediatric_trauma", "delayed onset", 5, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_16_06", "paediatric_trauma", "delayed onset", 1, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_16_07", "paediatric_trauma", "delayed onset", 2, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_16_08", "paediatric_trauma", "delayed onset", 3, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_16_09", "paediatric_trauma", "delayed onset", 4, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_16_10", "paediatric_trauma", "delayed onset", 5, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_16_11", "paediatric_trauma", "delayed onset", 1, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_16_12", "paediatric_trauma", "delayed onset", 2, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_16_13", "paediatric_trauma", "delayed onset", 3, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_16_14", "paediatric_trauma", "delayed onset", 4, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_16_15", "paediatric_trauma", "delayed onset", 5, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_16_16", "paediatric_trauma", "delayed onset", 1, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_16_17", "paediatric_trauma", "delayed onset", 2, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_16_18", "paediatric_trauma", "delayed onset", 3, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_16_19", "paediatric_trauma", "delayed onset", 4, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_16_20", "paediatric_trauma", "delayed onset", 5, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_16_21", "paediatric_trauma", "delayed onset", 1, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_16_22", "paediatric_trauma", "delayed onset", 2, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_16_23", "paediatric_trauma", "delayed onset", 3, "IADT", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_17_00", "paediatric_trauma", "medical vulnerability", 1, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_17_01", "paediatric_trauma", "medical vulnerability", 2, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_17_02", "paediatric_trauma", "medical vulnerability", 3, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_17_03", "paediatric_trauma", "medical vulnerability", 4, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_17_04", "paediatric_trauma", "medical vulnerability", 5, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_17_05", "paediatric_trauma", "medical vulnerability", 1, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_17_06", "paediatric_trauma", "medical vulnerability", 2, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_17_07", "paediatric_trauma", "medical vulnerability", 3, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_17_08", "paediatric_trauma", "medical vulnerability", 4, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_17_09", "paediatric_trauma", "medical vulnerability", 5, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_17_10", "paediatric_trauma", "medical vulnerability", 1, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_17_11", "paediatric_trauma", "medical vulnerability", 2, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_17_12", "paediatric_trauma", "medical vulnerability", 3, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_17_13", "paediatric_trauma", "medical vulnerability", 4, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_17_14", "paediatric_trauma", "medical vulnerability", 5, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_17_15", "paediatric_trauma", "medical vulnerability", 1, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_17_16", "paediatric_trauma", "medical vulnerability", 2, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_17_17", "paediatric_trauma", "medical vulnerability", 3, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_17_18", "paediatric_trauma", "medical vulnerability", 4, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_17_19", "paediatric_trauma", "medical vulnerability", 5, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_17_20", "paediatric_trauma", "medical vulnerability", 1, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_17_21", "paediatric_trauma", "medical vulnerability", 2, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_17_22", "paediatric_trauma", "medical vulnerability", 3, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_17_23", "paediatric_trauma", "medical vulnerability", 4, "ADA", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_18_00", "paediatric_trauma", "controlled symptoms", 2, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_18_01", "paediatric_trauma", "controlled symptoms", 3, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_18_02", "paediatric_trauma", "controlled symptoms", 4, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_18_03", "paediatric_trauma", "controlled symptoms", 5, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_18_04", "paediatric_trauma", "controlled symptoms", 1, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_18_05", "paediatric_trauma", "controlled symptoms", 2, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_18_06", "paediatric_trauma", "controlled symptoms", 3, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_18_07", "paediatric_trauma", "controlled symptoms", 4, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_18_08", "paediatric_trauma", "controlled symptoms", 5, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_18_09", "paediatric_trauma", "controlled symptoms", 1, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_18_10", "paediatric_trauma", "controlled symptoms", 2, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_18_11", "paediatric_trauma", "controlled symptoms", 3, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_18_12", "paediatric_trauma", "controlled symptoms", 4, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_18_13", "paediatric_trauma", "controlled symptoms", 5, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_18_14", "paediatric_trauma", "controlled symptoms", 1, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_18_15", "paediatric_trauma", "controlled symptoms", 2, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_18_16", "paediatric_trauma", "controlled symptoms", 3, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_18_17", "paediatric_trauma", "controlled symptoms", 4, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_18_18", "paediatric_trauma", "controlled symptoms", 5, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_18_19", "paediatric_trauma", "controlled symptoms", 1, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_18_20", "paediatric_trauma", "controlled symptoms", 2, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_18_21", "paediatric_trauma", "controlled symptoms", 3, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_18_22", "paediatric_trauma", "controlled symptoms", 4, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_18_23", "paediatric_trauma", "controlled symptoms", 5, "AAPD", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_19_00", "paediatric_trauma", "systemic illness", 3, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_19_01", "paediatric_trauma", "systemic illness", 4, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_19_02", "paediatric_trauma", "systemic illness", 5, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_19_03", "paediatric_trauma", "systemic illness", 1, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_19_04", "paediatric_trauma", "systemic illness", 2, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_19_05", "paediatric_trauma", "systemic illness", 3, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_19_06", "paediatric_trauma", "systemic illness", 4, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_19_07", "paediatric_trauma", "systemic illness", 5, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_19_08", "paediatric_trauma", "systemic illness", 1, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_19_09", "paediatric_trauma", "systemic illness", 2, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_19_10", "paediatric_trauma", "systemic illness", 3, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_19_11", "paediatric_trauma", "systemic illness", 4, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_19_12", "paediatric_trauma", "systemic illness", 5, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_19_13", "paediatric_trauma", "systemic illness", 1, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_19_14", "paediatric_trauma", "systemic illness", 2, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_19_15", "paediatric_trauma", "systemic illness", 3, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_19_16", "paediatric_trauma", "systemic illness", 4, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_19_17", "paediatric_trauma", "systemic illness", 5, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_19_18", "paediatric_trauma", "systemic illness", 1, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_19_19", "paediatric_trauma", "systemic illness", 2, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_19_20", "paediatric_trauma", "systemic illness", 3, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_19_21", "paediatric_trauma", "systemic illness", 4, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_19_22", "paediatric_trauma", "systemic illness", 5, "AAE", "D4"
    ),
    ClinicalSignal(
        "paediatric_trauma_19_23", "paediatric_trauma", "systemic illness", 1, "AAE", "D4"
    ),
    ClinicalSignal(
        "routine_chronic_00_00", "routine_chronic", "localised swelling", 5, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_00_01", "routine_chronic", "localised swelling", 1, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_00_02", "routine_chronic", "localised swelling", 2, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_00_03", "routine_chronic", "localised swelling", 3, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_00_04", "routine_chronic", "localised swelling", 4, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_00_05", "routine_chronic", "localised swelling", 5, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_00_06", "routine_chronic", "localised swelling", 1, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_00_07", "routine_chronic", "localised swelling", 2, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_00_08", "routine_chronic", "localised swelling", 3, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_00_09", "routine_chronic", "localised swelling", 4, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_00_10", "routine_chronic", "localised swelling", 5, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_00_11", "routine_chronic", "localised swelling", 1, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_00_12", "routine_chronic", "localised swelling", 2, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_00_13", "routine_chronic", "localised swelling", 3, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_00_14", "routine_chronic", "localised swelling", 4, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_00_15", "routine_chronic", "localised swelling", 5, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_00_16", "routine_chronic", "localised swelling", 1, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_00_17", "routine_chronic", "localised swelling", 2, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_00_18", "routine_chronic", "localised swelling", 3, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_00_19", "routine_chronic", "localised swelling", 4, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_00_20", "routine_chronic", "localised swelling", 5, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_00_21", "routine_chronic", "localised swelling", 1, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_00_22", "routine_chronic", "localised swelling", 2, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_00_23", "routine_chronic", "localised swelling", 3, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_01_00", "routine_chronic", "progressive swelling", 1, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_01_01", "routine_chronic", "progressive swelling", 2, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_01_02", "routine_chronic", "progressive swelling", 3, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_01_03", "routine_chronic", "progressive swelling", 4, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_01_04", "routine_chronic", "progressive swelling", 5, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_01_05", "routine_chronic", "progressive swelling", 1, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_01_06", "routine_chronic", "progressive swelling", 2, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_01_07", "routine_chronic", "progressive swelling", 3, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_01_08", "routine_chronic", "progressive swelling", 4, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_01_09", "routine_chronic", "progressive swelling", 5, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_01_10", "routine_chronic", "progressive swelling", 1, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_01_11", "routine_chronic", "progressive swelling", 2, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_01_12", "routine_chronic", "progressive swelling", 3, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_01_13", "routine_chronic", "progressive swelling", 4, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_01_14", "routine_chronic", "progressive swelling", 5, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_01_15", "routine_chronic", "progressive swelling", 1, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_01_16", "routine_chronic", "progressive swelling", 2, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_01_17", "routine_chronic", "progressive swelling", 3, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_01_18", "routine_chronic", "progressive swelling", 4, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_01_19", "routine_chronic", "progressive swelling", 5, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_01_20", "routine_chronic", "progressive swelling", 1, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_01_21", "routine_chronic", "progressive swelling", 2, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_01_22", "routine_chronic", "progressive swelling", 3, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_01_23", "routine_chronic", "progressive swelling", 4, "AAPD", "D5"
    ),
    ClinicalSignal("routine_chronic_02_00", "routine_chronic", "moderate pain", 2, "AAE", "D5"),
    ClinicalSignal("routine_chronic_02_01", "routine_chronic", "moderate pain", 3, "AAE", "D5"),
    ClinicalSignal("routine_chronic_02_02", "routine_chronic", "moderate pain", 4, "AAE", "D5"),
    ClinicalSignal("routine_chronic_02_03", "routine_chronic", "moderate pain", 5, "AAE", "D5"),
    ClinicalSignal("routine_chronic_02_04", "routine_chronic", "moderate pain", 1, "AAE", "D5"),
    ClinicalSignal("routine_chronic_02_05", "routine_chronic", "moderate pain", 2, "AAE", "D5"),
    ClinicalSignal("routine_chronic_02_06", "routine_chronic", "moderate pain", 3, "AAE", "D5"),
    ClinicalSignal("routine_chronic_02_07", "routine_chronic", "moderate pain", 4, "AAE", "D5"),
    ClinicalSignal("routine_chronic_02_08", "routine_chronic", "moderate pain", 5, "AAE", "D5"),
    ClinicalSignal("routine_chronic_02_09", "routine_chronic", "moderate pain", 1, "AAE", "D5"),
    ClinicalSignal("routine_chronic_02_10", "routine_chronic", "moderate pain", 2, "AAE", "D5"),
    ClinicalSignal("routine_chronic_02_11", "routine_chronic", "moderate pain", 3, "AAE", "D5"),
    ClinicalSignal("routine_chronic_02_12", "routine_chronic", "moderate pain", 4, "AAE", "D5"),
    ClinicalSignal("routine_chronic_02_13", "routine_chronic", "moderate pain", 5, "AAE", "D5"),
    ClinicalSignal("routine_chronic_02_14", "routine_chronic", "moderate pain", 1, "AAE", "D5"),
    ClinicalSignal("routine_chronic_02_15", "routine_chronic", "moderate pain", 2, "AAE", "D5"),
    ClinicalSignal("routine_chronic_02_16", "routine_chronic", "moderate pain", 3, "AAE", "D5"),
    ClinicalSignal("routine_chronic_02_17", "routine_chronic", "moderate pain", 4, "AAE", "D5"),
    ClinicalSignal("routine_chronic_02_18", "routine_chronic", "moderate pain", 5, "AAE", "D5"),
    ClinicalSignal("routine_chronic_02_19", "routine_chronic", "moderate pain", 1, "AAE", "D5"),
    ClinicalSignal("routine_chronic_02_20", "routine_chronic", "moderate pain", 2, "AAE", "D5"),
    ClinicalSignal("routine_chronic_02_21", "routine_chronic", "moderate pain", 3, "AAE", "D5"),
    ClinicalSignal("routine_chronic_02_22", "routine_chronic", "moderate pain", 4, "AAE", "D5"),
    ClinicalSignal("routine_chronic_02_23", "routine_chronic", "moderate pain", 5, "AAE", "D5"),
    ClinicalSignal("routine_chronic_03_00", "routine_chronic", "high fever", 3, "IADT", "D5"),
    ClinicalSignal("routine_chronic_03_01", "routine_chronic", "high fever", 4, "IADT", "D5"),
    ClinicalSignal("routine_chronic_03_02", "routine_chronic", "high fever", 5, "IADT", "D5"),
    ClinicalSignal("routine_chronic_03_03", "routine_chronic", "high fever", 1, "IADT", "D5"),
    ClinicalSignal("routine_chronic_03_04", "routine_chronic", "high fever", 2, "IADT", "D5"),
    ClinicalSignal("routine_chronic_03_05", "routine_chronic", "high fever", 3, "IADT", "D5"),
    ClinicalSignal("routine_chronic_03_06", "routine_chronic", "high fever", 4, "IADT", "D5"),
    ClinicalSignal("routine_chronic_03_07", "routine_chronic", "high fever", 5, "IADT", "D5"),
    ClinicalSignal("routine_chronic_03_08", "routine_chronic", "high fever", 1, "IADT", "D5"),
    ClinicalSignal("routine_chronic_03_09", "routine_chronic", "high fever", 2, "IADT", "D5"),
    ClinicalSignal("routine_chronic_03_10", "routine_chronic", "high fever", 3, "IADT", "D5"),
    ClinicalSignal("routine_chronic_03_11", "routine_chronic", "high fever", 4, "IADT", "D5"),
    ClinicalSignal("routine_chronic_03_12", "routine_chronic", "high fever", 5, "IADT", "D5"),
    ClinicalSignal("routine_chronic_03_13", "routine_chronic", "high fever", 1, "IADT", "D5"),
    ClinicalSignal("routine_chronic_03_14", "routine_chronic", "high fever", 2, "IADT", "D5"),
    ClinicalSignal("routine_chronic_03_15", "routine_chronic", "high fever", 3, "IADT", "D5"),
    ClinicalSignal("routine_chronic_03_16", "routine_chronic", "high fever", 4, "IADT", "D5"),
    ClinicalSignal("routine_chronic_03_17", "routine_chronic", "high fever", 5, "IADT", "D5"),
    ClinicalSignal("routine_chronic_03_18", "routine_chronic", "high fever", 1, "IADT", "D5"),
    ClinicalSignal("routine_chronic_03_19", "routine_chronic", "high fever", 2, "IADT", "D5"),
    ClinicalSignal("routine_chronic_03_20", "routine_chronic", "high fever", 3, "IADT", "D5"),
    ClinicalSignal("routine_chronic_03_21", "routine_chronic", "high fever", 4, "IADT", "D5"),
    ClinicalSignal("routine_chronic_03_22", "routine_chronic", "high fever", 5, "IADT", "D5"),
    ClinicalSignal("routine_chronic_03_23", "routine_chronic", "high fever", 1, "IADT", "D5"),
    ClinicalSignal(
        "routine_chronic_04_00", "routine_chronic", "significant trismus", 4, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_04_01", "routine_chronic", "significant trismus", 5, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_04_02", "routine_chronic", "significant trismus", 1, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_04_03", "routine_chronic", "significant trismus", 2, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_04_04", "routine_chronic", "significant trismus", 3, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_04_05", "routine_chronic", "significant trismus", 4, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_04_06", "routine_chronic", "significant trismus", 5, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_04_07", "routine_chronic", "significant trismus", 1, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_04_08", "routine_chronic", "significant trismus", 2, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_04_09", "routine_chronic", "significant trismus", 3, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_04_10", "routine_chronic", "significant trismus", 4, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_04_11", "routine_chronic", "significant trismus", 5, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_04_12", "routine_chronic", "significant trismus", 1, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_04_13", "routine_chronic", "significant trismus", 2, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_04_14", "routine_chronic", "significant trismus", 3, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_04_15", "routine_chronic", "significant trismus", 4, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_04_16", "routine_chronic", "significant trismus", 5, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_04_17", "routine_chronic", "significant trismus", 1, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_04_18", "routine_chronic", "significant trismus", 2, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_04_19", "routine_chronic", "significant trismus", 3, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_04_20", "routine_chronic", "significant trismus", 4, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_04_21", "routine_chronic", "significant trismus", 5, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_04_22", "routine_chronic", "significant trismus", 1, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_04_23", "routine_chronic", "significant trismus", 2, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_05_00", "routine_chronic", "difficulty swallowing", 5, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_05_01", "routine_chronic", "difficulty swallowing", 1, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_05_02", "routine_chronic", "difficulty swallowing", 2, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_05_03", "routine_chronic", "difficulty swallowing", 3, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_05_04", "routine_chronic", "difficulty swallowing", 4, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_05_05", "routine_chronic", "difficulty swallowing", 5, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_05_06", "routine_chronic", "difficulty swallowing", 1, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_05_07", "routine_chronic", "difficulty swallowing", 2, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_05_08", "routine_chronic", "difficulty swallowing", 3, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_05_09", "routine_chronic", "difficulty swallowing", 4, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_05_10", "routine_chronic", "difficulty swallowing", 5, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_05_11", "routine_chronic", "difficulty swallowing", 1, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_05_12", "routine_chronic", "difficulty swallowing", 2, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_05_13", "routine_chronic", "difficulty swallowing", 3, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_05_14", "routine_chronic", "difficulty swallowing", 4, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_05_15", "routine_chronic", "difficulty swallowing", 5, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_05_16", "routine_chronic", "difficulty swallowing", 1, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_05_17", "routine_chronic", "difficulty swallowing", 2, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_05_18", "routine_chronic", "difficulty swallowing", 3, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_05_19", "routine_chronic", "difficulty swallowing", 4, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_05_20", "routine_chronic", "difficulty swallowing", 5, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_05_21", "routine_chronic", "difficulty swallowing", 1, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_05_22", "routine_chronic", "difficulty swallowing", 2, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_05_23", "routine_chronic", "difficulty swallowing", 3, "AAPD", "D5"
    ),
    ClinicalSignal("routine_chronic_06_00", "routine_chronic", "airway noise", 1, "AAE", "D5"),
    ClinicalSignal("routine_chronic_06_01", "routine_chronic", "airway noise", 2, "AAE", "D5"),
    ClinicalSignal("routine_chronic_06_02", "routine_chronic", "airway noise", 3, "AAE", "D5"),
    ClinicalSignal("routine_chronic_06_03", "routine_chronic", "airway noise", 4, "AAE", "D5"),
    ClinicalSignal("routine_chronic_06_04", "routine_chronic", "airway noise", 5, "AAE", "D5"),
    ClinicalSignal("routine_chronic_06_05", "routine_chronic", "airway noise", 1, "AAE", "D5"),
    ClinicalSignal("routine_chronic_06_06", "routine_chronic", "airway noise", 2, "AAE", "D5"),
    ClinicalSignal("routine_chronic_06_07", "routine_chronic", "airway noise", 3, "AAE", "D5"),
    ClinicalSignal("routine_chronic_06_08", "routine_chronic", "airway noise", 4, "AAE", "D5"),
    ClinicalSignal("routine_chronic_06_09", "routine_chronic", "airway noise", 5, "AAE", "D5"),
    ClinicalSignal("routine_chronic_06_10", "routine_chronic", "airway noise", 1, "AAE", "D5"),
    ClinicalSignal("routine_chronic_06_11", "routine_chronic", "airway noise", 2, "AAE", "D5"),
    ClinicalSignal("routine_chronic_06_12", "routine_chronic", "airway noise", 3, "AAE", "D5"),
    ClinicalSignal("routine_chronic_06_13", "routine_chronic", "airway noise", 4, "AAE", "D5"),
    ClinicalSignal("routine_chronic_06_14", "routine_chronic", "airway noise", 5, "AAE", "D5"),
    ClinicalSignal("routine_chronic_06_15", "routine_chronic", "airway noise", 1, "AAE", "D5"),
    ClinicalSignal("routine_chronic_06_16", "routine_chronic", "airway noise", 2, "AAE", "D5"),
    ClinicalSignal("routine_chronic_06_17", "routine_chronic", "airway noise", 3, "AAE", "D5"),
    ClinicalSignal("routine_chronic_06_18", "routine_chronic", "airway noise", 4, "AAE", "D5"),
    ClinicalSignal("routine_chronic_06_19", "routine_chronic", "airway noise", 5, "AAE", "D5"),
    ClinicalSignal("routine_chronic_06_20", "routine_chronic", "airway noise", 1, "AAE", "D5"),
    ClinicalSignal("routine_chronic_06_21", "routine_chronic", "airway noise", 2, "AAE", "D5"),
    ClinicalSignal("routine_chronic_06_22", "routine_chronic", "airway noise", 3, "AAE", "D5"),
    ClinicalSignal("routine_chronic_06_23", "routine_chronic", "airway noise", 4, "AAE", "D5"),
    ClinicalSignal(
        "routine_chronic_07_00", "routine_chronic", "uncontrolled bleeding", 2, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_07_01", "routine_chronic", "uncontrolled bleeding", 3, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_07_02", "routine_chronic", "uncontrolled bleeding", 4, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_07_03", "routine_chronic", "uncontrolled bleeding", 5, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_07_04", "routine_chronic", "uncontrolled bleeding", 1, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_07_05", "routine_chronic", "uncontrolled bleeding", 2, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_07_06", "routine_chronic", "uncontrolled bleeding", 3, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_07_07", "routine_chronic", "uncontrolled bleeding", 4, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_07_08", "routine_chronic", "uncontrolled bleeding", 5, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_07_09", "routine_chronic", "uncontrolled bleeding", 1, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_07_10", "routine_chronic", "uncontrolled bleeding", 2, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_07_11", "routine_chronic", "uncontrolled bleeding", 3, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_07_12", "routine_chronic", "uncontrolled bleeding", 4, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_07_13", "routine_chronic", "uncontrolled bleeding", 5, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_07_14", "routine_chronic", "uncontrolled bleeding", 1, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_07_15", "routine_chronic", "uncontrolled bleeding", 2, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_07_16", "routine_chronic", "uncontrolled bleeding", 3, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_07_17", "routine_chronic", "uncontrolled bleeding", 4, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_07_18", "routine_chronic", "uncontrolled bleeding", 5, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_07_19", "routine_chronic", "uncontrolled bleeding", 1, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_07_20", "routine_chronic", "uncontrolled bleeding", 2, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_07_21", "routine_chronic", "uncontrolled bleeding", 3, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_07_22", "routine_chronic", "uncontrolled bleeding", 4, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_07_23", "routine_chronic", "uncontrolled bleeding", 5, "IADT", "D5"
    ),
    ClinicalSignal("routine_chronic_08_00", "routine_chronic", "minor sensitivity", 3, "ADA", "D5"),
    ClinicalSignal("routine_chronic_08_01", "routine_chronic", "minor sensitivity", 4, "ADA", "D5"),
    ClinicalSignal("routine_chronic_08_02", "routine_chronic", "minor sensitivity", 5, "ADA", "D5"),
    ClinicalSignal("routine_chronic_08_03", "routine_chronic", "minor sensitivity", 1, "ADA", "D5"),
    ClinicalSignal("routine_chronic_08_04", "routine_chronic", "minor sensitivity", 2, "ADA", "D5"),
    ClinicalSignal("routine_chronic_08_05", "routine_chronic", "minor sensitivity", 3, "ADA", "D5"),
    ClinicalSignal("routine_chronic_08_06", "routine_chronic", "minor sensitivity", 4, "ADA", "D5"),
    ClinicalSignal("routine_chronic_08_07", "routine_chronic", "minor sensitivity", 5, "ADA", "D5"),
    ClinicalSignal("routine_chronic_08_08", "routine_chronic", "minor sensitivity", 1, "ADA", "D5"),
    ClinicalSignal("routine_chronic_08_09", "routine_chronic", "minor sensitivity", 2, "ADA", "D5"),
    ClinicalSignal("routine_chronic_08_10", "routine_chronic", "minor sensitivity", 3, "ADA", "D5"),
    ClinicalSignal("routine_chronic_08_11", "routine_chronic", "minor sensitivity", 4, "ADA", "D5"),
    ClinicalSignal("routine_chronic_08_12", "routine_chronic", "minor sensitivity", 5, "ADA", "D5"),
    ClinicalSignal("routine_chronic_08_13", "routine_chronic", "minor sensitivity", 1, "ADA", "D5"),
    ClinicalSignal("routine_chronic_08_14", "routine_chronic", "minor sensitivity", 2, "ADA", "D5"),
    ClinicalSignal("routine_chronic_08_15", "routine_chronic", "minor sensitivity", 3, "ADA", "D5"),
    ClinicalSignal("routine_chronic_08_16", "routine_chronic", "minor sensitivity", 4, "ADA", "D5"),
    ClinicalSignal("routine_chronic_08_17", "routine_chronic", "minor sensitivity", 5, "ADA", "D5"),
    ClinicalSignal("routine_chronic_08_18", "routine_chronic", "minor sensitivity", 1, "ADA", "D5"),
    ClinicalSignal("routine_chronic_08_19", "routine_chronic", "minor sensitivity", 2, "ADA", "D5"),
    ClinicalSignal("routine_chronic_08_20", "routine_chronic", "minor sensitivity", 3, "ADA", "D5"),
    ClinicalSignal("routine_chronic_08_21", "routine_chronic", "minor sensitivity", 4, "ADA", "D5"),
    ClinicalSignal("routine_chronic_08_22", "routine_chronic", "minor sensitivity", 5, "ADA", "D5"),
    ClinicalSignal("routine_chronic_08_23", "routine_chronic", "minor sensitivity", 1, "ADA", "D5"),
    ClinicalSignal(
        "routine_chronic_09_00", "routine_chronic", "preventive enquiry", 4, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_09_01", "routine_chronic", "preventive enquiry", 5, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_09_02", "routine_chronic", "preventive enquiry", 1, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_09_03", "routine_chronic", "preventive enquiry", 2, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_09_04", "routine_chronic", "preventive enquiry", 3, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_09_05", "routine_chronic", "preventive enquiry", 4, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_09_06", "routine_chronic", "preventive enquiry", 5, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_09_07", "routine_chronic", "preventive enquiry", 1, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_09_08", "routine_chronic", "preventive enquiry", 2, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_09_09", "routine_chronic", "preventive enquiry", 3, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_09_10", "routine_chronic", "preventive enquiry", 4, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_09_11", "routine_chronic", "preventive enquiry", 5, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_09_12", "routine_chronic", "preventive enquiry", 1, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_09_13", "routine_chronic", "preventive enquiry", 2, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_09_14", "routine_chronic", "preventive enquiry", 3, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_09_15", "routine_chronic", "preventive enquiry", 4, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_09_16", "routine_chronic", "preventive enquiry", 5, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_09_17", "routine_chronic", "preventive enquiry", 1, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_09_18", "routine_chronic", "preventive enquiry", 2, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_09_19", "routine_chronic", "preventive enquiry", 3, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_09_20", "routine_chronic", "preventive enquiry", 4, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_09_21", "routine_chronic", "preventive enquiry", 5, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_09_22", "routine_chronic", "preventive enquiry", 1, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_09_23", "routine_chronic", "preventive enquiry", 2, "AAPD", "D5"
    ),
    ClinicalSignal("routine_chronic_10_00", "routine_chronic", "facial asymmetry", 5, "AAE", "D5"),
    ClinicalSignal("routine_chronic_10_01", "routine_chronic", "facial asymmetry", 1, "AAE", "D5"),
    ClinicalSignal("routine_chronic_10_02", "routine_chronic", "facial asymmetry", 2, "AAE", "D5"),
    ClinicalSignal("routine_chronic_10_03", "routine_chronic", "facial asymmetry", 3, "AAE", "D5"),
    ClinicalSignal("routine_chronic_10_04", "routine_chronic", "facial asymmetry", 4, "AAE", "D5"),
    ClinicalSignal("routine_chronic_10_05", "routine_chronic", "facial asymmetry", 5, "AAE", "D5"),
    ClinicalSignal("routine_chronic_10_06", "routine_chronic", "facial asymmetry", 1, "AAE", "D5"),
    ClinicalSignal("routine_chronic_10_07", "routine_chronic", "facial asymmetry", 2, "AAE", "D5"),
    ClinicalSignal("routine_chronic_10_08", "routine_chronic", "facial asymmetry", 3, "AAE", "D5"),
    ClinicalSignal("routine_chronic_10_09", "routine_chronic", "facial asymmetry", 4, "AAE", "D5"),
    ClinicalSignal("routine_chronic_10_10", "routine_chronic", "facial asymmetry", 5, "AAE", "D5"),
    ClinicalSignal("routine_chronic_10_11", "routine_chronic", "facial asymmetry", 1, "AAE", "D5"),
    ClinicalSignal("routine_chronic_10_12", "routine_chronic", "facial asymmetry", 2, "AAE", "D5"),
    ClinicalSignal("routine_chronic_10_13", "routine_chronic", "facial asymmetry", 3, "AAE", "D5"),
    ClinicalSignal("routine_chronic_10_14", "routine_chronic", "facial asymmetry", 4, "AAE", "D5"),
    ClinicalSignal("routine_chronic_10_15", "routine_chronic", "facial asymmetry", 5, "AAE", "D5"),
    ClinicalSignal("routine_chronic_10_16", "routine_chronic", "facial asymmetry", 1, "AAE", "D5"),
    ClinicalSignal("routine_chronic_10_17", "routine_chronic", "facial asymmetry", 2, "AAE", "D5"),
    ClinicalSignal("routine_chronic_10_18", "routine_chronic", "facial asymmetry", 3, "AAE", "D5"),
    ClinicalSignal("routine_chronic_10_19", "routine_chronic", "facial asymmetry", 4, "AAE", "D5"),
    ClinicalSignal("routine_chronic_10_20", "routine_chronic", "facial asymmetry", 5, "AAE", "D5"),
    ClinicalSignal("routine_chronic_10_21", "routine_chronic", "facial asymmetry", 1, "AAE", "D5"),
    ClinicalSignal("routine_chronic_10_22", "routine_chronic", "facial asymmetry", 2, "AAE", "D5"),
    ClinicalSignal("routine_chronic_10_23", "routine_chronic", "facial asymmetry", 3, "AAE", "D5"),
    ClinicalSignal(
        "routine_chronic_11_00", "routine_chronic", "floor of mouth elevation", 1, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_11_01", "routine_chronic", "floor of mouth elevation", 2, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_11_02", "routine_chronic", "floor of mouth elevation", 3, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_11_03", "routine_chronic", "floor of mouth elevation", 4, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_11_04", "routine_chronic", "floor of mouth elevation", 5, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_11_05", "routine_chronic", "floor of mouth elevation", 1, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_11_06", "routine_chronic", "floor of mouth elevation", 2, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_11_07", "routine_chronic", "floor of mouth elevation", 3, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_11_08", "routine_chronic", "floor of mouth elevation", 4, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_11_09", "routine_chronic", "floor of mouth elevation", 5, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_11_10", "routine_chronic", "floor of mouth elevation", 1, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_11_11", "routine_chronic", "floor of mouth elevation", 2, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_11_12", "routine_chronic", "floor of mouth elevation", 3, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_11_13", "routine_chronic", "floor of mouth elevation", 4, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_11_14", "routine_chronic", "floor of mouth elevation", 5, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_11_15", "routine_chronic", "floor of mouth elevation", 1, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_11_16", "routine_chronic", "floor of mouth elevation", 2, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_11_17", "routine_chronic", "floor of mouth elevation", 3, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_11_18", "routine_chronic", "floor of mouth elevation", 4, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_11_19", "routine_chronic", "floor of mouth elevation", 5, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_11_20", "routine_chronic", "floor of mouth elevation", 1, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_11_21", "routine_chronic", "floor of mouth elevation", 2, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_11_22", "routine_chronic", "floor of mouth elevation", 3, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_11_23", "routine_chronic", "floor of mouth elevation", 4, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_12_00", "routine_chronic", "tongue displacement", 2, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_12_01", "routine_chronic", "tongue displacement", 3, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_12_02", "routine_chronic", "tongue displacement", 4, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_12_03", "routine_chronic", "tongue displacement", 5, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_12_04", "routine_chronic", "tongue displacement", 1, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_12_05", "routine_chronic", "tongue displacement", 2, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_12_06", "routine_chronic", "tongue displacement", 3, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_12_07", "routine_chronic", "tongue displacement", 4, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_12_08", "routine_chronic", "tongue displacement", 5, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_12_09", "routine_chronic", "tongue displacement", 1, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_12_10", "routine_chronic", "tongue displacement", 2, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_12_11", "routine_chronic", "tongue displacement", 3, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_12_12", "routine_chronic", "tongue displacement", 4, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_12_13", "routine_chronic", "tongue displacement", 5, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_12_14", "routine_chronic", "tongue displacement", 1, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_12_15", "routine_chronic", "tongue displacement", 2, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_12_16", "routine_chronic", "tongue displacement", 3, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_12_17", "routine_chronic", "tongue displacement", 4, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_12_18", "routine_chronic", "tongue displacement", 5, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_12_19", "routine_chronic", "tongue displacement", 1, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_12_20", "routine_chronic", "tongue displacement", 2, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_12_21", "routine_chronic", "tongue displacement", 3, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_12_22", "routine_chronic", "tongue displacement", 4, "ADA", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_12_23", "routine_chronic", "tongue displacement", 5, "ADA", "D5"
    ),
    ClinicalSignal("routine_chronic_13_00", "routine_chronic", "slow progression", 3, "AAPD", "D5"),
    ClinicalSignal("routine_chronic_13_01", "routine_chronic", "slow progression", 4, "AAPD", "D5"),
    ClinicalSignal("routine_chronic_13_02", "routine_chronic", "slow progression", 5, "AAPD", "D5"),
    ClinicalSignal("routine_chronic_13_03", "routine_chronic", "slow progression", 1, "AAPD", "D5"),
    ClinicalSignal("routine_chronic_13_04", "routine_chronic", "slow progression", 2, "AAPD", "D5"),
    ClinicalSignal("routine_chronic_13_05", "routine_chronic", "slow progression", 3, "AAPD", "D5"),
    ClinicalSignal("routine_chronic_13_06", "routine_chronic", "slow progression", 4, "AAPD", "D5"),
    ClinicalSignal("routine_chronic_13_07", "routine_chronic", "slow progression", 5, "AAPD", "D5"),
    ClinicalSignal("routine_chronic_13_08", "routine_chronic", "slow progression", 1, "AAPD", "D5"),
    ClinicalSignal("routine_chronic_13_09", "routine_chronic", "slow progression", 2, "AAPD", "D5"),
    ClinicalSignal("routine_chronic_13_10", "routine_chronic", "slow progression", 3, "AAPD", "D5"),
    ClinicalSignal("routine_chronic_13_11", "routine_chronic", "slow progression", 4, "AAPD", "D5"),
    ClinicalSignal("routine_chronic_13_12", "routine_chronic", "slow progression", 5, "AAPD", "D5"),
    ClinicalSignal("routine_chronic_13_13", "routine_chronic", "slow progression", 1, "AAPD", "D5"),
    ClinicalSignal("routine_chronic_13_14", "routine_chronic", "slow progression", 2, "AAPD", "D5"),
    ClinicalSignal("routine_chronic_13_15", "routine_chronic", "slow progression", 3, "AAPD", "D5"),
    ClinicalSignal("routine_chronic_13_16", "routine_chronic", "slow progression", 4, "AAPD", "D5"),
    ClinicalSignal("routine_chronic_13_17", "routine_chronic", "slow progression", 5, "AAPD", "D5"),
    ClinicalSignal("routine_chronic_13_18", "routine_chronic", "slow progression", 1, "AAPD", "D5"),
    ClinicalSignal("routine_chronic_13_19", "routine_chronic", "slow progression", 2, "AAPD", "D5"),
    ClinicalSignal("routine_chronic_13_20", "routine_chronic", "slow progression", 3, "AAPD", "D5"),
    ClinicalSignal("routine_chronic_13_21", "routine_chronic", "slow progression", 4, "AAPD", "D5"),
    ClinicalSignal("routine_chronic_13_22", "routine_chronic", "slow progression", 5, "AAPD", "D5"),
    ClinicalSignal("routine_chronic_13_23", "routine_chronic", "slow progression", 1, "AAPD", "D5"),
    ClinicalSignal("routine_chronic_14_00", "routine_chronic", "rapid progression", 4, "AAE", "D5"),
    ClinicalSignal("routine_chronic_14_01", "routine_chronic", "rapid progression", 5, "AAE", "D5"),
    ClinicalSignal("routine_chronic_14_02", "routine_chronic", "rapid progression", 1, "AAE", "D5"),
    ClinicalSignal("routine_chronic_14_03", "routine_chronic", "rapid progression", 2, "AAE", "D5"),
    ClinicalSignal("routine_chronic_14_04", "routine_chronic", "rapid progression", 3, "AAE", "D5"),
    ClinicalSignal("routine_chronic_14_05", "routine_chronic", "rapid progression", 4, "AAE", "D5"),
    ClinicalSignal("routine_chronic_14_06", "routine_chronic", "rapid progression", 5, "AAE", "D5"),
    ClinicalSignal("routine_chronic_14_07", "routine_chronic", "rapid progression", 1, "AAE", "D5"),
    ClinicalSignal("routine_chronic_14_08", "routine_chronic", "rapid progression", 2, "AAE", "D5"),
    ClinicalSignal("routine_chronic_14_09", "routine_chronic", "rapid progression", 3, "AAE", "D5"),
    ClinicalSignal("routine_chronic_14_10", "routine_chronic", "rapid progression", 4, "AAE", "D5"),
    ClinicalSignal("routine_chronic_14_11", "routine_chronic", "rapid progression", 5, "AAE", "D5"),
    ClinicalSignal("routine_chronic_14_12", "routine_chronic", "rapid progression", 1, "AAE", "D5"),
    ClinicalSignal("routine_chronic_14_13", "routine_chronic", "rapid progression", 2, "AAE", "D5"),
    ClinicalSignal("routine_chronic_14_14", "routine_chronic", "rapid progression", 3, "AAE", "D5"),
    ClinicalSignal("routine_chronic_14_15", "routine_chronic", "rapid progression", 4, "AAE", "D5"),
    ClinicalSignal("routine_chronic_14_16", "routine_chronic", "rapid progression", 5, "AAE", "D5"),
    ClinicalSignal("routine_chronic_14_17", "routine_chronic", "rapid progression", 1, "AAE", "D5"),
    ClinicalSignal("routine_chronic_14_18", "routine_chronic", "rapid progression", 2, "AAE", "D5"),
    ClinicalSignal("routine_chronic_14_19", "routine_chronic", "rapid progression", 3, "AAE", "D5"),
    ClinicalSignal("routine_chronic_14_20", "routine_chronic", "rapid progression", 4, "AAE", "D5"),
    ClinicalSignal("routine_chronic_14_21", "routine_chronic", "rapid progression", 5, "AAE", "D5"),
    ClinicalSignal("routine_chronic_14_22", "routine_chronic", "rapid progression", 1, "AAE", "D5"),
    ClinicalSignal("routine_chronic_14_23", "routine_chronic", "rapid progression", 2, "AAE", "D5"),
    ClinicalSignal(
        "routine_chronic_15_00", "routine_chronic", "attenuated inflammation", 5, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_15_01", "routine_chronic", "attenuated inflammation", 1, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_15_02", "routine_chronic", "attenuated inflammation", 2, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_15_03", "routine_chronic", "attenuated inflammation", 3, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_15_04", "routine_chronic", "attenuated inflammation", 4, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_15_05", "routine_chronic", "attenuated inflammation", 5, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_15_06", "routine_chronic", "attenuated inflammation", 1, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_15_07", "routine_chronic", "attenuated inflammation", 2, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_15_08", "routine_chronic", "attenuated inflammation", 3, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_15_09", "routine_chronic", "attenuated inflammation", 4, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_15_10", "routine_chronic", "attenuated inflammation", 5, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_15_11", "routine_chronic", "attenuated inflammation", 1, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_15_12", "routine_chronic", "attenuated inflammation", 2, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_15_13", "routine_chronic", "attenuated inflammation", 3, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_15_14", "routine_chronic", "attenuated inflammation", 4, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_15_15", "routine_chronic", "attenuated inflammation", 5, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_15_16", "routine_chronic", "attenuated inflammation", 1, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_15_17", "routine_chronic", "attenuated inflammation", 2, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_15_18", "routine_chronic", "attenuated inflammation", 3, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_15_19", "routine_chronic", "attenuated inflammation", 4, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_15_20", "routine_chronic", "attenuated inflammation", 5, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_15_21", "routine_chronic", "attenuated inflammation", 1, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_15_22", "routine_chronic", "attenuated inflammation", 2, "IADT", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_15_23", "routine_chronic", "attenuated inflammation", 3, "IADT", "D5"
    ),
    ClinicalSignal("routine_chronic_16_00", "routine_chronic", "delayed onset", 1, "ADA", "D5"),
    ClinicalSignal("routine_chronic_16_01", "routine_chronic", "delayed onset", 2, "ADA", "D5"),
    ClinicalSignal("routine_chronic_16_02", "routine_chronic", "delayed onset", 3, "ADA", "D5"),
    ClinicalSignal("routine_chronic_16_03", "routine_chronic", "delayed onset", 4, "ADA", "D5"),
    ClinicalSignal("routine_chronic_16_04", "routine_chronic", "delayed onset", 5, "ADA", "D5"),
    ClinicalSignal("routine_chronic_16_05", "routine_chronic", "delayed onset", 1, "ADA", "D5"),
    ClinicalSignal("routine_chronic_16_06", "routine_chronic", "delayed onset", 2, "ADA", "D5"),
    ClinicalSignal("routine_chronic_16_07", "routine_chronic", "delayed onset", 3, "ADA", "D5"),
    ClinicalSignal("routine_chronic_16_08", "routine_chronic", "delayed onset", 4, "ADA", "D5"),
    ClinicalSignal("routine_chronic_16_09", "routine_chronic", "delayed onset", 5, "ADA", "D5"),
    ClinicalSignal("routine_chronic_16_10", "routine_chronic", "delayed onset", 1, "ADA", "D5"),
    ClinicalSignal("routine_chronic_16_11", "routine_chronic", "delayed onset", 2, "ADA", "D5"),
    ClinicalSignal("routine_chronic_16_12", "routine_chronic", "delayed onset", 3, "ADA", "D5"),
    ClinicalSignal("routine_chronic_16_13", "routine_chronic", "delayed onset", 4, "ADA", "D5"),
    ClinicalSignal("routine_chronic_16_14", "routine_chronic", "delayed onset", 5, "ADA", "D5"),
    ClinicalSignal("routine_chronic_16_15", "routine_chronic", "delayed onset", 1, "ADA", "D5"),
    ClinicalSignal("routine_chronic_16_16", "routine_chronic", "delayed onset", 2, "ADA", "D5"),
    ClinicalSignal("routine_chronic_16_17", "routine_chronic", "delayed onset", 3, "ADA", "D5"),
    ClinicalSignal("routine_chronic_16_18", "routine_chronic", "delayed onset", 4, "ADA", "D5"),
    ClinicalSignal("routine_chronic_16_19", "routine_chronic", "delayed onset", 5, "ADA", "D5"),
    ClinicalSignal("routine_chronic_16_20", "routine_chronic", "delayed onset", 1, "ADA", "D5"),
    ClinicalSignal("routine_chronic_16_21", "routine_chronic", "delayed onset", 2, "ADA", "D5"),
    ClinicalSignal("routine_chronic_16_22", "routine_chronic", "delayed onset", 3, "ADA", "D5"),
    ClinicalSignal("routine_chronic_16_23", "routine_chronic", "delayed onset", 4, "ADA", "D5"),
    ClinicalSignal(
        "routine_chronic_17_00", "routine_chronic", "medical vulnerability", 2, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_17_01", "routine_chronic", "medical vulnerability", 3, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_17_02", "routine_chronic", "medical vulnerability", 4, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_17_03", "routine_chronic", "medical vulnerability", 5, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_17_04", "routine_chronic", "medical vulnerability", 1, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_17_05", "routine_chronic", "medical vulnerability", 2, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_17_06", "routine_chronic", "medical vulnerability", 3, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_17_07", "routine_chronic", "medical vulnerability", 4, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_17_08", "routine_chronic", "medical vulnerability", 5, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_17_09", "routine_chronic", "medical vulnerability", 1, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_17_10", "routine_chronic", "medical vulnerability", 2, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_17_11", "routine_chronic", "medical vulnerability", 3, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_17_12", "routine_chronic", "medical vulnerability", 4, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_17_13", "routine_chronic", "medical vulnerability", 5, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_17_14", "routine_chronic", "medical vulnerability", 1, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_17_15", "routine_chronic", "medical vulnerability", 2, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_17_16", "routine_chronic", "medical vulnerability", 3, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_17_17", "routine_chronic", "medical vulnerability", 4, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_17_18", "routine_chronic", "medical vulnerability", 5, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_17_19", "routine_chronic", "medical vulnerability", 1, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_17_20", "routine_chronic", "medical vulnerability", 2, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_17_21", "routine_chronic", "medical vulnerability", 3, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_17_22", "routine_chronic", "medical vulnerability", 4, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_17_23", "routine_chronic", "medical vulnerability", 5, "AAPD", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_18_00", "routine_chronic", "controlled symptoms", 3, "AAE", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_18_01", "routine_chronic", "controlled symptoms", 4, "AAE", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_18_02", "routine_chronic", "controlled symptoms", 5, "AAE", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_18_03", "routine_chronic", "controlled symptoms", 1, "AAE", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_18_04", "routine_chronic", "controlled symptoms", 2, "AAE", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_18_05", "routine_chronic", "controlled symptoms", 3, "AAE", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_18_06", "routine_chronic", "controlled symptoms", 4, "AAE", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_18_07", "routine_chronic", "controlled symptoms", 5, "AAE", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_18_08", "routine_chronic", "controlled symptoms", 1, "AAE", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_18_09", "routine_chronic", "controlled symptoms", 2, "AAE", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_18_10", "routine_chronic", "controlled symptoms", 3, "AAE", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_18_11", "routine_chronic", "controlled symptoms", 4, "AAE", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_18_12", "routine_chronic", "controlled symptoms", 5, "AAE", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_18_13", "routine_chronic", "controlled symptoms", 1, "AAE", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_18_14", "routine_chronic", "controlled symptoms", 2, "AAE", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_18_15", "routine_chronic", "controlled symptoms", 3, "AAE", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_18_16", "routine_chronic", "controlled symptoms", 4, "AAE", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_18_17", "routine_chronic", "controlled symptoms", 5, "AAE", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_18_18", "routine_chronic", "controlled symptoms", 1, "AAE", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_18_19", "routine_chronic", "controlled symptoms", 2, "AAE", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_18_20", "routine_chronic", "controlled symptoms", 3, "AAE", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_18_21", "routine_chronic", "controlled symptoms", 4, "AAE", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_18_22", "routine_chronic", "controlled symptoms", 5, "AAE", "D5"
    ),
    ClinicalSignal(
        "routine_chronic_18_23", "routine_chronic", "controlled symptoms", 1, "AAE", "D5"
    ),
    ClinicalSignal("routine_chronic_19_00", "routine_chronic", "systemic illness", 4, "IADT", "D5"),
    ClinicalSignal("routine_chronic_19_01", "routine_chronic", "systemic illness", 5, "IADT", "D5"),
    ClinicalSignal("routine_chronic_19_02", "routine_chronic", "systemic illness", 1, "IADT", "D5"),
    ClinicalSignal("routine_chronic_19_03", "routine_chronic", "systemic illness", 2, "IADT", "D5"),
    ClinicalSignal("routine_chronic_19_04", "routine_chronic", "systemic illness", 3, "IADT", "D5"),
    ClinicalSignal("routine_chronic_19_05", "routine_chronic", "systemic illness", 4, "IADT", "D5"),
    ClinicalSignal("routine_chronic_19_06", "routine_chronic", "systemic illness", 5, "IADT", "D5"),
    ClinicalSignal("routine_chronic_19_07", "routine_chronic", "systemic illness", 1, "IADT", "D5"),
    ClinicalSignal("routine_chronic_19_08", "routine_chronic", "systemic illness", 2, "IADT", "D5"),
    ClinicalSignal("routine_chronic_19_09", "routine_chronic", "systemic illness", 3, "IADT", "D5"),
    ClinicalSignal("routine_chronic_19_10", "routine_chronic", "systemic illness", 4, "IADT", "D5"),
    ClinicalSignal("routine_chronic_19_11", "routine_chronic", "systemic illness", 5, "IADT", "D5"),
    ClinicalSignal("routine_chronic_19_12", "routine_chronic", "systemic illness", 1, "IADT", "D5"),
    ClinicalSignal("routine_chronic_19_13", "routine_chronic", "systemic illness", 2, "IADT", "D5"),
    ClinicalSignal("routine_chronic_19_14", "routine_chronic", "systemic illness", 3, "IADT", "D5"),
    ClinicalSignal("routine_chronic_19_15", "routine_chronic", "systemic illness", 4, "IADT", "D5"),
    ClinicalSignal("routine_chronic_19_16", "routine_chronic", "systemic illness", 5, "IADT", "D5"),
    ClinicalSignal("routine_chronic_19_17", "routine_chronic", "systemic illness", 1, "IADT", "D5"),
    ClinicalSignal("routine_chronic_19_18", "routine_chronic", "systemic illness", 2, "IADT", "D5"),
    ClinicalSignal("routine_chronic_19_19", "routine_chronic", "systemic illness", 3, "IADT", "D5"),
    ClinicalSignal("routine_chronic_19_20", "routine_chronic", "systemic illness", 4, "IADT", "D5"),
    ClinicalSignal("routine_chronic_19_21", "routine_chronic", "systemic illness", 5, "IADT", "D5"),
    ClinicalSignal("routine_chronic_19_22", "routine_chronic", "systemic illness", 1, "IADT", "D5"),
    ClinicalSignal("routine_chronic_19_23", "routine_chronic", "systemic illness", 2, "IADT", "D5"),
    ClinicalSignal(
        "immunocompromised_00_00", "immunocompromised", "localised swelling", 1, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_00_01", "immunocompromised", "localised swelling", 2, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_00_02", "immunocompromised", "localised swelling", 3, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_00_03", "immunocompromised", "localised swelling", 4, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_00_04", "immunocompromised", "localised swelling", 5, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_00_05", "immunocompromised", "localised swelling", 1, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_00_06", "immunocompromised", "localised swelling", 2, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_00_07", "immunocompromised", "localised swelling", 3, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_00_08", "immunocompromised", "localised swelling", 4, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_00_09", "immunocompromised", "localised swelling", 5, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_00_10", "immunocompromised", "localised swelling", 1, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_00_11", "immunocompromised", "localised swelling", 2, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_00_12", "immunocompromised", "localised swelling", 3, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_00_13", "immunocompromised", "localised swelling", 4, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_00_14", "immunocompromised", "localised swelling", 5, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_00_15", "immunocompromised", "localised swelling", 1, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_00_16", "immunocompromised", "localised swelling", 2, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_00_17", "immunocompromised", "localised swelling", 3, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_00_18", "immunocompromised", "localised swelling", 4, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_00_19", "immunocompromised", "localised swelling", 5, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_00_20", "immunocompromised", "localised swelling", 1, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_00_21", "immunocompromised", "localised swelling", 2, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_00_22", "immunocompromised", "localised swelling", 3, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_00_23", "immunocompromised", "localised swelling", 4, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_01_00", "immunocompromised", "progressive swelling", 2, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_01_01", "immunocompromised", "progressive swelling", 3, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_01_02", "immunocompromised", "progressive swelling", 4, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_01_03", "immunocompromised", "progressive swelling", 5, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_01_04", "immunocompromised", "progressive swelling", 1, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_01_05", "immunocompromised", "progressive swelling", 2, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_01_06", "immunocompromised", "progressive swelling", 3, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_01_07", "immunocompromised", "progressive swelling", 4, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_01_08", "immunocompromised", "progressive swelling", 5, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_01_09", "immunocompromised", "progressive swelling", 1, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_01_10", "immunocompromised", "progressive swelling", 2, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_01_11", "immunocompromised", "progressive swelling", 3, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_01_12", "immunocompromised", "progressive swelling", 4, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_01_13", "immunocompromised", "progressive swelling", 5, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_01_14", "immunocompromised", "progressive swelling", 1, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_01_15", "immunocompromised", "progressive swelling", 2, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_01_16", "immunocompromised", "progressive swelling", 3, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_01_17", "immunocompromised", "progressive swelling", 4, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_01_18", "immunocompromised", "progressive swelling", 5, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_01_19", "immunocompromised", "progressive swelling", 1, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_01_20", "immunocompromised", "progressive swelling", 2, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_01_21", "immunocompromised", "progressive swelling", 3, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_01_22", "immunocompromised", "progressive swelling", 4, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_01_23", "immunocompromised", "progressive swelling", 5, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_02_00", "immunocompromised", "moderate pain", 3, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_02_01", "immunocompromised", "moderate pain", 4, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_02_02", "immunocompromised", "moderate pain", 5, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_02_03", "immunocompromised", "moderate pain", 1, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_02_04", "immunocompromised", "moderate pain", 2, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_02_05", "immunocompromised", "moderate pain", 3, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_02_06", "immunocompromised", "moderate pain", 4, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_02_07", "immunocompromised", "moderate pain", 5, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_02_08", "immunocompromised", "moderate pain", 1, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_02_09", "immunocompromised", "moderate pain", 2, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_02_10", "immunocompromised", "moderate pain", 3, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_02_11", "immunocompromised", "moderate pain", 4, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_02_12", "immunocompromised", "moderate pain", 5, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_02_13", "immunocompromised", "moderate pain", 1, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_02_14", "immunocompromised", "moderate pain", 2, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_02_15", "immunocompromised", "moderate pain", 3, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_02_16", "immunocompromised", "moderate pain", 4, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_02_17", "immunocompromised", "moderate pain", 5, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_02_18", "immunocompromised", "moderate pain", 1, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_02_19", "immunocompromised", "moderate pain", 2, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_02_20", "immunocompromised", "moderate pain", 3, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_02_21", "immunocompromised", "moderate pain", 4, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_02_22", "immunocompromised", "moderate pain", 5, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_02_23", "immunocompromised", "moderate pain", 1, "IADT", "D6"
    ),
    ClinicalSignal("immunocompromised_03_00", "immunocompromised", "high fever", 4, "ADA", "D6"),
    ClinicalSignal("immunocompromised_03_01", "immunocompromised", "high fever", 5, "ADA", "D6"),
    ClinicalSignal("immunocompromised_03_02", "immunocompromised", "high fever", 1, "ADA", "D6"),
    ClinicalSignal("immunocompromised_03_03", "immunocompromised", "high fever", 2, "ADA", "D6"),
    ClinicalSignal("immunocompromised_03_04", "immunocompromised", "high fever", 3, "ADA", "D6"),
    ClinicalSignal("immunocompromised_03_05", "immunocompromised", "high fever", 4, "ADA", "D6"),
    ClinicalSignal("immunocompromised_03_06", "immunocompromised", "high fever", 5, "ADA", "D6"),
    ClinicalSignal("immunocompromised_03_07", "immunocompromised", "high fever", 1, "ADA", "D6"),
    ClinicalSignal("immunocompromised_03_08", "immunocompromised", "high fever", 2, "ADA", "D6"),
    ClinicalSignal("immunocompromised_03_09", "immunocompromised", "high fever", 3, "ADA", "D6"),
    ClinicalSignal("immunocompromised_03_10", "immunocompromised", "high fever", 4, "ADA", "D6"),
    ClinicalSignal("immunocompromised_03_11", "immunocompromised", "high fever", 5, "ADA", "D6"),
    ClinicalSignal("immunocompromised_03_12", "immunocompromised", "high fever", 1, "ADA", "D6"),
    ClinicalSignal("immunocompromised_03_13", "immunocompromised", "high fever", 2, "ADA", "D6"),
    ClinicalSignal("immunocompromised_03_14", "immunocompromised", "high fever", 3, "ADA", "D6"),
    ClinicalSignal("immunocompromised_03_15", "immunocompromised", "high fever", 4, "ADA", "D6"),
    ClinicalSignal("immunocompromised_03_16", "immunocompromised", "high fever", 5, "ADA", "D6"),
    ClinicalSignal("immunocompromised_03_17", "immunocompromised", "high fever", 1, "ADA", "D6"),
    ClinicalSignal("immunocompromised_03_18", "immunocompromised", "high fever", 2, "ADA", "D6"),
    ClinicalSignal("immunocompromised_03_19", "immunocompromised", "high fever", 3, "ADA", "D6"),
    ClinicalSignal("immunocompromised_03_20", "immunocompromised", "high fever", 4, "ADA", "D6"),
    ClinicalSignal("immunocompromised_03_21", "immunocompromised", "high fever", 5, "ADA", "D6"),
    ClinicalSignal("immunocompromised_03_22", "immunocompromised", "high fever", 1, "ADA", "D6"),
    ClinicalSignal("immunocompromised_03_23", "immunocompromised", "high fever", 2, "ADA", "D6"),
    ClinicalSignal(
        "immunocompromised_04_00", "immunocompromised", "significant trismus", 5, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_04_01", "immunocompromised", "significant trismus", 1, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_04_02", "immunocompromised", "significant trismus", 2, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_04_03", "immunocompromised", "significant trismus", 3, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_04_04", "immunocompromised", "significant trismus", 4, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_04_05", "immunocompromised", "significant trismus", 5, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_04_06", "immunocompromised", "significant trismus", 1, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_04_07", "immunocompromised", "significant trismus", 2, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_04_08", "immunocompromised", "significant trismus", 3, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_04_09", "immunocompromised", "significant trismus", 4, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_04_10", "immunocompromised", "significant trismus", 5, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_04_11", "immunocompromised", "significant trismus", 1, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_04_12", "immunocompromised", "significant trismus", 2, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_04_13", "immunocompromised", "significant trismus", 3, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_04_14", "immunocompromised", "significant trismus", 4, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_04_15", "immunocompromised", "significant trismus", 5, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_04_16", "immunocompromised", "significant trismus", 1, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_04_17", "immunocompromised", "significant trismus", 2, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_04_18", "immunocompromised", "significant trismus", 3, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_04_19", "immunocompromised", "significant trismus", 4, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_04_20", "immunocompromised", "significant trismus", 5, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_04_21", "immunocompromised", "significant trismus", 1, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_04_22", "immunocompromised", "significant trismus", 2, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_04_23", "immunocompromised", "significant trismus", 3, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_05_00", "immunocompromised", "difficulty swallowing", 1, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_05_01", "immunocompromised", "difficulty swallowing", 2, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_05_02", "immunocompromised", "difficulty swallowing", 3, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_05_03", "immunocompromised", "difficulty swallowing", 4, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_05_04", "immunocompromised", "difficulty swallowing", 5, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_05_05", "immunocompromised", "difficulty swallowing", 1, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_05_06", "immunocompromised", "difficulty swallowing", 2, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_05_07", "immunocompromised", "difficulty swallowing", 3, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_05_08", "immunocompromised", "difficulty swallowing", 4, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_05_09", "immunocompromised", "difficulty swallowing", 5, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_05_10", "immunocompromised", "difficulty swallowing", 1, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_05_11", "immunocompromised", "difficulty swallowing", 2, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_05_12", "immunocompromised", "difficulty swallowing", 3, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_05_13", "immunocompromised", "difficulty swallowing", 4, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_05_14", "immunocompromised", "difficulty swallowing", 5, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_05_15", "immunocompromised", "difficulty swallowing", 1, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_05_16", "immunocompromised", "difficulty swallowing", 2, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_05_17", "immunocompromised", "difficulty swallowing", 3, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_05_18", "immunocompromised", "difficulty swallowing", 4, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_05_19", "immunocompromised", "difficulty swallowing", 5, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_05_20", "immunocompromised", "difficulty swallowing", 1, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_05_21", "immunocompromised", "difficulty swallowing", 2, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_05_22", "immunocompromised", "difficulty swallowing", 3, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_05_23", "immunocompromised", "difficulty swallowing", 4, "AAE", "D6"
    ),
    ClinicalSignal("immunocompromised_06_00", "immunocompromised", "airway noise", 2, "IADT", "D6"),
    ClinicalSignal("immunocompromised_06_01", "immunocompromised", "airway noise", 3, "IADT", "D6"),
    ClinicalSignal("immunocompromised_06_02", "immunocompromised", "airway noise", 4, "IADT", "D6"),
    ClinicalSignal("immunocompromised_06_03", "immunocompromised", "airway noise", 5, "IADT", "D6"),
    ClinicalSignal("immunocompromised_06_04", "immunocompromised", "airway noise", 1, "IADT", "D6"),
    ClinicalSignal("immunocompromised_06_05", "immunocompromised", "airway noise", 2, "IADT", "D6"),
    ClinicalSignal("immunocompromised_06_06", "immunocompromised", "airway noise", 3, "IADT", "D6"),
    ClinicalSignal("immunocompromised_06_07", "immunocompromised", "airway noise", 4, "IADT", "D6"),
    ClinicalSignal("immunocompromised_06_08", "immunocompromised", "airway noise", 5, "IADT", "D6"),
    ClinicalSignal("immunocompromised_06_09", "immunocompromised", "airway noise", 1, "IADT", "D6"),
    ClinicalSignal("immunocompromised_06_10", "immunocompromised", "airway noise", 2, "IADT", "D6"),
    ClinicalSignal("immunocompromised_06_11", "immunocompromised", "airway noise", 3, "IADT", "D6"),
    ClinicalSignal("immunocompromised_06_12", "immunocompromised", "airway noise", 4, "IADT", "D6"),
    ClinicalSignal("immunocompromised_06_13", "immunocompromised", "airway noise", 5, "IADT", "D6"),
    ClinicalSignal("immunocompromised_06_14", "immunocompromised", "airway noise", 1, "IADT", "D6"),
    ClinicalSignal("immunocompromised_06_15", "immunocompromised", "airway noise", 2, "IADT", "D6"),
    ClinicalSignal("immunocompromised_06_16", "immunocompromised", "airway noise", 3, "IADT", "D6"),
    ClinicalSignal("immunocompromised_06_17", "immunocompromised", "airway noise", 4, "IADT", "D6"),
    ClinicalSignal("immunocompromised_06_18", "immunocompromised", "airway noise", 5, "IADT", "D6"),
    ClinicalSignal("immunocompromised_06_19", "immunocompromised", "airway noise", 1, "IADT", "D6"),
    ClinicalSignal("immunocompromised_06_20", "immunocompromised", "airway noise", 2, "IADT", "D6"),
    ClinicalSignal("immunocompromised_06_21", "immunocompromised", "airway noise", 3, "IADT", "D6"),
    ClinicalSignal("immunocompromised_06_22", "immunocompromised", "airway noise", 4, "IADT", "D6"),
    ClinicalSignal("immunocompromised_06_23", "immunocompromised", "airway noise", 5, "IADT", "D6"),
    ClinicalSignal(
        "immunocompromised_07_00", "immunocompromised", "uncontrolled bleeding", 3, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_07_01", "immunocompromised", "uncontrolled bleeding", 4, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_07_02", "immunocompromised", "uncontrolled bleeding", 5, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_07_03", "immunocompromised", "uncontrolled bleeding", 1, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_07_04", "immunocompromised", "uncontrolled bleeding", 2, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_07_05", "immunocompromised", "uncontrolled bleeding", 3, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_07_06", "immunocompromised", "uncontrolled bleeding", 4, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_07_07", "immunocompromised", "uncontrolled bleeding", 5, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_07_08", "immunocompromised", "uncontrolled bleeding", 1, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_07_09", "immunocompromised", "uncontrolled bleeding", 2, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_07_10", "immunocompromised", "uncontrolled bleeding", 3, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_07_11", "immunocompromised", "uncontrolled bleeding", 4, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_07_12", "immunocompromised", "uncontrolled bleeding", 5, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_07_13", "immunocompromised", "uncontrolled bleeding", 1, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_07_14", "immunocompromised", "uncontrolled bleeding", 2, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_07_15", "immunocompromised", "uncontrolled bleeding", 3, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_07_16", "immunocompromised", "uncontrolled bleeding", 4, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_07_17", "immunocompromised", "uncontrolled bleeding", 5, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_07_18", "immunocompromised", "uncontrolled bleeding", 1, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_07_19", "immunocompromised", "uncontrolled bleeding", 2, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_07_20", "immunocompromised", "uncontrolled bleeding", 3, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_07_21", "immunocompromised", "uncontrolled bleeding", 4, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_07_22", "immunocompromised", "uncontrolled bleeding", 5, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_07_23", "immunocompromised", "uncontrolled bleeding", 1, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_08_00", "immunocompromised", "minor sensitivity", 4, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_08_01", "immunocompromised", "minor sensitivity", 5, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_08_02", "immunocompromised", "minor sensitivity", 1, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_08_03", "immunocompromised", "minor sensitivity", 2, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_08_04", "immunocompromised", "minor sensitivity", 3, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_08_05", "immunocompromised", "minor sensitivity", 4, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_08_06", "immunocompromised", "minor sensitivity", 5, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_08_07", "immunocompromised", "minor sensitivity", 1, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_08_08", "immunocompromised", "minor sensitivity", 2, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_08_09", "immunocompromised", "minor sensitivity", 3, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_08_10", "immunocompromised", "minor sensitivity", 4, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_08_11", "immunocompromised", "minor sensitivity", 5, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_08_12", "immunocompromised", "minor sensitivity", 1, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_08_13", "immunocompromised", "minor sensitivity", 2, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_08_14", "immunocompromised", "minor sensitivity", 3, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_08_15", "immunocompromised", "minor sensitivity", 4, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_08_16", "immunocompromised", "minor sensitivity", 5, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_08_17", "immunocompromised", "minor sensitivity", 1, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_08_18", "immunocompromised", "minor sensitivity", 2, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_08_19", "immunocompromised", "minor sensitivity", 3, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_08_20", "immunocompromised", "minor sensitivity", 4, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_08_21", "immunocompromised", "minor sensitivity", 5, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_08_22", "immunocompromised", "minor sensitivity", 1, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_08_23", "immunocompromised", "minor sensitivity", 2, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_09_00", "immunocompromised", "preventive enquiry", 5, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_09_01", "immunocompromised", "preventive enquiry", 1, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_09_02", "immunocompromised", "preventive enquiry", 2, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_09_03", "immunocompromised", "preventive enquiry", 3, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_09_04", "immunocompromised", "preventive enquiry", 4, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_09_05", "immunocompromised", "preventive enquiry", 5, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_09_06", "immunocompromised", "preventive enquiry", 1, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_09_07", "immunocompromised", "preventive enquiry", 2, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_09_08", "immunocompromised", "preventive enquiry", 3, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_09_09", "immunocompromised", "preventive enquiry", 4, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_09_10", "immunocompromised", "preventive enquiry", 5, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_09_11", "immunocompromised", "preventive enquiry", 1, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_09_12", "immunocompromised", "preventive enquiry", 2, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_09_13", "immunocompromised", "preventive enquiry", 3, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_09_14", "immunocompromised", "preventive enquiry", 4, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_09_15", "immunocompromised", "preventive enquiry", 5, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_09_16", "immunocompromised", "preventive enquiry", 1, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_09_17", "immunocompromised", "preventive enquiry", 2, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_09_18", "immunocompromised", "preventive enquiry", 3, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_09_19", "immunocompromised", "preventive enquiry", 4, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_09_20", "immunocompromised", "preventive enquiry", 5, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_09_21", "immunocompromised", "preventive enquiry", 1, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_09_22", "immunocompromised", "preventive enquiry", 2, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_09_23", "immunocompromised", "preventive enquiry", 3, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_10_00", "immunocompromised", "facial asymmetry", 1, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_10_01", "immunocompromised", "facial asymmetry", 2, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_10_02", "immunocompromised", "facial asymmetry", 3, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_10_03", "immunocompromised", "facial asymmetry", 4, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_10_04", "immunocompromised", "facial asymmetry", 5, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_10_05", "immunocompromised", "facial asymmetry", 1, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_10_06", "immunocompromised", "facial asymmetry", 2, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_10_07", "immunocompromised", "facial asymmetry", 3, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_10_08", "immunocompromised", "facial asymmetry", 4, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_10_09", "immunocompromised", "facial asymmetry", 5, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_10_10", "immunocompromised", "facial asymmetry", 1, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_10_11", "immunocompromised", "facial asymmetry", 2, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_10_12", "immunocompromised", "facial asymmetry", 3, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_10_13", "immunocompromised", "facial asymmetry", 4, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_10_14", "immunocompromised", "facial asymmetry", 5, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_10_15", "immunocompromised", "facial asymmetry", 1, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_10_16", "immunocompromised", "facial asymmetry", 2, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_10_17", "immunocompromised", "facial asymmetry", 3, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_10_18", "immunocompromised", "facial asymmetry", 4, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_10_19", "immunocompromised", "facial asymmetry", 5, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_10_20", "immunocompromised", "facial asymmetry", 1, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_10_21", "immunocompromised", "facial asymmetry", 2, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_10_22", "immunocompromised", "facial asymmetry", 3, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_10_23", "immunocompromised", "facial asymmetry", 4, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_11_00", "immunocompromised", "floor of mouth elevation", 2, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_11_01", "immunocompromised", "floor of mouth elevation", 3, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_11_02", "immunocompromised", "floor of mouth elevation", 4, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_11_03", "immunocompromised", "floor of mouth elevation", 5, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_11_04", "immunocompromised", "floor of mouth elevation", 1, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_11_05", "immunocompromised", "floor of mouth elevation", 2, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_11_06", "immunocompromised", "floor of mouth elevation", 3, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_11_07", "immunocompromised", "floor of mouth elevation", 4, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_11_08", "immunocompromised", "floor of mouth elevation", 5, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_11_09", "immunocompromised", "floor of mouth elevation", 1, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_11_10", "immunocompromised", "floor of mouth elevation", 2, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_11_11", "immunocompromised", "floor of mouth elevation", 3, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_11_12", "immunocompromised", "floor of mouth elevation", 4, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_11_13", "immunocompromised", "floor of mouth elevation", 5, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_11_14", "immunocompromised", "floor of mouth elevation", 1, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_11_15", "immunocompromised", "floor of mouth elevation", 2, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_11_16", "immunocompromised", "floor of mouth elevation", 3, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_11_17", "immunocompromised", "floor of mouth elevation", 4, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_11_18", "immunocompromised", "floor of mouth elevation", 5, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_11_19", "immunocompromised", "floor of mouth elevation", 1, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_11_20", "immunocompromised", "floor of mouth elevation", 2, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_11_21", "immunocompromised", "floor of mouth elevation", 3, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_11_22", "immunocompromised", "floor of mouth elevation", 4, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_11_23", "immunocompromised", "floor of mouth elevation", 5, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_12_00", "immunocompromised", "tongue displacement", 3, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_12_01", "immunocompromised", "tongue displacement", 4, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_12_02", "immunocompromised", "tongue displacement", 5, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_12_03", "immunocompromised", "tongue displacement", 1, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_12_04", "immunocompromised", "tongue displacement", 2, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_12_05", "immunocompromised", "tongue displacement", 3, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_12_06", "immunocompromised", "tongue displacement", 4, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_12_07", "immunocompromised", "tongue displacement", 5, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_12_08", "immunocompromised", "tongue displacement", 1, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_12_09", "immunocompromised", "tongue displacement", 2, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_12_10", "immunocompromised", "tongue displacement", 3, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_12_11", "immunocompromised", "tongue displacement", 4, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_12_12", "immunocompromised", "tongue displacement", 5, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_12_13", "immunocompromised", "tongue displacement", 1, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_12_14", "immunocompromised", "tongue displacement", 2, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_12_15", "immunocompromised", "tongue displacement", 3, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_12_16", "immunocompromised", "tongue displacement", 4, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_12_17", "immunocompromised", "tongue displacement", 5, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_12_18", "immunocompromised", "tongue displacement", 1, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_12_19", "immunocompromised", "tongue displacement", 2, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_12_20", "immunocompromised", "tongue displacement", 3, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_12_21", "immunocompromised", "tongue displacement", 4, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_12_22", "immunocompromised", "tongue displacement", 5, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_12_23", "immunocompromised", "tongue displacement", 1, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_13_00", "immunocompromised", "slow progression", 4, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_13_01", "immunocompromised", "slow progression", 5, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_13_02", "immunocompromised", "slow progression", 1, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_13_03", "immunocompromised", "slow progression", 2, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_13_04", "immunocompromised", "slow progression", 3, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_13_05", "immunocompromised", "slow progression", 4, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_13_06", "immunocompromised", "slow progression", 5, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_13_07", "immunocompromised", "slow progression", 1, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_13_08", "immunocompromised", "slow progression", 2, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_13_09", "immunocompromised", "slow progression", 3, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_13_10", "immunocompromised", "slow progression", 4, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_13_11", "immunocompromised", "slow progression", 5, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_13_12", "immunocompromised", "slow progression", 1, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_13_13", "immunocompromised", "slow progression", 2, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_13_14", "immunocompromised", "slow progression", 3, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_13_15", "immunocompromised", "slow progression", 4, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_13_16", "immunocompromised", "slow progression", 5, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_13_17", "immunocompromised", "slow progression", 1, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_13_18", "immunocompromised", "slow progression", 2, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_13_19", "immunocompromised", "slow progression", 3, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_13_20", "immunocompromised", "slow progression", 4, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_13_21", "immunocompromised", "slow progression", 5, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_13_22", "immunocompromised", "slow progression", 1, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_13_23", "immunocompromised", "slow progression", 2, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_14_00", "immunocompromised", "rapid progression", 5, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_14_01", "immunocompromised", "rapid progression", 1, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_14_02", "immunocompromised", "rapid progression", 2, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_14_03", "immunocompromised", "rapid progression", 3, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_14_04", "immunocompromised", "rapid progression", 4, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_14_05", "immunocompromised", "rapid progression", 5, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_14_06", "immunocompromised", "rapid progression", 1, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_14_07", "immunocompromised", "rapid progression", 2, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_14_08", "immunocompromised", "rapid progression", 3, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_14_09", "immunocompromised", "rapid progression", 4, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_14_10", "immunocompromised", "rapid progression", 5, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_14_11", "immunocompromised", "rapid progression", 1, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_14_12", "immunocompromised", "rapid progression", 2, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_14_13", "immunocompromised", "rapid progression", 3, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_14_14", "immunocompromised", "rapid progression", 4, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_14_15", "immunocompromised", "rapid progression", 5, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_14_16", "immunocompromised", "rapid progression", 1, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_14_17", "immunocompromised", "rapid progression", 2, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_14_18", "immunocompromised", "rapid progression", 3, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_14_19", "immunocompromised", "rapid progression", 4, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_14_20", "immunocompromised", "rapid progression", 5, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_14_21", "immunocompromised", "rapid progression", 1, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_14_22", "immunocompromised", "rapid progression", 2, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_14_23", "immunocompromised", "rapid progression", 3, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_15_00", "immunocompromised", "attenuated inflammation", 1, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_15_01", "immunocompromised", "attenuated inflammation", 2, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_15_02", "immunocompromised", "attenuated inflammation", 3, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_15_03", "immunocompromised", "attenuated inflammation", 4, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_15_04", "immunocompromised", "attenuated inflammation", 5, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_15_05", "immunocompromised", "attenuated inflammation", 1, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_15_06", "immunocompromised", "attenuated inflammation", 2, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_15_07", "immunocompromised", "attenuated inflammation", 3, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_15_08", "immunocompromised", "attenuated inflammation", 4, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_15_09", "immunocompromised", "attenuated inflammation", 5, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_15_10", "immunocompromised", "attenuated inflammation", 1, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_15_11", "immunocompromised", "attenuated inflammation", 2, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_15_12", "immunocompromised", "attenuated inflammation", 3, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_15_13", "immunocompromised", "attenuated inflammation", 4, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_15_14", "immunocompromised", "attenuated inflammation", 5, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_15_15", "immunocompromised", "attenuated inflammation", 1, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_15_16", "immunocompromised", "attenuated inflammation", 2, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_15_17", "immunocompromised", "attenuated inflammation", 3, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_15_18", "immunocompromised", "attenuated inflammation", 4, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_15_19", "immunocompromised", "attenuated inflammation", 5, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_15_20", "immunocompromised", "attenuated inflammation", 1, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_15_21", "immunocompromised", "attenuated inflammation", 2, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_15_22", "immunocompromised", "attenuated inflammation", 3, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_15_23", "immunocompromised", "attenuated inflammation", 4, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_16_00", "immunocompromised", "delayed onset", 2, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_16_01", "immunocompromised", "delayed onset", 3, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_16_02", "immunocompromised", "delayed onset", 4, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_16_03", "immunocompromised", "delayed onset", 5, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_16_04", "immunocompromised", "delayed onset", 1, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_16_05", "immunocompromised", "delayed onset", 2, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_16_06", "immunocompromised", "delayed onset", 3, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_16_07", "immunocompromised", "delayed onset", 4, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_16_08", "immunocompromised", "delayed onset", 5, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_16_09", "immunocompromised", "delayed onset", 1, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_16_10", "immunocompromised", "delayed onset", 2, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_16_11", "immunocompromised", "delayed onset", 3, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_16_12", "immunocompromised", "delayed onset", 4, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_16_13", "immunocompromised", "delayed onset", 5, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_16_14", "immunocompromised", "delayed onset", 1, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_16_15", "immunocompromised", "delayed onset", 2, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_16_16", "immunocompromised", "delayed onset", 3, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_16_17", "immunocompromised", "delayed onset", 4, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_16_18", "immunocompromised", "delayed onset", 5, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_16_19", "immunocompromised", "delayed onset", 1, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_16_20", "immunocompromised", "delayed onset", 2, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_16_21", "immunocompromised", "delayed onset", 3, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_16_22", "immunocompromised", "delayed onset", 4, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_16_23", "immunocompromised", "delayed onset", 5, "AAPD", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_17_00", "immunocompromised", "medical vulnerability", 3, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_17_01", "immunocompromised", "medical vulnerability", 4, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_17_02", "immunocompromised", "medical vulnerability", 5, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_17_03", "immunocompromised", "medical vulnerability", 1, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_17_04", "immunocompromised", "medical vulnerability", 2, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_17_05", "immunocompromised", "medical vulnerability", 3, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_17_06", "immunocompromised", "medical vulnerability", 4, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_17_07", "immunocompromised", "medical vulnerability", 5, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_17_08", "immunocompromised", "medical vulnerability", 1, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_17_09", "immunocompromised", "medical vulnerability", 2, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_17_10", "immunocompromised", "medical vulnerability", 3, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_17_11", "immunocompromised", "medical vulnerability", 4, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_17_12", "immunocompromised", "medical vulnerability", 5, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_17_13", "immunocompromised", "medical vulnerability", 1, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_17_14", "immunocompromised", "medical vulnerability", 2, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_17_15", "immunocompromised", "medical vulnerability", 3, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_17_16", "immunocompromised", "medical vulnerability", 4, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_17_17", "immunocompromised", "medical vulnerability", 5, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_17_18", "immunocompromised", "medical vulnerability", 1, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_17_19", "immunocompromised", "medical vulnerability", 2, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_17_20", "immunocompromised", "medical vulnerability", 3, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_17_21", "immunocompromised", "medical vulnerability", 4, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_17_22", "immunocompromised", "medical vulnerability", 5, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_17_23", "immunocompromised", "medical vulnerability", 1, "AAE", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_18_00", "immunocompromised", "controlled symptoms", 4, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_18_01", "immunocompromised", "controlled symptoms", 5, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_18_02", "immunocompromised", "controlled symptoms", 1, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_18_03", "immunocompromised", "controlled symptoms", 2, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_18_04", "immunocompromised", "controlled symptoms", 3, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_18_05", "immunocompromised", "controlled symptoms", 4, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_18_06", "immunocompromised", "controlled symptoms", 5, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_18_07", "immunocompromised", "controlled symptoms", 1, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_18_08", "immunocompromised", "controlled symptoms", 2, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_18_09", "immunocompromised", "controlled symptoms", 3, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_18_10", "immunocompromised", "controlled symptoms", 4, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_18_11", "immunocompromised", "controlled symptoms", 5, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_18_12", "immunocompromised", "controlled symptoms", 1, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_18_13", "immunocompromised", "controlled symptoms", 2, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_18_14", "immunocompromised", "controlled symptoms", 3, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_18_15", "immunocompromised", "controlled symptoms", 4, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_18_16", "immunocompromised", "controlled symptoms", 5, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_18_17", "immunocompromised", "controlled symptoms", 1, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_18_18", "immunocompromised", "controlled symptoms", 2, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_18_19", "immunocompromised", "controlled symptoms", 3, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_18_20", "immunocompromised", "controlled symptoms", 4, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_18_21", "immunocompromised", "controlled symptoms", 5, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_18_22", "immunocompromised", "controlled symptoms", 1, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_18_23", "immunocompromised", "controlled symptoms", 2, "IADT", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_19_00", "immunocompromised", "systemic illness", 5, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_19_01", "immunocompromised", "systemic illness", 1, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_19_02", "immunocompromised", "systemic illness", 2, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_19_03", "immunocompromised", "systemic illness", 3, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_19_04", "immunocompromised", "systemic illness", 4, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_19_05", "immunocompromised", "systemic illness", 5, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_19_06", "immunocompromised", "systemic illness", 1, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_19_07", "immunocompromised", "systemic illness", 2, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_19_08", "immunocompromised", "systemic illness", 3, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_19_09", "immunocompromised", "systemic illness", 4, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_19_10", "immunocompromised", "systemic illness", 5, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_19_11", "immunocompromised", "systemic illness", 1, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_19_12", "immunocompromised", "systemic illness", 2, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_19_13", "immunocompromised", "systemic illness", 3, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_19_14", "immunocompromised", "systemic illness", 4, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_19_15", "immunocompromised", "systemic illness", 5, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_19_16", "immunocompromised", "systemic illness", 1, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_19_17", "immunocompromised", "systemic illness", 2, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_19_18", "immunocompromised", "systemic illness", 3, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_19_19", "immunocompromised", "systemic illness", 4, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_19_20", "immunocompromised", "systemic illness", 5, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_19_21", "immunocompromised", "systemic illness", 1, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_19_22", "immunocompromised", "systemic illness", 2, "ADA", "D6"
    ),
    ClinicalSignal(
        "immunocompromised_19_23", "immunocompromised", "systemic illness", 3, "ADA", "D6"
    ),
    ClinicalSignal(
        "airway_compromise_00_00", "airway_compromise", "localised swelling", 2, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_00_01", "airway_compromise", "localised swelling", 3, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_00_02", "airway_compromise", "localised swelling", 4, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_00_03", "airway_compromise", "localised swelling", 5, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_00_04", "airway_compromise", "localised swelling", 1, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_00_05", "airway_compromise", "localised swelling", 2, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_00_06", "airway_compromise", "localised swelling", 3, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_00_07", "airway_compromise", "localised swelling", 4, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_00_08", "airway_compromise", "localised swelling", 5, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_00_09", "airway_compromise", "localised swelling", 1, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_00_10", "airway_compromise", "localised swelling", 2, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_00_11", "airway_compromise", "localised swelling", 3, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_00_12", "airway_compromise", "localised swelling", 4, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_00_13", "airway_compromise", "localised swelling", 5, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_00_14", "airway_compromise", "localised swelling", 1, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_00_15", "airway_compromise", "localised swelling", 2, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_00_16", "airway_compromise", "localised swelling", 3, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_00_17", "airway_compromise", "localised swelling", 4, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_00_18", "airway_compromise", "localised swelling", 5, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_00_19", "airway_compromise", "localised swelling", 1, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_00_20", "airway_compromise", "localised swelling", 2, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_00_21", "airway_compromise", "localised swelling", 3, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_00_22", "airway_compromise", "localised swelling", 4, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_00_23", "airway_compromise", "localised swelling", 5, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_01_00", "airway_compromise", "progressive swelling", 3, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_01_01", "airway_compromise", "progressive swelling", 4, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_01_02", "airway_compromise", "progressive swelling", 5, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_01_03", "airway_compromise", "progressive swelling", 1, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_01_04", "airway_compromise", "progressive swelling", 2, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_01_05", "airway_compromise", "progressive swelling", 3, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_01_06", "airway_compromise", "progressive swelling", 4, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_01_07", "airway_compromise", "progressive swelling", 5, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_01_08", "airway_compromise", "progressive swelling", 1, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_01_09", "airway_compromise", "progressive swelling", 2, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_01_10", "airway_compromise", "progressive swelling", 3, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_01_11", "airway_compromise", "progressive swelling", 4, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_01_12", "airway_compromise", "progressive swelling", 5, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_01_13", "airway_compromise", "progressive swelling", 1, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_01_14", "airway_compromise", "progressive swelling", 2, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_01_15", "airway_compromise", "progressive swelling", 3, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_01_16", "airway_compromise", "progressive swelling", 4, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_01_17", "airway_compromise", "progressive swelling", 5, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_01_18", "airway_compromise", "progressive swelling", 1, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_01_19", "airway_compromise", "progressive swelling", 2, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_01_20", "airway_compromise", "progressive swelling", 3, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_01_21", "airway_compromise", "progressive swelling", 4, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_01_22", "airway_compromise", "progressive swelling", 5, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_01_23", "airway_compromise", "progressive swelling", 1, "IADT", "D7"
    ),
    ClinicalSignal("airway_compromise_02_00", "airway_compromise", "moderate pain", 4, "ADA", "D7"),
    ClinicalSignal("airway_compromise_02_01", "airway_compromise", "moderate pain", 5, "ADA", "D7"),
    ClinicalSignal("airway_compromise_02_02", "airway_compromise", "moderate pain", 1, "ADA", "D7"),
    ClinicalSignal("airway_compromise_02_03", "airway_compromise", "moderate pain", 2, "ADA", "D7"),
    ClinicalSignal("airway_compromise_02_04", "airway_compromise", "moderate pain", 3, "ADA", "D7"),
    ClinicalSignal("airway_compromise_02_05", "airway_compromise", "moderate pain", 4, "ADA", "D7"),
    ClinicalSignal("airway_compromise_02_06", "airway_compromise", "moderate pain", 5, "ADA", "D7"),
    ClinicalSignal("airway_compromise_02_07", "airway_compromise", "moderate pain", 1, "ADA", "D7"),
    ClinicalSignal("airway_compromise_02_08", "airway_compromise", "moderate pain", 2, "ADA", "D7"),
    ClinicalSignal("airway_compromise_02_09", "airway_compromise", "moderate pain", 3, "ADA", "D7"),
    ClinicalSignal("airway_compromise_02_10", "airway_compromise", "moderate pain", 4, "ADA", "D7"),
    ClinicalSignal("airway_compromise_02_11", "airway_compromise", "moderate pain", 5, "ADA", "D7"),
    ClinicalSignal("airway_compromise_02_12", "airway_compromise", "moderate pain", 1, "ADA", "D7"),
    ClinicalSignal("airway_compromise_02_13", "airway_compromise", "moderate pain", 2, "ADA", "D7"),
    ClinicalSignal("airway_compromise_02_14", "airway_compromise", "moderate pain", 3, "ADA", "D7"),
    ClinicalSignal("airway_compromise_02_15", "airway_compromise", "moderate pain", 4, "ADA", "D7"),
    ClinicalSignal("airway_compromise_02_16", "airway_compromise", "moderate pain", 5, "ADA", "D7"),
    ClinicalSignal("airway_compromise_02_17", "airway_compromise", "moderate pain", 1, "ADA", "D7"),
    ClinicalSignal("airway_compromise_02_18", "airway_compromise", "moderate pain", 2, "ADA", "D7"),
    ClinicalSignal("airway_compromise_02_19", "airway_compromise", "moderate pain", 3, "ADA", "D7"),
    ClinicalSignal("airway_compromise_02_20", "airway_compromise", "moderate pain", 4, "ADA", "D7"),
    ClinicalSignal("airway_compromise_02_21", "airway_compromise", "moderate pain", 5, "ADA", "D7"),
    ClinicalSignal("airway_compromise_02_22", "airway_compromise", "moderate pain", 1, "ADA", "D7"),
    ClinicalSignal("airway_compromise_02_23", "airway_compromise", "moderate pain", 2, "ADA", "D7"),
    ClinicalSignal("airway_compromise_03_00", "airway_compromise", "high fever", 5, "AAPD", "D7"),
    ClinicalSignal("airway_compromise_03_01", "airway_compromise", "high fever", 1, "AAPD", "D7"),
    ClinicalSignal("airway_compromise_03_02", "airway_compromise", "high fever", 2, "AAPD", "D7"),
    ClinicalSignal("airway_compromise_03_03", "airway_compromise", "high fever", 3, "AAPD", "D7"),
    ClinicalSignal("airway_compromise_03_04", "airway_compromise", "high fever", 4, "AAPD", "D7"),
    ClinicalSignal("airway_compromise_03_05", "airway_compromise", "high fever", 5, "AAPD", "D7"),
    ClinicalSignal("airway_compromise_03_06", "airway_compromise", "high fever", 1, "AAPD", "D7"),
    ClinicalSignal("airway_compromise_03_07", "airway_compromise", "high fever", 2, "AAPD", "D7"),
    ClinicalSignal("airway_compromise_03_08", "airway_compromise", "high fever", 3, "AAPD", "D7"),
    ClinicalSignal("airway_compromise_03_09", "airway_compromise", "high fever", 4, "AAPD", "D7"),
    ClinicalSignal("airway_compromise_03_10", "airway_compromise", "high fever", 5, "AAPD", "D7"),
    ClinicalSignal("airway_compromise_03_11", "airway_compromise", "high fever", 1, "AAPD", "D7"),
    ClinicalSignal("airway_compromise_03_12", "airway_compromise", "high fever", 2, "AAPD", "D7"),
    ClinicalSignal("airway_compromise_03_13", "airway_compromise", "high fever", 3, "AAPD", "D7"),
    ClinicalSignal("airway_compromise_03_14", "airway_compromise", "high fever", 4, "AAPD", "D7"),
    ClinicalSignal("airway_compromise_03_15", "airway_compromise", "high fever", 5, "AAPD", "D7"),
    ClinicalSignal("airway_compromise_03_16", "airway_compromise", "high fever", 1, "AAPD", "D7"),
    ClinicalSignal("airway_compromise_03_17", "airway_compromise", "high fever", 2, "AAPD", "D7"),
    ClinicalSignal("airway_compromise_03_18", "airway_compromise", "high fever", 3, "AAPD", "D7"),
    ClinicalSignal("airway_compromise_03_19", "airway_compromise", "high fever", 4, "AAPD", "D7"),
    ClinicalSignal("airway_compromise_03_20", "airway_compromise", "high fever", 5, "AAPD", "D7"),
    ClinicalSignal("airway_compromise_03_21", "airway_compromise", "high fever", 1, "AAPD", "D7"),
    ClinicalSignal("airway_compromise_03_22", "airway_compromise", "high fever", 2, "AAPD", "D7"),
    ClinicalSignal("airway_compromise_03_23", "airway_compromise", "high fever", 3, "AAPD", "D7"),
    ClinicalSignal(
        "airway_compromise_04_00", "airway_compromise", "significant trismus", 1, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_04_01", "airway_compromise", "significant trismus", 2, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_04_02", "airway_compromise", "significant trismus", 3, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_04_03", "airway_compromise", "significant trismus", 4, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_04_04", "airway_compromise", "significant trismus", 5, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_04_05", "airway_compromise", "significant trismus", 1, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_04_06", "airway_compromise", "significant trismus", 2, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_04_07", "airway_compromise", "significant trismus", 3, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_04_08", "airway_compromise", "significant trismus", 4, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_04_09", "airway_compromise", "significant trismus", 5, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_04_10", "airway_compromise", "significant trismus", 1, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_04_11", "airway_compromise", "significant trismus", 2, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_04_12", "airway_compromise", "significant trismus", 3, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_04_13", "airway_compromise", "significant trismus", 4, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_04_14", "airway_compromise", "significant trismus", 5, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_04_15", "airway_compromise", "significant trismus", 1, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_04_16", "airway_compromise", "significant trismus", 2, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_04_17", "airway_compromise", "significant trismus", 3, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_04_18", "airway_compromise", "significant trismus", 4, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_04_19", "airway_compromise", "significant trismus", 5, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_04_20", "airway_compromise", "significant trismus", 1, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_04_21", "airway_compromise", "significant trismus", 2, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_04_22", "airway_compromise", "significant trismus", 3, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_04_23", "airway_compromise", "significant trismus", 4, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_05_00", "airway_compromise", "difficulty swallowing", 2, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_05_01", "airway_compromise", "difficulty swallowing", 3, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_05_02", "airway_compromise", "difficulty swallowing", 4, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_05_03", "airway_compromise", "difficulty swallowing", 5, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_05_04", "airway_compromise", "difficulty swallowing", 1, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_05_05", "airway_compromise", "difficulty swallowing", 2, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_05_06", "airway_compromise", "difficulty swallowing", 3, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_05_07", "airway_compromise", "difficulty swallowing", 4, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_05_08", "airway_compromise", "difficulty swallowing", 5, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_05_09", "airway_compromise", "difficulty swallowing", 1, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_05_10", "airway_compromise", "difficulty swallowing", 2, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_05_11", "airway_compromise", "difficulty swallowing", 3, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_05_12", "airway_compromise", "difficulty swallowing", 4, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_05_13", "airway_compromise", "difficulty swallowing", 5, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_05_14", "airway_compromise", "difficulty swallowing", 1, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_05_15", "airway_compromise", "difficulty swallowing", 2, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_05_16", "airway_compromise", "difficulty swallowing", 3, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_05_17", "airway_compromise", "difficulty swallowing", 4, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_05_18", "airway_compromise", "difficulty swallowing", 5, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_05_19", "airway_compromise", "difficulty swallowing", 1, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_05_20", "airway_compromise", "difficulty swallowing", 2, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_05_21", "airway_compromise", "difficulty swallowing", 3, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_05_22", "airway_compromise", "difficulty swallowing", 4, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_05_23", "airway_compromise", "difficulty swallowing", 5, "IADT", "D7"
    ),
    ClinicalSignal("airway_compromise_06_00", "airway_compromise", "airway noise", 3, "ADA", "D7"),
    ClinicalSignal("airway_compromise_06_01", "airway_compromise", "airway noise", 4, "ADA", "D7"),
    ClinicalSignal("airway_compromise_06_02", "airway_compromise", "airway noise", 5, "ADA", "D7"),
    ClinicalSignal("airway_compromise_06_03", "airway_compromise", "airway noise", 1, "ADA", "D7"),
    ClinicalSignal("airway_compromise_06_04", "airway_compromise", "airway noise", 2, "ADA", "D7"),
    ClinicalSignal("airway_compromise_06_05", "airway_compromise", "airway noise", 3, "ADA", "D7"),
    ClinicalSignal("airway_compromise_06_06", "airway_compromise", "airway noise", 4, "ADA", "D7"),
    ClinicalSignal("airway_compromise_06_07", "airway_compromise", "airway noise", 5, "ADA", "D7"),
    ClinicalSignal("airway_compromise_06_08", "airway_compromise", "airway noise", 1, "ADA", "D7"),
    ClinicalSignal("airway_compromise_06_09", "airway_compromise", "airway noise", 2, "ADA", "D7"),
    ClinicalSignal("airway_compromise_06_10", "airway_compromise", "airway noise", 3, "ADA", "D7"),
    ClinicalSignal("airway_compromise_06_11", "airway_compromise", "airway noise", 4, "ADA", "D7"),
    ClinicalSignal("airway_compromise_06_12", "airway_compromise", "airway noise", 5, "ADA", "D7"),
    ClinicalSignal("airway_compromise_06_13", "airway_compromise", "airway noise", 1, "ADA", "D7"),
    ClinicalSignal("airway_compromise_06_14", "airway_compromise", "airway noise", 2, "ADA", "D7"),
    ClinicalSignal("airway_compromise_06_15", "airway_compromise", "airway noise", 3, "ADA", "D7"),
    ClinicalSignal("airway_compromise_06_16", "airway_compromise", "airway noise", 4, "ADA", "D7"),
    ClinicalSignal("airway_compromise_06_17", "airway_compromise", "airway noise", 5, "ADA", "D7"),
    ClinicalSignal("airway_compromise_06_18", "airway_compromise", "airway noise", 1, "ADA", "D7"),
    ClinicalSignal("airway_compromise_06_19", "airway_compromise", "airway noise", 2, "ADA", "D7"),
    ClinicalSignal("airway_compromise_06_20", "airway_compromise", "airway noise", 3, "ADA", "D7"),
    ClinicalSignal("airway_compromise_06_21", "airway_compromise", "airway noise", 4, "ADA", "D7"),
    ClinicalSignal("airway_compromise_06_22", "airway_compromise", "airway noise", 5, "ADA", "D7"),
    ClinicalSignal("airway_compromise_06_23", "airway_compromise", "airway noise", 1, "ADA", "D7"),
    ClinicalSignal(
        "airway_compromise_07_00", "airway_compromise", "uncontrolled bleeding", 4, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_07_01", "airway_compromise", "uncontrolled bleeding", 5, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_07_02", "airway_compromise", "uncontrolled bleeding", 1, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_07_03", "airway_compromise", "uncontrolled bleeding", 2, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_07_04", "airway_compromise", "uncontrolled bleeding", 3, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_07_05", "airway_compromise", "uncontrolled bleeding", 4, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_07_06", "airway_compromise", "uncontrolled bleeding", 5, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_07_07", "airway_compromise", "uncontrolled bleeding", 1, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_07_08", "airway_compromise", "uncontrolled bleeding", 2, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_07_09", "airway_compromise", "uncontrolled bleeding", 3, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_07_10", "airway_compromise", "uncontrolled bleeding", 4, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_07_11", "airway_compromise", "uncontrolled bleeding", 5, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_07_12", "airway_compromise", "uncontrolled bleeding", 1, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_07_13", "airway_compromise", "uncontrolled bleeding", 2, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_07_14", "airway_compromise", "uncontrolled bleeding", 3, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_07_15", "airway_compromise", "uncontrolled bleeding", 4, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_07_16", "airway_compromise", "uncontrolled bleeding", 5, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_07_17", "airway_compromise", "uncontrolled bleeding", 1, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_07_18", "airway_compromise", "uncontrolled bleeding", 2, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_07_19", "airway_compromise", "uncontrolled bleeding", 3, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_07_20", "airway_compromise", "uncontrolled bleeding", 4, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_07_21", "airway_compromise", "uncontrolled bleeding", 5, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_07_22", "airway_compromise", "uncontrolled bleeding", 1, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_07_23", "airway_compromise", "uncontrolled bleeding", 2, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_08_00", "airway_compromise", "minor sensitivity", 5, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_08_01", "airway_compromise", "minor sensitivity", 1, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_08_02", "airway_compromise", "minor sensitivity", 2, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_08_03", "airway_compromise", "minor sensitivity", 3, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_08_04", "airway_compromise", "minor sensitivity", 4, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_08_05", "airway_compromise", "minor sensitivity", 5, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_08_06", "airway_compromise", "minor sensitivity", 1, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_08_07", "airway_compromise", "minor sensitivity", 2, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_08_08", "airway_compromise", "minor sensitivity", 3, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_08_09", "airway_compromise", "minor sensitivity", 4, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_08_10", "airway_compromise", "minor sensitivity", 5, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_08_11", "airway_compromise", "minor sensitivity", 1, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_08_12", "airway_compromise", "minor sensitivity", 2, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_08_13", "airway_compromise", "minor sensitivity", 3, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_08_14", "airway_compromise", "minor sensitivity", 4, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_08_15", "airway_compromise", "minor sensitivity", 5, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_08_16", "airway_compromise", "minor sensitivity", 1, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_08_17", "airway_compromise", "minor sensitivity", 2, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_08_18", "airway_compromise", "minor sensitivity", 3, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_08_19", "airway_compromise", "minor sensitivity", 4, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_08_20", "airway_compromise", "minor sensitivity", 5, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_08_21", "airway_compromise", "minor sensitivity", 1, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_08_22", "airway_compromise", "minor sensitivity", 2, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_08_23", "airway_compromise", "minor sensitivity", 3, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_09_00", "airway_compromise", "preventive enquiry", 1, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_09_01", "airway_compromise", "preventive enquiry", 2, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_09_02", "airway_compromise", "preventive enquiry", 3, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_09_03", "airway_compromise", "preventive enquiry", 4, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_09_04", "airway_compromise", "preventive enquiry", 5, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_09_05", "airway_compromise", "preventive enquiry", 1, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_09_06", "airway_compromise", "preventive enquiry", 2, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_09_07", "airway_compromise", "preventive enquiry", 3, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_09_08", "airway_compromise", "preventive enquiry", 4, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_09_09", "airway_compromise", "preventive enquiry", 5, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_09_10", "airway_compromise", "preventive enquiry", 1, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_09_11", "airway_compromise", "preventive enquiry", 2, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_09_12", "airway_compromise", "preventive enquiry", 3, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_09_13", "airway_compromise", "preventive enquiry", 4, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_09_14", "airway_compromise", "preventive enquiry", 5, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_09_15", "airway_compromise", "preventive enquiry", 1, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_09_16", "airway_compromise", "preventive enquiry", 2, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_09_17", "airway_compromise", "preventive enquiry", 3, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_09_18", "airway_compromise", "preventive enquiry", 4, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_09_19", "airway_compromise", "preventive enquiry", 5, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_09_20", "airway_compromise", "preventive enquiry", 1, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_09_21", "airway_compromise", "preventive enquiry", 2, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_09_22", "airway_compromise", "preventive enquiry", 3, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_09_23", "airway_compromise", "preventive enquiry", 4, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_10_00", "airway_compromise", "facial asymmetry", 2, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_10_01", "airway_compromise", "facial asymmetry", 3, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_10_02", "airway_compromise", "facial asymmetry", 4, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_10_03", "airway_compromise", "facial asymmetry", 5, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_10_04", "airway_compromise", "facial asymmetry", 1, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_10_05", "airway_compromise", "facial asymmetry", 2, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_10_06", "airway_compromise", "facial asymmetry", 3, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_10_07", "airway_compromise", "facial asymmetry", 4, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_10_08", "airway_compromise", "facial asymmetry", 5, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_10_09", "airway_compromise", "facial asymmetry", 1, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_10_10", "airway_compromise", "facial asymmetry", 2, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_10_11", "airway_compromise", "facial asymmetry", 3, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_10_12", "airway_compromise", "facial asymmetry", 4, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_10_13", "airway_compromise", "facial asymmetry", 5, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_10_14", "airway_compromise", "facial asymmetry", 1, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_10_15", "airway_compromise", "facial asymmetry", 2, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_10_16", "airway_compromise", "facial asymmetry", 3, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_10_17", "airway_compromise", "facial asymmetry", 4, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_10_18", "airway_compromise", "facial asymmetry", 5, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_10_19", "airway_compromise", "facial asymmetry", 1, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_10_20", "airway_compromise", "facial asymmetry", 2, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_10_21", "airway_compromise", "facial asymmetry", 3, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_10_22", "airway_compromise", "facial asymmetry", 4, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_10_23", "airway_compromise", "facial asymmetry", 5, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_11_00", "airway_compromise", "floor of mouth elevation", 3, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_11_01", "airway_compromise", "floor of mouth elevation", 4, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_11_02", "airway_compromise", "floor of mouth elevation", 5, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_11_03", "airway_compromise", "floor of mouth elevation", 1, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_11_04", "airway_compromise", "floor of mouth elevation", 2, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_11_05", "airway_compromise", "floor of mouth elevation", 3, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_11_06", "airway_compromise", "floor of mouth elevation", 4, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_11_07", "airway_compromise", "floor of mouth elevation", 5, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_11_08", "airway_compromise", "floor of mouth elevation", 1, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_11_09", "airway_compromise", "floor of mouth elevation", 2, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_11_10", "airway_compromise", "floor of mouth elevation", 3, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_11_11", "airway_compromise", "floor of mouth elevation", 4, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_11_12", "airway_compromise", "floor of mouth elevation", 5, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_11_13", "airway_compromise", "floor of mouth elevation", 1, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_11_14", "airway_compromise", "floor of mouth elevation", 2, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_11_15", "airway_compromise", "floor of mouth elevation", 3, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_11_16", "airway_compromise", "floor of mouth elevation", 4, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_11_17", "airway_compromise", "floor of mouth elevation", 5, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_11_18", "airway_compromise", "floor of mouth elevation", 1, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_11_19", "airway_compromise", "floor of mouth elevation", 2, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_11_20", "airway_compromise", "floor of mouth elevation", 3, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_11_21", "airway_compromise", "floor of mouth elevation", 4, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_11_22", "airway_compromise", "floor of mouth elevation", 5, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_11_23", "airway_compromise", "floor of mouth elevation", 1, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_12_00", "airway_compromise", "tongue displacement", 4, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_12_01", "airway_compromise", "tongue displacement", 5, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_12_02", "airway_compromise", "tongue displacement", 1, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_12_03", "airway_compromise", "tongue displacement", 2, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_12_04", "airway_compromise", "tongue displacement", 3, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_12_05", "airway_compromise", "tongue displacement", 4, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_12_06", "airway_compromise", "tongue displacement", 5, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_12_07", "airway_compromise", "tongue displacement", 1, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_12_08", "airway_compromise", "tongue displacement", 2, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_12_09", "airway_compromise", "tongue displacement", 3, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_12_10", "airway_compromise", "tongue displacement", 4, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_12_11", "airway_compromise", "tongue displacement", 5, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_12_12", "airway_compromise", "tongue displacement", 1, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_12_13", "airway_compromise", "tongue displacement", 2, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_12_14", "airway_compromise", "tongue displacement", 3, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_12_15", "airway_compromise", "tongue displacement", 4, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_12_16", "airway_compromise", "tongue displacement", 5, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_12_17", "airway_compromise", "tongue displacement", 1, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_12_18", "airway_compromise", "tongue displacement", 2, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_12_19", "airway_compromise", "tongue displacement", 3, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_12_20", "airway_compromise", "tongue displacement", 4, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_12_21", "airway_compromise", "tongue displacement", 5, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_12_22", "airway_compromise", "tongue displacement", 1, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_12_23", "airway_compromise", "tongue displacement", 2, "AAE", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_13_00", "airway_compromise", "slow progression", 5, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_13_01", "airway_compromise", "slow progression", 1, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_13_02", "airway_compromise", "slow progression", 2, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_13_03", "airway_compromise", "slow progression", 3, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_13_04", "airway_compromise", "slow progression", 4, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_13_05", "airway_compromise", "slow progression", 5, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_13_06", "airway_compromise", "slow progression", 1, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_13_07", "airway_compromise", "slow progression", 2, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_13_08", "airway_compromise", "slow progression", 3, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_13_09", "airway_compromise", "slow progression", 4, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_13_10", "airway_compromise", "slow progression", 5, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_13_11", "airway_compromise", "slow progression", 1, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_13_12", "airway_compromise", "slow progression", 2, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_13_13", "airway_compromise", "slow progression", 3, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_13_14", "airway_compromise", "slow progression", 4, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_13_15", "airway_compromise", "slow progression", 5, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_13_16", "airway_compromise", "slow progression", 1, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_13_17", "airway_compromise", "slow progression", 2, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_13_18", "airway_compromise", "slow progression", 3, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_13_19", "airway_compromise", "slow progression", 4, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_13_20", "airway_compromise", "slow progression", 5, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_13_21", "airway_compromise", "slow progression", 1, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_13_22", "airway_compromise", "slow progression", 2, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_13_23", "airway_compromise", "slow progression", 3, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_14_00", "airway_compromise", "rapid progression", 1, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_14_01", "airway_compromise", "rapid progression", 2, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_14_02", "airway_compromise", "rapid progression", 3, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_14_03", "airway_compromise", "rapid progression", 4, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_14_04", "airway_compromise", "rapid progression", 5, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_14_05", "airway_compromise", "rapid progression", 1, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_14_06", "airway_compromise", "rapid progression", 2, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_14_07", "airway_compromise", "rapid progression", 3, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_14_08", "airway_compromise", "rapid progression", 4, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_14_09", "airway_compromise", "rapid progression", 5, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_14_10", "airway_compromise", "rapid progression", 1, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_14_11", "airway_compromise", "rapid progression", 2, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_14_12", "airway_compromise", "rapid progression", 3, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_14_13", "airway_compromise", "rapid progression", 4, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_14_14", "airway_compromise", "rapid progression", 5, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_14_15", "airway_compromise", "rapid progression", 1, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_14_16", "airway_compromise", "rapid progression", 2, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_14_17", "airway_compromise", "rapid progression", 3, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_14_18", "airway_compromise", "rapid progression", 4, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_14_19", "airway_compromise", "rapid progression", 5, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_14_20", "airway_compromise", "rapid progression", 1, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_14_21", "airway_compromise", "rapid progression", 2, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_14_22", "airway_compromise", "rapid progression", 3, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_14_23", "airway_compromise", "rapid progression", 4, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_15_00", "airway_compromise", "attenuated inflammation", 2, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_15_01", "airway_compromise", "attenuated inflammation", 3, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_15_02", "airway_compromise", "attenuated inflammation", 4, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_15_03", "airway_compromise", "attenuated inflammation", 5, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_15_04", "airway_compromise", "attenuated inflammation", 1, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_15_05", "airway_compromise", "attenuated inflammation", 2, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_15_06", "airway_compromise", "attenuated inflammation", 3, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_15_07", "airway_compromise", "attenuated inflammation", 4, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_15_08", "airway_compromise", "attenuated inflammation", 5, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_15_09", "airway_compromise", "attenuated inflammation", 1, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_15_10", "airway_compromise", "attenuated inflammation", 2, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_15_11", "airway_compromise", "attenuated inflammation", 3, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_15_12", "airway_compromise", "attenuated inflammation", 4, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_15_13", "airway_compromise", "attenuated inflammation", 5, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_15_14", "airway_compromise", "attenuated inflammation", 1, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_15_15", "airway_compromise", "attenuated inflammation", 2, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_15_16", "airway_compromise", "attenuated inflammation", 3, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_15_17", "airway_compromise", "attenuated inflammation", 4, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_15_18", "airway_compromise", "attenuated inflammation", 5, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_15_19", "airway_compromise", "attenuated inflammation", 1, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_15_20", "airway_compromise", "attenuated inflammation", 2, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_15_21", "airway_compromise", "attenuated inflammation", 3, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_15_22", "airway_compromise", "attenuated inflammation", 4, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_15_23", "airway_compromise", "attenuated inflammation", 5, "AAPD", "D7"
    ),
    ClinicalSignal("airway_compromise_16_00", "airway_compromise", "delayed onset", 3, "AAE", "D7"),
    ClinicalSignal("airway_compromise_16_01", "airway_compromise", "delayed onset", 4, "AAE", "D7"),
    ClinicalSignal("airway_compromise_16_02", "airway_compromise", "delayed onset", 5, "AAE", "D7"),
    ClinicalSignal("airway_compromise_16_03", "airway_compromise", "delayed onset", 1, "AAE", "D7"),
    ClinicalSignal("airway_compromise_16_04", "airway_compromise", "delayed onset", 2, "AAE", "D7"),
    ClinicalSignal("airway_compromise_16_05", "airway_compromise", "delayed onset", 3, "AAE", "D7"),
    ClinicalSignal("airway_compromise_16_06", "airway_compromise", "delayed onset", 4, "AAE", "D7"),
    ClinicalSignal("airway_compromise_16_07", "airway_compromise", "delayed onset", 5, "AAE", "D7"),
    ClinicalSignal("airway_compromise_16_08", "airway_compromise", "delayed onset", 1, "AAE", "D7"),
    ClinicalSignal("airway_compromise_16_09", "airway_compromise", "delayed onset", 2, "AAE", "D7"),
    ClinicalSignal("airway_compromise_16_10", "airway_compromise", "delayed onset", 3, "AAE", "D7"),
    ClinicalSignal("airway_compromise_16_11", "airway_compromise", "delayed onset", 4, "AAE", "D7"),
    ClinicalSignal("airway_compromise_16_12", "airway_compromise", "delayed onset", 5, "AAE", "D7"),
    ClinicalSignal("airway_compromise_16_13", "airway_compromise", "delayed onset", 1, "AAE", "D7"),
    ClinicalSignal("airway_compromise_16_14", "airway_compromise", "delayed onset", 2, "AAE", "D7"),
    ClinicalSignal("airway_compromise_16_15", "airway_compromise", "delayed onset", 3, "AAE", "D7"),
    ClinicalSignal("airway_compromise_16_16", "airway_compromise", "delayed onset", 4, "AAE", "D7"),
    ClinicalSignal("airway_compromise_16_17", "airway_compromise", "delayed onset", 5, "AAE", "D7"),
    ClinicalSignal("airway_compromise_16_18", "airway_compromise", "delayed onset", 1, "AAE", "D7"),
    ClinicalSignal("airway_compromise_16_19", "airway_compromise", "delayed onset", 2, "AAE", "D7"),
    ClinicalSignal("airway_compromise_16_20", "airway_compromise", "delayed onset", 3, "AAE", "D7"),
    ClinicalSignal("airway_compromise_16_21", "airway_compromise", "delayed onset", 4, "AAE", "D7"),
    ClinicalSignal("airway_compromise_16_22", "airway_compromise", "delayed onset", 5, "AAE", "D7"),
    ClinicalSignal("airway_compromise_16_23", "airway_compromise", "delayed onset", 1, "AAE", "D7"),
    ClinicalSignal(
        "airway_compromise_17_00", "airway_compromise", "medical vulnerability", 4, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_17_01", "airway_compromise", "medical vulnerability", 5, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_17_02", "airway_compromise", "medical vulnerability", 1, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_17_03", "airway_compromise", "medical vulnerability", 2, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_17_04", "airway_compromise", "medical vulnerability", 3, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_17_05", "airway_compromise", "medical vulnerability", 4, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_17_06", "airway_compromise", "medical vulnerability", 5, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_17_07", "airway_compromise", "medical vulnerability", 1, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_17_08", "airway_compromise", "medical vulnerability", 2, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_17_09", "airway_compromise", "medical vulnerability", 3, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_17_10", "airway_compromise", "medical vulnerability", 4, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_17_11", "airway_compromise", "medical vulnerability", 5, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_17_12", "airway_compromise", "medical vulnerability", 1, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_17_13", "airway_compromise", "medical vulnerability", 2, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_17_14", "airway_compromise", "medical vulnerability", 3, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_17_15", "airway_compromise", "medical vulnerability", 4, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_17_16", "airway_compromise", "medical vulnerability", 5, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_17_17", "airway_compromise", "medical vulnerability", 1, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_17_18", "airway_compromise", "medical vulnerability", 2, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_17_19", "airway_compromise", "medical vulnerability", 3, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_17_20", "airway_compromise", "medical vulnerability", 4, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_17_21", "airway_compromise", "medical vulnerability", 5, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_17_22", "airway_compromise", "medical vulnerability", 1, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_17_23", "airway_compromise", "medical vulnerability", 2, "IADT", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_18_00", "airway_compromise", "controlled symptoms", 5, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_18_01", "airway_compromise", "controlled symptoms", 1, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_18_02", "airway_compromise", "controlled symptoms", 2, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_18_03", "airway_compromise", "controlled symptoms", 3, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_18_04", "airway_compromise", "controlled symptoms", 4, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_18_05", "airway_compromise", "controlled symptoms", 5, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_18_06", "airway_compromise", "controlled symptoms", 1, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_18_07", "airway_compromise", "controlled symptoms", 2, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_18_08", "airway_compromise", "controlled symptoms", 3, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_18_09", "airway_compromise", "controlled symptoms", 4, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_18_10", "airway_compromise", "controlled symptoms", 5, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_18_11", "airway_compromise", "controlled symptoms", 1, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_18_12", "airway_compromise", "controlled symptoms", 2, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_18_13", "airway_compromise", "controlled symptoms", 3, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_18_14", "airway_compromise", "controlled symptoms", 4, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_18_15", "airway_compromise", "controlled symptoms", 5, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_18_16", "airway_compromise", "controlled symptoms", 1, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_18_17", "airway_compromise", "controlled symptoms", 2, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_18_18", "airway_compromise", "controlled symptoms", 3, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_18_19", "airway_compromise", "controlled symptoms", 4, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_18_20", "airway_compromise", "controlled symptoms", 5, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_18_21", "airway_compromise", "controlled symptoms", 1, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_18_22", "airway_compromise", "controlled symptoms", 2, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_18_23", "airway_compromise", "controlled symptoms", 3, "ADA", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_19_00", "airway_compromise", "systemic illness", 1, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_19_01", "airway_compromise", "systemic illness", 2, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_19_02", "airway_compromise", "systemic illness", 3, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_19_03", "airway_compromise", "systemic illness", 4, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_19_04", "airway_compromise", "systemic illness", 5, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_19_05", "airway_compromise", "systemic illness", 1, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_19_06", "airway_compromise", "systemic illness", 2, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_19_07", "airway_compromise", "systemic illness", 3, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_19_08", "airway_compromise", "systemic illness", 4, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_19_09", "airway_compromise", "systemic illness", 5, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_19_10", "airway_compromise", "systemic illness", 1, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_19_11", "airway_compromise", "systemic illness", 2, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_19_12", "airway_compromise", "systemic illness", 3, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_19_13", "airway_compromise", "systemic illness", 4, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_19_14", "airway_compromise", "systemic illness", 5, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_19_15", "airway_compromise", "systemic illness", 1, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_19_16", "airway_compromise", "systemic illness", 2, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_19_17", "airway_compromise", "systemic illness", 3, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_19_18", "airway_compromise", "systemic illness", 4, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_19_19", "airway_compromise", "systemic illness", 5, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_19_20", "airway_compromise", "systemic illness", 1, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_19_21", "airway_compromise", "systemic illness", 2, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_19_22", "airway_compromise", "systemic illness", 3, "AAPD", "D7"
    ),
    ClinicalSignal(
        "airway_compromise_19_23", "airway_compromise", "systemic illness", 4, "AAPD", "D7"
    ),
    ClinicalSignal(
        "post_procedural_bleeding_00_00",
        "post_procedural_bleeding",
        "localised swelling",
        3,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_00_01",
        "post_procedural_bleeding",
        "localised swelling",
        4,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_00_02",
        "post_procedural_bleeding",
        "localised swelling",
        5,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_00_03",
        "post_procedural_bleeding",
        "localised swelling",
        1,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_00_04",
        "post_procedural_bleeding",
        "localised swelling",
        2,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_00_05",
        "post_procedural_bleeding",
        "localised swelling",
        3,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_00_06",
        "post_procedural_bleeding",
        "localised swelling",
        4,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_00_07",
        "post_procedural_bleeding",
        "localised swelling",
        5,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_00_08",
        "post_procedural_bleeding",
        "localised swelling",
        1,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_00_09",
        "post_procedural_bleeding",
        "localised swelling",
        2,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_00_10",
        "post_procedural_bleeding",
        "localised swelling",
        3,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_00_11",
        "post_procedural_bleeding",
        "localised swelling",
        4,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_00_12",
        "post_procedural_bleeding",
        "localised swelling",
        5,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_00_13",
        "post_procedural_bleeding",
        "localised swelling",
        1,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_00_14",
        "post_procedural_bleeding",
        "localised swelling",
        2,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_00_15",
        "post_procedural_bleeding",
        "localised swelling",
        3,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_00_16",
        "post_procedural_bleeding",
        "localised swelling",
        4,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_00_17",
        "post_procedural_bleeding",
        "localised swelling",
        5,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_00_18",
        "post_procedural_bleeding",
        "localised swelling",
        1,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_00_19",
        "post_procedural_bleeding",
        "localised swelling",
        2,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_00_20",
        "post_procedural_bleeding",
        "localised swelling",
        3,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_00_21",
        "post_procedural_bleeding",
        "localised swelling",
        4,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_00_22",
        "post_procedural_bleeding",
        "localised swelling",
        5,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_00_23",
        "post_procedural_bleeding",
        "localised swelling",
        1,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_01_00",
        "post_procedural_bleeding",
        "progressive swelling",
        4,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_01_01",
        "post_procedural_bleeding",
        "progressive swelling",
        5,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_01_02",
        "post_procedural_bleeding",
        "progressive swelling",
        1,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_01_03",
        "post_procedural_bleeding",
        "progressive swelling",
        2,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_01_04",
        "post_procedural_bleeding",
        "progressive swelling",
        3,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_01_05",
        "post_procedural_bleeding",
        "progressive swelling",
        4,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_01_06",
        "post_procedural_bleeding",
        "progressive swelling",
        5,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_01_07",
        "post_procedural_bleeding",
        "progressive swelling",
        1,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_01_08",
        "post_procedural_bleeding",
        "progressive swelling",
        2,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_01_09",
        "post_procedural_bleeding",
        "progressive swelling",
        3,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_01_10",
        "post_procedural_bleeding",
        "progressive swelling",
        4,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_01_11",
        "post_procedural_bleeding",
        "progressive swelling",
        5,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_01_12",
        "post_procedural_bleeding",
        "progressive swelling",
        1,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_01_13",
        "post_procedural_bleeding",
        "progressive swelling",
        2,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_01_14",
        "post_procedural_bleeding",
        "progressive swelling",
        3,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_01_15",
        "post_procedural_bleeding",
        "progressive swelling",
        4,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_01_16",
        "post_procedural_bleeding",
        "progressive swelling",
        5,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_01_17",
        "post_procedural_bleeding",
        "progressive swelling",
        1,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_01_18",
        "post_procedural_bleeding",
        "progressive swelling",
        2,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_01_19",
        "post_procedural_bleeding",
        "progressive swelling",
        3,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_01_20",
        "post_procedural_bleeding",
        "progressive swelling",
        4,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_01_21",
        "post_procedural_bleeding",
        "progressive swelling",
        5,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_01_22",
        "post_procedural_bleeding",
        "progressive swelling",
        1,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_01_23",
        "post_procedural_bleeding",
        "progressive swelling",
        2,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_02_00",
        "post_procedural_bleeding",
        "moderate pain",
        5,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_02_01",
        "post_procedural_bleeding",
        "moderate pain",
        1,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_02_02",
        "post_procedural_bleeding",
        "moderate pain",
        2,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_02_03",
        "post_procedural_bleeding",
        "moderate pain",
        3,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_02_04",
        "post_procedural_bleeding",
        "moderate pain",
        4,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_02_05",
        "post_procedural_bleeding",
        "moderate pain",
        5,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_02_06",
        "post_procedural_bleeding",
        "moderate pain",
        1,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_02_07",
        "post_procedural_bleeding",
        "moderate pain",
        2,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_02_08",
        "post_procedural_bleeding",
        "moderate pain",
        3,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_02_09",
        "post_procedural_bleeding",
        "moderate pain",
        4,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_02_10",
        "post_procedural_bleeding",
        "moderate pain",
        5,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_02_11",
        "post_procedural_bleeding",
        "moderate pain",
        1,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_02_12",
        "post_procedural_bleeding",
        "moderate pain",
        2,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_02_13",
        "post_procedural_bleeding",
        "moderate pain",
        3,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_02_14",
        "post_procedural_bleeding",
        "moderate pain",
        4,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_02_15",
        "post_procedural_bleeding",
        "moderate pain",
        5,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_02_16",
        "post_procedural_bleeding",
        "moderate pain",
        1,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_02_17",
        "post_procedural_bleeding",
        "moderate pain",
        2,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_02_18",
        "post_procedural_bleeding",
        "moderate pain",
        3,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_02_19",
        "post_procedural_bleeding",
        "moderate pain",
        4,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_02_20",
        "post_procedural_bleeding",
        "moderate pain",
        5,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_02_21",
        "post_procedural_bleeding",
        "moderate pain",
        1,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_02_22",
        "post_procedural_bleeding",
        "moderate pain",
        2,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_02_23",
        "post_procedural_bleeding",
        "moderate pain",
        3,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_03_00", "post_procedural_bleeding", "high fever", 1, "AAE", "D8"
    ),
    ClinicalSignal(
        "post_procedural_bleeding_03_01", "post_procedural_bleeding", "high fever", 2, "AAE", "D8"
    ),
    ClinicalSignal(
        "post_procedural_bleeding_03_02", "post_procedural_bleeding", "high fever", 3, "AAE", "D8"
    ),
    ClinicalSignal(
        "post_procedural_bleeding_03_03", "post_procedural_bleeding", "high fever", 4, "AAE", "D8"
    ),
    ClinicalSignal(
        "post_procedural_bleeding_03_04", "post_procedural_bleeding", "high fever", 5, "AAE", "D8"
    ),
    ClinicalSignal(
        "post_procedural_bleeding_03_05", "post_procedural_bleeding", "high fever", 1, "AAE", "D8"
    ),
    ClinicalSignal(
        "post_procedural_bleeding_03_06", "post_procedural_bleeding", "high fever", 2, "AAE", "D8"
    ),
    ClinicalSignal(
        "post_procedural_bleeding_03_07", "post_procedural_bleeding", "high fever", 3, "AAE", "D8"
    ),
    ClinicalSignal(
        "post_procedural_bleeding_03_08", "post_procedural_bleeding", "high fever", 4, "AAE", "D8"
    ),
    ClinicalSignal(
        "post_procedural_bleeding_03_09", "post_procedural_bleeding", "high fever", 5, "AAE", "D8"
    ),
    ClinicalSignal(
        "post_procedural_bleeding_03_10", "post_procedural_bleeding", "high fever", 1, "AAE", "D8"
    ),
    ClinicalSignal(
        "post_procedural_bleeding_03_11", "post_procedural_bleeding", "high fever", 2, "AAE", "D8"
    ),
    ClinicalSignal(
        "post_procedural_bleeding_03_12", "post_procedural_bleeding", "high fever", 3, "AAE", "D8"
    ),
    ClinicalSignal(
        "post_procedural_bleeding_03_13", "post_procedural_bleeding", "high fever", 4, "AAE", "D8"
    ),
    ClinicalSignal(
        "post_procedural_bleeding_03_14", "post_procedural_bleeding", "high fever", 5, "AAE", "D8"
    ),
    ClinicalSignal(
        "post_procedural_bleeding_03_15", "post_procedural_bleeding", "high fever", 1, "AAE", "D8"
    ),
    ClinicalSignal(
        "post_procedural_bleeding_03_16", "post_procedural_bleeding", "high fever", 2, "AAE", "D8"
    ),
    ClinicalSignal(
        "post_procedural_bleeding_03_17", "post_procedural_bleeding", "high fever", 3, "AAE", "D8"
    ),
    ClinicalSignal(
        "post_procedural_bleeding_03_18", "post_procedural_bleeding", "high fever", 4, "AAE", "D8"
    ),
    ClinicalSignal(
        "post_procedural_bleeding_03_19", "post_procedural_bleeding", "high fever", 5, "AAE", "D8"
    ),
    ClinicalSignal(
        "post_procedural_bleeding_03_20", "post_procedural_bleeding", "high fever", 1, "AAE", "D8"
    ),
    ClinicalSignal(
        "post_procedural_bleeding_03_21", "post_procedural_bleeding", "high fever", 2, "AAE", "D8"
    ),
    ClinicalSignal(
        "post_procedural_bleeding_03_22", "post_procedural_bleeding", "high fever", 3, "AAE", "D8"
    ),
    ClinicalSignal(
        "post_procedural_bleeding_03_23", "post_procedural_bleeding", "high fever", 4, "AAE", "D8"
    ),
    ClinicalSignal(
        "post_procedural_bleeding_04_00",
        "post_procedural_bleeding",
        "significant trismus",
        2,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_04_01",
        "post_procedural_bleeding",
        "significant trismus",
        3,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_04_02",
        "post_procedural_bleeding",
        "significant trismus",
        4,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_04_03",
        "post_procedural_bleeding",
        "significant trismus",
        5,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_04_04",
        "post_procedural_bleeding",
        "significant trismus",
        1,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_04_05",
        "post_procedural_bleeding",
        "significant trismus",
        2,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_04_06",
        "post_procedural_bleeding",
        "significant trismus",
        3,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_04_07",
        "post_procedural_bleeding",
        "significant trismus",
        4,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_04_08",
        "post_procedural_bleeding",
        "significant trismus",
        5,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_04_09",
        "post_procedural_bleeding",
        "significant trismus",
        1,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_04_10",
        "post_procedural_bleeding",
        "significant trismus",
        2,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_04_11",
        "post_procedural_bleeding",
        "significant trismus",
        3,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_04_12",
        "post_procedural_bleeding",
        "significant trismus",
        4,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_04_13",
        "post_procedural_bleeding",
        "significant trismus",
        5,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_04_14",
        "post_procedural_bleeding",
        "significant trismus",
        1,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_04_15",
        "post_procedural_bleeding",
        "significant trismus",
        2,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_04_16",
        "post_procedural_bleeding",
        "significant trismus",
        3,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_04_17",
        "post_procedural_bleeding",
        "significant trismus",
        4,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_04_18",
        "post_procedural_bleeding",
        "significant trismus",
        5,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_04_19",
        "post_procedural_bleeding",
        "significant trismus",
        1,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_04_20",
        "post_procedural_bleeding",
        "significant trismus",
        2,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_04_21",
        "post_procedural_bleeding",
        "significant trismus",
        3,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_04_22",
        "post_procedural_bleeding",
        "significant trismus",
        4,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_04_23",
        "post_procedural_bleeding",
        "significant trismus",
        5,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_05_00",
        "post_procedural_bleeding",
        "difficulty swallowing",
        3,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_05_01",
        "post_procedural_bleeding",
        "difficulty swallowing",
        4,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_05_02",
        "post_procedural_bleeding",
        "difficulty swallowing",
        5,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_05_03",
        "post_procedural_bleeding",
        "difficulty swallowing",
        1,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_05_04",
        "post_procedural_bleeding",
        "difficulty swallowing",
        2,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_05_05",
        "post_procedural_bleeding",
        "difficulty swallowing",
        3,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_05_06",
        "post_procedural_bleeding",
        "difficulty swallowing",
        4,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_05_07",
        "post_procedural_bleeding",
        "difficulty swallowing",
        5,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_05_08",
        "post_procedural_bleeding",
        "difficulty swallowing",
        1,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_05_09",
        "post_procedural_bleeding",
        "difficulty swallowing",
        2,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_05_10",
        "post_procedural_bleeding",
        "difficulty swallowing",
        3,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_05_11",
        "post_procedural_bleeding",
        "difficulty swallowing",
        4,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_05_12",
        "post_procedural_bleeding",
        "difficulty swallowing",
        5,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_05_13",
        "post_procedural_bleeding",
        "difficulty swallowing",
        1,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_05_14",
        "post_procedural_bleeding",
        "difficulty swallowing",
        2,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_05_15",
        "post_procedural_bleeding",
        "difficulty swallowing",
        3,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_05_16",
        "post_procedural_bleeding",
        "difficulty swallowing",
        4,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_05_17",
        "post_procedural_bleeding",
        "difficulty swallowing",
        5,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_05_18",
        "post_procedural_bleeding",
        "difficulty swallowing",
        1,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_05_19",
        "post_procedural_bleeding",
        "difficulty swallowing",
        2,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_05_20",
        "post_procedural_bleeding",
        "difficulty swallowing",
        3,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_05_21",
        "post_procedural_bleeding",
        "difficulty swallowing",
        4,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_05_22",
        "post_procedural_bleeding",
        "difficulty swallowing",
        5,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_05_23",
        "post_procedural_bleeding",
        "difficulty swallowing",
        1,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_06_00",
        "post_procedural_bleeding",
        "airway noise",
        4,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_06_01",
        "post_procedural_bleeding",
        "airway noise",
        5,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_06_02",
        "post_procedural_bleeding",
        "airway noise",
        1,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_06_03",
        "post_procedural_bleeding",
        "airway noise",
        2,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_06_04",
        "post_procedural_bleeding",
        "airway noise",
        3,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_06_05",
        "post_procedural_bleeding",
        "airway noise",
        4,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_06_06",
        "post_procedural_bleeding",
        "airway noise",
        5,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_06_07",
        "post_procedural_bleeding",
        "airway noise",
        1,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_06_08",
        "post_procedural_bleeding",
        "airway noise",
        2,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_06_09",
        "post_procedural_bleeding",
        "airway noise",
        3,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_06_10",
        "post_procedural_bleeding",
        "airway noise",
        4,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_06_11",
        "post_procedural_bleeding",
        "airway noise",
        5,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_06_12",
        "post_procedural_bleeding",
        "airway noise",
        1,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_06_13",
        "post_procedural_bleeding",
        "airway noise",
        2,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_06_14",
        "post_procedural_bleeding",
        "airway noise",
        3,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_06_15",
        "post_procedural_bleeding",
        "airway noise",
        4,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_06_16",
        "post_procedural_bleeding",
        "airway noise",
        5,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_06_17",
        "post_procedural_bleeding",
        "airway noise",
        1,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_06_18",
        "post_procedural_bleeding",
        "airway noise",
        2,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_06_19",
        "post_procedural_bleeding",
        "airway noise",
        3,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_06_20",
        "post_procedural_bleeding",
        "airway noise",
        4,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_06_21",
        "post_procedural_bleeding",
        "airway noise",
        5,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_06_22",
        "post_procedural_bleeding",
        "airway noise",
        1,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_06_23",
        "post_procedural_bleeding",
        "airway noise",
        2,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_07_00",
        "post_procedural_bleeding",
        "uncontrolled bleeding",
        5,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_07_01",
        "post_procedural_bleeding",
        "uncontrolled bleeding",
        1,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_07_02",
        "post_procedural_bleeding",
        "uncontrolled bleeding",
        2,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_07_03",
        "post_procedural_bleeding",
        "uncontrolled bleeding",
        3,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_07_04",
        "post_procedural_bleeding",
        "uncontrolled bleeding",
        4,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_07_05",
        "post_procedural_bleeding",
        "uncontrolled bleeding",
        5,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_07_06",
        "post_procedural_bleeding",
        "uncontrolled bleeding",
        1,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_07_07",
        "post_procedural_bleeding",
        "uncontrolled bleeding",
        2,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_07_08",
        "post_procedural_bleeding",
        "uncontrolled bleeding",
        3,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_07_09",
        "post_procedural_bleeding",
        "uncontrolled bleeding",
        4,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_07_10",
        "post_procedural_bleeding",
        "uncontrolled bleeding",
        5,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_07_11",
        "post_procedural_bleeding",
        "uncontrolled bleeding",
        1,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_07_12",
        "post_procedural_bleeding",
        "uncontrolled bleeding",
        2,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_07_13",
        "post_procedural_bleeding",
        "uncontrolled bleeding",
        3,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_07_14",
        "post_procedural_bleeding",
        "uncontrolled bleeding",
        4,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_07_15",
        "post_procedural_bleeding",
        "uncontrolled bleeding",
        5,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_07_16",
        "post_procedural_bleeding",
        "uncontrolled bleeding",
        1,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_07_17",
        "post_procedural_bleeding",
        "uncontrolled bleeding",
        2,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_07_18",
        "post_procedural_bleeding",
        "uncontrolled bleeding",
        3,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_07_19",
        "post_procedural_bleeding",
        "uncontrolled bleeding",
        4,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_07_20",
        "post_procedural_bleeding",
        "uncontrolled bleeding",
        5,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_07_21",
        "post_procedural_bleeding",
        "uncontrolled bleeding",
        1,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_07_22",
        "post_procedural_bleeding",
        "uncontrolled bleeding",
        2,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_07_23",
        "post_procedural_bleeding",
        "uncontrolled bleeding",
        3,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_08_00",
        "post_procedural_bleeding",
        "minor sensitivity",
        1,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_08_01",
        "post_procedural_bleeding",
        "minor sensitivity",
        2,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_08_02",
        "post_procedural_bleeding",
        "minor sensitivity",
        3,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_08_03",
        "post_procedural_bleeding",
        "minor sensitivity",
        4,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_08_04",
        "post_procedural_bleeding",
        "minor sensitivity",
        5,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_08_05",
        "post_procedural_bleeding",
        "minor sensitivity",
        1,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_08_06",
        "post_procedural_bleeding",
        "minor sensitivity",
        2,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_08_07",
        "post_procedural_bleeding",
        "minor sensitivity",
        3,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_08_08",
        "post_procedural_bleeding",
        "minor sensitivity",
        4,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_08_09",
        "post_procedural_bleeding",
        "minor sensitivity",
        5,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_08_10",
        "post_procedural_bleeding",
        "minor sensitivity",
        1,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_08_11",
        "post_procedural_bleeding",
        "minor sensitivity",
        2,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_08_12",
        "post_procedural_bleeding",
        "minor sensitivity",
        3,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_08_13",
        "post_procedural_bleeding",
        "minor sensitivity",
        4,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_08_14",
        "post_procedural_bleeding",
        "minor sensitivity",
        5,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_08_15",
        "post_procedural_bleeding",
        "minor sensitivity",
        1,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_08_16",
        "post_procedural_bleeding",
        "minor sensitivity",
        2,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_08_17",
        "post_procedural_bleeding",
        "minor sensitivity",
        3,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_08_18",
        "post_procedural_bleeding",
        "minor sensitivity",
        4,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_08_19",
        "post_procedural_bleeding",
        "minor sensitivity",
        5,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_08_20",
        "post_procedural_bleeding",
        "minor sensitivity",
        1,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_08_21",
        "post_procedural_bleeding",
        "minor sensitivity",
        2,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_08_22",
        "post_procedural_bleeding",
        "minor sensitivity",
        3,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_08_23",
        "post_procedural_bleeding",
        "minor sensitivity",
        4,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_09_00",
        "post_procedural_bleeding",
        "preventive enquiry",
        2,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_09_01",
        "post_procedural_bleeding",
        "preventive enquiry",
        3,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_09_02",
        "post_procedural_bleeding",
        "preventive enquiry",
        4,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_09_03",
        "post_procedural_bleeding",
        "preventive enquiry",
        5,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_09_04",
        "post_procedural_bleeding",
        "preventive enquiry",
        1,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_09_05",
        "post_procedural_bleeding",
        "preventive enquiry",
        2,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_09_06",
        "post_procedural_bleeding",
        "preventive enquiry",
        3,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_09_07",
        "post_procedural_bleeding",
        "preventive enquiry",
        4,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_09_08",
        "post_procedural_bleeding",
        "preventive enquiry",
        5,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_09_09",
        "post_procedural_bleeding",
        "preventive enquiry",
        1,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_09_10",
        "post_procedural_bleeding",
        "preventive enquiry",
        2,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_09_11",
        "post_procedural_bleeding",
        "preventive enquiry",
        3,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_09_12",
        "post_procedural_bleeding",
        "preventive enquiry",
        4,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_09_13",
        "post_procedural_bleeding",
        "preventive enquiry",
        5,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_09_14",
        "post_procedural_bleeding",
        "preventive enquiry",
        1,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_09_15",
        "post_procedural_bleeding",
        "preventive enquiry",
        2,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_09_16",
        "post_procedural_bleeding",
        "preventive enquiry",
        3,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_09_17",
        "post_procedural_bleeding",
        "preventive enquiry",
        4,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_09_18",
        "post_procedural_bleeding",
        "preventive enquiry",
        5,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_09_19",
        "post_procedural_bleeding",
        "preventive enquiry",
        1,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_09_20",
        "post_procedural_bleeding",
        "preventive enquiry",
        2,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_09_21",
        "post_procedural_bleeding",
        "preventive enquiry",
        3,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_09_22",
        "post_procedural_bleeding",
        "preventive enquiry",
        4,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_09_23",
        "post_procedural_bleeding",
        "preventive enquiry",
        5,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_10_00",
        "post_procedural_bleeding",
        "facial asymmetry",
        3,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_10_01",
        "post_procedural_bleeding",
        "facial asymmetry",
        4,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_10_02",
        "post_procedural_bleeding",
        "facial asymmetry",
        5,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_10_03",
        "post_procedural_bleeding",
        "facial asymmetry",
        1,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_10_04",
        "post_procedural_bleeding",
        "facial asymmetry",
        2,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_10_05",
        "post_procedural_bleeding",
        "facial asymmetry",
        3,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_10_06",
        "post_procedural_bleeding",
        "facial asymmetry",
        4,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_10_07",
        "post_procedural_bleeding",
        "facial asymmetry",
        5,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_10_08",
        "post_procedural_bleeding",
        "facial asymmetry",
        1,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_10_09",
        "post_procedural_bleeding",
        "facial asymmetry",
        2,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_10_10",
        "post_procedural_bleeding",
        "facial asymmetry",
        3,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_10_11",
        "post_procedural_bleeding",
        "facial asymmetry",
        4,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_10_12",
        "post_procedural_bleeding",
        "facial asymmetry",
        5,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_10_13",
        "post_procedural_bleeding",
        "facial asymmetry",
        1,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_10_14",
        "post_procedural_bleeding",
        "facial asymmetry",
        2,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_10_15",
        "post_procedural_bleeding",
        "facial asymmetry",
        3,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_10_16",
        "post_procedural_bleeding",
        "facial asymmetry",
        4,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_10_17",
        "post_procedural_bleeding",
        "facial asymmetry",
        5,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_10_18",
        "post_procedural_bleeding",
        "facial asymmetry",
        1,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_10_19",
        "post_procedural_bleeding",
        "facial asymmetry",
        2,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_10_20",
        "post_procedural_bleeding",
        "facial asymmetry",
        3,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_10_21",
        "post_procedural_bleeding",
        "facial asymmetry",
        4,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_10_22",
        "post_procedural_bleeding",
        "facial asymmetry",
        5,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_10_23",
        "post_procedural_bleeding",
        "facial asymmetry",
        1,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_11_00",
        "post_procedural_bleeding",
        "floor of mouth elevation",
        4,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_11_01",
        "post_procedural_bleeding",
        "floor of mouth elevation",
        5,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_11_02",
        "post_procedural_bleeding",
        "floor of mouth elevation",
        1,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_11_03",
        "post_procedural_bleeding",
        "floor of mouth elevation",
        2,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_11_04",
        "post_procedural_bleeding",
        "floor of mouth elevation",
        3,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_11_05",
        "post_procedural_bleeding",
        "floor of mouth elevation",
        4,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_11_06",
        "post_procedural_bleeding",
        "floor of mouth elevation",
        5,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_11_07",
        "post_procedural_bleeding",
        "floor of mouth elevation",
        1,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_11_08",
        "post_procedural_bleeding",
        "floor of mouth elevation",
        2,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_11_09",
        "post_procedural_bleeding",
        "floor of mouth elevation",
        3,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_11_10",
        "post_procedural_bleeding",
        "floor of mouth elevation",
        4,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_11_11",
        "post_procedural_bleeding",
        "floor of mouth elevation",
        5,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_11_12",
        "post_procedural_bleeding",
        "floor of mouth elevation",
        1,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_11_13",
        "post_procedural_bleeding",
        "floor of mouth elevation",
        2,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_11_14",
        "post_procedural_bleeding",
        "floor of mouth elevation",
        3,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_11_15",
        "post_procedural_bleeding",
        "floor of mouth elevation",
        4,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_11_16",
        "post_procedural_bleeding",
        "floor of mouth elevation",
        5,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_11_17",
        "post_procedural_bleeding",
        "floor of mouth elevation",
        1,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_11_18",
        "post_procedural_bleeding",
        "floor of mouth elevation",
        2,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_11_19",
        "post_procedural_bleeding",
        "floor of mouth elevation",
        3,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_11_20",
        "post_procedural_bleeding",
        "floor of mouth elevation",
        4,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_11_21",
        "post_procedural_bleeding",
        "floor of mouth elevation",
        5,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_11_22",
        "post_procedural_bleeding",
        "floor of mouth elevation",
        1,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_11_23",
        "post_procedural_bleeding",
        "floor of mouth elevation",
        2,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_12_00",
        "post_procedural_bleeding",
        "tongue displacement",
        5,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_12_01",
        "post_procedural_bleeding",
        "tongue displacement",
        1,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_12_02",
        "post_procedural_bleeding",
        "tongue displacement",
        2,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_12_03",
        "post_procedural_bleeding",
        "tongue displacement",
        3,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_12_04",
        "post_procedural_bleeding",
        "tongue displacement",
        4,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_12_05",
        "post_procedural_bleeding",
        "tongue displacement",
        5,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_12_06",
        "post_procedural_bleeding",
        "tongue displacement",
        1,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_12_07",
        "post_procedural_bleeding",
        "tongue displacement",
        2,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_12_08",
        "post_procedural_bleeding",
        "tongue displacement",
        3,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_12_09",
        "post_procedural_bleeding",
        "tongue displacement",
        4,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_12_10",
        "post_procedural_bleeding",
        "tongue displacement",
        5,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_12_11",
        "post_procedural_bleeding",
        "tongue displacement",
        1,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_12_12",
        "post_procedural_bleeding",
        "tongue displacement",
        2,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_12_13",
        "post_procedural_bleeding",
        "tongue displacement",
        3,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_12_14",
        "post_procedural_bleeding",
        "tongue displacement",
        4,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_12_15",
        "post_procedural_bleeding",
        "tongue displacement",
        5,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_12_16",
        "post_procedural_bleeding",
        "tongue displacement",
        1,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_12_17",
        "post_procedural_bleeding",
        "tongue displacement",
        2,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_12_18",
        "post_procedural_bleeding",
        "tongue displacement",
        3,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_12_19",
        "post_procedural_bleeding",
        "tongue displacement",
        4,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_12_20",
        "post_procedural_bleeding",
        "tongue displacement",
        5,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_12_21",
        "post_procedural_bleeding",
        "tongue displacement",
        1,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_12_22",
        "post_procedural_bleeding",
        "tongue displacement",
        2,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_12_23",
        "post_procedural_bleeding",
        "tongue displacement",
        3,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_13_00",
        "post_procedural_bleeding",
        "slow progression",
        1,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_13_01",
        "post_procedural_bleeding",
        "slow progression",
        2,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_13_02",
        "post_procedural_bleeding",
        "slow progression",
        3,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_13_03",
        "post_procedural_bleeding",
        "slow progression",
        4,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_13_04",
        "post_procedural_bleeding",
        "slow progression",
        5,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_13_05",
        "post_procedural_bleeding",
        "slow progression",
        1,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_13_06",
        "post_procedural_bleeding",
        "slow progression",
        2,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_13_07",
        "post_procedural_bleeding",
        "slow progression",
        3,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_13_08",
        "post_procedural_bleeding",
        "slow progression",
        4,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_13_09",
        "post_procedural_bleeding",
        "slow progression",
        5,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_13_10",
        "post_procedural_bleeding",
        "slow progression",
        1,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_13_11",
        "post_procedural_bleeding",
        "slow progression",
        2,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_13_12",
        "post_procedural_bleeding",
        "slow progression",
        3,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_13_13",
        "post_procedural_bleeding",
        "slow progression",
        4,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_13_14",
        "post_procedural_bleeding",
        "slow progression",
        5,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_13_15",
        "post_procedural_bleeding",
        "slow progression",
        1,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_13_16",
        "post_procedural_bleeding",
        "slow progression",
        2,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_13_17",
        "post_procedural_bleeding",
        "slow progression",
        3,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_13_18",
        "post_procedural_bleeding",
        "slow progression",
        4,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_13_19",
        "post_procedural_bleeding",
        "slow progression",
        5,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_13_20",
        "post_procedural_bleeding",
        "slow progression",
        1,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_13_21",
        "post_procedural_bleeding",
        "slow progression",
        2,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_13_22",
        "post_procedural_bleeding",
        "slow progression",
        3,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_13_23",
        "post_procedural_bleeding",
        "slow progression",
        4,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_14_00",
        "post_procedural_bleeding",
        "rapid progression",
        2,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_14_01",
        "post_procedural_bleeding",
        "rapid progression",
        3,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_14_02",
        "post_procedural_bleeding",
        "rapid progression",
        4,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_14_03",
        "post_procedural_bleeding",
        "rapid progression",
        5,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_14_04",
        "post_procedural_bleeding",
        "rapid progression",
        1,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_14_05",
        "post_procedural_bleeding",
        "rapid progression",
        2,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_14_06",
        "post_procedural_bleeding",
        "rapid progression",
        3,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_14_07",
        "post_procedural_bleeding",
        "rapid progression",
        4,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_14_08",
        "post_procedural_bleeding",
        "rapid progression",
        5,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_14_09",
        "post_procedural_bleeding",
        "rapid progression",
        1,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_14_10",
        "post_procedural_bleeding",
        "rapid progression",
        2,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_14_11",
        "post_procedural_bleeding",
        "rapid progression",
        3,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_14_12",
        "post_procedural_bleeding",
        "rapid progression",
        4,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_14_13",
        "post_procedural_bleeding",
        "rapid progression",
        5,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_14_14",
        "post_procedural_bleeding",
        "rapid progression",
        1,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_14_15",
        "post_procedural_bleeding",
        "rapid progression",
        2,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_14_16",
        "post_procedural_bleeding",
        "rapid progression",
        3,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_14_17",
        "post_procedural_bleeding",
        "rapid progression",
        4,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_14_18",
        "post_procedural_bleeding",
        "rapid progression",
        5,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_14_19",
        "post_procedural_bleeding",
        "rapid progression",
        1,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_14_20",
        "post_procedural_bleeding",
        "rapid progression",
        2,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_14_21",
        "post_procedural_bleeding",
        "rapid progression",
        3,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_14_22",
        "post_procedural_bleeding",
        "rapid progression",
        4,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_14_23",
        "post_procedural_bleeding",
        "rapid progression",
        5,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_15_00",
        "post_procedural_bleeding",
        "attenuated inflammation",
        3,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_15_01",
        "post_procedural_bleeding",
        "attenuated inflammation",
        4,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_15_02",
        "post_procedural_bleeding",
        "attenuated inflammation",
        5,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_15_03",
        "post_procedural_bleeding",
        "attenuated inflammation",
        1,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_15_04",
        "post_procedural_bleeding",
        "attenuated inflammation",
        2,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_15_05",
        "post_procedural_bleeding",
        "attenuated inflammation",
        3,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_15_06",
        "post_procedural_bleeding",
        "attenuated inflammation",
        4,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_15_07",
        "post_procedural_bleeding",
        "attenuated inflammation",
        5,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_15_08",
        "post_procedural_bleeding",
        "attenuated inflammation",
        1,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_15_09",
        "post_procedural_bleeding",
        "attenuated inflammation",
        2,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_15_10",
        "post_procedural_bleeding",
        "attenuated inflammation",
        3,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_15_11",
        "post_procedural_bleeding",
        "attenuated inflammation",
        4,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_15_12",
        "post_procedural_bleeding",
        "attenuated inflammation",
        5,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_15_13",
        "post_procedural_bleeding",
        "attenuated inflammation",
        1,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_15_14",
        "post_procedural_bleeding",
        "attenuated inflammation",
        2,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_15_15",
        "post_procedural_bleeding",
        "attenuated inflammation",
        3,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_15_16",
        "post_procedural_bleeding",
        "attenuated inflammation",
        4,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_15_17",
        "post_procedural_bleeding",
        "attenuated inflammation",
        5,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_15_18",
        "post_procedural_bleeding",
        "attenuated inflammation",
        1,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_15_19",
        "post_procedural_bleeding",
        "attenuated inflammation",
        2,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_15_20",
        "post_procedural_bleeding",
        "attenuated inflammation",
        3,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_15_21",
        "post_procedural_bleeding",
        "attenuated inflammation",
        4,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_15_22",
        "post_procedural_bleeding",
        "attenuated inflammation",
        5,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_15_23",
        "post_procedural_bleeding",
        "attenuated inflammation",
        1,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_16_00",
        "post_procedural_bleeding",
        "delayed onset",
        4,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_16_01",
        "post_procedural_bleeding",
        "delayed onset",
        5,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_16_02",
        "post_procedural_bleeding",
        "delayed onset",
        1,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_16_03",
        "post_procedural_bleeding",
        "delayed onset",
        2,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_16_04",
        "post_procedural_bleeding",
        "delayed onset",
        3,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_16_05",
        "post_procedural_bleeding",
        "delayed onset",
        4,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_16_06",
        "post_procedural_bleeding",
        "delayed onset",
        5,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_16_07",
        "post_procedural_bleeding",
        "delayed onset",
        1,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_16_08",
        "post_procedural_bleeding",
        "delayed onset",
        2,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_16_09",
        "post_procedural_bleeding",
        "delayed onset",
        3,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_16_10",
        "post_procedural_bleeding",
        "delayed onset",
        4,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_16_11",
        "post_procedural_bleeding",
        "delayed onset",
        5,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_16_12",
        "post_procedural_bleeding",
        "delayed onset",
        1,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_16_13",
        "post_procedural_bleeding",
        "delayed onset",
        2,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_16_14",
        "post_procedural_bleeding",
        "delayed onset",
        3,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_16_15",
        "post_procedural_bleeding",
        "delayed onset",
        4,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_16_16",
        "post_procedural_bleeding",
        "delayed onset",
        5,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_16_17",
        "post_procedural_bleeding",
        "delayed onset",
        1,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_16_18",
        "post_procedural_bleeding",
        "delayed onset",
        2,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_16_19",
        "post_procedural_bleeding",
        "delayed onset",
        3,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_16_20",
        "post_procedural_bleeding",
        "delayed onset",
        4,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_16_21",
        "post_procedural_bleeding",
        "delayed onset",
        5,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_16_22",
        "post_procedural_bleeding",
        "delayed onset",
        1,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_16_23",
        "post_procedural_bleeding",
        "delayed onset",
        2,
        "IADT",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_17_00",
        "post_procedural_bleeding",
        "medical vulnerability",
        5,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_17_01",
        "post_procedural_bleeding",
        "medical vulnerability",
        1,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_17_02",
        "post_procedural_bleeding",
        "medical vulnerability",
        2,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_17_03",
        "post_procedural_bleeding",
        "medical vulnerability",
        3,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_17_04",
        "post_procedural_bleeding",
        "medical vulnerability",
        4,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_17_05",
        "post_procedural_bleeding",
        "medical vulnerability",
        5,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_17_06",
        "post_procedural_bleeding",
        "medical vulnerability",
        1,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_17_07",
        "post_procedural_bleeding",
        "medical vulnerability",
        2,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_17_08",
        "post_procedural_bleeding",
        "medical vulnerability",
        3,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_17_09",
        "post_procedural_bleeding",
        "medical vulnerability",
        4,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_17_10",
        "post_procedural_bleeding",
        "medical vulnerability",
        5,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_17_11",
        "post_procedural_bleeding",
        "medical vulnerability",
        1,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_17_12",
        "post_procedural_bleeding",
        "medical vulnerability",
        2,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_17_13",
        "post_procedural_bleeding",
        "medical vulnerability",
        3,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_17_14",
        "post_procedural_bleeding",
        "medical vulnerability",
        4,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_17_15",
        "post_procedural_bleeding",
        "medical vulnerability",
        5,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_17_16",
        "post_procedural_bleeding",
        "medical vulnerability",
        1,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_17_17",
        "post_procedural_bleeding",
        "medical vulnerability",
        2,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_17_18",
        "post_procedural_bleeding",
        "medical vulnerability",
        3,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_17_19",
        "post_procedural_bleeding",
        "medical vulnerability",
        4,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_17_20",
        "post_procedural_bleeding",
        "medical vulnerability",
        5,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_17_21",
        "post_procedural_bleeding",
        "medical vulnerability",
        1,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_17_22",
        "post_procedural_bleeding",
        "medical vulnerability",
        2,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_17_23",
        "post_procedural_bleeding",
        "medical vulnerability",
        3,
        "ADA",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_18_00",
        "post_procedural_bleeding",
        "controlled symptoms",
        1,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_18_01",
        "post_procedural_bleeding",
        "controlled symptoms",
        2,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_18_02",
        "post_procedural_bleeding",
        "controlled symptoms",
        3,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_18_03",
        "post_procedural_bleeding",
        "controlled symptoms",
        4,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_18_04",
        "post_procedural_bleeding",
        "controlled symptoms",
        5,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_18_05",
        "post_procedural_bleeding",
        "controlled symptoms",
        1,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_18_06",
        "post_procedural_bleeding",
        "controlled symptoms",
        2,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_18_07",
        "post_procedural_bleeding",
        "controlled symptoms",
        3,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_18_08",
        "post_procedural_bleeding",
        "controlled symptoms",
        4,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_18_09",
        "post_procedural_bleeding",
        "controlled symptoms",
        5,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_18_10",
        "post_procedural_bleeding",
        "controlled symptoms",
        1,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_18_11",
        "post_procedural_bleeding",
        "controlled symptoms",
        2,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_18_12",
        "post_procedural_bleeding",
        "controlled symptoms",
        3,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_18_13",
        "post_procedural_bleeding",
        "controlled symptoms",
        4,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_18_14",
        "post_procedural_bleeding",
        "controlled symptoms",
        5,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_18_15",
        "post_procedural_bleeding",
        "controlled symptoms",
        1,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_18_16",
        "post_procedural_bleeding",
        "controlled symptoms",
        2,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_18_17",
        "post_procedural_bleeding",
        "controlled symptoms",
        3,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_18_18",
        "post_procedural_bleeding",
        "controlled symptoms",
        4,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_18_19",
        "post_procedural_bleeding",
        "controlled symptoms",
        5,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_18_20",
        "post_procedural_bleeding",
        "controlled symptoms",
        1,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_18_21",
        "post_procedural_bleeding",
        "controlled symptoms",
        2,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_18_22",
        "post_procedural_bleeding",
        "controlled symptoms",
        3,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_18_23",
        "post_procedural_bleeding",
        "controlled symptoms",
        4,
        "AAPD",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_19_00",
        "post_procedural_bleeding",
        "systemic illness",
        2,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_19_01",
        "post_procedural_bleeding",
        "systemic illness",
        3,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_19_02",
        "post_procedural_bleeding",
        "systemic illness",
        4,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_19_03",
        "post_procedural_bleeding",
        "systemic illness",
        5,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_19_04",
        "post_procedural_bleeding",
        "systemic illness",
        1,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_19_05",
        "post_procedural_bleeding",
        "systemic illness",
        2,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_19_06",
        "post_procedural_bleeding",
        "systemic illness",
        3,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_19_07",
        "post_procedural_bleeding",
        "systemic illness",
        4,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_19_08",
        "post_procedural_bleeding",
        "systemic illness",
        5,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_19_09",
        "post_procedural_bleeding",
        "systemic illness",
        1,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_19_10",
        "post_procedural_bleeding",
        "systemic illness",
        2,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_19_11",
        "post_procedural_bleeding",
        "systemic illness",
        3,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_19_12",
        "post_procedural_bleeding",
        "systemic illness",
        4,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_19_13",
        "post_procedural_bleeding",
        "systemic illness",
        5,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_19_14",
        "post_procedural_bleeding",
        "systemic illness",
        1,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_19_15",
        "post_procedural_bleeding",
        "systemic illness",
        2,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_19_16",
        "post_procedural_bleeding",
        "systemic illness",
        3,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_19_17",
        "post_procedural_bleeding",
        "systemic illness",
        4,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_19_18",
        "post_procedural_bleeding",
        "systemic illness",
        5,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_19_19",
        "post_procedural_bleeding",
        "systemic illness",
        1,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_19_20",
        "post_procedural_bleeding",
        "systemic illness",
        2,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_19_21",
        "post_procedural_bleeding",
        "systemic illness",
        3,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_19_22",
        "post_procedural_bleeding",
        "systemic illness",
        4,
        "AAE",
        "D8",
    ),
    ClinicalSignal(
        "post_procedural_bleeding_19_23",
        "post_procedural_bleeding",
        "systemic illness",
        5,
        "AAE",
        "D8",
    ),
    ClinicalSignal("red_herring_00_00", "red_herring", "localised swelling", 4, "ADA", "D9"),
    ClinicalSignal("red_herring_00_01", "red_herring", "localised swelling", 5, "ADA", "D9"),
    ClinicalSignal("red_herring_00_02", "red_herring", "localised swelling", 1, "ADA", "D9"),
    ClinicalSignal("red_herring_00_03", "red_herring", "localised swelling", 2, "ADA", "D9"),
    ClinicalSignal("red_herring_00_04", "red_herring", "localised swelling", 3, "ADA", "D9"),
    ClinicalSignal("red_herring_00_05", "red_herring", "localised swelling", 4, "ADA", "D9"),
    ClinicalSignal("red_herring_00_06", "red_herring", "localised swelling", 5, "ADA", "D9"),
    ClinicalSignal("red_herring_00_07", "red_herring", "localised swelling", 1, "ADA", "D9"),
    ClinicalSignal("red_herring_00_08", "red_herring", "localised swelling", 2, "ADA", "D9"),
    ClinicalSignal("red_herring_00_09", "red_herring", "localised swelling", 3, "ADA", "D9"),
    ClinicalSignal("red_herring_00_10", "red_herring", "localised swelling", 4, "ADA", "D9"),
    ClinicalSignal("red_herring_00_11", "red_herring", "localised swelling", 5, "ADA", "D9"),
    ClinicalSignal("red_herring_00_12", "red_herring", "localised swelling", 1, "ADA", "D9"),
    ClinicalSignal("red_herring_00_13", "red_herring", "localised swelling", 2, "ADA", "D9"),
    ClinicalSignal("red_herring_00_14", "red_herring", "localised swelling", 3, "ADA", "D9"),
    ClinicalSignal("red_herring_00_15", "red_herring", "localised swelling", 4, "ADA", "D9"),
    ClinicalSignal("red_herring_00_16", "red_herring", "localised swelling", 5, "ADA", "D9"),
    ClinicalSignal("red_herring_00_17", "red_herring", "localised swelling", 1, "ADA", "D9"),
    ClinicalSignal("red_herring_00_18", "red_herring", "localised swelling", 2, "ADA", "D9"),
    ClinicalSignal("red_herring_00_19", "red_herring", "localised swelling", 3, "ADA", "D9"),
    ClinicalSignal("red_herring_00_20", "red_herring", "localised swelling", 4, "ADA", "D9"),
    ClinicalSignal("red_herring_00_21", "red_herring", "localised swelling", 5, "ADA", "D9"),
    ClinicalSignal("red_herring_00_22", "red_herring", "localised swelling", 1, "ADA", "D9"),
    ClinicalSignal("red_herring_00_23", "red_herring", "localised swelling", 2, "ADA", "D9"),
    ClinicalSignal("red_herring_01_00", "red_herring", "progressive swelling", 5, "AAPD", "D9"),
    ClinicalSignal("red_herring_01_01", "red_herring", "progressive swelling", 1, "AAPD", "D9"),
    ClinicalSignal("red_herring_01_02", "red_herring", "progressive swelling", 2, "AAPD", "D9"),
    ClinicalSignal("red_herring_01_03", "red_herring", "progressive swelling", 3, "AAPD", "D9"),
    ClinicalSignal("red_herring_01_04", "red_herring", "progressive swelling", 4, "AAPD", "D9"),
    ClinicalSignal("red_herring_01_05", "red_herring", "progressive swelling", 5, "AAPD", "D9"),
    ClinicalSignal("red_herring_01_06", "red_herring", "progressive swelling", 1, "AAPD", "D9"),
    ClinicalSignal("red_herring_01_07", "red_herring", "progressive swelling", 2, "AAPD", "D9"),
    ClinicalSignal("red_herring_01_08", "red_herring", "progressive swelling", 3, "AAPD", "D9"),
    ClinicalSignal("red_herring_01_09", "red_herring", "progressive swelling", 4, "AAPD", "D9"),
    ClinicalSignal("red_herring_01_10", "red_herring", "progressive swelling", 5, "AAPD", "D9"),
    ClinicalSignal("red_herring_01_11", "red_herring", "progressive swelling", 1, "AAPD", "D9"),
    ClinicalSignal("red_herring_01_12", "red_herring", "progressive swelling", 2, "AAPD", "D9"),
    ClinicalSignal("red_herring_01_13", "red_herring", "progressive swelling", 3, "AAPD", "D9"),
    ClinicalSignal("red_herring_01_14", "red_herring", "progressive swelling", 4, "AAPD", "D9"),
    ClinicalSignal("red_herring_01_15", "red_herring", "progressive swelling", 5, "AAPD", "D9"),
    ClinicalSignal("red_herring_01_16", "red_herring", "progressive swelling", 1, "AAPD", "D9"),
    ClinicalSignal("red_herring_01_17", "red_herring", "progressive swelling", 2, "AAPD", "D9"),
    ClinicalSignal("red_herring_01_18", "red_herring", "progressive swelling", 3, "AAPD", "D9"),
    ClinicalSignal("red_herring_01_19", "red_herring", "progressive swelling", 4, "AAPD", "D9"),
    ClinicalSignal("red_herring_01_20", "red_herring", "progressive swelling", 5, "AAPD", "D9"),
    ClinicalSignal("red_herring_01_21", "red_herring", "progressive swelling", 1, "AAPD", "D9"),
    ClinicalSignal("red_herring_01_22", "red_herring", "progressive swelling", 2, "AAPD", "D9"),
    ClinicalSignal("red_herring_01_23", "red_herring", "progressive swelling", 3, "AAPD", "D9"),
    ClinicalSignal("red_herring_02_00", "red_herring", "moderate pain", 1, "AAE", "D9"),
    ClinicalSignal("red_herring_02_01", "red_herring", "moderate pain", 2, "AAE", "D9"),
    ClinicalSignal("red_herring_02_02", "red_herring", "moderate pain", 3, "AAE", "D9"),
    ClinicalSignal("red_herring_02_03", "red_herring", "moderate pain", 4, "AAE", "D9"),
    ClinicalSignal("red_herring_02_04", "red_herring", "moderate pain", 5, "AAE", "D9"),
    ClinicalSignal("red_herring_02_05", "red_herring", "moderate pain", 1, "AAE", "D9"),
    ClinicalSignal("red_herring_02_06", "red_herring", "moderate pain", 2, "AAE", "D9"),
    ClinicalSignal("red_herring_02_07", "red_herring", "moderate pain", 3, "AAE", "D9"),
    ClinicalSignal("red_herring_02_08", "red_herring", "moderate pain", 4, "AAE", "D9"),
    ClinicalSignal("red_herring_02_09", "red_herring", "moderate pain", 5, "AAE", "D9"),
    ClinicalSignal("red_herring_02_10", "red_herring", "moderate pain", 1, "AAE", "D9"),
    ClinicalSignal("red_herring_02_11", "red_herring", "moderate pain", 2, "AAE", "D9"),
    ClinicalSignal("red_herring_02_12", "red_herring", "moderate pain", 3, "AAE", "D9"),
    ClinicalSignal("red_herring_02_13", "red_herring", "moderate pain", 4, "AAE", "D9"),
    ClinicalSignal("red_herring_02_14", "red_herring", "moderate pain", 5, "AAE", "D9"),
    ClinicalSignal("red_herring_02_15", "red_herring", "moderate pain", 1, "AAE", "D9"),
    ClinicalSignal("red_herring_02_16", "red_herring", "moderate pain", 2, "AAE", "D9"),
    ClinicalSignal("red_herring_02_17", "red_herring", "moderate pain", 3, "AAE", "D9"),
    ClinicalSignal("red_herring_02_18", "red_herring", "moderate pain", 4, "AAE", "D9"),
    ClinicalSignal("red_herring_02_19", "red_herring", "moderate pain", 5, "AAE", "D9"),
    ClinicalSignal("red_herring_02_20", "red_herring", "moderate pain", 1, "AAE", "D9"),
    ClinicalSignal("red_herring_02_21", "red_herring", "moderate pain", 2, "AAE", "D9"),
    ClinicalSignal("red_herring_02_22", "red_herring", "moderate pain", 3, "AAE", "D9"),
    ClinicalSignal("red_herring_02_23", "red_herring", "moderate pain", 4, "AAE", "D9"),
    ClinicalSignal("red_herring_03_00", "red_herring", "high fever", 2, "IADT", "D9"),
    ClinicalSignal("red_herring_03_01", "red_herring", "high fever", 3, "IADT", "D9"),
    ClinicalSignal("red_herring_03_02", "red_herring", "high fever", 4, "IADT", "D9"),
    ClinicalSignal("red_herring_03_03", "red_herring", "high fever", 5, "IADT", "D9"),
    ClinicalSignal("red_herring_03_04", "red_herring", "high fever", 1, "IADT", "D9"),
    ClinicalSignal("red_herring_03_05", "red_herring", "high fever", 2, "IADT", "D9"),
    ClinicalSignal("red_herring_03_06", "red_herring", "high fever", 3, "IADT", "D9"),
    ClinicalSignal("red_herring_03_07", "red_herring", "high fever", 4, "IADT", "D9"),
    ClinicalSignal("red_herring_03_08", "red_herring", "high fever", 5, "IADT", "D9"),
    ClinicalSignal("red_herring_03_09", "red_herring", "high fever", 1, "IADT", "D9"),
    ClinicalSignal("red_herring_03_10", "red_herring", "high fever", 2, "IADT", "D9"),
    ClinicalSignal("red_herring_03_11", "red_herring", "high fever", 3, "IADT", "D9"),
    ClinicalSignal("red_herring_03_12", "red_herring", "high fever", 4, "IADT", "D9"),
    ClinicalSignal("red_herring_03_13", "red_herring", "high fever", 5, "IADT", "D9"),
    ClinicalSignal("red_herring_03_14", "red_herring", "high fever", 1, "IADT", "D9"),
    ClinicalSignal("red_herring_03_15", "red_herring", "high fever", 2, "IADT", "D9"),
    ClinicalSignal("red_herring_03_16", "red_herring", "high fever", 3, "IADT", "D9"),
    ClinicalSignal("red_herring_03_17", "red_herring", "high fever", 4, "IADT", "D9"),
    ClinicalSignal("red_herring_03_18", "red_herring", "high fever", 5, "IADT", "D9"),
    ClinicalSignal("red_herring_03_19", "red_herring", "high fever", 1, "IADT", "D9"),
    ClinicalSignal("red_herring_03_20", "red_herring", "high fever", 2, "IADT", "D9"),
    ClinicalSignal("red_herring_03_21", "red_herring", "high fever", 3, "IADT", "D9"),
    ClinicalSignal("red_herring_03_22", "red_herring", "high fever", 4, "IADT", "D9"),
    ClinicalSignal("red_herring_03_23", "red_herring", "high fever", 5, "IADT", "D9"),
    ClinicalSignal("red_herring_04_00", "red_herring", "significant trismus", 3, "ADA", "D9"),
    ClinicalSignal("red_herring_04_01", "red_herring", "significant trismus", 4, "ADA", "D9"),
    ClinicalSignal("red_herring_04_02", "red_herring", "significant trismus", 5, "ADA", "D9"),
    ClinicalSignal("red_herring_04_03", "red_herring", "significant trismus", 1, "ADA", "D9"),
    ClinicalSignal("red_herring_04_04", "red_herring", "significant trismus", 2, "ADA", "D9"),
    ClinicalSignal("red_herring_04_05", "red_herring", "significant trismus", 3, "ADA", "D9"),
    ClinicalSignal("red_herring_04_06", "red_herring", "significant trismus", 4, "ADA", "D9"),
    ClinicalSignal("red_herring_04_07", "red_herring", "significant trismus", 5, "ADA", "D9"),
    ClinicalSignal("red_herring_04_08", "red_herring", "significant trismus", 1, "ADA", "D9"),
    ClinicalSignal("red_herring_04_09", "red_herring", "significant trismus", 2, "ADA", "D9"),
    ClinicalSignal("red_herring_04_10", "red_herring", "significant trismus", 3, "ADA", "D9"),
    ClinicalSignal("red_herring_04_11", "red_herring", "significant trismus", 4, "ADA", "D9"),
    ClinicalSignal("red_herring_04_12", "red_herring", "significant trismus", 5, "ADA", "D9"),
    ClinicalSignal("red_herring_04_13", "red_herring", "significant trismus", 1, "ADA", "D9"),
    ClinicalSignal("red_herring_04_14", "red_herring", "significant trismus", 2, "ADA", "D9"),
    ClinicalSignal("red_herring_04_15", "red_herring", "significant trismus", 3, "ADA", "D9"),
    ClinicalSignal("red_herring_04_16", "red_herring", "significant trismus", 4, "ADA", "D9"),
    ClinicalSignal("red_herring_04_17", "red_herring", "significant trismus", 5, "ADA", "D9"),
    ClinicalSignal("red_herring_04_18", "red_herring", "significant trismus", 1, "ADA", "D9"),
    ClinicalSignal("red_herring_04_19", "red_herring", "significant trismus", 2, "ADA", "D9"),
    ClinicalSignal("red_herring_04_20", "red_herring", "significant trismus", 3, "ADA", "D9"),
    ClinicalSignal("red_herring_04_21", "red_herring", "significant trismus", 4, "ADA", "D9"),
    ClinicalSignal("red_herring_04_22", "red_herring", "significant trismus", 5, "ADA", "D9"),
    ClinicalSignal("red_herring_04_23", "red_herring", "significant trismus", 1, "ADA", "D9"),
    ClinicalSignal("red_herring_05_00", "red_herring", "difficulty swallowing", 4, "AAPD", "D9"),
    ClinicalSignal("red_herring_05_01", "red_herring", "difficulty swallowing", 5, "AAPD", "D9"),
    ClinicalSignal("red_herring_05_02", "red_herring", "difficulty swallowing", 1, "AAPD", "D9"),
    ClinicalSignal("red_herring_05_03", "red_herring", "difficulty swallowing", 2, "AAPD", "D9"),
    ClinicalSignal("red_herring_05_04", "red_herring", "difficulty swallowing", 3, "AAPD", "D9"),
    ClinicalSignal("red_herring_05_05", "red_herring", "difficulty swallowing", 4, "AAPD", "D9"),
    ClinicalSignal("red_herring_05_06", "red_herring", "difficulty swallowing", 5, "AAPD", "D9"),
    ClinicalSignal("red_herring_05_07", "red_herring", "difficulty swallowing", 1, "AAPD", "D9"),
    ClinicalSignal("red_herring_05_08", "red_herring", "difficulty swallowing", 2, "AAPD", "D9"),
    ClinicalSignal("red_herring_05_09", "red_herring", "difficulty swallowing", 3, "AAPD", "D9"),
    ClinicalSignal("red_herring_05_10", "red_herring", "difficulty swallowing", 4, "AAPD", "D9"),
    ClinicalSignal("red_herring_05_11", "red_herring", "difficulty swallowing", 5, "AAPD", "D9"),
    ClinicalSignal("red_herring_05_12", "red_herring", "difficulty swallowing", 1, "AAPD", "D9"),
    ClinicalSignal("red_herring_05_13", "red_herring", "difficulty swallowing", 2, "AAPD", "D9"),
    ClinicalSignal("red_herring_05_14", "red_herring", "difficulty swallowing", 3, "AAPD", "D9"),
    ClinicalSignal("red_herring_05_15", "red_herring", "difficulty swallowing", 4, "AAPD", "D9"),
    ClinicalSignal("red_herring_05_16", "red_herring", "difficulty swallowing", 5, "AAPD", "D9"),
    ClinicalSignal("red_herring_05_17", "red_herring", "difficulty swallowing", 1, "AAPD", "D9"),
    ClinicalSignal("red_herring_05_18", "red_herring", "difficulty swallowing", 2, "AAPD", "D9"),
    ClinicalSignal("red_herring_05_19", "red_herring", "difficulty swallowing", 3, "AAPD", "D9"),
    ClinicalSignal("red_herring_05_20", "red_herring", "difficulty swallowing", 4, "AAPD", "D9"),
    ClinicalSignal("red_herring_05_21", "red_herring", "difficulty swallowing", 5, "AAPD", "D9"),
    ClinicalSignal("red_herring_05_22", "red_herring", "difficulty swallowing", 1, "AAPD", "D9"),
    ClinicalSignal("red_herring_05_23", "red_herring", "difficulty swallowing", 2, "AAPD", "D9"),
    ClinicalSignal("red_herring_06_00", "red_herring", "airway noise", 5, "AAE", "D9"),
    ClinicalSignal("red_herring_06_01", "red_herring", "airway noise", 1, "AAE", "D9"),
    ClinicalSignal("red_herring_06_02", "red_herring", "airway noise", 2, "AAE", "D9"),
    ClinicalSignal("red_herring_06_03", "red_herring", "airway noise", 3, "AAE", "D9"),
    ClinicalSignal("red_herring_06_04", "red_herring", "airway noise", 4, "AAE", "D9"),
    ClinicalSignal("red_herring_06_05", "red_herring", "airway noise", 5, "AAE", "D9"),
    ClinicalSignal("red_herring_06_06", "red_herring", "airway noise", 1, "AAE", "D9"),
    ClinicalSignal("red_herring_06_07", "red_herring", "airway noise", 2, "AAE", "D9"),
    ClinicalSignal("red_herring_06_08", "red_herring", "airway noise", 3, "AAE", "D9"),
    ClinicalSignal("red_herring_06_09", "red_herring", "airway noise", 4, "AAE", "D9"),
    ClinicalSignal("red_herring_06_10", "red_herring", "airway noise", 5, "AAE", "D9"),
    ClinicalSignal("red_herring_06_11", "red_herring", "airway noise", 1, "AAE", "D9"),
    ClinicalSignal("red_herring_06_12", "red_herring", "airway noise", 2, "AAE", "D9"),
    ClinicalSignal("red_herring_06_13", "red_herring", "airway noise", 3, "AAE", "D9"),
    ClinicalSignal("red_herring_06_14", "red_herring", "airway noise", 4, "AAE", "D9"),
    ClinicalSignal("red_herring_06_15", "red_herring", "airway noise", 5, "AAE", "D9"),
    ClinicalSignal("red_herring_06_16", "red_herring", "airway noise", 1, "AAE", "D9"),
    ClinicalSignal("red_herring_06_17", "red_herring", "airway noise", 2, "AAE", "D9"),
    ClinicalSignal("red_herring_06_18", "red_herring", "airway noise", 3, "AAE", "D9"),
    ClinicalSignal("red_herring_06_19", "red_herring", "airway noise", 4, "AAE", "D9"),
    ClinicalSignal("red_herring_06_20", "red_herring", "airway noise", 5, "AAE", "D9"),
    ClinicalSignal("red_herring_06_21", "red_herring", "airway noise", 1, "AAE", "D9"),
    ClinicalSignal("red_herring_06_22", "red_herring", "airway noise", 2, "AAE", "D9"),
    ClinicalSignal("red_herring_06_23", "red_herring", "airway noise", 3, "AAE", "D9"),
    ClinicalSignal("red_herring_07_00", "red_herring", "uncontrolled bleeding", 1, "IADT", "D9"),
    ClinicalSignal("red_herring_07_01", "red_herring", "uncontrolled bleeding", 2, "IADT", "D9"),
    ClinicalSignal("red_herring_07_02", "red_herring", "uncontrolled bleeding", 3, "IADT", "D9"),
    ClinicalSignal("red_herring_07_03", "red_herring", "uncontrolled bleeding", 4, "IADT", "D9"),
    ClinicalSignal("red_herring_07_04", "red_herring", "uncontrolled bleeding", 5, "IADT", "D9"),
    ClinicalSignal("red_herring_07_05", "red_herring", "uncontrolled bleeding", 1, "IADT", "D9"),
    ClinicalSignal("red_herring_07_06", "red_herring", "uncontrolled bleeding", 2, "IADT", "D9"),
    ClinicalSignal("red_herring_07_07", "red_herring", "uncontrolled bleeding", 3, "IADT", "D9"),
    ClinicalSignal("red_herring_07_08", "red_herring", "uncontrolled bleeding", 4, "IADT", "D9"),
    ClinicalSignal("red_herring_07_09", "red_herring", "uncontrolled bleeding", 5, "IADT", "D9"),
    ClinicalSignal("red_herring_07_10", "red_herring", "uncontrolled bleeding", 1, "IADT", "D9"),
    ClinicalSignal("red_herring_07_11", "red_herring", "uncontrolled bleeding", 2, "IADT", "D9"),
    ClinicalSignal("red_herring_07_12", "red_herring", "uncontrolled bleeding", 3, "IADT", "D9"),
    ClinicalSignal("red_herring_07_13", "red_herring", "uncontrolled bleeding", 4, "IADT", "D9"),
    ClinicalSignal("red_herring_07_14", "red_herring", "uncontrolled bleeding", 5, "IADT", "D9"),
    ClinicalSignal("red_herring_07_15", "red_herring", "uncontrolled bleeding", 1, "IADT", "D9"),
    ClinicalSignal("red_herring_07_16", "red_herring", "uncontrolled bleeding", 2, "IADT", "D9"),
    ClinicalSignal("red_herring_07_17", "red_herring", "uncontrolled bleeding", 3, "IADT", "D9"),
    ClinicalSignal("red_herring_07_18", "red_herring", "uncontrolled bleeding", 4, "IADT", "D9"),
    ClinicalSignal("red_herring_07_19", "red_herring", "uncontrolled bleeding", 5, "IADT", "D9"),
    ClinicalSignal("red_herring_07_20", "red_herring", "uncontrolled bleeding", 1, "IADT", "D9"),
    ClinicalSignal("red_herring_07_21", "red_herring", "uncontrolled bleeding", 2, "IADT", "D9"),
    ClinicalSignal("red_herring_07_22", "red_herring", "uncontrolled bleeding", 3, "IADT", "D9"),
    ClinicalSignal("red_herring_07_23", "red_herring", "uncontrolled bleeding", 4, "IADT", "D9"),
    ClinicalSignal("red_herring_08_00", "red_herring", "minor sensitivity", 2, "ADA", "D9"),
    ClinicalSignal("red_herring_08_01", "red_herring", "minor sensitivity", 3, "ADA", "D9"),
    ClinicalSignal("red_herring_08_02", "red_herring", "minor sensitivity", 4, "ADA", "D9"),
    ClinicalSignal("red_herring_08_03", "red_herring", "minor sensitivity", 5, "ADA", "D9"),
    ClinicalSignal("red_herring_08_04", "red_herring", "minor sensitivity", 1, "ADA", "D9"),
    ClinicalSignal("red_herring_08_05", "red_herring", "minor sensitivity", 2, "ADA", "D9"),
    ClinicalSignal("red_herring_08_06", "red_herring", "minor sensitivity", 3, "ADA", "D9"),
    ClinicalSignal("red_herring_08_07", "red_herring", "minor sensitivity", 4, "ADA", "D9"),
    ClinicalSignal("red_herring_08_08", "red_herring", "minor sensitivity", 5, "ADA", "D9"),
    ClinicalSignal("red_herring_08_09", "red_herring", "minor sensitivity", 1, "ADA", "D9"),
    ClinicalSignal("red_herring_08_10", "red_herring", "minor sensitivity", 2, "ADA", "D9"),
    ClinicalSignal("red_herring_08_11", "red_herring", "minor sensitivity", 3, "ADA", "D9"),
    ClinicalSignal("red_herring_08_12", "red_herring", "minor sensitivity", 4, "ADA", "D9"),
    ClinicalSignal("red_herring_08_13", "red_herring", "minor sensitivity", 5, "ADA", "D9"),
    ClinicalSignal("red_herring_08_14", "red_herring", "minor sensitivity", 1, "ADA", "D9"),
    ClinicalSignal("red_herring_08_15", "red_herring", "minor sensitivity", 2, "ADA", "D9"),
    ClinicalSignal("red_herring_08_16", "red_herring", "minor sensitivity", 3, "ADA", "D9"),
    ClinicalSignal("red_herring_08_17", "red_herring", "minor sensitivity", 4, "ADA", "D9"),
    ClinicalSignal("red_herring_08_18", "red_herring", "minor sensitivity", 5, "ADA", "D9"),
    ClinicalSignal("red_herring_08_19", "red_herring", "minor sensitivity", 1, "ADA", "D9"),
    ClinicalSignal("red_herring_08_20", "red_herring", "minor sensitivity", 2, "ADA", "D9"),
    ClinicalSignal("red_herring_08_21", "red_herring", "minor sensitivity", 3, "ADA", "D9"),
    ClinicalSignal("red_herring_08_22", "red_herring", "minor sensitivity", 4, "ADA", "D9"),
    ClinicalSignal("red_herring_08_23", "red_herring", "minor sensitivity", 5, "ADA", "D9"),
    ClinicalSignal("red_herring_09_00", "red_herring", "preventive enquiry", 3, "AAPD", "D9"),
    ClinicalSignal("red_herring_09_01", "red_herring", "preventive enquiry", 4, "AAPD", "D9"),
    ClinicalSignal("red_herring_09_02", "red_herring", "preventive enquiry", 5, "AAPD", "D9"),
    ClinicalSignal("red_herring_09_03", "red_herring", "preventive enquiry", 1, "AAPD", "D9"),
    ClinicalSignal("red_herring_09_04", "red_herring", "preventive enquiry", 2, "AAPD", "D9"),
    ClinicalSignal("red_herring_09_05", "red_herring", "preventive enquiry", 3, "AAPD", "D9"),
    ClinicalSignal("red_herring_09_06", "red_herring", "preventive enquiry", 4, "AAPD", "D9"),
    ClinicalSignal("red_herring_09_07", "red_herring", "preventive enquiry", 5, "AAPD", "D9"),
    ClinicalSignal("red_herring_09_08", "red_herring", "preventive enquiry", 1, "AAPD", "D9"),
    ClinicalSignal("red_herring_09_09", "red_herring", "preventive enquiry", 2, "AAPD", "D9"),
    ClinicalSignal("red_herring_09_10", "red_herring", "preventive enquiry", 3, "AAPD", "D9"),
    ClinicalSignal("red_herring_09_11", "red_herring", "preventive enquiry", 4, "AAPD", "D9"),
    ClinicalSignal("red_herring_09_12", "red_herring", "preventive enquiry", 5, "AAPD", "D9"),
    ClinicalSignal("red_herring_09_13", "red_herring", "preventive enquiry", 1, "AAPD", "D9"),
    ClinicalSignal("red_herring_09_14", "red_herring", "preventive enquiry", 2, "AAPD", "D9"),
    ClinicalSignal("red_herring_09_15", "red_herring", "preventive enquiry", 3, "AAPD", "D9"),
    ClinicalSignal("red_herring_09_16", "red_herring", "preventive enquiry", 4, "AAPD", "D9"),
    ClinicalSignal("red_herring_09_17", "red_herring", "preventive enquiry", 5, "AAPD", "D9"),
    ClinicalSignal("red_herring_09_18", "red_herring", "preventive enquiry", 1, "AAPD", "D9"),
    ClinicalSignal("red_herring_09_19", "red_herring", "preventive enquiry", 2, "AAPD", "D9"),
    ClinicalSignal("red_herring_09_20", "red_herring", "preventive enquiry", 3, "AAPD", "D9"),
    ClinicalSignal("red_herring_09_21", "red_herring", "preventive enquiry", 4, "AAPD", "D9"),
    ClinicalSignal("red_herring_09_22", "red_herring", "preventive enquiry", 5, "AAPD", "D9"),
    ClinicalSignal("red_herring_09_23", "red_herring", "preventive enquiry", 1, "AAPD", "D9"),
    ClinicalSignal("red_herring_10_00", "red_herring", "facial asymmetry", 4, "AAE", "D9"),
    ClinicalSignal("red_herring_10_01", "red_herring", "facial asymmetry", 5, "AAE", "D9"),
    ClinicalSignal("red_herring_10_02", "red_herring", "facial asymmetry", 1, "AAE", "D9"),
    ClinicalSignal("red_herring_10_03", "red_herring", "facial asymmetry", 2, "AAE", "D9"),
    ClinicalSignal("red_herring_10_04", "red_herring", "facial asymmetry", 3, "AAE", "D9"),
    ClinicalSignal("red_herring_10_05", "red_herring", "facial asymmetry", 4, "AAE", "D9"),
    ClinicalSignal("red_herring_10_06", "red_herring", "facial asymmetry", 5, "AAE", "D9"),
    ClinicalSignal("red_herring_10_07", "red_herring", "facial asymmetry", 1, "AAE", "D9"),
    ClinicalSignal("red_herring_10_08", "red_herring", "facial asymmetry", 2, "AAE", "D9"),
    ClinicalSignal("red_herring_10_09", "red_herring", "facial asymmetry", 3, "AAE", "D9"),
    ClinicalSignal("red_herring_10_10", "red_herring", "facial asymmetry", 4, "AAE", "D9"),
    ClinicalSignal("red_herring_10_11", "red_herring", "facial asymmetry", 5, "AAE", "D9"),
    ClinicalSignal("red_herring_10_12", "red_herring", "facial asymmetry", 1, "AAE", "D9"),
    ClinicalSignal("red_herring_10_13", "red_herring", "facial asymmetry", 2, "AAE", "D9"),
    ClinicalSignal("red_herring_10_14", "red_herring", "facial asymmetry", 3, "AAE", "D9"),
    ClinicalSignal("red_herring_10_15", "red_herring", "facial asymmetry", 4, "AAE", "D9"),
    ClinicalSignal("red_herring_10_16", "red_herring", "facial asymmetry", 5, "AAE", "D9"),
    ClinicalSignal("red_herring_10_17", "red_herring", "facial asymmetry", 1, "AAE", "D9"),
    ClinicalSignal("red_herring_10_18", "red_herring", "facial asymmetry", 2, "AAE", "D9"),
    ClinicalSignal("red_herring_10_19", "red_herring", "facial asymmetry", 3, "AAE", "D9"),
    ClinicalSignal("red_herring_10_20", "red_herring", "facial asymmetry", 4, "AAE", "D9"),
    ClinicalSignal("red_herring_10_21", "red_herring", "facial asymmetry", 5, "AAE", "D9"),
    ClinicalSignal("red_herring_10_22", "red_herring", "facial asymmetry", 1, "AAE", "D9"),
    ClinicalSignal("red_herring_10_23", "red_herring", "facial asymmetry", 2, "AAE", "D9"),
    ClinicalSignal("red_herring_11_00", "red_herring", "floor of mouth elevation", 5, "IADT", "D9"),
    ClinicalSignal("red_herring_11_01", "red_herring", "floor of mouth elevation", 1, "IADT", "D9"),
    ClinicalSignal("red_herring_11_02", "red_herring", "floor of mouth elevation", 2, "IADT", "D9"),
    ClinicalSignal("red_herring_11_03", "red_herring", "floor of mouth elevation", 3, "IADT", "D9"),
    ClinicalSignal("red_herring_11_04", "red_herring", "floor of mouth elevation", 4, "IADT", "D9"),
    ClinicalSignal("red_herring_11_05", "red_herring", "floor of mouth elevation", 5, "IADT", "D9"),
    ClinicalSignal("red_herring_11_06", "red_herring", "floor of mouth elevation", 1, "IADT", "D9"),
    ClinicalSignal("red_herring_11_07", "red_herring", "floor of mouth elevation", 2, "IADT", "D9"),
    ClinicalSignal("red_herring_11_08", "red_herring", "floor of mouth elevation", 3, "IADT", "D9"),
    ClinicalSignal("red_herring_11_09", "red_herring", "floor of mouth elevation", 4, "IADT", "D9"),
    ClinicalSignal("red_herring_11_10", "red_herring", "floor of mouth elevation", 5, "IADT", "D9"),
    ClinicalSignal("red_herring_11_11", "red_herring", "floor of mouth elevation", 1, "IADT", "D9"),
    ClinicalSignal("red_herring_11_12", "red_herring", "floor of mouth elevation", 2, "IADT", "D9"),
    ClinicalSignal("red_herring_11_13", "red_herring", "floor of mouth elevation", 3, "IADT", "D9"),
    ClinicalSignal("red_herring_11_14", "red_herring", "floor of mouth elevation", 4, "IADT", "D9"),
    ClinicalSignal("red_herring_11_15", "red_herring", "floor of mouth elevation", 5, "IADT", "D9"),
    ClinicalSignal("red_herring_11_16", "red_herring", "floor of mouth elevation", 1, "IADT", "D9"),
    ClinicalSignal("red_herring_11_17", "red_herring", "floor of mouth elevation", 2, "IADT", "D9"),
    ClinicalSignal("red_herring_11_18", "red_herring", "floor of mouth elevation", 3, "IADT", "D9"),
    ClinicalSignal("red_herring_11_19", "red_herring", "floor of mouth elevation", 4, "IADT", "D9"),
    ClinicalSignal("red_herring_11_20", "red_herring", "floor of mouth elevation", 5, "IADT", "D9"),
    ClinicalSignal("red_herring_11_21", "red_herring", "floor of mouth elevation", 1, "IADT", "D9"),
    ClinicalSignal("red_herring_11_22", "red_herring", "floor of mouth elevation", 2, "IADT", "D9"),
    ClinicalSignal("red_herring_11_23", "red_herring", "floor of mouth elevation", 3, "IADT", "D9"),
    ClinicalSignal("red_herring_12_00", "red_herring", "tongue displacement", 1, "ADA", "D9"),
    ClinicalSignal("red_herring_12_01", "red_herring", "tongue displacement", 2, "ADA", "D9"),
    ClinicalSignal("red_herring_12_02", "red_herring", "tongue displacement", 3, "ADA", "D9"),
    ClinicalSignal("red_herring_12_03", "red_herring", "tongue displacement", 4, "ADA", "D9"),
    ClinicalSignal("red_herring_12_04", "red_herring", "tongue displacement", 5, "ADA", "D9"),
    ClinicalSignal("red_herring_12_05", "red_herring", "tongue displacement", 1, "ADA", "D9"),
    ClinicalSignal("red_herring_12_06", "red_herring", "tongue displacement", 2, "ADA", "D9"),
    ClinicalSignal("red_herring_12_07", "red_herring", "tongue displacement", 3, "ADA", "D9"),
    ClinicalSignal("red_herring_12_08", "red_herring", "tongue displacement", 4, "ADA", "D9"),
    ClinicalSignal("red_herring_12_09", "red_herring", "tongue displacement", 5, "ADA", "D9"),
    ClinicalSignal("red_herring_12_10", "red_herring", "tongue displacement", 1, "ADA", "D9"),
    ClinicalSignal("red_herring_12_11", "red_herring", "tongue displacement", 2, "ADA", "D9"),
    ClinicalSignal("red_herring_12_12", "red_herring", "tongue displacement", 3, "ADA", "D9"),
    ClinicalSignal("red_herring_12_13", "red_herring", "tongue displacement", 4, "ADA", "D9"),
    ClinicalSignal("red_herring_12_14", "red_herring", "tongue displacement", 5, "ADA", "D9"),
    ClinicalSignal("red_herring_12_15", "red_herring", "tongue displacement", 1, "ADA", "D9"),
    ClinicalSignal("red_herring_12_16", "red_herring", "tongue displacement", 2, "ADA", "D9"),
    ClinicalSignal("red_herring_12_17", "red_herring", "tongue displacement", 3, "ADA", "D9"),
    ClinicalSignal("red_herring_12_18", "red_herring", "tongue displacement", 4, "ADA", "D9"),
    ClinicalSignal("red_herring_12_19", "red_herring", "tongue displacement", 5, "ADA", "D9"),
    ClinicalSignal("red_herring_12_20", "red_herring", "tongue displacement", 1, "ADA", "D9"),
    ClinicalSignal("red_herring_12_21", "red_herring", "tongue displacement", 2, "ADA", "D9"),
    ClinicalSignal("red_herring_12_22", "red_herring", "tongue displacement", 3, "ADA", "D9"),
    ClinicalSignal("red_herring_12_23", "red_herring", "tongue displacement", 4, "ADA", "D9"),
    ClinicalSignal("red_herring_13_00", "red_herring", "slow progression", 2, "AAPD", "D9"),
    ClinicalSignal("red_herring_13_01", "red_herring", "slow progression", 3, "AAPD", "D9"),
    ClinicalSignal("red_herring_13_02", "red_herring", "slow progression", 4, "AAPD", "D9"),
    ClinicalSignal("red_herring_13_03", "red_herring", "slow progression", 5, "AAPD", "D9"),
    ClinicalSignal("red_herring_13_04", "red_herring", "slow progression", 1, "AAPD", "D9"),
    ClinicalSignal("red_herring_13_05", "red_herring", "slow progression", 2, "AAPD", "D9"),
    ClinicalSignal("red_herring_13_06", "red_herring", "slow progression", 3, "AAPD", "D9"),
    ClinicalSignal("red_herring_13_07", "red_herring", "slow progression", 4, "AAPD", "D9"),
    ClinicalSignal("red_herring_13_08", "red_herring", "slow progression", 5, "AAPD", "D9"),
    ClinicalSignal("red_herring_13_09", "red_herring", "slow progression", 1, "AAPD", "D9"),
    ClinicalSignal("red_herring_13_10", "red_herring", "slow progression", 2, "AAPD", "D9"),
    ClinicalSignal("red_herring_13_11", "red_herring", "slow progression", 3, "AAPD", "D9"),
    ClinicalSignal("red_herring_13_12", "red_herring", "slow progression", 4, "AAPD", "D9"),
    ClinicalSignal("red_herring_13_13", "red_herring", "slow progression", 5, "AAPD", "D9"),
    ClinicalSignal("red_herring_13_14", "red_herring", "slow progression", 1, "AAPD", "D9"),
    ClinicalSignal("red_herring_13_15", "red_herring", "slow progression", 2, "AAPD", "D9"),
    ClinicalSignal("red_herring_13_16", "red_herring", "slow progression", 3, "AAPD", "D9"),
    ClinicalSignal("red_herring_13_17", "red_herring", "slow progression", 4, "AAPD", "D9"),
    ClinicalSignal("red_herring_13_18", "red_herring", "slow progression", 5, "AAPD", "D9"),
    ClinicalSignal("red_herring_13_19", "red_herring", "slow progression", 1, "AAPD", "D9"),
    ClinicalSignal("red_herring_13_20", "red_herring", "slow progression", 2, "AAPD", "D9"),
    ClinicalSignal("red_herring_13_21", "red_herring", "slow progression", 3, "AAPD", "D9"),
    ClinicalSignal("red_herring_13_22", "red_herring", "slow progression", 4, "AAPD", "D9"),
    ClinicalSignal("red_herring_13_23", "red_herring", "slow progression", 5, "AAPD", "D9"),
    ClinicalSignal("red_herring_14_00", "red_herring", "rapid progression", 3, "AAE", "D9"),
    ClinicalSignal("red_herring_14_01", "red_herring", "rapid progression", 4, "AAE", "D9"),
    ClinicalSignal("red_herring_14_02", "red_herring", "rapid progression", 5, "AAE", "D9"),
    ClinicalSignal("red_herring_14_03", "red_herring", "rapid progression", 1, "AAE", "D9"),
    ClinicalSignal("red_herring_14_04", "red_herring", "rapid progression", 2, "AAE", "D9"),
    ClinicalSignal("red_herring_14_05", "red_herring", "rapid progression", 3, "AAE", "D9"),
    ClinicalSignal("red_herring_14_06", "red_herring", "rapid progression", 4, "AAE", "D9"),
    ClinicalSignal("red_herring_14_07", "red_herring", "rapid progression", 5, "AAE", "D9"),
    ClinicalSignal("red_herring_14_08", "red_herring", "rapid progression", 1, "AAE", "D9"),
    ClinicalSignal("red_herring_14_09", "red_herring", "rapid progression", 2, "AAE", "D9"),
    ClinicalSignal("red_herring_14_10", "red_herring", "rapid progression", 3, "AAE", "D9"),
    ClinicalSignal("red_herring_14_11", "red_herring", "rapid progression", 4, "AAE", "D9"),
    ClinicalSignal("red_herring_14_12", "red_herring", "rapid progression", 5, "AAE", "D9"),
    ClinicalSignal("red_herring_14_13", "red_herring", "rapid progression", 1, "AAE", "D9"),
    ClinicalSignal("red_herring_14_14", "red_herring", "rapid progression", 2, "AAE", "D9"),
    ClinicalSignal("red_herring_14_15", "red_herring", "rapid progression", 3, "AAE", "D9"),
    ClinicalSignal("red_herring_14_16", "red_herring", "rapid progression", 4, "AAE", "D9"),
    ClinicalSignal("red_herring_14_17", "red_herring", "rapid progression", 5, "AAE", "D9"),
    ClinicalSignal("red_herring_14_18", "red_herring", "rapid progression", 1, "AAE", "D9"),
    ClinicalSignal("red_herring_14_19", "red_herring", "rapid progression", 2, "AAE", "D9"),
    ClinicalSignal("red_herring_14_20", "red_herring", "rapid progression", 3, "AAE", "D9"),
    ClinicalSignal("red_herring_14_21", "red_herring", "rapid progression", 4, "AAE", "D9"),
    ClinicalSignal("red_herring_14_22", "red_herring", "rapid progression", 5, "AAE", "D9"),
    ClinicalSignal("red_herring_14_23", "red_herring", "rapid progression", 1, "AAE", "D9"),
    ClinicalSignal("red_herring_15_00", "red_herring", "attenuated inflammation", 4, "IADT", "D9"),
    ClinicalSignal("red_herring_15_01", "red_herring", "attenuated inflammation", 5, "IADT", "D9"),
    ClinicalSignal("red_herring_15_02", "red_herring", "attenuated inflammation", 1, "IADT", "D9"),
    ClinicalSignal("red_herring_15_03", "red_herring", "attenuated inflammation", 2, "IADT", "D9"),
    ClinicalSignal("red_herring_15_04", "red_herring", "attenuated inflammation", 3, "IADT", "D9"),
    ClinicalSignal("red_herring_15_05", "red_herring", "attenuated inflammation", 4, "IADT", "D9"),
    ClinicalSignal("red_herring_15_06", "red_herring", "attenuated inflammation", 5, "IADT", "D9"),
    ClinicalSignal("red_herring_15_07", "red_herring", "attenuated inflammation", 1, "IADT", "D9"),
    ClinicalSignal("red_herring_15_08", "red_herring", "attenuated inflammation", 2, "IADT", "D9"),
    ClinicalSignal("red_herring_15_09", "red_herring", "attenuated inflammation", 3, "IADT", "D9"),
    ClinicalSignal("red_herring_15_10", "red_herring", "attenuated inflammation", 4, "IADT", "D9"),
    ClinicalSignal("red_herring_15_11", "red_herring", "attenuated inflammation", 5, "IADT", "D9"),
    ClinicalSignal("red_herring_15_12", "red_herring", "attenuated inflammation", 1, "IADT", "D9"),
    ClinicalSignal("red_herring_15_13", "red_herring", "attenuated inflammation", 2, "IADT", "D9"),
    ClinicalSignal("red_herring_15_14", "red_herring", "attenuated inflammation", 3, "IADT", "D9"),
    ClinicalSignal("red_herring_15_15", "red_herring", "attenuated inflammation", 4, "IADT", "D9"),
    ClinicalSignal("red_herring_15_16", "red_herring", "attenuated inflammation", 5, "IADT", "D9"),
    ClinicalSignal("red_herring_15_17", "red_herring", "attenuated inflammation", 1, "IADT", "D9"),
    ClinicalSignal("red_herring_15_18", "red_herring", "attenuated inflammation", 2, "IADT", "D9"),
    ClinicalSignal("red_herring_15_19", "red_herring", "attenuated inflammation", 3, "IADT", "D9"),
    ClinicalSignal("red_herring_15_20", "red_herring", "attenuated inflammation", 4, "IADT", "D9"),
    ClinicalSignal("red_herring_15_21", "red_herring", "attenuated inflammation", 5, "IADT", "D9"),
    ClinicalSignal("red_herring_15_22", "red_herring", "attenuated inflammation", 1, "IADT", "D9"),
    ClinicalSignal("red_herring_15_23", "red_herring", "attenuated inflammation", 2, "IADT", "D9"),
    ClinicalSignal("red_herring_16_00", "red_herring", "delayed onset", 5, "ADA", "D9"),
    ClinicalSignal("red_herring_16_01", "red_herring", "delayed onset", 1, "ADA", "D9"),
    ClinicalSignal("red_herring_16_02", "red_herring", "delayed onset", 2, "ADA", "D9"),
    ClinicalSignal("red_herring_16_03", "red_herring", "delayed onset", 3, "ADA", "D9"),
    ClinicalSignal("red_herring_16_04", "red_herring", "delayed onset", 4, "ADA", "D9"),
    ClinicalSignal("red_herring_16_05", "red_herring", "delayed onset", 5, "ADA", "D9"),
    ClinicalSignal("red_herring_16_06", "red_herring", "delayed onset", 1, "ADA", "D9"),
    ClinicalSignal("red_herring_16_07", "red_herring", "delayed onset", 2, "ADA", "D9"),
    ClinicalSignal("red_herring_16_08", "red_herring", "delayed onset", 3, "ADA", "D9"),
    ClinicalSignal("red_herring_16_09", "red_herring", "delayed onset", 4, "ADA", "D9"),
    ClinicalSignal("red_herring_16_10", "red_herring", "delayed onset", 5, "ADA", "D9"),
    ClinicalSignal("red_herring_16_11", "red_herring", "delayed onset", 1, "ADA", "D9"),
    ClinicalSignal("red_herring_16_12", "red_herring", "delayed onset", 2, "ADA", "D9"),
    ClinicalSignal("red_herring_16_13", "red_herring", "delayed onset", 3, "ADA", "D9"),
    ClinicalSignal("red_herring_16_14", "red_herring", "delayed onset", 4, "ADA", "D9"),
    ClinicalSignal("red_herring_16_15", "red_herring", "delayed onset", 5, "ADA", "D9"),
    ClinicalSignal("red_herring_16_16", "red_herring", "delayed onset", 1, "ADA", "D9"),
    ClinicalSignal("red_herring_16_17", "red_herring", "delayed onset", 2, "ADA", "D9"),
    ClinicalSignal("red_herring_16_18", "red_herring", "delayed onset", 3, "ADA", "D9"),
    ClinicalSignal("red_herring_16_19", "red_herring", "delayed onset", 4, "ADA", "D9"),
    ClinicalSignal("red_herring_16_20", "red_herring", "delayed onset", 5, "ADA", "D9"),
    ClinicalSignal("red_herring_16_21", "red_herring", "delayed onset", 1, "ADA", "D9"),
    ClinicalSignal("red_herring_16_22", "red_herring", "delayed onset", 2, "ADA", "D9"),
    ClinicalSignal("red_herring_16_23", "red_herring", "delayed onset", 3, "ADA", "D9"),
    ClinicalSignal("red_herring_17_00", "red_herring", "medical vulnerability", 1, "AAPD", "D9"),
    ClinicalSignal("red_herring_17_01", "red_herring", "medical vulnerability", 2, "AAPD", "D9"),
    ClinicalSignal("red_herring_17_02", "red_herring", "medical vulnerability", 3, "AAPD", "D9"),
    ClinicalSignal("red_herring_17_03", "red_herring", "medical vulnerability", 4, "AAPD", "D9"),
    ClinicalSignal("red_herring_17_04", "red_herring", "medical vulnerability", 5, "AAPD", "D9"),
    ClinicalSignal("red_herring_17_05", "red_herring", "medical vulnerability", 1, "AAPD", "D9"),
    ClinicalSignal("red_herring_17_06", "red_herring", "medical vulnerability", 2, "AAPD", "D9"),
    ClinicalSignal("red_herring_17_07", "red_herring", "medical vulnerability", 3, "AAPD", "D9"),
    ClinicalSignal("red_herring_17_08", "red_herring", "medical vulnerability", 4, "AAPD", "D9"),
    ClinicalSignal("red_herring_17_09", "red_herring", "medical vulnerability", 5, "AAPD", "D9"),
    ClinicalSignal("red_herring_17_10", "red_herring", "medical vulnerability", 1, "AAPD", "D9"),
    ClinicalSignal("red_herring_17_11", "red_herring", "medical vulnerability", 2, "AAPD", "D9"),
    ClinicalSignal("red_herring_17_12", "red_herring", "medical vulnerability", 3, "AAPD", "D9"),
    ClinicalSignal("red_herring_17_13", "red_herring", "medical vulnerability", 4, "AAPD", "D9"),
    ClinicalSignal("red_herring_17_14", "red_herring", "medical vulnerability", 5, "AAPD", "D9"),
    ClinicalSignal("red_herring_17_15", "red_herring", "medical vulnerability", 1, "AAPD", "D9"),
    ClinicalSignal("red_herring_17_16", "red_herring", "medical vulnerability", 2, "AAPD", "D9"),
    ClinicalSignal("red_herring_17_17", "red_herring", "medical vulnerability", 3, "AAPD", "D9"),
    ClinicalSignal("red_herring_17_18", "red_herring", "medical vulnerability", 4, "AAPD", "D9"),
    ClinicalSignal("red_herring_17_19", "red_herring", "medical vulnerability", 5, "AAPD", "D9"),
    ClinicalSignal("red_herring_17_20", "red_herring", "medical vulnerability", 1, "AAPD", "D9"),
    ClinicalSignal("red_herring_17_21", "red_herring", "medical vulnerability", 2, "AAPD", "D9"),
    ClinicalSignal("red_herring_17_22", "red_herring", "medical vulnerability", 3, "AAPD", "D9"),
    ClinicalSignal("red_herring_17_23", "red_herring", "medical vulnerability", 4, "AAPD", "D9"),
    ClinicalSignal("red_herring_18_00", "red_herring", "controlled symptoms", 2, "AAE", "D9"),
    ClinicalSignal("red_herring_18_01", "red_herring", "controlled symptoms", 3, "AAE", "D9"),
    ClinicalSignal("red_herring_18_02", "red_herring", "controlled symptoms", 4, "AAE", "D9"),
    ClinicalSignal("red_herring_18_03", "red_herring", "controlled symptoms", 5, "AAE", "D9"),
    ClinicalSignal("red_herring_18_04", "red_herring", "controlled symptoms", 1, "AAE", "D9"),
    ClinicalSignal("red_herring_18_05", "red_herring", "controlled symptoms", 2, "AAE", "D9"),
    ClinicalSignal("red_herring_18_06", "red_herring", "controlled symptoms", 3, "AAE", "D9"),
    ClinicalSignal("red_herring_18_07", "red_herring", "controlled symptoms", 4, "AAE", "D9"),
    ClinicalSignal("red_herring_18_08", "red_herring", "controlled symptoms", 5, "AAE", "D9"),
    ClinicalSignal("red_herring_18_09", "red_herring", "controlled symptoms", 1, "AAE", "D9"),
    ClinicalSignal("red_herring_18_10", "red_herring", "controlled symptoms", 2, "AAE", "D9"),
    ClinicalSignal("red_herring_18_11", "red_herring", "controlled symptoms", 3, "AAE", "D9"),
    ClinicalSignal("red_herring_18_12", "red_herring", "controlled symptoms", 4, "AAE", "D9"),
    ClinicalSignal("red_herring_18_13", "red_herring", "controlled symptoms", 5, "AAE", "D9"),
    ClinicalSignal("red_herring_18_14", "red_herring", "controlled symptoms", 1, "AAE", "D9"),
    ClinicalSignal("red_herring_18_15", "red_herring", "controlled symptoms", 2, "AAE", "D9"),
    ClinicalSignal("red_herring_18_16", "red_herring", "controlled symptoms", 3, "AAE", "D9"),
    ClinicalSignal("red_herring_18_17", "red_herring", "controlled symptoms", 4, "AAE", "D9"),
    ClinicalSignal("red_herring_18_18", "red_herring", "controlled symptoms", 5, "AAE", "D9"),
    ClinicalSignal("red_herring_18_19", "red_herring", "controlled symptoms", 1, "AAE", "D9"),
    ClinicalSignal("red_herring_18_20", "red_herring", "controlled symptoms", 2, "AAE", "D9"),
    ClinicalSignal("red_herring_18_21", "red_herring", "controlled symptoms", 3, "AAE", "D9"),
    ClinicalSignal("red_herring_18_22", "red_herring", "controlled symptoms", 4, "AAE", "D9"),
    ClinicalSignal("red_herring_18_23", "red_herring", "controlled symptoms", 5, "AAE", "D9"),
    ClinicalSignal("red_herring_19_00", "red_herring", "systemic illness", 3, "IADT", "D9"),
    ClinicalSignal("red_herring_19_01", "red_herring", "systemic illness", 4, "IADT", "D9"),
    ClinicalSignal("red_herring_19_02", "red_herring", "systemic illness", 5, "IADT", "D9"),
    ClinicalSignal("red_herring_19_03", "red_herring", "systemic illness", 1, "IADT", "D9"),
    ClinicalSignal("red_herring_19_04", "red_herring", "systemic illness", 2, "IADT", "D9"),
    ClinicalSignal("red_herring_19_05", "red_herring", "systemic illness", 3, "IADT", "D9"),
    ClinicalSignal("red_herring_19_06", "red_herring", "systemic illness", 4, "IADT", "D9"),
    ClinicalSignal("red_herring_19_07", "red_herring", "systemic illness", 5, "IADT", "D9"),
    ClinicalSignal("red_herring_19_08", "red_herring", "systemic illness", 1, "IADT", "D9"),
    ClinicalSignal("red_herring_19_09", "red_herring", "systemic illness", 2, "IADT", "D9"),
    ClinicalSignal("red_herring_19_10", "red_herring", "systemic illness", 3, "IADT", "D9"),
    ClinicalSignal("red_herring_19_11", "red_herring", "systemic illness", 4, "IADT", "D9"),
    ClinicalSignal("red_herring_19_12", "red_herring", "systemic illness", 5, "IADT", "D9"),
    ClinicalSignal("red_herring_19_13", "red_herring", "systemic illness", 1, "IADT", "D9"),
    ClinicalSignal("red_herring_19_14", "red_herring", "systemic illness", 2, "IADT", "D9"),
    ClinicalSignal("red_herring_19_15", "red_herring", "systemic illness", 3, "IADT", "D9"),
    ClinicalSignal("red_herring_19_16", "red_herring", "systemic illness", 4, "IADT", "D9"),
    ClinicalSignal("red_herring_19_17", "red_herring", "systemic illness", 5, "IADT", "D9"),
    ClinicalSignal("red_herring_19_18", "red_herring", "systemic illness", 1, "IADT", "D9"),
    ClinicalSignal("red_herring_19_19", "red_herring", "systemic illness", 2, "IADT", "D9"),
    ClinicalSignal("red_herring_19_20", "red_herring", "systemic illness", 3, "IADT", "D9"),
    ClinicalSignal("red_herring_19_21", "red_herring", "systemic illness", 4, "IADT", "D9"),
    ClinicalSignal("red_herring_19_22", "red_herring", "systemic illness", 5, "IADT", "D9"),
    ClinicalSignal("red_herring_19_23", "red_herring", "systemic illness", 1, "IADT", "D9"),
)


BY_KEY = {signal.key: signal for signal in SIGNALS}


def signals_for_condition(condition: str) -> tuple[ClinicalSignal, ...]:
    return tuple(signal for signal in SIGNALS if signal.condition == condition)


def signals_for_level(level: int) -> tuple[ClinicalSignal, ...]:
    return tuple(signal for signal in SIGNALS if signal.level == level)


def signals_for_source(source: str) -> tuple[ClinicalSignal, ...]:
    return tuple(signal for signal in SIGNALS if signal.source == source)
