import lightning as L
from typing import Optional
import os


SYSTEM_PACKAGES = """
sudo apt update
sudo apt -y upgrade
""".split('\n')

R_INSTALL = """
sudo apt-get install r-base
""".split('\n')

R_STUDIO = """
sudo apt-get install gdebi-core
wget https://download2.rstudio.org/server/bionic/amd64/rstudio-server-2022.07.1-554-amd64.deb
sudo gdebi -n rstudio-server-2022.07.1-554-amd64.deb
chmod +777 /etc/rstudio/rserver.conf
""".split('\n')

class CustomBuildConfig(L.BuildConfig):
    def build_commands(self):
        return SYSTEM_PACKAGES + R_INSTALL + R_STUDIO

class RStudioServer(L.LightningWork):
    def __init__(self, cloud_compute: Optional[L.CloudCompute] = None):
        super().__init__(cloud_compute=cloud_compute, cloud_build_config=CustomBuildConfig(), parallel=True)
        self.rstudio_url = None

    def run(self):
        os.system("'www-port={self.port}' >> /etc/rstudio/rserver.conf")
        os.system("sudo rstudio-server restart")
