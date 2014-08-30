#Peptide Extractor (PepEx) 0.01

PepEx is a proteomics/peptidomics visualization tool that allows the
representation of quantitative data. The program localizes the position of
each peptide in their respective proteins and returns the total abundances
associated with each amino acid of the sequence by summing the peptides that
contains them. The output file can be easily represented (i.e with Excel).
The resulting plot or proteolytic map shows the areas of preferential
proteolysis within the protein.


####Chromatographic Input file
It is a .csv file located at the csv_input_file folder.
The file format is five columns:
 * `Name`:    Peptide sequence in one letter format
 * `Volumen': Peptide quantitative information (i.e number of counts)
 * `Notes`:   Protein ID in uniprot format (i.e sp|Q9TUM6|PLIN2_BOVIN)
 * `Sample`:  When multiple samples are included on the file, a name for each
    one is required
 * `Phospho`: Number of phosphorylated residues (or any other PTM or peptide
    attribute). PepEx can filter and analyze the data containing specific
    values or ranges of values  for this column.

####Protein files
Protein sequences should be included on the fasta_input_files folder in .fasta
format and named with the uniprot number (i.e Q9TUM6.fasta). If one protein
included on the input file (“Notes” column) is not on the folder the
analysis will stop.

####Configuration file
SamplewiseSequenceAlignerConfig.xml can be opened with a text editor. Two options:
 * Route and name of the input file: can be changed at the third line.
 * Phosphorylation: can filter the data according to column “Phospho” from the
   input file. Can be changed at the fifth line.

###Running PepEx
Once the input file, protein fasta files and the configuration file have been
set, the analysis can be performed clicking on testScript.py.

####Output file

Output file will be generated at the csv_output_files folder. The file will
have multiple tables, one table per protein and each table will have the
following format.


|AA Index|AA| Volume | Exp1.d | Exp2.d | Exp3.d | Exp4.d | Exp5.d |
|--------|--|--------|--------|--------|--------|--------|--------|
|16      |R |15329260|775302  |2446862 |1145531 |5781107 |574183  |
|17      |E |16982790|1219449 |2582336 |1404984 |5781107 |627134  |
|18      |L |17385701|1364979 |2744509 |1481942 |5781107 |627134  |
|19      |E |17560980|1364979 |2795431 |1481942 |5781107 |627134  |
|20      |E |17560980|1364979 |2795431 |1481942 |5781107 |627134  |
|21      |L |17651764|1364979 |2822736 |1481942 |5781107 |627134  |
|22      |N |18696031|1364979 |3002235 |1481942 |6229211 |627134  |
|23      |V |18696031|1364979 |3002235 |1481942 |6229211 |627134  |
|24      |P |18696031|1364979 |3002235 |1481942 |6229211 |627134  |
|25      |G |18696031|1364979 |3002235 |1481942 |6229211 |627134  |


The column named “AA Index” for the amino acid (AA) numeration, a second column
named “AA” for the amino acid single-letter code, a third column named “Volume”
contains the sum of the subsequent columns and a number of columns, one for
each experiment included on the analysis, with their corresponding names. The
followings columns contain the corresponding abundances of the displayed
peptide range within the labeled experiment. Amino acid sequence is listed
from the N-terminus (top) to the C-terminus (bottom).
