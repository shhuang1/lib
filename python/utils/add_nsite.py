import os
import sys

import methylpy.DMRfind
import shared.LoggerFactory
import get_region_nsite

def main():

    if (len(sys.argv)!=7):
        print("Expected 6 arguments, but got %d"%len(sys.argv))
        print("Usage: %s inputf outputf allc_path sample mc_type min_cov"%sys.argv[0])
        sys.exit(1)

    inputf,outputf,allc_path,sample,mc_type,min_cov = sys.argv[1:]
    logger = shared.LoggerFactory.get_logger(outputf+'.log')
    shared.LoggerFactory.log_command(logger,sys.argv)

    min_cov = int(min_cov)
    get_region_nsite.get_nsite_DMRfind(inputf=inputf,
                                       output=outputf,
                                       samples=[sample],
                                       use_mc_status=False,
                                       path_to_allc=allc_path,
                                       mc_type=[mc_type],
                                       num_procs=1,
                                       min_cov=min_cov)
    logger.info('Done!')
    
if __name__=='__main__':
    main()

