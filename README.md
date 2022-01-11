# Monopole1718
These files are in lxplus.  
CMS release version :CMSSW_10_6_23  
## Monopole Analysis
**To generate ntuple locally:**  
 `scarm b `  
 `cmsRun cmsRun ntuple.py inputFiles=file:input.root maxEvents=-1 outputFile=output.root `  

**To submit jobs onto Condor:**  

please change your file (real)path in the submit.sh, remoteFileList.txt,tmpSUB.SUB before you submit

You also have to create new folder for condor Output, Error, Log messages from condor job  

`realpath RECOfile-directory >> remoteFileList.txt`

Add "file:" in front of all lines (see remoteFileList.txt for example)  

`condor_submit tmpSUB.SUB`  

Check the status of your jobs  

`condor_q`  

## Systematic Uncertainty

To switch OFF the spike algorithm (for Ecal sysematic uncertainty):

`vim RecoParticleFlow/PFClusterProducer/python/particleFlowRecHitECAL_cfi.py`
switch True to False for these lines:
      timingCleaning = cms.bool(True),
      topologicalCleaning = cms.bool(True),

To modify the Dedx crosstalk effect with 10% (for X0 or X1 or X2):

`vim SimGeneral/MixingModule/python/SiStripSimParameters_cfi.py`

We only choose to change X0 up and down with 10% for systematic study, so you only need to comment the default numbers and open the X0(up or down).


Useful condor tutorial:  
https://batchdocs.web.cern.ch/local/quick.html  
