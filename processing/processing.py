import pandas as pd

metadata = pd.read_csv(
    '../metadata.tsv.gz',
    sep='\t',
    usecols=['strain', 'genbank_accession', 'gisaid_epi_isl'])
assignments = pd.read_csv('../assignments.tsv.gz',
                          sep='\t',
                          names=['strain', 'pango_lineage_armadillin'])
both = metadata.merge(assignments, on='strain')
both.to_csv('../assignments.tsv.gz', sep='\t', index=False)
