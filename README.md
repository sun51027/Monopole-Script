# Monopole1718
These files are in lxplus.  
CMS release version :CMSSW_10_6_23  

**To generate ntuple locally:**  
 `scarm b `  
 `cmsRun cmsRun ntuple.py inputFiles=file:YourInputFile.root maxEvents=-1 outputFile=YourOutputName.root `  

**To submit jobs onto Condor:**  
*please change your file (real)path in the submit.sh, remoteFileList.txt,tmpSUB.SUB before you submit*  
You also have to create new folder for condor Output, Error, Log messages from condor job  

`condor_submit tmpSUB.SUB`  

Check the status of your jobs  

`condor_q`  

Useful condor tutorial:  
https://batchdocs.web.cern.ch/local/quick.html  
