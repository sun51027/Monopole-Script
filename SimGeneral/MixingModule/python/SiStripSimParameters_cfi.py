import FWCore.ParameterSet.Config as cms

SiStripSimBlock = cms.PSet(
    #---SiLinearChargeDivider
    DeltaProductionCut      = cms.double(0.120425),
    APVpeakmode             = cms.bool(False), # also SiStripDigitizerAlgorithm
    LandauFluctuations      = cms.bool(True),
    chargeDivisionsPerStrip = cms.int32(10),
    CosmicDelayShift        = cms.untracked.double(0.0), # also SiStripDigitizerAlgorithm
    
    APVShapeDecoFile = cms.FileInPath("SimTracker/SiStripDigitizer/data/APVShapeDeco_default.txt"),
    APVShapePeakFile = cms.FileInPath("SimTracker/SiStripDigitizer/data/APVShapePeak_default.txt"),

    #---SiHitDigitizer
    DepletionVoltage        = cms.double(170.0),
    AppliedVoltage          = cms.double(300.0),
    ChargeMobility          = cms.double(310.0),
    Temperature             = cms.double(273.0),
    GevPerElectron          = cms.double(3.61e-09),
    ChargeDistributionRMS   = cms.double(6.5e-10),
    noDiffusion             = cms.bool(False),
    #---SiTrivialInduceChargeOnStrips
    #switch to use different coupling constants set
    #if True RunII cross talk will be used
    #if False RunI cross talk will be used
    CouplingConstantsRunIIDecB   = cms.bool(True), #for TIB and TOB
    CouplingConstantsRunIIDecW   = cms.bool(True), #for TID and TEC
    #TIB
    CouplingConstantDecIB1  = cms.vdouble(0.8523, 0.0574,0.0165),                    
    CouplingConstantDecIB2  = cms.vdouble(0.9130, 0.0341,0.0094),                    
    CouplingConstantPeakIB1 = cms.vdouble(0.9006, 0.0497),                           
    CouplingConstantPeakIB2 = cms.vdouble(0.9342, 0.0328),                           
    #TOB
    CouplingConstantDecOB1  = cms.vdouble(0.7558, 0.0879, 0.0342),                   
    CouplingConstantDecOB2  = cms.vdouble(0.7975, 0.0739, 0.0273),                   
    CouplingConstantPeakOB1 = cms.vdouble(0.8542, 0.0729),                           
    CouplingConstantPeakOB2 = cms.vdouble(0.8719, 0.0640),
    #TID
    CouplingConstantDecW1a  = cms.vdouble(0.8646, 0.0537, 0.014),                      
    CouplingConstantDecW2a  = cms.vdouble(0.8758, 0.0517, 0.0104),                   
    CouplingConstantDecW3a  = cms.vdouble(0.8980, 0.0492, 0.0018),                   
    CouplingConstantPeakW1a = cms.vdouble(0.996, 0.002),                             
    CouplingConstantPeakW2a = cms.vdouble(1.0,   0.000),                             
    CouplingConstantPeakW3a = cms.vdouble(0.996, 0.002),
    #TEC
    CouplingConstantPeakW1b = cms.vdouble(0.976, 0.012),                             
    CouplingConstantPeakW2b = cms.vdouble(0.998, 0.001),                             
    CouplingConstantPeakW3b = cms.vdouble(0.992, 0.004),                             
    CouplingConstantPeakW4  = cms.vdouble(0.992, 0.004),                             
    CouplingConstantPeakW5  = cms.vdouble(0.968, 0.016),
    CouplingConstantPeakW6  = cms.vdouble(0.972, 0.014),
    CouplingConstantPeakW7  = cms.vdouble(0.964, 0.018),

    #RunII (2018) deconvolution parameters 


    #TIB----Up x0 10% x2 const
#    CouplingConstantRunIIDecIB1 = cms.vdouble(0.9197, 0.0284, 0.0117),
#    CouplingConstantRunIIDecIB2 = cms.vdouble(0.9477, 0.0157, 0.0104),
    #TIB----Down x0 10% x2 const
#    CouplingConstantRunIIDecIB1 = cms.vdouble(0.7524, 0.1121, 0.0117),
#    CouplingConstantRunIIDecIB2 = cms.vdouble(0.7754, 0.1019, 0.0104),
    #TIB----Up x1 10% x2 const
#    CouplingConstantRunIIDecIB1 = cms.vdouble(0.8220, 0.0773, 0.0117),
#    CouplingConstantRunIIDecIB2 = cms.vdouble(0.8500, 0.0646, 0.0104),
#    #TIB----Down x1 10% x2 const
    # CouplingConstantRunIIDecIB1 = cms.vdouble(0.8502, 0.0632., 0.0117),
    # CouplingConstantRunIIDecIB2 = cms.vdouble(0.8734, 0.0529, 0.0104),
    #TIB----Up x1 10% x0 const
    CouplingConstantRunIIDecIB1 = cms.vdouble(0.8361, 0.0773, 0.0046),
    CouplingConstantRunIIDecIB2 = cms.vdouble(0.8616, 0.0646, 0.0046),
   #TIB----Down x1 10% x0 const
    CouplingConstantRunIIDecIB1 = cms.vdouble(0.8361, 0.0632, 0.0187),
    CouplingConstantRunIIDecIB2 = cms.vdouble(0.8616, 0.0529, 0.0163),
#    #TIB----Up x2 10% x1 const
#    CouplingConstantRunIIDecIB1 = cms.vdouble(0., 0.0703, 0.),
#    CouplingConstantRunIIDecIB2 = cms.vdouble(0., 0.0588, 0.),
#    #TIB----Down x2 10% x1 const
#    CouplingConstantRunIIDecIB1 = cms.vdouble(0., 0.0703, 0.),
#    CouplingConstantRunIIDecIB2 = cms.vdouble(0., 0.0588, 0.),
#    #TIB
#    CouplingConstantRunIIDecIB1 = cms.vdouble(0.8361, 0.0703, 0.0117),
#    CouplingConstantRunIIDecIB2 = cms.vdouble(0.8616, 0.0588, 0.0104),

    #-----------

    #TOB--Up x0 10% x2 const
#    CouplingConstantRunIIDecOB2 = cms.vdouble(0.8717, 0.0438, 0.0203),
#    CouplingConstantRunIIDecOB1 = cms.vdouble(0.8207, 0.0623, 0.0273),
    #TOB--Down x0 10% x2 const
#    CouplingConstantRunIIDecOB2 = cms.vdouble(0.7132, 0.1231, 0.0203),
#    CouplingConstantRunIIDecOB1 = cms.vdouble(0.6714, 0.1370, 0.0273),
    #TOB--Up x1 10% x2 const
#    CouplingConstantRunIIDecOB2 = cms.vdouble(0.7760, 0.0917, 0.0203),
#    CouplingConstantRunIIDecOB1 = cms.vdouble(0.7264, 0.1095, 0.0273),
#    #TOB--Down x1 10% x2 const
    # CouplingConstantRunIIDecOB2 = cms.vdouble(0.8094, 0.0750, 0.0203),
    # CouplingConstantRunIIDecOB1 = cms.vdouble(0.7662, 0.0896, 0.0273),
    #TOB--Up x1 10% x0 const
   CouplingConstantRunIIDecOB2 = cms.vdouble(0.7925, 0.0917, 0.0917),
   CouplingConstantRunIIDecOB1 = cms.vdouble(0.7461, 0.1095, 0.0174),
#    #TOB--Down x1 10% x0 const
    CouplingConstantRunIIDecOB2 = cms.vdouble(0.7925, 0.0750, 0.0287),
    CouplingConstantRunIIDecOB1 = cms.vdouble(0.7461, 0.0896, 0.0373),
#    #TOB--Up x2 10% x1 const
#    CouplingConstantRunIIDecOB2 = cms.vdouble(0.7886, 0.0834, 0.0223),
#    CouplingConstantRunIIDecOB1 = cms.vdouble(0.7408, 0.0996, 0.0300),
#    #TOB--Down x2 10% x1 const
#    CouplingConstantRunIIDecOB2 = cms.vdouble(0.7968, 0.0834, 0.0182),
#    CouplingConstantRunIIDecOB1 = cms.vdouble(0.7518, 0.0996, 0.0245),
#    #TOB
#    CouplingConstantRunIIDecOB2 = cms.vdouble(0.7925, 0.0834, 0.0203),
#    CouplingConstantRunIIDecOB1 = cms.vdouble(0.7461, 0.0996, 0.0273),
#
    #-----------

   #TID----Up x0 10% x2 const
#    CouplingConstantRunIIDecW1a = cms.vdouble(0.9428, 0.0180, 0.0106),
#    CouplingConstantRunIIDecW2a = cms.vdouble(0.9747, 0.0046, 0.008),
#    CouplingConstantRunIIDecW3a = cms.vdouble(0.9882, 0.0045, 0.0014),
#    #TID----Down x0 10% x2 const
#    CouplingConstantRunIIDecW1a = cms.vdouble(0.7713, 0.1073, 0.0106),
#    CouplingConstantRunIIDecW2a = cms.vdouble(0.7974, 0.0933, 0.008),
#    CouplingConstantRunIIDecW3a = cms.vdouble(0.8085, 0.0943, 0.0014),
     #TID---Up x1 10% x2 const
#    CouplingConstantRunIIDecW1a = cms.vdouble(0.8452, 0.0668, 0.0106),
#    CouplingConstantRunIIDecW2a = cms.vdouble(0.8762, 0.0539, 0.008),
#    CouplingConstantRunIIDecW3a = cms.vdouble(0.8886, 0.0543, 0.0014),
#     #TID---Down x1 10% x2 const
    # CouplingConstantRunIIDecW1a = cms.vdouble(0.8694, 0.0547, 0.0106),
    # CouplingConstantRunIIDecW2a = cms.vdouble(0.8958, 0.0441, 0.008),
    # CouplingConstantRunIIDecW3a = cms.vdouble(0.9084, 0.0444, 0.0014),
     #TID---Up x1 10% x0 const
   CouplingConstantRunIIDecW1a = cms.vdouble(0.8571, 0.0668, 0.0046),
   CouplingConstantRunIIDecW2a = cms.vdouble(0.8861, 0.0539, 0.0175),
   CouplingConstantRunIIDecW3a = cms.vdouble(0.8984, 0.0543, -0.0035),
#     #TID---Down x1 10% x0 const
    CouplingConstantRunIIDecW1a = cms.vdouble(0.8571, 0.0547, 0.0167),
    CouplingConstantRunIIDecW2a = cms.vdouble(0.8861, 0.0441, 0.0128),
    CouplingConstantRunIIDecW3a = cms.vdouble(0.8984, 0.0444, 0.0064),
#     #TID---Up x2 10% x1 const
#    CouplingConstantRunIIDecW1a = cms.vdouble(0.8552, 0.0608, 0.0116),
#    CouplingConstantRunIIDecW2a = cms.vdouble(0.8844, 0.0490, 0.0088),
#    CouplingConstantRunIIDecW3a = cms.vdouble(0.8982, 0.0494, 0.015),
#     #TID---Down x2 10% x1 const
#    CouplingConstantRunIIDecW1a = cms.vdouble(0.8594, 0.0608, 0.0095),
#    CouplingConstantRunIIDecW2a = cms.vdouble(0.8876, 0.0490, 0.0072),
#    CouplingConstantRunIIDecW3a = cms.vdouble(0.8988, 0.0494, 0.0012),
#    #TID
#    CouplingConstantRunIIDecW1a = cms.vdouble(0.8571, 0.0608, 0.0106),
#    CouplingConstantRunIIDecW2a = cms.vdouble(0.8861, 0.049, 0.008),
#    CouplingConstantRunIIDecW3a = cms.vdouble(0.8984, 0.0494, 0.0014),
    #-----------




    #TEC----Up x0 10% x2 const
#    CouplingConstantRunIIDecW1b = cms.vdouble(0.9709, 0.0077, 0.0068),
#    CouplingConstantRunIIDecW2b = cms.vdouble(0.9837, 0.0035, 0.0046),
#    CouplingConstantRunIIDecW3b = cms.vdouble(0.9472, 0.0143, 0.0121),
#    CouplingConstantRunIIDecW4  = cms.vdouble(0.9769, 0.0100, 0.0015),
#    CouplingConstantRunIIDecW5  = cms.vdouble(0.8796, 0.0371, 0.0231),
#    CouplingConstantRunIIDecW6  = cms.vdouble(0.8873, 0.0365, 0.0198),
#    CouplingConstantRunIIDecW7  = cms.vdouble(0.8671, 0.0493, 0.0171),
    #TEC---Down x0 10% x2 const
#    CouplingConstantRunIIDecW1b = cms.vdouble(0.7944, 0.0960, 0.0068),
#    CouplingConstantRunIIDecW2b = cms.vdouble(0.8048, 0.0930, 0.0046),
#    CouplingConstantRunIIDecW3b = cms.vdouble(0.7749, 0.1004, 0.0121),
#    CouplingConstantRunIIDecW4  = cms.vdouble(0.7992, 0.0989, 0.0015),
#    CouplingConstantRunIIDecW5  = cms.vdouble(0.7197, 0.1170, 0.0231),
#    CouplingConstantRunIIDecW6  = cms.vdouble(0.7260, 0.1172, 0.0198),
#    CouplingConstantRunIIDecW7  = cms.vdouble(0.7094, 0.1282, 0.0171),
    #TEC---Up x1 10% x2 const
#    CouplingConstantRunIIDecW1b = cms.vdouble(0.8726, 0.0569, 0.0068),
#    CouplingConstantRunIIDecW2b = cms.vdouble(0.8846, 0.0531, 0.0046),
#    CouplingConstantRunIIDecW3b = cms.vdouble(0.8498, 0.0630, 0.0121),
#    CouplingConstantRunIIDecW4  = cms.vdouble(0.8774, 0.0598, 0.0015),
#    CouplingConstantRunIIDecW5  = cms.vdouble(0.7844, 0.0847, 0.0231),
#    CouplingConstantRunIIDecW6  = cms.vdouble(0.7914, 0.0845, 0.0198),
#    CouplingConstantRunIIDecW7  = cms.vdouble(0.7706, 0.0976, 0.0171),
#    #TEC---Down x1 10% x2 const
    # CouplingConstantRunIIDecW1b = cms.vdouble(0.8932, 0.0466, 0.0068),
    # CouplingConstantRunIIDecW2b = cms.vdouble(0.9040, 0.0434, 0.0046),
    # CouplingConstantRunIIDecW3b = cms.vdouble(0.8728, 0.0515, 0.0121),
    # CouplingConstantRunIIDecW4  = cms.vdouble(0.8992, 0.0489, 0.0015),
    # CouplingConstantRunIIDecW5  = cms.vdouble(0.8152, 0.0693, 0.0231),
    # CouplingConstantRunIIDecW6  = cms.vdouble(0.8220, 0.0692, 0.0198),
    # CouplingConstantRunIIDecW7  = cms.vdouble(0.8060, 0.0799, 0.0171),
    #TEC---Up x1 10% x0 const
   CouplingConstantRunIIDecW1b = cms.vdouble(0.8827, 0.0569, 0.0017),
   CouplingConstantRunIIDecW2b = cms.vdouble(0.8943, 0.0531, -0.0002),
   CouplingConstantRunIIDecW3b = cms.vdouble(0.8611, 0.0630, 0.0064),
   CouplingConstantRunIIDecW4  = cms.vdouble(0.8881, 0.0598, -0.0038),
   CouplingConstantRunIIDecW5  = cms.vdouble(0.7997, 0.0847, 0.0154),
   CouplingConstantRunIIDecW6  = cms.vdouble(0.8067, 0.0845, 0.0121),
   CouplingConstantRunIIDecW7  = cms.vdouble(0.7883, 0.0976, 0.0082),
#    #TEC---Down x1 10% x0 const
    CouplingConstantRunIIDecW1b = cms.vdouble(0.8827, 0.0466, 0.0120),
    CouplingConstantRunIIDecW2b = cms.vdouble(0.8943, 0.0434, 0.0084),
    CouplingConstantRunIIDecW3b = cms.vdouble(0.8611, 0.0515, 0.0179),
    CouplingConstantRunIIDecW4  = cms.vdouble(0.8881, 0.0489, 0.0070),
    CouplingConstantRunIIDecW5  = cms.vdouble(0.7997, 0.0693, 0.0308),
    CouplingConstantRunIIDecW6  = cms.vdouble(0.8067, 0.0692, 0.0274),
    CouplingConstantRunIIDecW7  = cms.vdouble(0.7883, 0.0799, 0.0259),
#
#    #TEC---Up x2 10% x1 const
#    CouplingConstantRunIIDecW1b = cms.vdouble(0.8816, 0.0518, 0.0074),
#    CouplingConstantRunIIDecW2b = cms.vdouble(0.8934, 0.0483, 0.0050),
#    CouplingConstantRunIIDecW3b = cms.vdouble(0.8588, 0.0573, 0.0133),
#    CouplingConstantRunIIDecW4  = cms.vdouble(0.8880, 0.0544, 0.0016),
#    CouplingConstantRunIIDecW5  = cms.vdouble(0.7952, 0.0770, 0.0254),
#    CouplingConstantRunIIDecW6  = cms.vdouble(0.8028, 0.0769, 0.0217),
#    CouplingConstantRunIIDecW7  = cms.vdouble(0.7848, 0.0888, 0.0188),
#
#    #TEC---Up x2 10% x1 const
#    CouplingConstantRunIIDecW1b = cms.vdouble(0.8842, 0.0518, 0.0061),
#    CouplingConstantRunIIDecW2b = cms.vdouble(0.8952, 0.0483, 0.0041),
#    CouplingConstantRunIIDecW3b = cms.vdouble(0.8638, 0.0573, 0.0108),
#    CouplingConstantRunIIDecW4  = cms.vdouble(0.8886, 0.0544, 0.0013),
#    CouplingConstantRunIIDecW5  = cms.vdouble(0.8046, 0.0770, 0.0207),
#    CouplingConstantRunIIDecW6  = cms.vdouble(0.8106, 0.0769, 0.0178),
#    CouplingConstantRunIIDecW7  = cms.vdouble(0.7918, 0.0888, 0.0153),
#    #TEC
#    CouplingConstantRunIIDecW1b = cms.vdouble(0.8827, 0.0518, 0.0068),
#    CouplingConstantRunIIDecW2b = cms.vdouble(0.8943, 0.0483, 0.0046),
#    CouplingConstantRunIIDecW3b = cms.vdouble(0.8611, 0.0573, 0.0121),
#    CouplingConstantRunIIDecW4  = cms.vdouble(0.8881, 0.0544, 0.0015),
#    CouplingConstantRunIIDecW5  = cms.vdouble(0.7997, 0.077, 0.0231),
#    CouplingConstantRunIIDecW6  = cms.vdouble(0.8067, 0.0769, 0.0198),
#    CouplingConstantRunIIDecW7  = cms.vdouble(0.7883, 0.0888, 0.0171),

    #-----SiStripDigitizer
    DigiModeList = cms.PSet(SCDigi = cms.string('ScopeMode'),
                            ZSDigi = cms.string('ZeroSuppressed'),
                            PRDigi = cms.string('ProcessedRaw'),
                            VRDigi = cms.string('VirginRaw')),
    ROUList = cms.vstring("TrackerHitsTIBLowTof","TrackerHitsTIBHighTof",
                          "TrackerHitsTIDLowTof","TrackerHitsTIDHighTof",
                          "TrackerHitsTOBLowTof","TrackerHitsTOBHighTof",
                          "TrackerHitsTECLowTof","TrackerHitsTECHighTof"),
    GeometryType               = cms.string('idealForDigi'),
    TrackerConfigurationFromDB = cms.bool(False),
    ZeroSuppression            = cms.bool(True),
    LorentzAngle               = cms.string(''),
    Gain                       = cms.string(''),
    #-----SiStripDigitizerAlgorithm
    PreMixingMode              = cms.bool(False),
    NoiseSigmaThreshold        = cms.double(2.0),
    electronPerAdcDec          = cms.double(247.0), #tuned on collisions at 7 TeV
    electronPerAdcPeak         = cms.double(262.0), #tuned on craft08
    FedAlgorithm               = cms.int32(4),
    FedAlgorithm_PM            = cms.int32(4),  # extra degree of freedom for PreMixing
    Noise                      = cms.bool(True), ## NOTE : turning Noise ON/OFF will make a big change
    #Parameters valid only if Noise = True and ZeroSuppression = False
    RealPedestals              = cms.bool(True), #The pedestal for each stip is read from the Db. if False it is added to all the strips the cnetral strip pedestal value
    SingleStripNoise           = cms.bool(True), #The noise RMS is read from the Db. If false it is considered the central strip noise
    CommonModeNoise            = cms.bool(True),
    BaselineShift              = cms.bool(True),
    APVSaturationFromHIP       = cms.bool(False),
    APVSaturationProbScaling   = cms.double(1.0),
    APVProbabilityFile         = cms.FileInPath("SimTracker/SiStripDigitizer/data/APVProbaList.txt"),
    cmnRMStib                  = cms.double(5.92),
    cmnRMStob                  = cms.double(1.08),
    cmnRMStid                  = cms.double(3.08),
    cmnRMStec                  = cms.double(2.44),
    PedestalsOffset            = cms.double(128),
    #
    TOFCutForDeconvolution     = cms.double(50.0),
    TOFCutForPeak              = cms.double(100.0),
    Inefficiency               = cms.double(0.0),
    # APV Dynamic Gain Simulation
    includeAPVSimulation       = cms.bool( False ),
    apv_maxResponse            = cms.double( 729 ),
    apv_rate                   = cms.double( 66.2 ),
    apv_mVPerQ                 = cms.double( 5.5 ),
    apvfCPerElectron           = cms.double( 1.602e-4 ),
    fracOfEventsToSimAPV       = cms.double( 0.0 ), # fraction of events to simulate APV saturation
)

