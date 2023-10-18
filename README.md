# PHB_Degrading_Analysis

[Mega software](https://www.megasoftware.net)

## Convert all .txt to .csv

```bash
    parallel 'mv {} {.}.csv' ::: *.txt
```
