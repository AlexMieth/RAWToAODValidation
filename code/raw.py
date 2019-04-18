# Auto generated configuration file
# using: 
# Revision: 1.303.2.7 
# Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: reco -s RAW2DIGI,L1Reco,RECO --data --conditions FT_R_42_V10A::All --eventcontent AOD --customise Configuration/GlobalRuns/reco_TLR_42X.customisePPData --no_exec --python reco_cmsdriver2010.py
import FWCore.ParameterSet.Config as cms
import argparse
import sys

#Configure command line arguments
parser = argparse.ArgumentParser(
    description='Validation code for reprocessing AOD from 2010 RAW samples.')
parser.add_argument('-d','--dataset', type=str,
    help='Specify which dataset you want to analyze. For example: Electron')

#Get command line arguments
args = parser.parse_args()
input_dataset = args.dataset    #Dataset specified by the user at the command line

# Set input and output filenames based on command line argument
if input_dataset is "Electron":
    input_filename = 'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Electron/RAW/v1/000/146/712/185AE5B4-CAC9-DF11-9DF4-0030487CD6D2.root'
    output_filename = 'reco_Electron10_AOD.root'

elif input_dataset is "Jet":
    input_filename = 'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Jet/RAW/v1/000/146/807/04DC3275-DFCA-DF11-B54B-003048F024FA.root'
    output_filename = 'reco_Jet10_AOD.root'

elif input_dataset is "MinimumBias":
    input_filename = 'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/MinimumBias/RAW/v1/000/146/428/08886392-77C6-DF11-BFC9-0030487CAF0E.root'
    output_filename = 'reco_MinimumBias10_AOD.root'

elif input_dataset is "Mu":
    input_filename = 'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/RAW/v1/000/146/589/6609EC50-86C8-DF11-898D-001D09F25456.root'
    output_filename = 'reco_Mu10_AOD.root'

elif input_dataset is None:
    sys.exit("Error: You must specify a dataset using the -d argument. The possible options are Electron, Jet, MinimumBias, or Mu.")

else:
    error_msg = "Error: " + input_dataset + " is not a supported dataset for this example. The possible options are Electron, Jet, MinimumBias, or Mu."
    sys.exit(error_msg)



process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(input_filename)
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.303.2.7 $'),
    annotation = cms.untracked.string('reco nevts:1'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.AODoutput = cms.OutputModule("PoolOutputModule",
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    outputCommands = process.AODEventContent.outputCommands,
    fileName = cms.untracked.string(output_filename),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('')
    )
)

# Additional output definition

# Other statements
#process.GlobalTag.globaltag = 'FT_R_42_V10A::All'
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/FT_R_42_V10A.db')
process.GlobalTag.globaltag = 'FT_R_42_V10A::All'

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODoutput_step = cms.EndPath(process.AODoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.AODoutput_step)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.GlobalRuns.reco_TLR_42X
from Configuration.GlobalRuns.reco_TLR_42X import customisePPData 

#call to customisation function customisePPData imported from Configuration.GlobalRuns.reco_TLR_42X
process = customisePPData(process)

# End of customisation functions

#del process.lumiProducer


