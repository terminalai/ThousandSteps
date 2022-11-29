drop table if exists pdbiostamp;

CREATE TABLE pdbiostamp (
    "ID" TEXT,
    "Timestamp" FLOAT,
    "IsParkinson" BOOLEAN,
    "ChestX" FLOAT,
    "ChestY" FLOAT,
    "ChestZ" FLOAT,
    "LeftLegX" FLOAT,
    "LeftLegY" FLOAT,
    "LeftLegZ" FLOAT,
    "RightLegX" FLOAT,
    "RightLegY" FLOAT,
    "RightLegZ" FLOAT,
    "LeftHandX" FLOAT,
    "LeftHandY" FLOAT,
    "LeftHandZ" FLOAT,
    "RightHandX" FLOAT,
    "RightHandY" FLOAT,
    "RightHandZ" FLOAT,
)