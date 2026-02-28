import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv("src/.env")

HOST = os.getenv("PG_HOST", "localhost")
PORT = os.getenv("PG_PORT", "5433")
DB = os.getenv("PG_DB", "rfm_db")
USER = os.getenv("PG_USER", "captain")
PASSWORD = os.getenv("PG_PASSWORD", "")


def main():
    outdir = Path("outputs")
    outdir.mkdir(parents=True, exist_ok=True)

    url = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    engine = create_engine(url)

    seg = pd.read_sql("SELECT * FROM public.rfm_segments;", engine)
    summ = pd.read_sql("SELECT * FROM public.rfm_segment_summary;", engine)

    seg.to_csv(outdir / "rfm_segments.csv", index=False)
    summ.to_csv(outdir / "rfm_segment_summary.csv", index=False)

    print("Saved:")
    print("outputs/rfm_segments.csv rows:", len(seg))
    print("outputs/rfm_segment_summary.csv rows:", len(summ))


if __name__ == "__main__":
    main()
