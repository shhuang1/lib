import os
import os.path
import logging

LOGGER_LEVEL=logging.INFO
LOGGER_FORMAT='%(asctime)s %(levelname)s %(message)s'

SHELL='#!/bin/bash'
BSUB_SHELL='#!/bin/sh'

#THUMPER1_HOME=os.environ['THUMPER1_HOME']
#DATA_PATH=os.path.join(THUMPER1_HOME,'data')
#DEVEL_PATH=os.path.join(THUMPER1_HOME,'devel')
#PROJECTS_PATH=os.path.join(THUMPER1_HOME,'projects')
#PACKAGES_PATH=os.path.join(THUMPER1_HOME,'packages')
DATA_PATH=os.environ['SHHUANG_DATA_PATH']
DEVEL_PATH=os.environ['SHHUANG_DEVEL_PATH']
PROJECTS_PATH=os.environ['SHHUANG_PROJECTS_PATH']
PACKAGES_PATH=os.environ['SHHUANG_PACKAGES_PATH']
DEVEL_LIB_PATH=os.path.join(DEVEL_PATH,'lib')
PYTHONLIB_PATH=os.path.join(DEVEL_LIB_PATH,'python')
PY_TEMPL_PATH=os.path.join(PYTHONLIB_PATH,'Templates')
PYTHONUTILS_PATH=os.path.join(PYTHONLIB_PATH,'Utils')
RLIB_PATH=os.path.join(DEVEL_LIB_PATH,'R')
RLOCALSHARED_PATH=os.path.join(RLIB_PATH,'localshared')

GENOMES_PATH='/nfs/genomes'
GENOMES_PATH_LOCAL=os.path.join(DATA_PATH,'genomes')
GENOMES_PATH_ORG={'hs':'human_gp_mar_06',
                  'hs18':'human_gp_mar_06',
                  'hs17':'human_gp_may_04',
                  'mm9':'mouse_gp_jul_07',
                  'sc':'yeast_gp_oct_03',
                  'sgd':'sgd'}
ANNOT_PATH='/nfs/data/annotations'
GOANNOT_PATH=os.path.join(ANNOT_PATH,'GeneOntology')
GENESETS_PATH=os.path.join(GOANNOT_PATH,'GeneSets')
GENESETS_hs1=os.path.join(GENESETS_PATH,'GOGOA_Hsa-filtered-IC-IDA-TAS.tab')
NCBI_TAXONOMY_ID = {'hs':'9606'}

INTERACTOMES_PATH=os.path.join(DATA_PATH,'interactomes')
INTERACTOMES_BG_hs=os.path.join(INTERACTOMES_PATH,'BIOGRID-ORGANISM-Homo_sapiens-2.0.26.tab.txt')
BIOGRID2EG_HS_PICKLE=os.path.join(INTERACTOMES_PATH,'BIOGRID-ORGANISM-Homo_sapiens-2.0.26_interactors.biogrid.pkl')
INTERACTOMES_HPRD=os.path.join(INTERACTOMES_PATH,'HPRD_Release_6_01012007.txt')
INTERACTOMES_BIOGRID = os.path.join(INTERACTOMES_PATH,'BIOGRID')
INTERACTOMES_BIOGRID_GRAPHPKL = os.path.join(INTERACTOMES_BIOGRID,'graphpkl')
INTERACTOMES_STRING = os.path.join(INTERACTOMES_PATH,'STRING')

EG_PATH=os.path.join(ANNOT_PATH,'EntrezGene')
EG_HS_PICKLE=os.path.join(EG_PATH,'ncbi_symbol2gene.pkl')
GENE2REFSEQ_HS_PKL=os.path.join(EG_PATH,'gene2refseq_20070517_hs.eg.pkl')

HGNC_FILE=os.path.join(ANNOT_PATH,'HGNC','hgnc_alldata_20070406.hgnc')
HGNC_PICKLE=HGNC_FILE+'.pkl'

MGI_PATH=os.path.join(ANNOT_PATH,'MGI')
MGI2EG_PICKLE=os.path.join(MGI_PATH,'MGI_EntrezGene_20070416.rpt.pkl')

OMIM_PATH=os.path.join(ANNOT_PATH,'OMIM')
OMIM2EG_PICKLE=os.path.join(OMIM_PATH,'mim2gene_20070416.pkl')

TFBSCONSSITES_UP2REFSEQ=os.path.join(GENOMES_PATH_LOCAL,GENOMES_PATH_ORG['hs'],'anno','refGene_u2000d200_by_tfbsConsSitesUP.txt')
TFBSCONSSITES_EG2REFSEQ=os.path.join(GENOMES_PATH_LOCAL,GENOMES_PATH_ORG['hs'],'anno','refGene_u2000d200_by_tfbsConsSitesEG.txt')
TFBSCONSSITES_EG2EG=os.path.join(GENOMES_PATH_LOCAL,GENOMES_PATH_ORG['hs'],'anno','refGeneEG_u2000d200_by_tfbsConsSitesEG.txt')
SGD_PATH = os.path.join(GENOMES_PATH_LOCAL,GENOMES_PATH_ORG['sgd'])

