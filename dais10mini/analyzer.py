"""
DAIS-10 Mini Analyzer (Final Stable Version)

Lightweight deterministic data quality scoring utility.

Features:
- Completeness scoring
- Row ranking
- Column statistics
- Human-readable summaries

Complexity:
- Time: O(n × m)
- Space: O(n + m)
"""

from typing import List, Dict, Any


class Analyzer:
    """Deterministic data quality analyzer"""

    def __init__(self, domain: str = "general"):
        self.domain = domain

    # -------------------------------------------------
    # Core Analysis Engine
    # -------------------------------------------------

    def analyze(self, rows: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze dataset quality"""

        if not isinstance(rows, list):
            raise TypeError("rows must be List[Dict]")

        if len(rows) == 0:
            raise ValueError("No data to analyze")

        columns = list(rows[0].keys())
        total_rows = len(rows)

        # -----------------------------
        # Column completeness statistics
        # -----------------------------
        column_stats = {}

        for col in columns:
            missing = sum(
                1 for r in rows
                if not r.get(col) or str(r.get(col)).strip() == ""
            )

            completeness = round(
                ((total_rows - missing) / total_rows * 100)
                if total_rows > 0 else 0,
                1
            )

            column_stats[col] = {
                "completeness": completeness,
                "missing_count": missing,
                "total_count": total_rows,
            }

        # -----------------------------
        # Average completeness score
        # -----------------------------
        if len(column_stats) > 0:
            avg_score = round(
                sum(v["completeness"] for v in column_stats.values())
                / len(column_stats),
                1
            )
        else:
            avg_score = 0

        # -----------------------------
        # Row scoring
        # -----------------------------
        row_scores = []

        for idx, row in enumerate(rows):
            filled = sum(
                1 for col in columns
                if row.get(col) and str(row.get(col)).strip() != ""
            )

            score = round(
                (filled / len(columns) * 100) if len(columns) > 0 else 0,
                1
            )

            if score >= 80:
                status = "GOOD"
            elif score >= 50:
                status = "FAIR"
            else:
                status = "POOR"

            row_scores.append({
                "row_id": idx + 1,
                "score": score,
                "status": status
            })

        # Sort ranking
        row_scores_sorted = sorted(
            row_scores,
            key=lambda x: x["score"],
            reverse=True
        )

        return {
            "domain": self.domain,
            "total_rows": total_rows,
            "total_columns": len(columns),
            "columns": columns,
            "average_score": avg_score,
            "column_stats": column_stats,
            "best_rows": row_scores_sorted[:10],
            "worst_rows": row_scores_sorted[-10:],
            "all_rows": row_scores
        }

    # -------------------------------------------------
    # Summary Generator
    # -------------------------------------------------

    def get_summary(self, analysis_results: Dict[str, Any]) -> str:
        """Generate human-readable summary"""

        res = analysis_results

        summary = f"""
DAIS-10 Mini - Analysis Summary
{"=" * 50}
Domain:          {res['domain']}
Total Rows:      {res['total_rows']}
Total Columns:   {res['total_columns']}
Average Score:   {res['average_score']}/100

Top 3 Best Rows:
"""

        for row in res["best_rows"][:3]:
            summary += (
                f"  Row {row['row_id']:5d}: "
                f"{row['score']:6.1f}/100 ({row['status']})\n"
            )

        summary += "\nTop 3 Worst Rows:\n"

        for row in res["worst_rows"][:3]:
            summary += (
                f"  Row {row['row_id']:5d}: "
                f"{row['score']:6.1f}/100 ({row['status']})\n"
            )

        return summary.strip()