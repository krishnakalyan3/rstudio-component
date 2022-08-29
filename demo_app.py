#!/usr/bin/env python3

import os
import lightning as L
from lit_rstudio import RStudioServer

class RootFlow(L.LightningFlow):
    def __init__(self) -> None:
        super().__init__()
        self.rstudio_work = RStudioServer(cloud_compute=L.CloudCompute(os.getenv("COMPUTE", "cpu-small")))

    def run(self):
        self.rstudio_work.run()
    
    def configure_layout(self):
        return [{'name': "VSCode", 'content': self.rstudio_work}]

app = L.LightningApp(RootFlow())
