import os
import sys

import methylpy.DMRfind
import shared.LoggerFactory

def main():

    if (len(sys.argv)!=6):
        print("Expected 5 arguments, but got %d"%len(sys.argv))
        print("Usage: %s inputf outputf allc_path sample mc_type"%sys.argv[0])
        sys.exit(1)
        
    inputf,outputf,allc_path,sample,mc_type = sys.argv[1:]
    logger = shared.LoggerFactory.get_logger(outputf+'.log')

    shared.LoggerFactory.log_command(logger,sys.argv)
    methylpy.DMRfind.get_methylation_levels_DMRfind(inputf=inputf,
                                                    output=outputf,
                                                    samples=sample.split(','),
                                                    use_mc_status=False,
                                                    path_to_allc=allc_path,
                                                    mc_type=mc_type.split(','),
                                                    num_procs=2)
    logger.info('Done!')
    
if __name__=='__main__':
    main()