#################################################
# activate APV simulation for 2016 Strip detector (UL 2016)
# According to this document https://indico.cern.ch/event/560226/contributions/2277448/attachments/1324704/1988050/wgm_vfp_change_ebutz.pdf
# the first LHC fill taken with vfp=0 settings is https://cmswbm.cern.ch/cmsdb/servlet/FillReport?FILL=5198 (run 278801)
# cf Prompt-Reco DQM: https://tinyurl.com/y2gybwx7
# pre-VFP  runs: 273150-278800 lumi: 19480.4566773 /pb
# post-VFP runs: 278801-284044 lumi: 16755.0362868 /pb
# ~53.8% of luminosity is affected by APV saturation
#################################################

from Configuration.Eras.Modifier_tracker_apv_vfp30_2016_cff import tracker_apv_vfp30_2016
tracker_apv_vfp30_2016.toModify(SiStripSimBlock,
                                includeAPVSimulation = True,
                                fracOfEventsToSimAPV = 1.0
                                )

from Configuration.ProcessModifiers.premix_stage1_cff import premix_stage1
premix_stage1.toModify(SiStripSimBlock,
    Noise = False,
    PreMixingMode = True,
    FedAlgorithm = 5, # special ZS mode: accept adc>0
    includeAPVSimulation = False # APV simulation is off for premix stage1
)

from Configuration.Eras.Modifier_run2_common_cff import run2_common
run2_common.toModify(SiStripSimBlock,
                     CouplingConstantsRunIIDecB = True, #for TIB and TOB
                     CouplingConstantsRunIIDecW = True,  #for TID and TEC
                     APVShapeDecoFile =cms.FileInPath("SimTracker/SiStripDigitizer/data/APVShapeDeco_320.txt")
                     )
