# Pro-Fit Scanner Test Cases

| ID | Test | Expected |
|---|---|---|
| TC-01 | Complete valid CSV | Accepted |
| TC-02 | Missing `tof_mm` | Validation error |
| TC-03 | Negative ToF | Validation error |
| TC-04 | Negative load | Validation error |
| TC-05 | Empty dataset | Validation error |
| TC-06 | Filtering | Same row count |
| TC-07 | Summary | Correct count/extrema |
| TC-08 | CSV processing | Processed CSV created |

Run:
```bash
pytest -q
```
