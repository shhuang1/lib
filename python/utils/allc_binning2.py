import os
import sys

from methylpy.DMRfind import get_binned_methylation_levels_DMRfind
import shared.LoggerFactory

argvs = sys.argv

samples = [argvs[1]]
mc_type = [argvs[2]]
min_depth = 4
min_c = 4

for chr in [1,2,3,4,5]:
    output = "/gale/netapp/seq3/illumina_runs/taiji/1001/allc_binned_" + mc_type[0] + "/allc_"+samples[0]+"_" + mc_type[0] + "_" + str(chr) + ".tsv"
    inputf = "/gale/netapp/seq3/illumina_runs/taiji/1001/reference/TAIR10_100bp_" + str(chr) + ".bed"
    #print output
    #print inputf
    get_binned_methylation_levels_DMRfind(inputf,output,samples,path_to_allc= "/gale/netapp/seq3/illumina_runs/taiji/1001/allc/",mc_type = mc_type,num_procs=1,use_mc_status=False,depth = 4, c = 4)


    samples = [h1]
path_to_allc = "allc/"

input_file = sys.argv[1]
output_file = sys.argv[2]

methylpy.DMRfind.get_methylation_levels_DMRfind(inputf= input_file,
                                                output= output_file,
                                                samples=samples,
                                                use_mc_status=False,
                                                path_to_allc=path_to_allc,
                                                mc_type=["CGN"],
                                                num_procs=1)


def main():

    inputf,outputf,allc_path,samples,mc_type = sys.argv[1:]
    logger = shared.LoggerFactory.get_logger(outputf+'.log')
    
    methylpy.DMRfind.get_methylation_levels_DMRfind(inputf= input_file,
                                                output= output_file,
                                                samples=samples,
                                                use_mc_status=False,
                                                path_to_allc=path_to_allc,
                                                mc_type=["CGN"],
                                                num_procs=1)


    
if __name__==' __main__':
    main()