TAMO_PATH='/nfs/apps/python/lib/python2.3/site-packages/TAMO'
THEME_PATH=os.path.join(TAMO_PATH,'THEME')
THEME_BIN='/nfs/data/macisaac/cvEM/THEME.py'
FBP_PATH=os.path.join(TAMO_PATH,'FBP_profiles')

KEGG_PATH=os.path.join(ANNOT_PATH,'KEGG')
PATHWAY_DATA_PATH=os.path.join(DATA_PATH,'pathways')
KEGG_PATHWAY_PATH=os.path.join(PATHWAY_DATA_PATH,'KEGG')
KEGG_PATHGENES_HSA_PICKLE=os.path.join(KEGG_PATH,'pathwaygenes_hsa_20070406.kpg.pkl')
KEGG_PATH_RELGENES_HSA_PICKLE=os.path.join(KEGG_PATH,'pathwayrelgenes_hsa_20070513.kpg.pkl')
KEGG_PATH_RELATIONS_HSA_PICKLE=os.path.join(KEGG_PATH,'pathwayrelations_hsa_20070530.kpg.pkl')
KEGG_PATHGENES_SCE_PICKLE=os.path.join(KEGG_PATH,'pathwaygenes_sce_20090107.kpg.pkl')
KEGG_PATH_RELATIONS_SCE_PICKLE=os.path.join(KEGG_PATH,'pathwayrelations_sce_20090107.kpg.pkl')
KEGG_GENE_PATH=os.path.join(ANNOT_PATH,'KEGG')
KEGG_GENE_MAP_HSA_PICKLE=os.path.join(KEGG_GENE_PATH,'hsa_xrefall_20061116.kg.pkl')

KEGG_WSDL_URL='http://soap.genome.jp/KEGG.wsdl'

THEME_RESULT_TEMPL=os.path.join(PY_TEMPL_PATH,'THEME_results_summary_link.wiki.tmpl')
THEME_RESULTS_SET_TEMPL=os.path.join(PY_TEMPL_PATH,'THEME_results_summary_set.wiki.tmpl')

WEBSERVER_URL='http://fraenkel.mit.edu/shhuang'
PROJECTS_URL=os.path.join(WEBSERVER_URL,'projects')

Jaspar2FBPfamily={'CAAT-BOX':'CBFB_NFYA','E2F':'E2F_TDP','ETS':'Ets','FORKHEAD':'Fork_head','ZN-FINGER, GATA':'GATA', 'HOMEO-ZIP':'HALZ','bHLH':'HLH','HMG':'HMG_box','TRP-CLUSTER':'IRF','PAIRED':'PAX','IPT/TIG domain':'RHD','RUNT':'Runt','MADS':'SRF-RF','TATA-box':'TBP','AP2':'TF_AP-2','HOMEO':'homeobox','ZN-FINGER, C2H2':'zf-C2H2','NUCLEAR RECEPTOR':'zf-C4','ZN-FINGER, DOF':'zf-Dof','T-BOX':'T-box'}

PIANA_DBNAME='piana_147_feb_09'
PIANA_DBHOST='fraenkel-node7'
PIANA_DBUSER='piana_user'
PIANA_DBPASS='delectible'

PIANA_DB_SETTINGS = {'147_feb_09':{'PIANA_DBNAME':'piana_147_feb_09',
                                   'PIANA_DBHOST':'fraenkel-node7',
                                   'PIANA_DBUSER':'piana_user',
                                   'PIANA_DBPASS':'delectible'},
                     '147':{'PIANA_DBNAME':'piana_147',
                            'PIANA_DBHOST':'fraenkel-node7',
                            'PIANA_DBUSER':'piana_user',
                            'PIANA_DBPASS':'delectible'}}

DHEA=os.path.join(PACKAGES_PATH,'dhea-code','dhea.sh')
DHEA_PBS=os.path.join(PACKAGES_PATH,'dhea-code','dhea_pbs.sh')

REACTOME_WSDL_VERSION = 'http://www.reactome.org:8080/caBIOWebApp/services/Version?wsdl'
REACTOME_WSDL_BIOPAXEXPORTER = 'http://www.reactome.org:8080/caBIOWebApp/services/BioPAXExporter?wsdl'
REACTOME_WSDL_CABIOSERVICE = 'http://www.reactome.org:8080/caBIOWebApp/services/caBIOService?wsdl'

UNIPROT_WS_BASE_URL = 'http://www.uniprot.org/uniprot/'
UNIPROT_WS_BATCH_URL = UNIPROT_WS_BASE_URL+'batch/'
DAVID_WSDL = 'http://david.abcc.ncifcrf.gov/webservice/services/DAVIDWebService?wsdl'
