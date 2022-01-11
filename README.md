# Monopole-Script
These files are in lxplus.  
CMS release version :CMSSW_10_6_23  
## Monopole Analysis
**To generate ntuple locally:**  
 `scarm b `  
 `cmsRun ntuple.py inputFiles=file:input.root maxEvents=-1 outputFile=output.root `  

**To submit jobs onto Condor:**  

Please change your file (real)path in the submit.sh, remoteFileList.txt, tmpSUB.SUB before you submit jobs.

You also have to create new folder for condor Output, Error, Log messages from condor job.
 
Load the RECO files in Phat's eos space:

current path:/eos/cms/store/user/srimanob/monopole/13TeV/Legacy-RECO-v2/

`realpath RECOfile-directory >> remoteFileList.txt`

Add "file:" in front of all lines (see remoteFileList.txt for example)  

Submit jobs:

`condor_submit tmpSUB.SUB`  

Check the status of your jobs:

`condor_q`  

## Systematic Uncertainty

Load particular packages from CMSSW_RELEASE_BASE and compile:

`cp $CMSSW_RELEASE_BASE/src/{RecoParticleFlow,Configuration,SimGeneral} ~/CMSSW_10_6_23/src`

`scram b -j 4`

As long as structure in your workspace  is the same as the CMSSW_BASE, it will run the your local files first when `cmsRun`.
Note that I have modified SiStripSimParameters_cfi.py in SimGeneral, you can just copy my SiStripSimParameters_cfi.py to use. 
The usage see below:

**To modify the Dedx crosstalk effect with 10% (for X0 or X1 or X2):**

`vim SimGeneral/MixingModule/python/SiStripSimParameters_cfi.py`

We only choose to change X0 up and down with 10% for systematic study, so you only need to comment the default numbers and open the X0(up or down).


**To switch OFF the spike algorithm (for Ecal sysematic uncertainty):**

`vim RecoParticleFlow/PFClusterProducer/python/particleFlowRecHitECAL_cfi.py`

switch True to False for these lines:
      timingCleaning = cms.bool(True),
      topologicalCleaning = cms.bool(True),


Useful condor tutorial:  
https://batchdocs.web.cern.ch/local/quick.html  
