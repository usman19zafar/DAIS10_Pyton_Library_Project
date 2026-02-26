# DAIS‑10 Mini  
**Deterministic Schema‑Driven Completeness Scoring Utility**

DAIS‑10 Mini is a lightweight Python library for computing **weighted completeness scores** for tabular datasets using an **explicit schema definition**. It is designed for **educational, exploratory, and baseline data‑quality assessment**, not for governance, compliance, or semantic interpretation.

---

## Features
- Weighted completeness scoring  
- Schema‑controlled evaluation  
- Required‑field enforcement  
- Deterministic, repeatable outputs  
- Explicit failure signaling  
- Minimal, simple interface  

---

## Installation
```bash
pip install dais10mini
```
## Core Model

Schema Definition

A dataset 
𝐷
 with 
𝑛
 rows is evaluated against a schema:

```md
S = { (f_i, w_i) } for i = 1..k
```
Where:
```md
f_i — field name

w_i > 0 — weight
```
Field Completeness Ratio
```md
c_i = (non‑null count of f_i) / n
Weighted Dataset Score
```
```md
Score = ( Σ (w_i * c_i) ) / ( Σ w_i )
```
Deterministic Guarantee
For fixed dataset 
𝐷
 and schema 
𝑆
:

```md
f(D, S) → Score
Repeated execution always yields identical results.
```
Example
```python
import pandas as pd
from dais10mini import evaluate

data = pd.DataFrame({
    "name": ["A", "B", None],
    "age": [25, None, 40]
})

schema = [
    {"field": "name", "weight": 0.6, "required": True},
    {"field": "age", "weight": 0.4, "required": False}
]

result = evaluate(data, schema)

print(result.score)
```
## Output Structure
result.score → float in 
[ 0 , 1 ]

result.field_scores → per‑field completeness metrics

result.incomplete_required → list of required fields with missing values

## Edge Case Behavior
Condition	Response
Empty dataset	Raises ValueError
Missing schema	Raises ValueError
Zero total weight	Raises ValueError
Unknown field	Raises ValueError
Silent fallback behavior is not permitted.

Non‑Goals
DAIS‑10 Mini does not work as commercial version of Dais10, Images of full version and test results are included in github folder:

	Semantic interpretation
	Compliance certification
	Temporal drift modeling
	Fraud detection
	Regulatory enforcement

It is strictly a deterministic scoring utility.

# Version Philosophy
Minor versions → internal improvements

Major versions → scoring model changes

Any modification to the scoring formula requires a major version upgrade.

# License
Apache License 2.0

# Author
Dr. Usman Zafar

Repository
https://github.com/usman19zafar/DAIS10_Pyton_Library_Project
