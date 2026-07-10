# SOIL Subagent Batching

Use only when the user explicitly requests parallel generation and subagents are available.

1. Generate one representative content slide sequentially.
2. Review teaching clarity, layout, exact text, rounded typography, and style.
3. Save the approved golden sample and write its path into YAML.
4. Assign non-overlapping page ranges.
5. Give every worker the same spec, golden sample, output folder, and prompt contract.
6. Require separate prompt logs and visual inspection.
7. The primary agent reviews the final montage and selectively regenerates failures.

Parallel generation shares quota and does not guarantee consistency without the golden sample.

