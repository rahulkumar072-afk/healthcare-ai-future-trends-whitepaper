from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
for f in ['real_world_evidence.csv','medical_dataset_plan.csv','strategic_roadmap.csv','stakeholder_action_plan.csv']:
    print('\n'+f); print(pd.read_csv(ROOT/'data'/f).to_string(index=False))
print('\nNo patient-level data are included.')
