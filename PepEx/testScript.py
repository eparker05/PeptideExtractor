# Copyright 2013 Michael Xin Sun
# Edits copyright 2014 Evan Parker
#
# This file is distributed under the Apache V2 License. See LICENSE file
# for full terms.


from pySamplewiseSequenceAligner import configurationFromXML, SamplewiseSequenceAligner

# Run this file

config = configurationFromXML("SamplewiseSequenceAlignerConfig.xml")

samplewiseSequenceAligner = SamplewiseSequenceAligner(config)
samplewiseSequenceAligner.readFromFastas()
samplewiseSequenceAligner.readFromCsv()
samplewiseSequenceAligner.alignSequences()
samplewiseSequenceAligner.writeToCsvOneAAPerLine()

