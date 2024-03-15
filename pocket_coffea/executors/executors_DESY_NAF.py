import os
import sys
import socket
from coffea import processor as coffea_processor
from .executors_base import ExecutorFactoryABC
from .executors_base import IterativeExecutorFactory, FuturesExecutorFactory
from pocket_coffea.utils.network import check_port
from pocket_coffea.parameters.dask_env import setup_dask

import parsl
from parsl.providers import CondorProvider
from parsl.channels import LocalChannel
from parsl.config import Config
from parsl.executors import HighThroughputExecutor
from parsl.launchers import SrunLauncher, SingleNodeLauncher
from parsl.addresses import address_by_hostname, address_by_query
    

class ParslCondorExecutorFactory(ExecutorFactoryABC):
    '''
    Parsl executor based on condor for DESY NAF
    '''

    def __init__(self, run_options, outputdir, **kwargs):
        self.outputdir = outputdir
        super().__init__(run_options)

    def get_worker_env(self):
        env_worker = [
            'export XRD_RUNFORKHANDLER=1',
            'export MALLOC_TRIM_THRESHOLD_=0',
            f'export X509_USER_PROXY={self.x509_path}',
            'ulimit -u 32768',
            'export PYTHONPATH=$PYTHONPATH:$PWD'
            ]
        
        # Adding list of custom setup commands from user defined run options
        if self.run_options.get("custom-setup-commands", None):
            env_worker += self.run_options["custom-setup-commands"]
        if True:
            print("#"*50+"\n"+os.environ['CONDA_DEFAULT_ENV'])
            # ~ env_worker.append(f'export PATH={os.environ["CONDA_PREFIX"]}/bin:$PATH')
            env_worker.append(f'source {os.environ["HOME"]}/.zshrc')
            env_worker.append(f'micromamba activate pocket-coffea')
            # ~ print(os.environ['CONDA_DEFAULT_ENV'])
            # ~ print(os.environ['CONDA_DEFAULT_ENV'])
        # Now checking for conda environment  conda-env:true
        if self.run_options.get("conda-env", False):
            print("TEST in conda-env")
            env_worker.append(f'export PATH={os.environ["CONDA_PREFIX"]}/bin:$PATH')
            if "CONDA_ROOT_PREFIX" in os.environ:
                env_worker.append(f"{os.environ['CONDA_ROOT_PREFIX']} activate {os.environ['CONDA_DEFAULT_ENV']}")
            elif "MAMBA_ROOT_PREFIX" in os.environ:
                env_worker.append(f"{os.environ['MAMBA_ROOT_PREFIX']} activate {os.environ['CONDA_DEFAULT_ENV']}")
            else:
                raise Exception("CONDA prefix not found in env! Something is wrong with your conda installation if you want to use conda in the dask cluster.")

        # if local-virtual-env: true the dask job is configured to pickup
        # the local virtual environment. 
        if self.run_options.get("local-virtualenv", False):
            env_worker.append(f"source {sys.prefix}/bin/activate")

        return env_worker
    
        
    def setup(self):
        ''' Start the slurm cluster here'''
        self.setup_proxyfile()
        print(self.run_options.keys())
        condor_htex = Config(
                executors=[
                    HighThroughputExecutor(
                        label="coffea_parsl_condor",
                        address=address_by_hostname(),
                        max_workers=1,
                        # Condor
                        provider=CondorProvider(
                            nodes_per_block=1,
                            cores_per_slot=self.run_options["cores-per-worker"],
                            mem_per_slot=self.run_options["mem-per-worker"],
                            init_blocks=self.run_options["scaleout"],
                            max_blocks=(self.run_options["scaleout"]) + 10,
                            worker_init="\n".join(self.get_worker_env()),
                            walltime=self.run_options["walltime"],
                            requirements=self.run_options.get("requirements", ""),
                        ),
                    )
                ],
                retries=self.run_options["retries"],
            )

        self.condor_cluster = parsl.load(condor_htex)

        
    def get(self):
        return coffea_processor.parsl_executor(**self.customized_args())

    def customized_args(self):
        args = super().customized_args()
        # in the futures executor Nworkers == N scalout
        # ~ args["treereduction"] = self.run_options["tree-reduction"]
        # ~ args["skip-bad-files"] = self.run_options["skip-bad-files"]
        return args

    def close(self):
        self.condor_cluster.close()




def get_executor_factory(executor_name, **kwargs):
    if executor_name == "iterative":
        return IterativeExecutorFactory(**kwargs)
    elif executor_name == "futures":
        return FuturesExecutorFactory(**kwargs)
    elif  executor_name == "parsl-condor":
        return ParslCondorExecutorFactory(**kwargs)
    print(executor_name)
