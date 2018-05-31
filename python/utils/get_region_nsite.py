from methylpy.DMRfind import *

def get_nsite_DMRfind(inputf,output,samples,path_to_allc="",mc_type=["C"],num_procs=1,use_mc_status=True,min_cov=0):
    """
    This function assumes that allc files are of the format allc_<sample>_<chr>.tsv
    input is the path to a file containing collapsed DMR results
    output is the path to a file where the methylation values should be stored
    samples is a list of samples you'd like to compute the methylation level for
    path_to_allc is the path to the directory containing the allc files for these samples
    num_procs is an integer indicating the number of processors you'd like to use for calculating
        methylation level. This function can be parallelized up to the number of samples
    use_mc_status is a boolean value indicating whether or not you'd like to use the methylation
        status of a site when calculating the methylation level. The methylation status is typically
        derived from a binomial test, and if this is set to true, any site with a methylation status of 0
        will have its methylated read count automatically set to 0.
    """
    #dictionary of sample_name -> file handle
    allc_files = {}
    allc_lines = {}
    allc_fields = {}
    allc_prevbyte = {} #sample_name -> prevbyte (started from) in the file
    with open(inputf,'r') as f, open(output,'w') as g:
        line = f.readline()
        line = line.rstrip("\n")
        fields = line.split("\t")
        prefix_len = len(fields)    #number of fields in original file
        mc_type = expand_nucleotide_code(mc_type)
        g.write("\t".join(fields[:prefix_len])+"\t"+"\t".join(["nsite_"+sample for sample in samples])+"\n")
        prev_chrom = ""
        prev_end = ""
        dmr_lines=[]
        methylation_levels = {}
        for line in f:
            line = line.rstrip("\n")
            dmr_lines.append(line)
        if num_procs == 1:
            for sample in samples:
                methylation_levels[sample]=get_nsite_DMRfind_worker(dmr_lines,mc_type,sample,path_to_allc,output,min_cov,use_mc_status=False)
        else:
            pool = Pool(num_procs)
            results = {}
            for sample in samples:
                results[sample]=pool.apply_async(get_nsite_DMRfind_worker,(dmr_lines,mc_type,sample,path_to_allc,output,min_cov),{"use_mc_status":False})
            pool.close()
            pool.join()
            for sample in results:
                methylation_levels[sample]=results[sample].get()
        temp_files = {}
        for sample in samples:
            temp_files[sample]=open(output.replace(".tsv","")+"_"+sample+"_temp_nsite.tsv",'r')

        for index,line in enumerate(dmr_lines):
            g.write(line)
            for sample in samples:
                #g.write("\t"+methylation_levels[sample][index])
                g.write("\t"+temp_files[sample].readline().rstrip("\n"))
            g.write("\n")
        for sample in samples:
            temp_files[sample].close()
            subprocess.check_call(shlex.split("rm "+output.replace(".tsv","")+"_"+sample+"_temp_nsite.tsv"))

def get_nsite_DMRfind_worker(dmr_lines,mc_type,sample,path_to_allc,output,min_cov,use_mc_status=True):
    mc_type = expand_nucleotide_code(mc_type)
    prev_chrom = ""
    prev_end = ""
    methylation_level_list = []
    with open(output.replace(".tsv","")+"_"+sample+"_temp_nsite.tsv",'w') as f:
        for line in dmr_lines:
            line = line.rstrip("\n")
            fields = line.split("\t")
            dmr_chr=fields[0]
            dmr_start = int(fields[1])
            dmr_end = int(fields[2])
            #line_prefix = fields[:prefix_len]
            if prev_chrom != fields[0]:
                try:
                    allc_file.close()
                except:
                    pass
                allc_file=open(path_to_allc+"allc_"+sample+"_"+dmr_chr+".tsv",'r')
                allc_line=allc_file.readline()
                allc_field=allc_line.split("\t")
                allc_prevbyte = 0
                #read past header if it's present
                try:
                    int(allc_field[1])
                except:
                    allc_line=allc_file.readline()
                    allc_field=allc_line.split("\t")
            #If this new dmr overlaps with the previous, begin where the previous start was found
            elif prev_end and dmr_start < prev_end:
                allc_file.seek(allc_prevbyte)
                allc_line = allc_file.readline()
                allc_field = allc_line.split("\t")
                #read past header if it's present
                try:
                    int(allc_field[1])
                except:
                    allc_line=allc_file.readline()
                    allc_field=allc_line.split("\t")
            #read up to the beginning of the dmr
            byte = allc_prevbyte #in case the new dmr never enters the loop, keep byte the same as previously
            while allc_line and int(allc_field[1]) < dmr_start:
                byte = allc_file.tell()
                allc_line=allc_file.readline()
                allc_field=allc_line.split("\t")
            allc_prevbyte = byte #record the byte where dmr_start was found
            
            h = 0
            count = 0
            while allc_line and int(allc_field[1]) >= dmr_start and int(allc_field[1]) <= dmr_end:
                if allc_field[3] in mc_type and int(allc_field[5]) >= min_cov:
                    count += 1
                    h += int(allc_field[5])
                allc_line=allc_file.readline()
                allc_field=allc_line.split("\t")
            #if count != 0:
            #    methylation_level = str(float(h)/count)
            #else:
            #    methylation_level = "NA"
            methylation_level = count
            #methylation_level_list.append(methylation_level)
            f.write(str(methylation_level)+"\n")
                
            prev_chrom = dmr_chr
            prev_end = dmr_end
    return methylation_level_list

