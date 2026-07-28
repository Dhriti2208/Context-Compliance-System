from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@app.get("/analyze")
def analyze():

    logs = pd.read_csv(os.path.join(BASE_DIR, "synthetic_logs.csv"))

    # dataset already has violation_label column
    logs["prediction"] = logs["violation_label"].apply(
        lambda x: "violation" if str(x).lower() != "none" else "compliant"
    )

    total = len(logs)
    violations = (logs["prediction"] == "violation").sum()
    compliant = (logs["prediction"] == "compliant").sum()

    risk_score = violations / total if total > 0 else 0

    return {
        "total_logs": total,
        "violations": int(violations),
        "compliant": int(compliant),
        "risk_score": round(risk_score, 2)
    }