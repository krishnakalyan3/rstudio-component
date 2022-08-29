### RStudio Server Component
[RStudio](https://www.rstudio.com/) is an integrated development environment for R, a programming language for statistical computing and graphics. It is available in two formats: RStudio Desktop is a regular desktop application while RStudio Server runs on a remote server and allows accessing RStudio using a web browser.

### Usage
To use this component add modify the following variables below. Please consider checking out our documentation to understand they types of Cloud Compute instances supported. Startup time for this component with all kernels is around 5-6 minutes.

```
import os
import lightning as L
from lit_rstudio import RStudioServer

class RootFlow(L.LightningFlow):
    def __init__(self) -> None:
        super().__init__()
        self.rstudio_work = RStudioServer(cloud_compute=L.CloudCompute(os.getenv("COMPUTE", "cpu-small")), passwd=os.getenv("RS_PASS", "radmin"))

    def run(self):
        self.rstudio_work.run()
    
    def configure_layout(self):
        return [{'name': "RStudioServer", 'content': self.rstudio_work}]

app = L.LightningApp(RootFlow())
```

By default this component launches with cpu-small Compute Instance. This can be overridden using the COMPUTE environment variable. 

### Installation

```
lightning install component TODO/rstudio_component
```

Or to build locally
```bash
git clone TODO

cd rstudio_component
pip install -r requirements.txt
pip install -e .
```

### Login Credentials

```
username: zeus
password: radmin
```

### TODO
- [ ] Unit Test
- [ ] Application Check
- [ ] CI Pipeline
- [ ] Precommit
