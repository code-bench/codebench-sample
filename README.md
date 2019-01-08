# codebench-sample
A sample project using codebench

### Use Command Line Interface

```bash
codebench --script ./benchmark.py \
--report_types chart --commits cb91b8 3cd96d bb1541
```

### Use Configuration File

`.codebench.yml` on the root directory is as follows:
```yaml
before_each: ./before_script.sh

script: ./benchmark.py

report_types:
  - chart

commits:
  - cb91b8
  - 3cd96d
  - bb1541
```

Run `codebench` on the command line, it will read configurations
from `.codebench.yml` and run the program.
