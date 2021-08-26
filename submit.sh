#!/usr/bin/env sh
remoteFile=$1
processNum=$2
currentPath=$PWD
source /cvmfs/cms.cern.ch/cmsset_default.sh
cd /afs/cern.ch/user/l/lshih/CMSSW_10_6_23/src && eval $(scram runtime -sh)
cd $currentPath
cmsRun /afs/cern.ch/user/l/lshih/CMSSW_10_6_23/src/ntuple_mc_2018_cfg.py inputFiles=${remoteFile} 
mv MonoNtuple2018_MC_3000.root MonoNtuple2018_MC_3000_${processNum}.root 
