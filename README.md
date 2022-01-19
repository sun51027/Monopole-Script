# Monopole-Script
These files are in lxplus.  
CMS release version : CMSSW_10_6_23   
Set up enviroment before running the script  
`cmsrel CMSSW_10_6_23  
cd CMSSW_10_6_23/src  
git clone git@github.com:sun51027/Monopole-Script.git  
mv Monopole-Script/* .  
scram b -j 4` 
## Monopole Analysis
**To generate ntuple locally:**  
 `scarm b `  
 `cmsRun ntuple_mc_YEAR_cfg.py inputFiles=file:input.root maxEvents=-1 outputFile=output.root `  

Note: I recommend not to do this first, since all files in this repository were defaulted to be used for "Condor", see below topic. If you just want to run one file for test, you have to cancel the comments in these lines:
```c
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)
Output = cms.string(options.outputFile)
```
**To submit jobs onto Condor:**  

Please try to understand how submit.sh and tmpSUB.SUB work with relation to ntuple_mc_YEAR_cfg.py (the default year is 2018, mass 1000GeV), and change the file (real)path in the submit.sh, remoteFileList.txt, tmpSUB.SUB before you submit jobs. You also have to create new folder for condor Output, Error, Log messages from condor job.
 
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
