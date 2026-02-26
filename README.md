DAIS-10 Mini
Deterministic Schema-Driven Completeness Scoring Utility

DAIS-10 Mini is a lightweight Python library that computes weighted completeness scores for tabular datasets using an explicit schema definition.

This library is intended for educational, exploratory, and baseline data quality assessment use.

It is not a governance, compliance, or semantic analysis framework.

Installation
pip install dais10mini
Core Model

Given dataset 
𝐷
D with 
𝑛
n rows and schema:

𝑆
=
{
(
𝑓
𝑖
,
𝑤
𝑖
)
}
𝑖
=
1
𝑘
S={(f
i
	​

,w
i
	​

)}
i=1
k
	​


Where:

𝑓
𝑖
f
i
	​

 = field name

𝑤
𝑖
>
0
w
i
	​

>0 = weight

Field completeness ratio:

𝑐
𝑖
=
non-null count of 
𝑓
𝑖
𝑛
c
i
	​

=
n
non-null count of f
i
	​

	​


Weighted dataset score:

𝑆
𝑐
𝑜
𝑟
𝑒
=
∑
𝑖
=
1
𝑘
𝑤
𝑖
𝑐
𝑖
∑
𝑖
=
1
𝑘
𝑤
𝑖
Score=
∑
i=1
k
	​

w
i
	​

∑
i=1
k
	​

w
i
	​

c
i
	​

	​

Deterministic Guarantee

For fixed input dataset 
𝐷
D and schema 
𝑆
S:

𝑓
(
𝐷
,
𝑆
)
→
𝑆
𝑐
𝑜
𝑟
𝑒
f(D,S)→Score

Repeated execution produces identical output.

Features

Weighted completeness scoring

Schema-controlled evaluation

Required field enforcement

Deterministic outputs

Explicit failure signaling

Simple utility interface

Example
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
Output Structure
result.score → float (0 to 1)

result.field_scores → per-field completeness metrics

result.incomplete_required → list of required fields missing values
Edge Case Behavior
Condition	Response
Empty dataset	Raises ValueError
Missing schema	Raises ValueError
Zero total weight	Raises ValueError
Unknown field	Raises ValueError

Silent fallback behavior is not allowed.

Non Goals

DAIS-10 Mini does NOT provide:

Semantic interpretation

Compliance certification

Temporal drift modeling

Fraud detection

Regulatory enforcement

It is a deterministic scoring utility.

Version Philosophy

Minor versions → internal improvements

Major versions → scoring model change

Score formula modification requires major version upgrade.

License

Apache License 2.0

Author

Dr. Usman Zafar

Repository:
https://github.com/usman19zafar/DAIS10_Pyton_Library_Project